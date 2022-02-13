                     #QUESTION1
print('                 QUESTION1')
string1=str(input('Enter the string:'))
words=string1.lower().split()
if len(words)==1:
    words=words[0]
dict1=dict()
for word in words:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)        
        

    




                           #QUESTION2

print('                   \n\n\n\nQUESTION 2')
day=int(input('day:'))
month=int(input('month:'))
year=int(input('year:'))
if year%4==0:
    if day>=1 and day<=31 and month>=1 and month<=12 and year>=1800 and year<=2025:
        if day==28 and month==2:
            print('%d/2/%d'%(day+1,year))
        elif day==29 and month==2:
             print('1/3/%d'%(year))
        elif month==12:
            if day<=30:
                print('%d/%d/%d'%(day+1,month,year))
            else:
                print('1/1/%d'%(year+1))
        elif day==31:
            print('1/%d/%d'%(month+1,year))
        elif day==30:
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                print('31/%d/%d'%(month,year))
            else:
                print('1/%d/%d'%(month+1,year))
        
        else:
            print('%d/%d/%d'%(day+1,month,year))
else:
    if day>=1 and day<=31 and month>=1 and month<=12 and year>=1800 and year<=2025:
        if day==28 and month==2:
            print('1/3/%d'%year)
        elif month==12:
            if day<=30:
                print('%d/%d/%d'%(day+1,month,year))
            else:
                print('1/1/%d'%(year+1))    
            
        elif day==31:
            print('%d/%d/%d'%(day,month+1,year))
        elif day==30:
            if month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                print('31/%d/%d'%(month+1,year))
            else:
                 print('1/%d/%d'%(month+1,year))
       

        else:
             print('%d/%d/%d'%(day+1,month,year))

             #QUESTION3
print('                \n\n\n\n   QUESTION 3')
list1=int(input('Enter the number:'))
list2=list()
for i in range(list1) :
    list2.append((i,i**2))
print(list2)    



                #QUESTION4
print('                  \n\n\n\n  QUESTION 4')
grade=int(input('Enter Your Grade:'))
if grade==10:
    print('Your Grade is A+ and Outstanding Performance')
elif grade==9:
    print('Your Grade is A and Excellent Performance')
elif grade==8:
    print('Your Grade is B+ and Very Good Performance')
elif grade==7:
    print('Your Grade is B and Good Performance')
elif grade==6:
    print('Your Grade is C+ and Average Performance')
elif grade==5:
    print('Your Grade is C and Below Average Performance')
elif grade==4:
    print('Your Grade is D and Poor Performance')
else:
    print('ERROR:THE ENTERED GRADE IS OUT OF RANGE')


                 #QUESTION5
print('                 \n\n\n\n   QUESTION 5')
string2='ABCDEFGHIJK'
i=11
j=1
x=' '
while i>0 or j<=5:
    print(x*j,string2[0:i])
    j+=1
    i-=2


   #QUESTION6
print('              \n\n\n\n      QUESTION 6')
record=dict()
for i in range(0,3):
    name=str(input('Enter your name:'))
    sid=int(input('Enter your SID:'))
    record[sid]=name
    print('\n\n\n')
    print(record)
    for i in sorted(record):
        print(i,':',{record[i]})
    for i in sorted(record.values()):
        print(i)    
    sid_search=int(input('Enter SID to be searched:'))
    if sid_search in record:
        print(record[sid_search])
    else:
        print('Not in database')
    print('\n\n\n')    



                #QUESTION7

print('                      \n\n\n\nQUESTION 7')
n=int(input('Enter the number till which you want to print fibonacci numbers:'))
F1=0    #initializing value to f1 and f2 the first two fibonacci numbers
F2=1
while F1<=n:
    print(F1)
    F3=F1+F2
    F1=F2
    F2=F3


                    #QUESTION8
print('                    \n\n\n\n  QUESTION8')
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
print('Set1=',set1)
print('Set2=',set2)
print('Set3=',set3)
set4=set1 & set2
print(set4)
set5=set1|set2|set3
print(set5)
set6=set1&set2|set2&set3|set1&set3
print(set6)
set7={1,2,3,4,5,6,7,8,9,10}
set8= set7 - set1
print(set8)
set9=set7 - set1- set2 - set3
print(set9)

