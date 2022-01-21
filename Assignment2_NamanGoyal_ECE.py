
               #QUESTION 1

print('               QUESTION 1')
string='Python is a case sensitive language.'
print('The length of the string is:')
print(len(string))   #finding the length of the string
rev=string[::-1]     #reversing the string
print('Reverse of the string:')     
print(rev)
b=string[9:26] #storing 'a case sensitive' in a new variable using slicing
string2=string.replace('a case sensitive','object oriented')   #replacing part of string
print(string2)
print(string.find('a'))
print(string.replace(' ',''))


            #QUESTION 2

print('    \n\n\n          QUESTION 2')
name='Naman Goyal'
SID='21105015'
Dept_name='Electronics and Communication Engineering'
cgpa='9.5'
print('Hey, %s Here!'%name)   #using formatting of the strings
print('My SID is %s'%SID)
print('I am from %s department and my CGPA is %s'%(Dept_name,cgpa))


 
           #QUESTION 3

print('       \n\n\n      QUESTION 3')
a=56
b=10
print('a&b=',(a&b))
print('a|b=',(a|b))
print('a^b=',(a^b))
print('a<<2=',a<<2,'and','b<<2=',b<<2)
print('a>>2=',a>>2,'and','b>>4=',b>>4)



           #QUESTION 4

print('     \n\n\n       QUESTION 4')
num1=int(input('Enter the first number:'))  
num2=int(input('Enter the second number:'))
num3=int(input('Enter the third number:'))
if num1>num2 and num1>num3:    #making if and elif conditions to find the greatest number
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
elif num3>num1 and num3>num2:
    print(num3)



           #QUESTION 5
    
print('     \n\n\n           QUESTION 5')
string=str(input())
if 'name' in string: #using the 'in' function
    print('Yes')
else:
    print('No')



           #QUESTION 6
    
print('     \n\n\n          QUESTION 6')
s1=int(input()) #first side of the triangle and so on
s2=int(input())
s3=int(input())
if s1>s2+s3:    #condition for fisrt side and so on
    print('NO')
elif s2>s1+s3:  
    print('NO')
elif s3>s1+s2:
    print('NO')
else:
    print('YES')

           
            
    
    

           
            
    
    

