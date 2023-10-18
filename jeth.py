# Lesson 1: Print Any Output

# print("Chez and Cupcake")
# print("I loved  MENU in short Me n U eheheh")



#Lesson 2: Variables nd Different data types

# #Variable = used to store different values
#Variables and data types
# name = "Jether"
# age = "19"
# birthdate = "October 21, 2003"
# address = "Kipit Labason Zamboanga Del Norte"
#
#
# print("Hello everyone my name is " + name)
# print("I am " + age + "years old")
# print("I was born on " + birthdate)
# print("I lived in " + address)
#
#
# #revised code
# print("Revise Code")
#
#
# first_name = " Jether "
# last_name = " Bagor "
# full_name = first_name + last_name
# print(full_name)
#
#
#
# ccs_day = "Good day everyone "
# c_day = "Welcome to CCS "
# s_day = "Day!!!"
# wow_day = ccs_day + c_day + s_day
#
# print(wow_day)
#
#



#Int Data Type
#integer,float and double
# age = 19
# age += 1
# print(age)

#used type function to know what kind of data type you used

# print(type(age))

#print output to convert string into integer
#
# age = 19
# age += 10
#
# print("You are " + str(age) + " years old")


#Float data type = floating point number(Decimal number)
#It is a numeric value that can store  a number that includes decimal portion

# height = 5.5
# print("your height is " + str(height)+ " Feet and it will be added to compute your BMI")
# print(type(height))



#Bolean = used to store values whether true or false

# print("Is Jether a true human?")
# jether = True
# print("Congrats to Jether bekos he is " + str(jether) + " Human")
# print(type(jether))







#Lesson 3: Multiple Assignment
#Multiple assignment = allows us to store multiple variables at the same time in a one line of code

# name = "Chez"
# date = 34
# yes = False

# #Revised code
# name,date,yes = "Chez", 34 , False
# print(name)
# print(date)
# print(yes)
#
# #If you wanted to make and store the same value into different variables
#
# jeth = name = chez = 12
#
# print(jeth)
# print(name)
# print(chez)



# Lesson 4: Variable Demonstration
# print("Variable Demonstration")
# #Variable Demonstration
# name = "Jether Bagor"
# print(len(name))             #To print the length of the value of  variable name
# print(name.find("r"))      #To find or to count the index of the value of variable name
# print(name.capitalize()) #To capitalize only the first later of the variable name "jether"
# print(name.upper())       #Used to mae the variable name value into uppercase letter
# print(name.lower())        #Used to make the value of variable name into lowercase letter
# print(name.isdecimal()) #Used to check if the value of the variable name is decimal or not using isdigit() and isdecimal() function
# print(name.isalpha())     #Used to check to see if your string contains only letter and no spacing
# print(name.count("t"))      #Check to see if how many characters are there in the string
# print(name.replace("e", "o"))  #used to change the character of the variable name value
# print(name * 3)                 #Used to print your output in multiple times





#Lesson 5  Type Casting = convert the data type of a value to another data type
#You can change the value into another data type such as string, float and Integer
# a  = 0.7
# b  = 18
# c  = "21"
#
# a_int = int(a)
# b_str = float(b)
# c_int = float(c)
#
# print(a_int)
# print(b_str)
# print(c_int*4)

# print("Convert the values  in this arrangement Int,string, and float")
# j = 78.8
# c = 90
# b = "56"

# j_int = int(j)
# c_str = str(c)
# b_float = float(b)
#
# print(j_int)
# print(c_str)
# print(b_float)



#
# j_int = int(j)
# c_str = float(c)
# b_float = float(b)
#
# print(j_int*4)
# print(c_str - 2)
# print(b_float-1)


#
# #Lesson 6: accept some user input in python
# print("Lesson 6: Accept some user input using the Input(function) ")
#
# jeth = input("What do you want me to do?:  ")
# hi = float(input("What is the length of the oval from end to end?: "))
#
# print("I dont want you to say " + jeth + "!")
# print("Gotcha! " + str(hi) + "meters is correct!")



#Lesson 7: Import Module
print("Lesson 7 Import module")
# import math

# pi = 3.14159
# a = 45
# b = 78.6
# c = 37
# # print(round(pi))       #Is a built in function used to round up nmbers to its newest value
# print(math.ceil(pi))       #Just put the import "MATH" inside the print function and next is input .ceil function  to round up a number
# print(math.floor(pi))    #.floor function is a built in function inside the math and it is used to round down a number
# print(abs(pi))                 # abs function is a math function that will give you an absolute value of a number
# print(pow(pi,3))                  # A pow function will raise  a base number to a power ... we made two arguments a BASE and EXPONENT
                                           #so PI is the base and 3 is the exponent


# print(math.sqrt(780))         #this sqrt function is located in math module and sqrt is another term for square root so sqr of the constant value of the variable PI
# print(max(a,b,c,pi))           #Max function will find the largest of varying amount of  values.. lets say for an instance I inputted three different numbers and this MAX function will find and print the largest number
                                           # Whe using a max functon we need to create three arguments  and so on and so forth...


# print(min(a,b,c,pi))                        # min function is  used to find and print the minimum and or lowest number of inptted or constant values in the variables


jeth = float(input("Input a number: "))
jet = float(input("Input a number: "))
chez = float(input("Input a number: "))


# print(max(jeth,jet,chez ))
# print(min(jeth,jet,chez))




largest_num = max(jeth,jet,chez)
smallest_num = min(jeth,jet,chez)
print("The largest number is", largest_num)

print("and the smallest number is ", smallest_num )








#Problems:
#Print Sentences
#Print different values in data types
#Can print the different kinds of data types

#Prob.1 Printing values
#Introduce yourself
first_name = " Jether "
middle_name = " Cabilin "
last_name = " Bagor "
age = 19
birthdate = "October 21, 2003"
address = "Kipit Labason Zamboanga Del Norte"
hate = "Hard Headedness"
like = " Imissyoumore "
annoying_things = " I hate you "

full_name = first_name +  middle_name + last_name

print("Good day everyone! I am " + full_name + "cute nga "+ str(age))
print("I was born on  " + birthdate + " I lived in")
print(address)
print("I hate " + hate + " People")
print("I liked " + like + "and the annoying things that i dont want to hear was " + annoying_things)

#pro.2 Data type Check
#function used to chck the data type of a variable
print(type(full_name))
print(type(age))



#Prob.3 The difference  between floating point numbers and integer
a = 31
b = 45.9

print(str(a) + " Is  Integer because it doesnt have any decimal numbers")
print(str(b) + " Is floating point number because it stores number with decimal")


#Prob.4 Print the possible values of a Bolean variable
print("Hey Kit is  Jether is your first name and  Talisik is your last name?")
jether =  True
talisik = False

print(str(jether) + " My first name is Jether ")
print("But Talisik is " + str(talisik) + " Because my last name is Bagor")

#Prob.5 String, Integer, and Float Concatenation

name = " Chez and  "
other_name = "Cupcake"
nick_name = name + other_name
print(nick_name)
#This declarations are equal to str1 and str2 in the given problem

a = 23
b = 56.7
c = a + b
print(c)



# Prob.6 How to print Address data type
address = " Kipit Labason Zamboanga Del Norte "
print(address)


#Additional learnings:
#Type Conversion and Type Casting
#Type Conversion = convert an integer variable x into a floating-point number
#Type Casting = used to explicitly cast  variable to a different data type in python


a = 40
b = 50.9

float_a = float(a)
int_b = int(b)

print(float_a)
print(int_b)