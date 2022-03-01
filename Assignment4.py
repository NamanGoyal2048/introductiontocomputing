#QUESTION 1
print('              QUESTION 1')
print('\n\n')
def hanoi(n, source, endplace, temporary):  #endplace is where the disk has to end
                                       #temp is place taken in transition
    if n == 1:
        print('Move disk 1 from source',source,'to destination',endplace)
        return
    
    hanoi(n-1, source, temporary, endplace)
    print(f'Move Disk {n} from source {source} to destination {endplace}')
    hanoi(n-1, temporary, endplace, source)

#calling funtion for 3 disks
hanoi(3, 'A', 'B', 'C')
print('\n\n\n')



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#QUESTION 2

print('                QUESTION 2')
print('\n\n')
#input n number of rows
n = int(input("Enter number of rows to print: "))


#using loops
print("\nUsing loops:\n")
import math
for i in range(n):
    for j in range(n-i+1):
        #for spacing in front of line
        print(end=' ')
    for j in range(i+1):
        #using combinations
        print(math.factorial(i)//(math.factorial(j)*math.factorial(i-j)),end=' ')

    print("\n")    
        

#using recursions
def pascal(n,l1):             #n is the number of lines .
    if n == 0 :
        return
    
    pascal(n-1,l1)       

    l = len(l1)
    l2 = l1.copy()             
    l1.append(1)

    for i in range(0,l):              #Using iteration for next line
        if i == 0:
            l1[0] = 1
        else:
            l1[i] = l2[i] + l2[i-1]
    
    pattern(l1)                #Calling function to print the triangle.


#to print pascal's triangle in proper order
def pattern(l1):
    print(" "*(number - len(l1)), end = "")

    for j in l1:
        print(j , end = " ")
    print('\n')        
    
#number of line to print.
number = int(input("Enter the number of rows to print: "))
print('\n\n')

#recursive function to generate the pascal's traingle.
initial_list = []
pascal(number,initial_list)

print('\n\n\n')


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





#QUESTION3

print("                             QUESTION 3")
print("\n")

print("\n")
a=int(input("Enter  first integer: "))
b=int(input("Enter  second integer: "))
(quotient,remainder)=divmod(a,b)#finding the remainder and quotient using built-in function

#checking the finction callable or not

print(callable)
print(callable(quotient))
print(callable(remainder))

#adding values to the already existing set

newset=(quotient,remainder).__add__((4,5,6))
print(f'New set: {newset}')

#printing the set with values

value_bigger_than_4=[]
for i in range(len(newset)):
    if newset[i]>4:
        value_bigger_than_4.append(newset[i])
print(f'Set of values greater than 4: {value_bigger_than_4}')
c=set(value_bigger_than_4)
print(c)

#making set immutable

d=frozenset(c)
print(f'The immutable set is: {d}')

#finding the max value of set

print(f'The maximum value of the set is: ',max(d))

#hashing the max value

print(f'The hash value of the maximum value of set: ',hash(d))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#QUESTION4
print('                           QUESTION 4')
print("\n\n")
class Student:
    def __init__(self, studentname, sid):
        self.studentname = studentname
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Naman Goyal", 21105015)

print(f"The name of the student is {student1.studentname} and SID is {student1.sid}.")

#deleting object
del student1
print('\n\n\n')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#QUESTION5
print("                            QUESTION 5")
print("\n\n")
class employeerecord:
    def __init__(self, number, name, salary):
        self.number=number
        self.name = name
        self.salary = salary
        print(f'Employee name is {self.name} is {self.salary}')
    
    def __del__(self):
        print(f'Employee {self.name} record deleted')

#records
employee1 = employeerecord(1,'Mehak', 40000)
employee2 = employeerecord(2,'Ashok', 50000)
employee3 = employeerecord(3,'Viren', 60000)
print('\n')

#changing salary
employee1.salary = 70000
print(f' The updated salary of the employee {employee1.name} is {employee1.salary}')
print('\n')

#deleting a record
print(' ', end='')
del employee3

print('\n\n\n')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#QUESTION6

print("                            QUESTION 6")
print('\n\n')
#taking input of words from both friends
george_word=str(input('Enter the word you want to be tested: '))
barbie_word=str(input('Enter the meaningful word made by you: '))
print('\n\n')
#initializing value of sums
sum1=0
sum2=0

#taking and then comparing the sumd of both words' characters ascii values

for letter in george_word:
    sum1=(ord(letter.lower())+sum1)
for letter in barbie_word:
    sum2=(ord(letter.lower())+sum2)
#if sums of ascii values equal then friendship test passed and if not then it does not

if sum1==sum2:
    answer=input('Is the word made meaningful? Y or N: ') #asking the shopkeeper to ask if the entered word is meaningful or not 
    if answer=='Y':
        print('Congratulations!!! You passed the test of friendship.')
    elif answer=='N':
        print('Sorry!!! But you failed the test of friendship.')
    else:
        print('Wrong input')
else:
    print('Sorry!!! But you failed the test of friendship')

