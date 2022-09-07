class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # creating a "cache" where we are storing whether or not at a certain index, a word(s) in the dictionary would satisify the problem
        dp = [False] * (len(s) + 1)
        # base case, there are no letters left in s, so it satisfies the requirement automatically. Need this in case theres a word in word_dict that matches string s entirely
        dp[len(s)] = True
        # starting from the end of s
        for i in range(len(s) - 1, -1 , -1):
            # we want to check if any of the words in wordDict has the possibility of breaking s
            for word in wordDict:
                # if the current index plus the lenght of the word is greater than s, then its not a valid word break
                # also check if the word exists within the string starting from index i
                if (i + len(word)) <= len(s) and s[i: i+len(word)] == word:
                    # if at dp[i + len(word)] also has a word break (is == true) then we can also set dp[i] == true, otherwise false
                    dp[i] = dp[i + len(word)]
                # since we can reuse words, once we know that a word has a match at index i, we can just break out of the loop
                if dp[i]:
                    break
        return dp[0]
            
