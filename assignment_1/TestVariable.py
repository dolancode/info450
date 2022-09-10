#1. This should print the sentance from the variable test
test = "Python error messaging is annoying."
print(test)

#2.  This should print the message 'One of Python's strengths is its diverse community.' in the output
message = "'One of Python's strengths is its diverse community.'"
print(message)

#3. This should print the LAST element of *any* string named "this". 
# The code currently outputs the first element in the string.

#EXAMPLE: If I input "testing" my output should be "g", if I input "this" it should output "s"

this = input("type a string name: ")
last_element = this[-1]
print(last_element)

# 4. Create a basic function using inputs that takes ANY two INTEGERS and will multiply them together, 
# coerce the final data type to be an INTEGER.
def multiply(x: int, y: int):
    return int(x * y)

y = input("input first integer:")
x = input("input second integer:")

y = int(y)
x = int (x)

print(multiply(x,y))

#5. Write a function that will take ANY string provided as an input, reverse it, and make the output ALL CAPITALIZED.
# EXAMPLE: weinstein -> NIETSNIEW  
s = input("input a string")

def reverse_capitalize(str: str):
    return str[::-1].capitalize()

print(reverse_capitalize(s)) 
