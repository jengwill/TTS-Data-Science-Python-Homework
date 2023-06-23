#!/usr/bin/env python
# coding: utf-8

# <b> Exercises for Python Module 1 </b>
# 
# Make sure to comment all your code!

# Accept the user's first and last name and print them in reverse order with a space between them. 
# 
# Keyword hints: print function, input function, append, add, string

# In[6]:


firstname = input("enter your first name: ") #registering first command
lastname = input("enter your last name: ") #registering second command

full_name = lastname + " " + firstname #creating the output requirement

print("Reversed name:", full_name)


# Ask the user "What country are you from?" then print the following statement: "I have heard that [input] is a beautiful country!"

# In[8]:


country = input("What country are you from? ")

print("I have heard that " + country + " is a beautiful country!")


# Explain the output for:
# 
# x = 36 / 4 * (3 +  2) * 4 + 2

# In[4]:


x = 36 / 4 * (3 + 2) * 4 + 2

r1 = 36 / 4
r2 = 3 + 2
r3 = r1 * r2
r4 = r3 * 4
r5 = r4 + 2 #explaing to python what all of the results are supposed to be

print("First: 36 / 4 =", r1) #doing the arithmetic w orders of operations and inserting result
print("Second: 3 + 2 =", r2)
print("Third:", r1, "*", r2, "=", r3)
print("Fourth:", r3, "* 4 =", r4)
print("Fifth:", r4, " + 2 =", r5)
print("Finally: x =", r5) #telling it the final result


# What is the output of the following code and what arithmetic operators is being used here? 
# 
# print(2%6)

# the output is 2 and the arithmetic operators being used are modular operators 

# What is the output of the following code and what arithmetic operators are used here? 
# 
# print(2 * 3 ** 3 * 4)

# the output of this code is 216 and the arithmetic operators being used are the mulitplication operator and the exponential operator

# Accept an integer (n) and compute the value of n+nn+nnn. For example, if n = 4, then n+nn+nnn should equal 492. 
# 
# Keyword hints: Hint(4+44+444)

# In[3]:


n = input("what is the number?") #to be honest i used your example in class
print(n)
print(n+n)
print(type(n))

#print(n+nn+nnn)
x=n
y=n+n
z=n+n+n

print(x)
print(y)
print(z)
print(int(x)+int(y)+int(z))


# What is an IDE?

# An IDE is an integrated development environment that is utilized for software development. uses building/testing/packaging

# What is a Text Editor?

# tool for changing text - can be used to highlight, auto-indent, search-and-replace, etc. 

# What is  filepath?

# In[ ]:


name that identifies location of a file


# Describe Python as a programming language?

# python is a user-friendly programming language that, while being a bit old, is really helpful for beginners.

# What is Jupyter Notebook, and how does it differ from other IDEs such as VSCode?

# Jupyter Notebook is what I'm currently on. It is also a browser user-interface that is obtained through the Anaconda-Navigator. It's helpful because it combines Python and whatever-else you want to put on here to create either an interactive notebook or whatever else your heart desires. Jupyter notebook differs as it allows you to run cells in the interface and is a lot easier than the other options. 

# What is the difference between a "code" cell (at the top of your notebook) and a "markdown" cell?

# code cell activates python, the markdown cell lets you type normally.

# Describe each operator catagory: (Notebook 01_03)

# Arithmetic Operations: basic math operations on intergers like + - * etc.
# 
# Bitwise Operations: logical operations on integers
# 
# Assignment Operations: using the = operator you can assign different variables with different operators attached to the = 
# 
# Comparison Operations: you can use the typical arthimetic comparators like =, <, <=, >, and it will return boolean values of true or false
# 
# Boolean Operations: and/or/not operators to combine values
# 
# Identiy and Membership Operators: prose-like operators to check for 
# identical/differents numbers and membership within compound objects. 

# Describe what the phrase "everything is an object" means in Python; what is an object?

# everything is an object in terms of python means that every bit of information you put into python is considered an object. this is helpful because it allows for consistency and quicker registering of what you're trying to code along with easy-readability. 
