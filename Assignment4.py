#QUESTION 1
print('              QUESTION 1')
print('\n\n')
def hanoi(n, source, endplace, temp):  #endplace is where the disk has to end
                                       #temp is place taken in transition
    if n == 0:
        return
    
    hanoi(n-1, source, endplace, temp)
    print(f'Move Disk {n} from {source} to {endplace}')
    hanoi(n-1, source, endplace, temp)

#calling funtion for 3 disks
hanoi(3, 'A', 'C', 'B')
print('\n\n\n')





#QUESTION 2

print('                QUESTION 2')
print('\n\n')
#input n number of rows
n = int(input("Enter number of rows you want to print: "))


#using loops
print("\nUsing loops:\n")
import math
for i in range(n):
    for j in range(n-i+1):
        #for spacing in front of line
        print(end=' ')
    for j in range(i+1):
        #using combinations
        print(math.factorial(i)//math.factorial(j)*math.factorial(i-j)),end=' ')

    print(" ")    
        

#using recursions
print('\nUsing recursions:\n')
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)
print('\n\n\n')

#QUESTION3

print("                             QUESTION 3")
print("\n")

print("\n")
a=int(input("Enter  first integer: "))
b=int(input("Enter  second integer: "))
c=a%b
d=a//b
print("Remainder is = ", c)
print("Quotient is = ",d)

if(c!=0):
    if (d!=0):
        print("Both values are non zero")
    else:
        print("One value is zero")
else:
    if (d!=0):
        print("One value is zero")
    else:
        print("Both values are zero")
set1=set()
for i in range (4,7):
    f=c+i
    g=d+i
    if(f>4):
        set1.add(f)
        print(set1)
    if(g>4):
        set1.add(g)
        print(set1)

print(set1)
set2=frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("Largest value in the set: ", max(set2))
k=max(set2)
print("Hash value: ", hash(k))
print("")


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
print('\n\n')

#deleting a record
print(' ', end='')
del employee3

print('\n\n\n')

#QUESTION6

print("                            QUESTION 6")
