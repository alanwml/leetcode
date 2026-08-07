class Solution:
    def check_similarity(self, string_list: list) -> bool:
        for i in string_list:
            if i != "":
                return False
        return True

    def is_gcd(self, gcd_string: str) -> str:
        x = ""
        for i in gcd_string:
            x += i
            print(f"x : {x}")
            y = gcd_string.split(x)
            if self.check_similarity(y):
                return x
        return gcd_string

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            gcd_string = self.is_gcd(str2)
            str3_list = str1.split(gcd_string)
            if self.check_similarity(str3_list):
                return gcd_string
            else:
                return ""
        else:
            gcd_string = self.is_gcd(str1)
            str3_list = str2.split(gcd_string)
            if self.check_similarity(str3_list):
                return gcd_string
            else:
                return ""
    
def main():
    str1 = "AAAAAAAB"
    str2 = "AAA"
    solution = Solution()
    answer = solution.gcdOfStrings(str1, str2)
    print(answer)

if __name__ == "__main__":
    main()