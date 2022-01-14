  #QUESTION 1
print('            First question\n')
number1=int(input('Enter the first number= '))  
number2=int(input('Enter the second number= '))
number3=int(input('Enter the second number= '))
avg=(number1+number2+number3)/3
print('Average of three numbers =',avg)
print('\n\n')


  #QUESTION 2
print('               Second question\n')
grossincome=float(input('Enter your Gross Income='))
numofdepend=int(input('Enter the number of dependents='))
taxableinc=grossincome-10000-(numofdepend*3000)
print('Your Taxable Income is =',taxableinc)
taxamount=(taxableinc*20)/100
print('Tax Amount = ',taxamount)
print('\n\n')

  #QUESTION 3
print('              Third question\n')
sid=int(input('Enter your Student ID: '))
name=str(input('Enter your Name: '))
gender=str(input('Enter your Gender out of "F","M" or "U":'))
branch=str(input('Enter your branch:'))
cgpa=float(input('Enter your cgpa:'))
student=[sid,name,gender,branch,cgpa]
print(student)
print('\n\n')

#QUESTION 4
print('             Fourth question\n')
marks=[90,89,72,65,57]
print('Marks of five studenst:',marks)
marks.sort()
print('sorted list of marks:',marks)

#QUESTION 5
print('             Fifth question\n')
colorslist=['Red','Green','White','Black','Pink','Yellow']
print('The list of colors:',colorslist)
colorslist.pop(3)
print('Updated colors list:',colorslist)
colorslist.pop(4)
colorslist.insert(3,'Purple')
print('Updated colors list:',colorslist)



