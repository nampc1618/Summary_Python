#num1 = int(input("Type num1: "))
#num2 = int(input("Type num2: "))

#num3 = num1 * num2
#print(num3)

#def Hello():
#    print("Nampc")
#    print("1618")
#Hello()

#def Main():
#    print("Started")
#    output = getInteger()
#    print("Number entered is: ",output)
    
#def getInteger():
#    result = int(input("Enter integer: "))
#    return result

#if(__name__=="__main__"):
#    Main()

#def CountNum():
#    for num in range(10):
#        if(num > 5 or num < 2):
#            print(num)
            
#def mainTest():
#    CountNum()

#if(__name__=="__main__"):
#    mainTest()


#import math

#def Main():
#    num = -85
    # fabs is used to get the absolute
    # value of a decimal
#    num = math.fabs(num)
#    print(num)
    
#if __name__ == "__main__":
#    Main()

# Python program to illustrate a list

# create a empty list
#nums = []
# appending data in list
#nums.append(1.618)
#nums.append("Nampc")
#nums.append("dz")
#nums.append(22)

#print(nums)

# create a empty dict
#Dict = []

# putting integer values
#Dict = {1: 'Vietnames', 2: 'English', 3: 'Catonese'}
#print(Dict[1])

#tup = ('Vietnamese', 22, "Chinese", 1.618)
#print(tup[3])

# import keyword as kw

# print("The list of keywords is: ")
# print(kw.kwlist)

# print(False == 0)
# print(True == 1)

# print(True + True + True)
# print(True + False + False)

# print(None == 0)
# print(None == [])

# print(True or False) # Return True

# print(False and True) # Return False

# print(not True) # Return False

# # Using "in" to check
# if 's' in 'Nampcs':
#     print("s is part of Nampcs")
# else:
#     print("s is not part of Nampcs")

# # Using "in" to loop through
# for i in 'Nampcs1.618':
#     print(i, end=";")

# print("\r")

# # using is to check object identify
# # string is immutable(cannot be changed once allocated)
# # hence occupy same memory location
# print(' ' is ' ')

# # using is to check object identify
# # dictionary is mutable(can be changed once allocated)
# # hence occupy different memory location
# print({} is {})

# for i in range(10):
#     print(i, end=" ")
#     if i == 6:
#         break
# print()
# i = 0
# while i < 10:
#     if i == 6:
#         i += 1
#         continue
#     else:
#         print(i,end=" ")
#     i += 1
# print()
# j = 20
# if j == 10:
#     print("j is 10")
# elif i == 20:
#     print("j is 20")
# else:
#     print("j is not present")

# Return keyword
# def fun():
#     S = 0
    
#     for i in range(10):
#         S += i
#     return S
# print(fun())

# Yield keyword
# def fun():
#     S = 0
    
#     for i in range(10):
#         S += i
#         yield S
# for i in fun():
#     print(i)

# class Keyword
# class Dog:
#     attr1 = "mammal"
#     attr2 = "dog"
    
#     def fun(self):
#         print("I'm a", self.attr1)
#         print("I'm a", self.attr2)
# Rodger = Dog()

# print(Rodger.attr1)
# Rodger.fun()

# class Student:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"[{self.id}] - {self.name} ({self.age} age)"
#     def __sizeof__(self):
#         return 100
#     def myFunc(self):
#         print("Hello my name is "+self.name)
        
# student1 = Student(1618, "Nampc", 30)
# student1.id = 1
# student1.name = "Nampcs"
# print(student1)
# print(student1.__sizeof__())
# print(student1.myFunc())

# using with statement
# file_path = ".\\test.txt"
# with open(file_path, 'w') as file:
#     file.write("Nampc")

# import math as gfg

# print(gfg.factorial(5))

# n = 10
# for i in range(n):
#     # do something
#     pass

# ld = lambda x: x*x*x
# ld2 = lambda y:(y + 20) * 10
# print(ld(10))
# print(ld2(12))

# import math
# print(math.factorial(10))

# from math import factorial
# print(factorial(20))

# a = 4
# b = 0

# try:
#     k = a//b # raise divide by zero exception
#     print(k)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally:
#     print("This is always executed")

# print("The value of a / b is: ")
# assert b != 0, "Divide by 0 error"
# print(a/b)

# var1 = 20
# var2 = "Nampc"

# print(var1)
# print(var2)

# del var1
# del var2

# print(var1)
# print(var2)


# a = 15 # global varibale
# b = 10 # global variable

# def add():
#     c = a + b
#     print(c)
# add()

# def fun():
#     var1 = 10
#     def gun():
#         nonlocal var1
#         var1 = var1 + 10
#         print(var1)
#     print(var1)
#     gun()
# fun()

# import keyword

# keys = ["for", "while", "Nampc", "break", "elif", "assert", "Catonese", "lambda", "None", "and", "global"
#         ,"finally", "nonlocal", "pass", "continue", "HappyNewYear"]

# for i  in range(len(keys)):
#     # checking which are keywords
#     if keyword.iskeyword(keys[i]):
#         print(keys[i] + " is python keyword")
#     else:
#         print(keys[i] + " is not python keyword")

# print(keyword.kwlist)
# print(keyword.kwlist.__len__())

# import sys

# sys.stdout.write("Nampcs ")
# sys.stdout.write("is the best company about technology in North Vietnam ")

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*lst)

# print("Nampc",end=" ")
# print("NampcNampcs")

# arr = [1, 2, 3, 4, 5]
# for i in range(5):
#     print(arr[i], end=" ")

# ----------------- CALCULATOR --------------------
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title("Calculator-Nampc")
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0,column=0, columnspan=3, ipady=2, pady=2)

def myClick(number):
    entry.insert(tk.END, number)
    
def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showerror("Error", "Syntax Error")
def clear():
    entry.delete(0, tk.END)

button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, command=lambda: myClick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, command=lambda: myClick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, command=lambda: myClick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, command=lambda: myClick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, command=lambda: myClick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, command=lambda: myClick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, command=lambda: myClick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, command=lambda: myClick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, command=lambda: myClick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, command=lambda: myClick(0))
button_0.grid(row=4, column=1, pady=2)
 
button_add = tk.Button(master=frame, text="+", padx=15,
                       pady=5, width=3, command=lambda: myClick('+'))
button_add.grid(row=5, column=0, pady=2)
 
button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myClick('-'))
button_subtract.grid(row=5, column=1, pady=2)
 
button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myClick('*'))
button_multiply.grid(row=5, column=2, pady=2)
 
button_div = tk.Button(master=frame, text="/", padx=15,
                       pady=5, width=3, command=lambda: myClick('/'))
button_div.grid(row=6, column=0, pady=2)
 
button_clear = tk.Button(master=frame, text="clear",
                         padx=15, pady=5, width=12, command=clear)
button_clear.grid(row=6, column=1, columnspan=2, pady=2)
 
button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=9, command=equal)
button_equal.grid(row=7, column=0, columnspan=3, pady=2)

window.mainloop()