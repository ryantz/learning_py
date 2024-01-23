#In python, there is no need to declare variable type
# "=" assigns a value to a variable

name = "Ryan" 
number = 2 #this is a number
string_number = "2" #this is a string
fraction = 0.5

#creating variables with class constructors
name2 = str("Ryan")
number2 = int("23")
fraction2 = float("0.5")


#checking data type:
print(type(name) == str) #true
print(isinstance(name, str)) #true
print(type(fraction)) # <class 'float'>

frac_to_int = int(fraction2) #casting fraction to int
print(type(frac_to_int)) # <class 'int'>

# more data types: complex, bool, list, tuple, range, dict, set

