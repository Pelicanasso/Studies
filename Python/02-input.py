#Command input can be add to variables for them to store the information in it
name = input("Type a name:")

#There are many ways to print a text with a variable in python
#1 - Using character formaters like in C, the '%s' works as a placeholder, then he will put the variable I declare in the end
print("Hello %s, here you will start your journey with python" % (name))
#2 - Using the format function
print("Hello {}, here you will start your journey with python".format(name))
#3 -Using formated strings
print(f"Hello {name}, here you will start your journey with python")