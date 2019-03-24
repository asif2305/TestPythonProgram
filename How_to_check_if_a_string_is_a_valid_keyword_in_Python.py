#Python code to demonstrate working of iskeyword() 
"""
python keyword:
False, elif, lambda,
None, else, nonlocal,
True, except, not,
and, finally, or,
as, for, pass,
assert, from, raise,
break, global, return,
class, if, try,
continue, import, while,
def, in, with,
del, is, yield,
"""
# importing "keyword" for keyword operations 
import keyword 

# initializing strings for testing 
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"
s6 = "shambhavi"
s7 = "True"
s8 = "False"
s9 = "akshat"
s10 = "akash"
s11 = "break"
s12 = "ashty"
s13 = "lambda"
s14 = "suman"
s15 = "try"
s16 = "vaishnavi"

# checking which are keyword

if keyword.iskeyword(s):
    print(s + " is a keyword of python")
else :
    print(s + " is not  a keyword of python")

if keyword.iskeyword(s1):
    print(s1 + " is a keyword of python")
else :
    print(s1 + " is not  a keyword of python")
if keyword.iskeyword(s2):
    print(s2 + " is a keyword of python")
else :
    print(s2 + " is not  a keyword of python")

if keyword.iskeyword(s3):
    print(s3 + " is a keyword of python")
else :
    print(s3 + " is not  a keyword of python")
if keyword.iskeyword(s4):
    print(s4 + " is a keyword of python")
else :
    print(s4 + " is not  a keyword of python")
if keyword.iskeyword(s5):
    print(s5 + " is a keyword of python")
else :
    print(s5 + " is not  a keyword of python")

if keyword.iskeyword(s6):
    print(s6 + " is a keyword of python")
else :
    print(s6 + " is not  a keyword of python")    

if keyword.iskeyword(s7):
    print(s7 + " is a keyword of python")
else :
    print(s7 + " is not  a keyword of python")

if keyword.iskeyword(s8):
    print(s8 + " is a keyword of python")
else :
    print(s8 + " is not  a keyword of python")

if keyword.iskeyword(s9):
    print(s9 + " is a keyword of python")
else :
    print(s9 + " is not  a keyword of python")

if keyword.iskeyword(s10):
    print(s10 + " is a keyword of python")
else :
    print(s10 + " is not  a keyword of python")

if keyword.iskeyword(s11):
    print(s11 + " is a keyword of python")
else :
    print(s11 + " is not  a keyword of python")

if keyword.iskeyword(s12):
    print(s12 + " is a keyword of python")
else :
    print(s12 + " is not  a keyword of python")

if keyword.iskeyword(s13):
    print(s13 + " is a keyword of python")
else :
    print(s13 + " is not  a keyword of python")

if keyword.iskeyword(s14):
    print(s14 + " is a keyword of python")
else :
    print(s14 + " is not  a keyword of python")

if keyword.iskeyword(s15):
    print(s15 + " is a keyword of python")
else :
    print(s15 + " is not  a keyword of python")

if keyword.iskeyword(s16):
    print(s16 + " is a keyword of python")
else :
    print(s16 + " is not  a keyword of python")        