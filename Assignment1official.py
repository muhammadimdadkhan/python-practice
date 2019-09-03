#!/usr/bin/env python
# coding: utf-8

# ## 1. Calculate Area of a Circle

# #### Write a Python program which accepts the radius of a circle from the user and compute the area.
# ###### Program Console Sample Output 1:
# ###### Input Radius: 0.5
# ###### Area of Circle with radius 0.5 is 0.7853981634

# In[1]:


r = int((input("Enter the radius in cms")))
Area = 3.147 * r**2
print (str(Area)+"cm^2")


# In[ ]:





# In[ ]:





# ## 2. Check Number either positive, negative or zero

# #### Write a Python program to check if a number is positive, negative or zero
# ###### Program Console Sample Output 1:
# ###### Enter Number: -1
# ##### Negative Number Entered
# ###### Program Console Sample Output 2:
# ##### Integer: 3
# ##### Positive Number Entered
# ###### Program Console Sample Output 3:
# ##### Integer: 0
# ###### Zero Entered

# In[2]:


a = int(input("Enter a number  "))
if  a == 0:
    print ("Zero entered")
elif  a<= 0 :
        print ("Negative number entered")
else:
        print ("Positive number entered")


# In[ ]:



        


# ## 3. Divisibility Check of two numbers

# #### Write a Python program to check whether a number is completely divisible by another number. Accept two integer values form the user
# ##### Program Console Sample Output 1:
# ###### Enter numerator: 4
# ###### Enter Denominator: 2
# ##### Number 4 is Completely divisible by 2
# ###### Program Console Sample Output 2:
# ##### Enter numerator: 7
# 
# ##### Enter Denominator: 4
# ###### Number 7 is not Completely divisible by 4

# In[5]:


numerator = int(input("Enter numerator"))
denominator = int(input("Enter denominator"))
d = (numerator % denominator)
print (d)
if d== 0:
    print ("The numerator is completely divisible by denominator.")
else:
    print ("The division has "+str(d)+" remainder and the numerator is not completely divisible.")


# In[ ]:





# In[ ]:





# In[ ]:





# ## 4. Calculate Volume of a sphere

# ##### Write a Python program to get the volume of a sphere, please take the radius as input from user

# ##### Program Console Output:
# ##### Enter Radius of Sphere: 1
# ###### Volume of the Sphere with Radius 1 is 4.18

# In[6]:


radius = float(input("Enter the radius of the sphere in cms "))
V = (4/3 * 3.147 * radius**3)
print(str(V)+"cm^3")


# In[ ]:





# In[ ]:





# ## 5. Copy string n times
# #### Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# ##### Program Console Output:
# ##### Enter String: Hi
# ###### How many copies of String you need: 4
# ###### 4 Copies of Hi are HiHiHiHi

# In[7]:


l=(input("Enter a phrase "))
n = int(input("No. of copies required"))
print (l*n)


# In[ ]:





# In[ ]:





# ## 6. Check if number is Even or Odd
# ### Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
# #### Program Console Output 1:
# ##### Enter Number: 4
# ###### 4 is Even
# #### Program Console Output 2:
# ##### Enter Number: 9
# ###### 9 is Odd

# In[8]:


g = int(input("Enter a number "))
o = (g%2)
print (o)
if o==0:
    print(str(g)+" is an even number")
else:
    print(str(g)+" is an odd number")


# In[ ]:





# In[ ]:





# ## 7. Vowel Tester
# ### Write a Python program to test whether a passed letter is a vowel or not
# #### Program Console Output 1:
# ##### Enter a character: A
# ###### Letter A is Vowel
# #### Program Console Output 2:
# ##### Enter a character: e
# ###### Letter e is Vowel
# #### Program Console Output 2:
# ##### Enter a character: N
# ###### Letter N is not Vowel

# In[10]:


c = (input("Enter a letter "))
if   c == ("a"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("e"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("i"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("o"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("u"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("A"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("E"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("I"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("O"):
    print ("Letter "+str(c)+" is a vowel.")
elif c == ("U"):
    print ("Letter "+str(c)+" is a vowel.")
else:
    print ("Letter "+str(c)+" is a consonant.")


# In[ ]:





# ## 8. Triangle area
# ### Write a Python program that will accept the base and height of a triangle and compute the area
# ###### Reference:
# https://www.mathgoodies.com/lessons/vol1/area_triangle

# In[11]:


H = int(input("Enter the height of a triangle in cms "))
B = int(input("Enter the base of a triangle in cms"))
Area_triangle = ((H*B)/2)
print (str(Area_triangle)+" cm^2")


# In[ ]:





# In[ ]:





# ## 9. Calculate Interest
# ### Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years
# #### Program Console Sample 1:
# ##### Please enter principal amount: 10000
# ###### Please Enter Rate of interest in %: 0.1
# ###### Enter number of years for investment: 5
# ###### After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1

# In[12]:


Principal = float(input("Enter the amount of loan in Rs. "))
rate_per_year = float(input("Enter the rate of interest "))
t = int(input("Enter number of years "))
A = (Principal*(1+r*t))
print (str(A))


# In[ ]:





# In[ ]:





# In[ ]:





# ## 10. Euclidean distance
# ### write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# #### Program Console Sample 1:
# ###### Enter Co-ordinate for x1: 2
# ###### Enter Co-ordinate for x2: 4
# ###### Enter Co-ordinate for y1: 4
# ###### Enter Co-ordinate for y2: 4
# ###### Distance between points (2, 4) and (4, 4) is 2

# ###### Reference:
# https://en.wikipedia.org/wiki/Euclidean_distance

# In[14]:


import math
print("Enter point 1 coordinates")
x1 = int(input("x1: "))
y1 = int(input("y1: "))
print("Enter point 2 coordinates")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
p = (x2-x1)**2
print( p ) 
q = (y2-y1)**2
print( q )
a = p + q
print(a)
dist = math.sqrt(a)
print( "distance between point 1 (" + str(x1) + ", " + str(y1) + ") and point 2 (" + str(x2) + ", " + str(y2) + "): " + str(dist) )


# ## 11. Feet to Centimeter Converter
# ### Write a Python program to convert height in feet to centimetres.
# ##### Program Console Sample 1:
# ###### Enter Height in Feet: 5
# ###### There are 152.4 Cm in 5 ft
# ###### Reference:
# https://www.rapidtables.com/convert/length/feet-to-cm.html

# In[15]:


height = int(input("Enter height in feet"))
cm=((height)*30.48)
print(str(cm)+"cms")


# In[ ]:





# In[ ]:





# ## 12. BMI Calculator
# ### Write a Python program to calculate body mass index
# ##### Program Console Sample 1:
# ###### Enter Height in Cm: 180
# ###### Enter Weight in Kg: 75
# ###### Your BMI is 23.15

# In[18]:


Height= float(input("Enter height in meters "))
Weight= int(input("Enter weight in kgs"))
BMI = Weight/(Height)**2
print(str(BMI)+"kg/m^2")


#  
#  

# ## 13. Sum of n Positive Integers
# ### Write a python program to sum of the first n positive integers
# #### Program Console Sample 1:
# ###### Enter value of n: 5
# ###### Sum of n Positive integers till 5 is 15

# In[19]:


i = int(input('Enter a number: '))
for e in range(i):
    i = i + e
    e-=1
print(i)


# In[ ]:





# ## 14. Digits Sum of a Number
# ### Write a Python program to calculate the sum of the digits in an integer
# #### Program Console Sample 1:
# ##### Enter a number: 15
# ###### Sum of 1 + 5 is 6
# #### Program Console Sample 2:
# ##### Enter a number: 1234
# ###### Sum of 1 + 2 + 3 + 4 is 10

# In[20]:


w= str(input("Enter number to calculate sum of "))
sum = 0
for i in w:
    sum = sum + int(i)
print('sum:', sum)


# In[21]:


##Question 15

b = int(input('Enter decimal number: '))
print(bin(b).replace("0b",""))


# In[24]:


##Question 16

b = int(input('Enter decimal number:'))
print(bin(b).replace("0b",""))


# In[25]:


## Question 17
string = input("Enter a string : ")
v = 0
c = 0

for w in string:
    if(w == 'a' or w == 'e' or w == 'i' or w== 'o' or w == 'u' or w == 'A' or w == 'E' or w == 'I' or w == 'O' or w == 'U'):
        v = v + 1
    else:
        c = c + 1
 
print("Total Number of Vowels: ", v)
print("Total Number of Consonants: ", c)


# In[27]:


##Question 18
s = input("Enter a string: ")
s = s.casefold()
str_rev = reversed(s)

if list(str_rev) == list(s):
    print("The input value is palindrome")
else:
    print("The input value is not palindrome")


#  

# In[28]:


##Question 19
s = input("Enter a string: ")
a =0
d = 0
sp = 0

for i in range(len(s)):
    if(s[i].isalpha()):
        a = a + 1
    elif(s[i].isdigit()):
        d = d + 1
    else:
        sp = sp + 1
        
print("\nNumber of Alphabets: ", a)
print("Number of Digits: ", d)
print("Number of Special Characters: ", sp)


# In[29]:


##Question 20
a = 1
i = "*"
while a <= 4:
    print(i * a)
    a += 1
while a > 0:
    print(i * a)
    a -= 1


# In[47]:


##Question 21
r=1
c=1
for r in range(1, 6):
    for c in range(1, r + 1):
        print(c, end=' ')
    print("\n")
r=4
for i in range (r,0,-1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("\n")


# In[56]:


for i in range(10):
    for j in range(i):
        print (i," ", end="") 
    print("\n")


# In[ ]:




