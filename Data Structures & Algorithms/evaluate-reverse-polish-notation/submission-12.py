class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calculationStack = []

        for token in tokens : 
            if token == "+" : 
                calculationStack.append(calculationStack.pop() + calculationStack.pop())
                continue

            if token == "-" : 
                lastNumber, firstNumber = calculationStack.pop(), calculationStack.pop()
                calculationStack.append(firstNumber - lastNumber)
                continue

            if token == "*" :
                calculationStack.append(calculationStack.pop() * calculationStack.pop())
                continue

            if token == "/" : 
                lastNumber, firstNumber = calculationStack.pop(), calculationStack.pop()
                if lastNumber == 0 :
                    raise Exception("Sorry, you can't divide by zero") 
                calculationStack.append(int(float(firstNumber / lastNumber)))
                continue

            calculationStack.append(int(token))
        
        return int(calculationStack[0])