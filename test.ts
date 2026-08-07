function getUserOrders(userId):
	# M1
	shippingBaseUrl = config.get("SHIPPING_SERVICE_BASE_URL")
	requestTimeoutMs = config.getInt("SHIPPING_TIMEOUT_MS", 2000)
	maxRetries = config.getInt("SHIPPING_MAX_RETRIES", 3)

	# S1
	if isBlank(userId):
		raise ValidationError("userId is required")

	try:
		# S1
		user = db.queryOne(
			"SELECT id, name, email FROM users WHERE id = ?",
			[userId]
		)

		if user is null:
			return []

		orders = db.query(
			"SELECT id, status, total, created_at FROM orders WHERE user_id = ?",
			[userId]
		)

		if orders is empty:
			return []

		orderIds = map(orders, (o) => o.id)

		# P1
		orderItemsRows = db.query(
			"SELECT order_id, sku, quantity, price FROM order_items WHERE order_id IN (?)",
			[orderIds]
		)
		itemsByOrderId = groupBy(orderItemsRows, "order_id")

	except DatabaseError as err:
		logger.error("getUserOrders database failure", {
			"userId": userId,
			"error": err.message
		})
		raise ServiceUnavailableError("Unable to load user orders right now")
	
	# R2
	shipmentsByOrderId = parallelMap(orderIds, (orderId) =>
		[orderId, fetchShipmentWithRetry(shippingBaseUrl, orderId, requestTimeoutMs, maxRetries)]
	).toDictionary()

	result = []
	for order in orders:
		result.append({
			"user": user,
			"order": order,
			"items": itemsByOrderId.get(order.id, []),
			"shipment": shipmentsByOrderId.get(order.id, {
				"status": "unknown",
				"reason": "shipment_unavailable"
			})
		})

	return result


function fetchShipmentWithRetry(baseUrl, orderId, timeoutMs, maxRetries):
	url = baseUrl + "/api/shipments/" + orderId

	for attempt in range(1, maxRetries + 1):
		try:
			response = http.get(url, timeout=timeoutMs)

			if response.statusCode == 200:
				return response.body

			if response.statusCode in [429, 500, 502, 503, 504]:
				raise RetryableHttpError("transient shipping-service failure")

			# R1
			return {
				"status": "unknown",
				"reason": "non_retryable_http_status",
				"httpStatus": response.statusCode
			}

		except TimeoutError, NetworkError, RetryableHttpError as err:
			if attempt == maxRetries:
				logger.warn("shipping lookup failed after retries", {
					"orderId": orderId,
					"attempts": attempt,
					"error": err.message
				})
				return {
					"status": "unknown",
					"reason": "shipping_service_timeout_or_unavailable"
				}

			sleep(exponentialBackoffWithJitter(attempt))

		except Exception as err:
			logger.error("unexpected shipping lookup error", {
				"orderId": orderId,
				"error": err.message
			})
			return {
				"status": "unknown",
				"reason": "unexpected_shipping_error"
			}
