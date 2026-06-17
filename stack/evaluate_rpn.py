class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in {'+','-','*','/'}:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if ch=="+":
                    stack.append(operand1+operand2)
                elif ch=='-':
                    stack.append(operand2-operand1)
                elif ch=='*':
                    stack.append(operand1*operand2)
                else:
                    stack.append(int(operand2/operand1))
            else:
                stack.append(int(ch))
                
        return stack[0]