class Solution(object):
    def subsets(self, s):
        result = []

        def find_subsequences(s, current=[], index=0):
            if index == len(s):
                result.append(current)  # Append the current subsequence
                return
            
            # Choice 1: Include current character
            find_subsequences(s, current + [s[index]], index + 1)
            
            # Choice 2: Exclude current character
            find_subsequences(s, current, index + 1)

        find_subsequences(s, [], 0)
        return result

# Example usage
solution = Solution()
print(solution.subsets([1, 2, 3]))  # Expecting all subsets of [1,2,3]

