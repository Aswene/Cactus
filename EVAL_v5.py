###Programme begins: 
import tkinter #code to import tkinter from the standard python library, this is required for the GUI
import math #code to import the math library from the standard python library, this is required for the evaluation of trig functions

VARIABLES_NAMES = []
VARIABLES_STRING_VALUES = []
###GUI
debug_config = 0 # 1 to enable debug messages, 0 to disable debug messages
def debug(msg): #create a debug function to be called at any point so intermediate steps can be observed
    if(debug_config == 1): #check if the debug function is enabled then proceeds to next step
        print("Debug msg: " + msg) #prints the debug message when function is called and enabled

class GUI(tkinter.Tk): #class - begin a class definition
    window = 0; #set window to zero
    def HELP_window(self): #opening a help window with a list of possible problems and theire relevant solutions
        if self.window == 0:
            self.window = tkinter.Toplevel(self,height=250,width=650) #create a window of size 250 by 650
            self.window.title("Expression Evaluator: HELP window") #set the tittle of the help window
            label_a = tkinter.Label(self.window,text="COMMAND LIST")
            label_a.place(x=0,y=1)
            label_i = tkinter.Label(self.window,text="i. Operators: Addition '+', Subtraction '-', Multiplication '*', Division '/', Power '^'")
            label_i.place(x=0,y=20)
            label_ii = tkinter.Label(self.window,text="ii. Always close each open bracket.")
            label_ii.place(x=0,y=40)
            label_iii = tkinter.Label(self.window,text="iii. Trigonometric functions: SIN(), COS(), TAN().")
            label_iii.place(x=0,y=60)
            label_iv = tkinter.Label(self.window,text="vi. Inverse trigonometric functions: ASIN(), ACOS(), ATAN().")
            label_iv.place(x=0,y=80)
            label_v = tkinter.Label(self.window,text="v. Hyperbolic functions: SINH(), COSH(), TANH().")
            label_v.place(x=0,y=100)
            label_vi = tkinter.Label(self.window,text="vi. Square root and exponentials: SQRT() and EXP().")
            label_vi.place(x=0,y=120)
            label_vii = tkinter.Label(self.window,text="vii. Binomial expansion format example: (2a+1b)^3.")
            label_vii.place(x=0,y=140)
            label_viii = tkinter.Label(self.window,text="viii. Integration format example: integrate(2x+3a,x) where x defines the variable to be integrated with respect to.")
            label_viii.place(x=0,y=160)
            label_ix = tkinter.Label(self.window,text="ix. Differentiation format example: derivative(2x+3a,x) where x defines the variable to be differentiated with respect to.")
            label_ix.place(x=0,y=180)
            label_x = tkinter.Label(self.window,text="x. Use '=' to assign a number to a variable, i.e. g = 5. If the value of g changes later re-assign the new number.")
            label_x.place(x=0,y=200)
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        self.window.destroy()
        self.window = 0 #reset window value to zero
    
    def __init__(self,parent): #def - begin a function declaration
        tkinter.Tk.__init__(self,parent) #constructor tkinter.Tk; parent - keeps a reference to the parent
        self.parent = parent #self refers to the currently bound object or variable
        self.GUI_widgets() #self refers to the currently bound object or variable

    def process(self,expr):
        special_function_found = False
        function = ''
        expr_conv = convert_equation(expr)
        ### check for special cases
        CASES = ['derivative','integrate']
        for case in CASES:
            if(case in expr_conv):
                special_function_found = True
                function = case

        if special_function_found == False:
            #check if user is assigning values
            for i in range(len(expr_conv)-1):
                if(expr_conv[i] == '='):
                    #everything before '=' goes to varaible names
                    #everything after goes to variable string values
                    variable_name = expr_conv[:i]
                    if not str.isnumeric(variable_name):
                        variable_string_value = expr_conv[(i+1):]
                        if variable_name in VARIABLES_NAMES: #if we have the value assigned to anything 
                            index_val = VARIABLES_NAMES.index(variable_name)
                            VARIABLES_STRING_VALUES[index_val] = variable_string_value #replace value
                        else:#otherwise add name and values
                            VARIABLES_NAMES.append(variable_name)
                            VARIABLES_STRING_VALUES.append(variable_string_value)
                        expr_eval ="\""
                        expr_eval += variable_string_value
                        expr_eval += "\" got assigned to name: \""
                        expr_eval += variable_name
                        expr_eval += "\""
                    else:
                        expr_eval = "Invalid name"
                    return expr_eval
            #this part is replacing every known variables and rechecks for unknowns
            was_replaced = True
            while(was_replaced):
                was_replaced = False
                #loop through the expression and look for anything that are not in operators or string based operators
                word = ''
                unknowns = []
                knowns = []
                for letter in expr_conv: #sift through the expression for variable names
                    if(letter not in OPERATORS and not str.isnumeric(letter) and letter != ' ' and letter != '.'):
                        word += letter #creates up the words
                        continue
                    else:
                        if(word != '' and word not in OPERATORS_STRING): #evaluate word
                            #meaning it is either unknown or just a previously set variable
                            if(word not in VARIABLES_NAMES):
                                #definitely unknown
                                if(word not in unknowns): #already registered?
                                    #GOTCHA
                                    unknowns.append(word)
                            else:
                                if(word not in knowns): #already registered?
                                    #GOTCHA
                                    knowns.append(word)
                        word = ''
                #additional evaluation for the last letter
                if(word != '' and word not in OPERATORS_STRING):
                    if(word not in VARIABLES_NAMES):
                        if(word not in unknowns):
                            unknowns.append(word)
                    else:
                        if(word not in knowns):
                            knowns.append(word)
                            
                #try replacing the known values in equation
                for name in knowns:
                    index_value = VARIABLES_NAMES.index(name)
                    value = '('
                    value += VARIABLES_STRING_VALUES[index_value]
                    value += ')'
                    expr_conv = expr_conv.replace(name,value)
                    was_replaced = True #if anything got replaced, it means there might be new unknowns so restart
            
            if(len(unknowns) > 0):            
            #if unknowns are present show equation
                expr_binom = look_for_binomial(expr_conv)
                expr_eval = "There are unknown varaibles in the expression.\nPlease assign values to:\n"
                for i in unknowns:
                    expr_eval += i
                    expr_eval += ", "
                expr_eval = expr_eval[:-2]
                expr_eval += "\n"
                expr_eval += expr_binom
            else:
                expr_postfix = infix_to_postfix(expr_conv)
                expr_eval = evaluate_postfix(expr_postfix)
        else:
            #where the functions are evaluated
            if(function == 'derivative'):
                if(expr_conv[0] == 'd'):
                    if(expr_conv[10] == '('):
                        arg1 = ''
                        arg2 = ''
                        coma_found = False;
                        for i in range(11,len(expr_conv)):
                            if(expr_conv[i] != ',' and coma_found == False):
                                arg1 += expr_conv[i]
                            else:
                                if(expr_conv[i] != ','):
                                    arg2 += expr_conv[i]
                                else:
                                    coma_found = True;
                        arg2 = arg2[:-1]
                        expr_eval = derivative(arg1,arg2)
                    else:
                        expr_eval = 'Invalid use of derivative'
                else:
                    expr_eval = 'Invalid use of derivative'
            if(function == 'integrate'):
                if(expr_conv[0] == 'i'):
                    if(expr_conv[9] == '('):
                        arg1 = ''
                        arg2 = ''
                        coma_found = False;
                        for i in range(10,len(expr_conv)):
                            if(expr_conv[i] != ',' and coma_found == False):
                                arg1 += expr_conv[i]
                            else:
                                if(expr_conv[i] != ','):
                                    arg2 += expr_conv[i]
                                else:
                                    coma_found = True;
                        arg2 = arg2[:-1]
                        expr_eval = integrate(arg1,arg2)
                    else:
                        expr_eval = 'Invalid use of integrate'
                else:
                    expr_eval = 'Invalid use of integrate'

                    
##            if(function == 'something else'):
##                pass
                            
        return expr_eval

    def Mouse(self): #function to produce the result when mouse is clicked
        expr = self.entryVariable.get() #read the entered expression in the 'entry' box
        try:
            expr = (self.process(expr))
            self.text_solu.delete('0.0','end')
            self.text_solu.insert('0.0', expr)
        except ValueError as error: #ValueError=the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified
            self.labelVariable.set("INPUT ERROR {}".format(error))
        #self.entry.focus_set() #focuses on entry elements
        self.entry.selection_range(0, tkinter.END) #highlights the entry text from start to end so it can all be deleted with one backspace press

    def Keyboard(self,event): #function to produce the result when 'Enter' is pressed on the keyboard
        expr = self.entryVariable.get()
        try:
            expr = (self.process(expr))
            self.text_solu.delete('0.0','end')
            self.text_solu.insert('0.0', expr)
        except ValueError as error:
            self.labelVariable.set("INPUT ERROR {}".format(error))
        #self.entry.focus_set() #focuses on entry elements
        self.entry.selection_range(0, tkinter.END) #highlights the entry text from start to end so it can all be deleted with one backspace press

    def GUI_widgets(self): #functon that contains all the GUI elements (labels, buttons, text...)
        self.grid() #create a grid layout manager for the GUI application to organise the widgets
        self.grid_columnconfigure(0,weight=1) #gid_columnconfigure(index, properties) where index is the column to be altered by the defined properties
        self.grid_columnconfigure(1,weight=10) #coloumn 1 will grow 10 times as fast as column 0
        label_msg = tkinter.Label(self, text="WARNING: Answers are provided in radians and variables are not case sensitive", foreground="black",background="orange") #message for user label
        label_msg.grid(column=1,row=0,columnspan=2,sticky='EW') #define the location of label_msg
        label_in = tkinter.Label(self, text="Enter your expression here:") #create a label to indicate where the user should type their expression
        label_in.grid(column=0,row=1) #define the location of label_in
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self,textvariable=self.entryVariable) #create the entry widget
        self.entry.grid(column=1,row=1,sticky='EW') #set the location of input box, sticky expands the widget to take up the entire cell [E=east(right),W=west(left),N=north(up),S=south(down)]
        self.entry.bind("<Return>", self.Keyboard)
        button_result = tkinter.Button(self,text="CLICK HERE OR PRESS ENTER ON KEYBOARD FOR SOLUTION", #creates a button to respond when the mouse clicks it
                                command=self.Mouse,foreground="black",background="cyan") #foreground defines text colour and background defines the widgets colour
        button_result.grid(column=0,row=2,columnspan=2,sticky='EW') #set the location of the button where columnspan is how many columns the button occupies
        label_out = tkinter.Label(self, text="Solution displayed here:") #create a label to indicate where the output would appear
        label_out.grid(column=0,row=3) #define the location of label_out
        self.labelVariable = tkinter.StringVar()
        self.text_solu = tkinter.Text(self,foreground="black",background="yellow",height=10)
        self.text_solu.grid(column=1,row=3,sticky='EW')
        button_help = tkinter.Button(self,text="Click here for HELP",command=self.HELP_window,foreground="black",background="red")
        button_help.grid(column=0,row=0,sticky='EW')
        self.button_help = button_help
        #button_rad2deg = tkinter.Button(self,text="Radians to Degrees",command=self.Mouse)
        #button_rad2deg.grid(column=0,row=4,sticky='EW')
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)

        
###BINOMIAL EXPANSION
def pascals_triangle(N):
    multipliers = [1,1]
    new_multi = [1]
    for i in range(N-1):
        new_multi = [1]
        for j in range(len(multipliers)-1):
            new_multi.append(multipliers[j]+multipliers[j+1])
        new_multi.append(1)
        multipliers = new_multi
    return multipliers
    
def binomial_expand(X,Y,N):
    expanded = ''
    multipliers = pascals_triangle(N)
    for k in range(N+1):
        expanded += str(multipliers[k])
        expanded += '*'
        expanded += X
        expanded += '^'
        expanded += str((N-k))
        expanded += '*'
        expanded += Y
        expanded += '^'
        expanded += str(k)
        expanded += '+'
    expanded = expanded[:-1]
    return expanded

def look_for_binomial(equation):
    #test equation = a+(b)+(c+d)^2+(e)
    #######
    ###MEMO: make it work with (a+(b+c)^2) The problem here is that it will think the closing bracket is the one closing the first opening bracket
    ###MEMO: create a simplify function that will look for *1,1*,brackets with one element inside will leave brackets, negative brackets will change signs inside the bracket and leave the brackets
    ###         all ^0 will be changed to 1 either single element or (insides)
    was_expanded = True
    while was_expanded:
        #look up all opening brackets position
        opening_brackets_positions = []
        for i in range(len(equation)):
            if (equation[i] == '('):
                opening_brackets_positions.append(int(i))
        #set up variables         
        was_expanded = False
        maybe_binomial = False
        looking_for_closing_bracket = False
        plus_minus_location = 0
        closing_bracket_location = 0
        for starting_position in opening_brackets_positions:
            #this time we know we started from an opening bracket, we need a plus/minus, a closing bracket and power in this order
            #loop through the remainder of the equation
            try_next_position = False
            for i in range(starting_position+1,len(equation)):
                if(try_next_position):
                    continue
                if(was_expanded):
                    break
                if(((equation[i] == '+')or(equation[i] == '-')) and not looking_for_closing_bracket):
                    looking_for_closing_bracket = True
                    plus_minus_location = i
                    continue
                if(equation[i] == ')'):
                    if(not looking_for_closing_bracket or i+1 >= len(equation)):
                        try_next_position = True
                        looking_for_closing_bracket = False
                        continue
                    else:
                        if(equation[i+1] == '^'):
                            closing_bracket_location = i
                            was_expanded = True
                            variable_1 = '('
                            variable_2 = '('
                            variable_1 += equation[starting_position+1:plus_minus_location]
                            variable_2 += equation[plus_minus_location+1:closing_bracket_location]
                            variable_1 += ')'
                            variable_2 += ')'
                            #INSTEAD OF USING THE IN-BUILT aA-zZ STORAGES, A VARIABLE WITH A LONG NAME (supercalifragilisticexpialidocious_1) IS USED AS A PLACEHOLDER
                            #THE VARIABLE IN THE EXPRESSION IS TEMPORARILY STORED IN THE PLACEHOLDER
                            placeholder1 = "supercalifragilisticexpialidocious_1"
                            placeholder2 = "supercalifragilisticexpialidocious_2"
                            N = ''
                            n = i+2
                            while str.isnumeric(equation[n]):                        
                                N += equation[n]
                                n += 1
                                if(n >= len(equation)):
                                    break
                            N = int(N)
                            if (N != 0):
                                plugin = '('
                                plugin += binomial_expand("supercalifragilisticexpialidocious_1","supercalifragilisticexpialidocious_2",N)
                                plugin += ')'
                            else:
                                #print("power was zero")
                                plugin = '(1)'
                            plugin = plugin.replace(placeholder1,variable_1)
                            plugin = plugin.replace(placeholder2,variable_2)
                            old_text = equation[starting_position:n]
                            #print(old_text)
                            #print(plugin)
                            equation = equation.replace(old_text,plugin)
    return equation



###BIDMAS(BODMAS) & FUNCTIONS EVALUATION
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

#DEFINE FUNCTIONS & OPERATORS
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
    'atan': Operator(1, 1, lambda a: [math.atan(a)]),
    'asinh': Operator(1, 1, lambda a: [math.asinh(a)]),
    'acosh': Operator(1, 1, lambda a: [math.acosh(a)]),
    'atanh': Operator(1, 1, lambda a: [math.atanh(a)])

}

OPERATORS = set(['+', '-', '*', '/', '(', ')','^']) #establish the operators for infix_to_postfix function
OPERATORS_STRING = ['sin','cos','tan','sinh','cosh','tanh','exp','sqrt','asin','acos','atan','asinh','acosh','atanh'] #establish the trigonometric, hyperbolic functions
#PRIORITY --> sets the priority of operations for the 'infix_to_postfix' function, according to the BIDMAS rule
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3, 'sin':4, 'cos':4, 'tan':4,'sinh':4, 'cosh':4, 'tanh':4, 'exp':4, 'sqrt':4, 'asin':4, 'acos':4, 'atan':4, 'asinh':4, 'acosh':4, 'atanh':4}
def infix_to_postfix(infix): #re-order expression
    debug(infix) #calls debug function to observe
    stack = [] #create stack to sort the order of operations and store it
    postfix = '' #postfix is initially declared as empty (nothing)
    equation = '' #equation is initially declared as empty (nothing)
    word = '' #word is initially declared as empty (nothing)
    for i in infix: #loop to ignore spaces and only copy over non spaced letters
        if(i != ' '):
            equation += i
    prevv= '+'#making sure it handles starting negative numbers well    
    for v in equation: #read the current character
        if (str.isalpha(v) or (v == '_')): #check if v is a letter in the alphabet or an underscore (for words such as x_init)
            word += v #if v is a letter build up a word
            continue #keep building up the word until there are no more letters in the input equation
        else:
            if(word != ''): #check if a word has been built up
                debug(word) #calls debug function to observe the word at this point
                #check if there was a number before
                if prevv not in OPERATORS:
                    stack.append('*')
                    postfix+=' ';
                stack.append(word) #add the built up word to the stack
                word ='' # reset the word list so that it is empty and ready to check for the next word in the equation
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
            debug("error while evaluating: "+c)
            try:
                operator = operators[c]
                operator(stack)
            except KeyError:
                raise ValueError("Invalid character(s) {}".format(c))
    return stack

###CONVERT ALL A-Z CHARACTERS TO LOWERCASE 
def convert_equation(expr): #converts the entire expression so that the trig functions are passed to the evaluation in its shortened formats, i.e: 'cos' instead of 'cosine'
    equation = ''
    for i in expr: #delete spaces from equation
        if(i != ' '): #if it is not a space then add it to the new equation
            equation += i
    expr = equation
    exprl = expr.lower() #changes the input expression into only lowercase so that the program can deal with any input format, i.e: uppercase or lowercase or a mixture of both
    cos = 'cos('
    cosine = 'cosine('
    sin = 'sin('
    sine = 'sine('
    tan = 'tan('
    tangent = 'tangent('
    if cosine and sine and tangent in exprl: #checks for all three trig functions in the expression to prioritise replacement order to prevent overlap
        exprlc = exprl.replace(cosine,cos) #replace any 'cosine' in the equation with 'cos' first as there is sine in the word cosine which would cause the result to be cosin
        exprls = exprlc.replace(sine,sin) #replace any 'sine' in the equation with 'sin' second
        exprlt = exprls.replace(tangent,tan) #replace any 'tangent' in the equation with 'tan' last
        out = exprlt #use this output for further evaluation if all trig functions are in the equation
        return out
    elif cosine and sine in exprl: #if only cosine and sine in the expression, proceed to next step:
        exprlc = exprl.replace(cosine,cos) #replace any 'cosine' in the equation with 'cos' first as there is sine in the word cosine which would cause the result to be cosin
        exprls = exprlc.replace(sine,sin) #replace any 'sine' in the equation with 'sin' second
        out = exprls #use this output for further evaluation if this 'if' function is used
        return out
    else:
        out = exprl #if no conversion is necessary use this output where the expression has been converted to lowercase
        return out

###DERIVATIVE 
def derivative(term,base): #user is required to enter the equation (term) and the variable to be integrated with (base)
    base_orig = base # normally the differentiation only works for powers, but we store the base for now
    coef_orig = '' #in case of non-numerical equation, the whole thing is to be treated as algebra
    exp_orig = '' #in case the powers have algebra
    print()
    print('Running derivative()')
    print(term)
    print(base)
    base = base + '^'; #extending the base with the power to use to split the equation into multiplier and power
    if base in term: #if the have both the base variable and power char in the equation 
        try: #see if all integers
            coef = int(term.split(base)[0])
        except: #if int parsing failed then initiate algebra mode
            coef_orig = term.split(base)[0] #store the algebra
            coef = 1 #do the math with multiplier of one for now
        try:
            exp = int(term.split(base)[1])#either way, the exponent is stored and int parsed
        except:
            exp_orig = term.split(base)[1] #if int parsing failed we have algebra at our hands
            exp = 1 #give it a value despite not being used
        print('')
        print('term: ', term)
        print('coef: ', coef)
        print('exp: ', exp)
        if (exp_orig != ''): #full on algebra
            newcoef = '('+str(coef) + '*' + exp_orig+')' #creating the new multiplier algebraicly
            newexp = '('+exp_orig+'-1)'; #creating the new exponent algebraically
        else:
            newcoef = coef * exp #in differentiation the value of exponent gets decreased by one, while the multiplier is multiplied with the former value of exponent
            newexp = exp - 1 #decrease by one
        if exp == 2: #special case, after differentiation we leave the power
            newterm = str(newcoef) + base_orig #assembly of the equation with new multiplier and the original variable we differentiated by
        else:
            newterm = str(newcoef) + base + str(newexp) #if no special case happened we assemble the multiplier, with the base and power sign and the new power
        if(coef_orig != ''):
            newterm = coef_orig +'*'+ newterm #in case the algebraic multiplier storage contains anything we extend the new equation with it and a multiplier character for clarity
        return str(newterm)
    elif base_orig in term: #if no powers are in the equation, the differentiation result is the multiplier part only
        coef = term.split(base_orig)[0]
        newterm = coef
        return str(newterm)
    else: #in case the base were not in the equation, then the output is a constant and is driven to zero
        print('term: ', term)
        return '0'

###INTEGRATE
def integrate(term,base): #user is required to enter the equation (term) and the variable to be integrated with (base)
    base_orig = base # normally the integration only works for powers, but we store the base for now
    coef_orig = '' #in case of non-numerical equation, the whole thing is to be treated as algebra
    exp_orig = '' #in case of non numerical exponent
    print()
    print('Running integration()')
    print(term)
    print(base)
    base = base + '^';#extending the base with the power to use to split the equation into multiplier and power
    if base in term:#if the have both the base variable and power char in the equation 
        try:#see if all integers
            coef = int(term.split(base)[0])
        except:#if int parsing failed then initiate algebra mode
            coef_orig = term.split(base)[0]
            coef = 1
        try:#try integer parsing the power
            exp = int(term.split(base)[1])
        except: #if not, then consider it 1 for math purposes and no algebra yet
            exp = 1
            exp_orig = term.split(base)[1]
        print('')
        print('term: ', term)
        print('coef: ', coef)
        print('coef_orig:', coef_orig)
        print('exp: ', exp)
        
        if (exp_orig != ''): #full on algebra
            newexp = '('+exp_orig+'+1)'; #creating the new exponent algebraicly
            newcoef = '('+str(coef) + '/' + newexp+')' #creating the new multiplier algebraically
        else:
            newexp = exp + 1 #increment power
            newcoef = coef / (exp+1) #applying the algebra of dividing by the increment of the power
        newterm = str(newcoef) + base + str(newexp) #rebuild the new equation
        if(coef_orig != ''):
            newterm = coef_orig +'*'+ newterm #if algebra happened in multiplication 
        return str(newterm)
    elif base_orig in term: # if no powers
        try:
            coef = int(term.replace(base_orig,'')) #splitting does not work, so remove the base from term
        except:
            coef_orig = term.replace(base_orig,'') #if multiplier was not int parseable then treat it as algebra
            coef = 1
        exp = 1
        print('')
        print('term: ', term)
        print('coef: ', coef)
        print('exp: ', exp)
        newcoef = coef / (exp+1) #no need for elgebra here, exponent is always 1
        newexp = exp + 1 #increment it 
        newterm = str(newcoef) + base + str(newexp) #assemble equation
        if(coef_orig != ''):
            newterm = coef_orig + '*' + newterm #add algebra part back
        return str(newterm)
    else: #in case the equation did not contain the base, then we just add it in
        print('term: ', term)
        newexp = term + base_orig
        return newexp

###EVENT DRIVEN PROGRAM - RUNS THE ENTIRE CODE TO PRODUCE THE GUI BOX FOR THE USER TO INTERACT WITH
if __name__ == "__main__": #parent is defined since main is executed when the program is run from the command line
    smc = GUI(None) #(none) represents how no parent is given as this is the first GUI element built
    smc.title('Expression Evaluator') #title of the GUI application block defined here
    smc.mainloop() #indefinite loop to wait for the users action and produces an instant result
