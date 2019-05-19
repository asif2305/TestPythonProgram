s="Strings are awesome for you."

#length of string

print("length of s=%d" % len(s))

print("The first character of the string a= %d " %s.index("a"))

# number of letter count

print("a occurs %d times" % s.count("a"))

#slicing the string into bits

print("The first 5 character are '%s'" % s[:5])


print("The next 5 character are '%s'" % s[5:10])


print("The fourteen character are '%s'" % s[13])


print("The  character with odd index are '%s'" % s[1::3])


print("The character are before last 5 index '%s'" % s[:-5])


print("The character start from 3 index '%s'" % s[3:])


print("strings are uppercase '%s'" % s.upper())


print("strings are lowercase '%s'" % s.lower())

#output 

'''
length of s=28
The first character of the string a= 8 
a occurs 2 times
The first 5 character are 'Strin'
The next 5 character are 'gs ar'
The fourteen character are 'w'
The  character with odd index are 'tn ewo ro'
The character are before last 5 index 'Strings are awesome for'
The character start from 3 index 'ings are awesome for you.'
strings are uppercase 'STRINGS ARE AWESOME FOR YOU.'
strings are lowercase 'strings are awesome for you.'

'''

