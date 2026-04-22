import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
        stack=[]
        for char in tokens:
            if char not in op:
                stack.append(int(char))
            elif char in op:
                a=stack.pop()
                b=stack.pop()
                stack.append(int(op[char](b,a)))
        return stack[0]
                
        