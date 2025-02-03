# I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic integrity

class Stack:
    # Defining initialization values
    def __init__(self):
        # Intializing the array, the top value, and a max size value
        self.max_size = 10
        self.stack_array = [None] * 10
        self.top = 0

    # Defining sizeOf function, that returns the current size of the Stack
    def sizeOf(self):
        return self.top
    
    # Defining isFull function which returns if the stack is full
    def isFull(self):
        return self.top == self.max_size - 1

    # Defining isEmpty which returns if the stack is empty
    def isEmpty(self):
        return self.top == 0

    # Defining push which allows a value to be pushed onto the top of the stack
    def push(self, item):
        # If the stack is full, then we increase the size of the stack
        if(Stack.isFull(self)):
            # I create a new array of double the size, then move values of stack into the new array, adjust the max size value, and set the new array to the stack's array
            array_size = self.max_size * 2
            new_array = [None] * array_size
            for x in range(self.max_size):
                new_array[x] = self.stack_array[x]
            self.stack_array = new_array
            self.max_size = array_size

        # Set the current top of the stack to the input, and increment the top value
        self.stack_array[self.top] = item
        self.top = self.top + 1

    # Defining pop which removes the value at the top of the stack and returns it
    def pop(self):
        # Returns an error if the stack is empty
        if self.isEmpty():
            raise IndexError("Trying to pop empty stack")
        pop_val = self.stack_array[self.top - 1]
        self.stack_array[self.top] = None
        self.top = self.top - 1
        return pop_val
        
    # Defining __str__ such that the stack can return as a string to console
    def __str__(self):
        return_var = ""
        for x in range(0, self.top + 1):
            if(self.stack_array[x] is not None):
                return_var = return_var + str(self.stack_array[x]) + " "
        return return_var

# Function 1

# This is defining the original 1st function
def FOne(n):
    if n > 1:
        if n % 2 == 0:
            FOne(n//2)
        else:
            FOne(3*n+1)
    print(n)

# Defining function 1 that uses the stack
def SFOne(n):
    # Initializing the stack
    S = Stack()
    # Pushing the value of n onto the stack
    S.push(n)
    # While loop to continue iterating till n is 1 or less
    while n > 1:
        # If n is divisable by 2, then divide it by 2 and push it onto the stack
        if n % 2 == 0:
            n = n // 2
            S.push(n)
        # Otherwise, multiply n by 3, add 1, then push it onto the stack
        else:
            n = (3 * n) + 1
            S.push(n)
    
    # After all values are added to stack, print the stack by popping each value 
    while not S.isEmpty():
        print(S.pop())

# Function 2
def FTwo(n):
    if n >= 6:
        FTwo(n // 3)
        FTwo(2 * n // 3)
    print(n)

# Defining function two that uses the stack
def SFTwo(n):
    # Initializing two seperate stacks; S is an intermediary stack while X holds the final values
    S = Stack()
    X = Stack()
    # Push the value of n onto S
    S.push(n)
    # While loop that iterates till S is empty
    while not S.isEmpty():
        # Popping the current value of S out into a variable
        n = S.pop()
        # Pushing the value popped from S into X
        X.push(n)
        # If n is greater than or equal to 6, push n // 3 and 2n // 3 onto S
        if n >= 6:
            S.push(n // 3)
            S.push(2 * n // 3)
    
    # Once S is empty, pop and print all values within X onto the console
    while not X.isEmpty():
        print(X.pop())



# Function 3

def FThree(a,b):
    if a <= b:
        m = (a+b)//2
        FThree(a, m-1)
        print(m)
        FThree(m+1,b)

# Defining function three that uses the stack
# This definition is different from the other stacks, as the output is printed during runtime and not after everything is stored in the stack; I spent a long
# time trying to figure it out as I had for the other functions but I couldn't :/
def SFThree(a,b):
    # Defining the stack S
    S = Stack()
    # Pushing the set of 3 values into the stack. The boolean value is used to have the print happen in the middle of the two recursive values
    S.push((a,b,False))
    # While loop that runs while S is not empty
    while not S.isEmpty():
        # Popping the value in S into 3 variables, where a = x, b = y, and z is the boolean
        (x,y,z) = S.pop()
        # If statement for the condition of the original for loop
        if x <= y:
            # Calculating the value of m
            m = (x+y) // 2
            # If the boolean is true, print m and push (m+1, y, False)
            if z:
                print(m)
                S.push((m+1,y,False))
            # If the boolean is false, then push (x,y,True) and (x,m-1,False) into the stack
            else:
                S.push((x,y,True))
                S.push((x,m-1,False))

    

# Function 4

def FFour(a,b):
    if a <= b:
        m = (a+b)//2
        FFour(a, m-1)
        FFour(m+1,b)
        print(m)

# Defining function four that uses the stack
def SFFour(a,b):
    # Defining the two stacks S and X
    S = Stack()
    X = Stack()
    # Pushing the inputted numbers into S
    S.push((a,b))
    # While loop that runs while S is not empty
    while not S.isEmpty():
        # Popping the value on the top of S into n and m
        (n,m) = S.pop()
        # Calculating the value of m from the original function into the variable x
        x = (n+m)//2
        # Running the condition from the original function
        if n <= m:
            # Pushing values into S, then pushing x into stack X
            S.push((n,x-1))
            S.push((x+1,m))
            X.push(x)
    # While X is full, pop the value in X and print it into the terminal
    while not X.isEmpty():
        print(X.pop())

# This is the test script that I used to print out both the results of the recursive and stack-based function to compare results for accuracy.
print("Function 1:")
print("")
print("n = 7:")
FOne(7)
print("")
SFOne(7)
print("")
print("n = 18:")
FOne(18)
print("")
SFOne(18)
print("")
print("n = 19:")
FOne(19)
print("")
SFOne(19)
print("")
print("n = 22:")
FOne(22)
print("")
SFOne(22)
print("")
print("n = 105:")
FOne(105)
print("")
SFOne(105)
print("")
print("")

print("Function 2:")
print("")
print("n = 7:")
FTwo(7)
print("")
SFTwo(7)
print("")
print("n = 18:")
FTwo(18)
print("")
SFTwo(18)
print("")
print("n = 19:")
FTwo(19)
print("")
SFTwo(19)
print("")
print("n = 22:")
FTwo(22)
print("")
SFTwo(22)
print("")
print("n = 43:")
FTwo(43)
print("")
SFTwo(43)
print("")
print("")

print("Function 3:")
print("")
print("(a,b) = (0,7):")
FThree(0,7)
print("")
SFThree(0,7)
print("")
print("(a,b) = (1,18):")
FThree(1,18)
print("")
SFThree(1,18)
print("")
print("(a,b) = (4,19):")
FThree(4,19)
print("")
SFThree(4,19)
print("")
print("(a,b) = (-1,22):")
FThree(-1,22)
print("")
SFThree(-1,22)
print("")
print("")

print("Function 4:")
print("")
print("(a,b) = (0,7):")
FFour(0,7)
print("")
SFFour(0,7)
print("")
print("(a,b) = (1,18):")
FFour(1,18)
print("")
SFFour(1,18)
print("")
print("(a,b) = (4,19):")
FFour(4,19)
print("")
SFFour(4,19)
print("")
print("(a,b) = (-1,22):")
FFour(-1,22)
print("")
SFFour(-1,22)
print("")
print("")



# This code was used during the initial development of my stack to test its various functions for whether they worked
'''
# Testing the stack
result_stack = Stack()

# Test push
result_stack.push(13)
result_stack.push(132)
print(result_stack)

# Test pop
result_stack.pop()
print(result_stack)
print(result_stack.pop())
print(result_stack)

# Test is empty
print(result_stack.isEmpty())
result_stack.push(1)
print(result_stack.isEmpty())

# Test is full
result_stack.push(2)
result_stack.push(3)
result_stack.push(4)
result_stack.push(5)
result_stack.push(6)
result_stack.push(7)
result_stack.push(8)
result_stack.push(9)
print(result_stack)
print(result_stack.isFull())
result_stack.push(10)
print(result_stack.isFull())

# Test bigger stack size

print(result_stack.sizeOf())
result_stack.push(11)
print(result_stack.sizeOf())
print(result_stack)
'''
