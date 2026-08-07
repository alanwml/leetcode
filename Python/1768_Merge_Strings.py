class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_word = ""
        same_length = min(len(word1), len(word2))
        for i in range(same_length):
            combined_word = combined_word + word1[i] + word2[i]

        if len(word1) > len(word2):
            for i in range(len(word1)):
                if i > same_length-1:
                    combined_word = combined_word + word1[i]
        if len(word2) > len(word1):
            for i in range(len(word2)):
                if i > same_length-1:
                    combined_word = combined_word + word2[i]
        
        return combined_word

def main():
    str1 = "ABCABC"
    str2 = "ABC"
    solution = Solution()
    answer = solution.mergeAlternately(str1, str2)
    print(answer)

if __name__ == "__main__":
    main()