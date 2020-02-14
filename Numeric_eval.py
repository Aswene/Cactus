###Programme begins:
import tkinter #code to import tkinter from the standard python library, this is required for the GUI
import math #code to import the math library from the standard python library, this is required for the evaluation of trig functions

###GUI
debug_config = 1 # 1 to enable debug messages, 0 ti disable debug messages
def debug(msg): #create a debug function to be called at any point so intermediate steps can be observed
    if(debug_config == 1): #check if the debug function is enabled then proceeds to next step
        print("Debug msg: " + msg) #prints the debug message when function is called and enabled

class GUI(tkinter.Tk): #class - begin a class definition
    def __init__(self,parent): #def - begin a function declaration
        tkinter.Tk.__init__(self,parent) #constructor tkinter.Tk; parent - keeps a reference to the parent
        self.parent = parent #self refers to the currently bound object or variable
        self.GUI_widgets() #self refers to the currently bound object or variable

    def Mouse(self): #function to produce the result when mouse is clicked
        expr = self.entryVariable.get() #read the entered expression in the 'entry' box
        try:
            self.labelVariable.set(evaluate_postfix(infix_to_postfix(convert_equation(expr))))
        except ValueError as error: #ValueError=the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified
            self.labelVariable.set("INPUT ERROR {}".format(error))
        #self.entry.focus_set() #focuses on entry elements
        self.entry.selection_range(0, tkinter.END) #highlights the entry text from start to end so it can all be deleted with one backspace press

    def Keyboard(self,event): #function to produce the result when 'Enter' is pressed on the keyboard
        expr = self.entryVariable.get()
        try:
            self.labelVariable.set(evaluate_postfix(infix_to_postfix(convert_equation(expr))))
        except ValueError as error:
            self.labelVariable.set("INPUT ERROR {}".format(error))
        #self.entry.focus_set() #focuses on entry elements
        self.entry.selection_range(0, tkinter.END) #highlights the entry text from start to end so it can all be deleted with one backspace press

    def GUI_widgets(self): #functon that contains all the GUI elements (labels, buttons, text...)
        self.grid() #create a grid layout manager for the GUI application to organise the widgets
        self.grid_columnconfigure(0,weight=1) #gid_columnconfigure(index, properties) where index is the column to be altered by the defined properties
        self.grid_columnconfigure(1,weight=10) #coloumn 1 will grow 10 times as fast as column 0
        label1 = tkinter.Label(self, text="Enter your expression here:") #create a label to indicate where the user should type their expression
        label1.grid(column=0,row=1) #define the location of label1
        label2 = tkinter.Label(self, text="Solution displayed here:") #create a label to indicate where the output would appear
        label2.grid(column=0,row=2) #define the location of label2
        label3 = tkinter.Label(self, text="MESSAGE FOR USER: Enter the values in RADIANS and answers are provided in RADIANS", foreground="black",background="red") #message for user label
        label3.grid(column=0,row=0,columnspan=2,sticky='EW') #define the location of label3
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable) #create the entry widget
        self.entry.grid(column=1,row=1,sticky='EW') #set the location of input box, sticky expands the widget to take up the entire cell [E=east(right),W=west(left),N=north(up),S=south(down)]
        self.entry.bind("<Return>", self.Keyboard)
        button = tkinter.Button(self,text="CLICK HERE OR PRESS ENTER ON KEYBOARD", #creates a button to respond when the mouse clicks it
                                command=self.Mouse,foreground="black",background="cyan") #foreground defines text colour and background defines the widgets colour
        button.grid(column=0,row=3,columnspan=2,sticky='EW') #set the location of the button where columnspan is how many columns the button occupies
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",foreground="black",background="yellow")
        label.grid(column=1,row=2,sticky='EW')
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

###BIDMAS(BODMAS)
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

operators = { #establish BIDMAS operators for evaluate_postfix function
    '*':  Operator(2, 1, lambda a,b: [a*b]), #('*':)=sets the character that performs the , self= calls 'class Operator', x_in=2, y_out=1, o=lambda a,b: [a*b]
    '/':  Operator(2, 1, lambda a,b: [a/b]),
    '+':  Operator(2, 1, lambda a,b: [a+b]),
    '-':  Operator(2, 1, lambda a,b: [a-b]),
    '^':  Operator(2, 1, lambda a,b: [a**b]),
    'sin': Operator(1, 1, lambda a: [math.sin(a)]), #change from (a) to (a*(math.pi/180)) to give answer in degrees
    'cos': Operator(1, 1, lambda a: [math.cos(a)]),
    'tan': Operator(1, 1, lambda a: [math.tan(a)]),
    'sinh': Operator(1, 1, lambda a: [math.sinh(a)]),
    'cosh': Operator(1, 1, lambda a: [math.cosh(a)]),
    'tanh': Operator(1, 1, lambda a: [math.tanh(a)]),
    'exp':  Operator(1, 1, lambda a: [math.exp(a)]),
    'sqrt':  Operator(1, 1, lambda a: [math.sqrt(a)]),
    'asin': Operator(1, 1, lambda a: [math.asin(a)]),
    'acos': Operator(1, 1, lambda a: [math.acos(a)]),
    'atan': Operator(1, 1, lambda a: [math.atan(a)])

}

OPERATORS = set(['+', '-', '*', '/', '(', ')','^']) #establish the operators for infix_to_postfix function
OPERATORS_STRING = ['sin','cos','tan','sinh','cosh','tanh','exp','sqrt','asin','acos','atan'] #establish the trigonometric, hyperbolic functions
#PRIORITY --> sets the priority of operations for the 'infix_to_postfix' function, according to the BIDMAS rule
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3, 'sin':4, 'cos':4, 'tan':4,'sinh':4, 'cosh':4, 'tanh':4, 'exp':4, 'sqrt':4, 'asin':4, 'acos':4, 'atan':4}
def infix_to_postfix(infix): #re-order expression
    debug(infix) #calls debug function to observe
    stack = [] #create stack to sort the order of operations and store it
    postfix = '' #postfix is initially declared as empty (nothing)
    equation = '' #equation is initially declared as empty (nothing)
    word = '' #word is initially declared as empty (nothing)
    for i in infix: #loop to create a space between each character in the equation
        if(i != ' '): #check if there already is a space between the characters, if there is no space then continue to next line
            equation += i #in this line a space is added between each of the characters
    prevv= '+'#making sure it handles starting negative numbers well
    for v in equation: #read the current character
        if (str.isalpha(v) or (v == '_')): #check if v is a letter in the alphabet or an underscore (for words such as x_init)
            word += v #if v is a letter build up a word
            continue #keep building up the word until there are no more letters in the input equation
        else:
            if(word != ''): #check if a word has been built up
                debug(word) #calls debug function to observe the word at this point
                stack.append(word) #add the built up word to the stack
                word ='' # rest the word list so that it is empty and ready to check for the next word in the equation
        debug(postfix) #calls debug function to observe the postfix at this point
        if v not in OPERATORS: #if read value is not an operator then push to stack
            postfix += v #when extracted the result displays previous solutions plus the current value (answer = answer + v)
        elif v == '(': #if read value is a left bracket then go to next line else skip to next 'elif'
            if(prevv == ')'): #checks if the previous character was a right bracket 
                stack.append('*') #if above two lines are true then inputs a multiplication symbol between the two brackets, i.e: )*(
            stack.append('(') #otherwise, updates existing stack when open bracket is encountered, prioritising it
            debug(str(stack)) #calls debug function to observe the stack at this point
        elif v == ')': #if read value is a right bracket then continue to next line, else skip
            postfix += ' '#
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
        if((tmp in OPERATORS) or (tmp in OPERATORS_STRING)):
            postfix += ' ';
        postfix += tmp;
    debug('Postfix: ' + postfix) #calls debug function to observe the postfix vesion of the equation
    return postfix

def evaluate_postfix(equation):
    n_str = lambda s: isinstance(s, str)
    if n_str(equation):
        equation = equation.split()
    stack = Stack()
    for c in equation:
        try:
            stack.append(float(c))
        except ValueError:
            try:
                operator = operators[c]
                operator(stack)
            except KeyError:
                raise ValueError("Invalid character(s) {}".format(c))
    return stack

def convert_equation(expr): #converts the entire expression so that the trig functions are passed to the evaluation in the 
    exprl = expr.lower() #changes the input expression into only lowercase so that the program can deal with any input format, i.e: uppercase or lowercase or a mixture of both
    cos = 'cos('
    cosine = 'cosine('
    sin = 'sin('
    sine = 'sine('
    tan = 'tan('
    tangent = 'tangent('
    cosh = 'cosh('
    sinh = 'sinh('
    tanh = 'tanh('
    exp = 'exp('
    sqrt = 'sqrt('
    acos = 'acos('
    asin = 'asin('
    atan = 'atan('
    if cosine and sine and tangent in exprl:
        exprlc = exprl.replace(cosine,cos) #replace any 'cosine' in the equation with 'cos'
        exprls = exprlc.replace(sine,sin)
        exprlt = exprls.replace(tangent,tan)
        out = exprlt
        return out
    elif cosine and sine in exprl:
        exprlc = exprl.replace(cosine,cos)
        exprls = exprlc.replace(sine,sin)
        out = exprls
        return out
    else:
        out = exprl
        return out

###EVENT DRIVEN PROGRAM - RUNS THE ENTIRE CODE TO PRODUCE THE GUI BOX FOR THE USER TO INTERACT WITH
if __name__ == "__main__": #parent is defined since main is executed when the program is run from the command line
    smc = GUI(None) #(none) represents how no parent is given as this is the first GUI element built
    smc.title('Expression Evaluator') #title of the GUI application block defined here
    smc.mainloop() #indefinite loop to wait for the users action and produces an instant result
