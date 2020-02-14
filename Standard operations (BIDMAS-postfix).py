class Stack(list):
    def pop(self, n):
        if n == 0:
            return []
        elif n <= len(self):
            res = self[-n:]
            del self[-n:]
            return res
        else:
            raise ValueError("cannot pop {} items, only {} in stack".format(n, len(self)))
    def push(self, n, items):
        self.extend(items)

class Operator:
    def __init__(self, x_in, y_out, o):
        self.x_in = x_in
        self.y_out = y_out
        self.o = o
    def __call__(self, stack):
        args = stack.pop(self.x_in)
        res = self.o(*args)
        stack.push(self.y_out, res)

operators = {
    '*':  Operator(2, 1, lambda a,b: [a*b]),
    '/':  Operator(2, 1, lambda a,b: [a/b]),
    '+':  Operator(2, 1, lambda a,b: [a+b]),
    '-':  Operator(2, 1, lambda a,b: [a-b]),
    '^':  Operator(2, 1, lambda a,b: [a**b]),

}

OPERATORS = set(['+', '-', '*', '/', '(', ')','^'])
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}

def infix_to_postfix(infix):
    stack = []
    postfix = ''
    equation = ''
    for i in infix:
        if(i != ' '):
            equation += i
    #print('Original: ' + infix)
    #print('Trimmed: ' + equation)
    prevv= '+'
    for v in equation:
        if v not in OPERATORS:
            postfix += v
        elif v == '(':
            stack.append('(')
        elif v == ')':
            while stack and stack[-1] != '(':
                tmp = stack.pop()
                if(tmp in OPERATORS):
                    postfix += ' ';
                postfix += tmp;
            stack.pop() 
        else:
            if(v == '-' and prevv in OPERATORS):
                postfix  += v
            else:
                postfix += ' ';
                while stack and stack[-1] != '(' and PRIORITY[v] <= PRIORITY[stack[-1]]:
                    postfix += stack.pop()
                    postfix += ' '
                stack.append(v)
        prevv = v;
    while stack:
        tmp = stack.pop()
        if(tmp in OPERATORS):
            postfix += ' ';
        postfix += tmp;
    return postfix

def evaluate_postfix(equation):
    n_str = lambda s: isinstance(s, str)
    if n_str(equation):
        equation = equation.split()
    stack = Stack()
    for c in equation:
        try:
            stack.append(int(c))
        except ValueError:
            try:
                operator = operators[c]
                operator(stack)
            except KeyError:
                raise ValueError("Invalid character(s) {}".format(c))
    return stack

def main():
    inp = input
    while True:
        try:
            expr = input('\nEnter an expression or EXIT: ').strip()
            if(expr == 'EXIT'):
                break
            print (infix_to_postfix(expr))
            print(evaluate_postfix(infix_to_postfix(expr)))
        except ValueError as error:
            print("INPUT ERROR {}".format(error))
            

if __name__=="__main__":
    main()
