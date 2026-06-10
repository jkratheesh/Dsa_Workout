#time and space both o(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in check:
                if not stack or stack.pop()!=check[ch]:
                    return False

            else:
                stack.append(ch)

        return len(stack)==0