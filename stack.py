def createStack():
	stack=[]
	return stack

# Function to determine the size of the stack
def size(stack):
	return len(stack)

# Stack is empty if the size is 0
def isEmpty(stack):
	if size(stack) == 0:
		return True

# Function to add an item to stack .
# It increases size by 1
def push(stack,item):
	stack.append(item)

#Function to remove an item from stack.
# It decreases size by 1
def pop(stack):
	if isEmpty(stack): return
	return stack.pop()

# A stack based function to reverse a string
def reverse(string):
	n = len(string)

	# Create a empty stack
	stack = createStack()

	# Push all characters of string to stack
	for i in range(0,n,1):
		push(stack,string[i])

	# Making the string empty since all
	#characters are saved in stack
	string=""

	for i in range(0,n,1):
		string+=pop(stack)

	return string
string="levissssasdasd"
string = reverse(string)
print("Reversed string is " + string)
