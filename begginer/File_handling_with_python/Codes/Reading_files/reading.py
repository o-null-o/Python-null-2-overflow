#Write a Python program to read an entire text file.
'''
def main(pointer):
    return pointer.read()
with open('sample.txt','r') as pointer:
    print(main(pointer))
'''

#write a funtion in python to search how many word ending with 's' in a file story.txt
'''
def main(file):
    temp=file.read().split()
    for count in temp:
        if count[-1] in 'Ss':
            print(count)
file=open('story.txt','r')
main(file)
file.close()
'''

#write a funtion in python to read data from student.txt 
#content roll name and total marks display the highest scorername

#this file can be coded in many ways mainly three ways 
#using readline function
'''
def main(pointer):
    roll,name,marks =list(),list(),list()
    text=pointer.readline().split()
    while (text):
        roll.append(text[0])
        name.append(text[1])
        marks.append(int(text[2]))
        text=pointer.readline().split()
    return roll , name, marks
def calculate(roll,name,marks):
    topper=marks.index(max(marks))
    print('the highest ranker is \n roll :- ',roll[topper],'\n name :- ',name[topper],'\nmarks :- ',marks[topper])

pointer=open('sample.txt','r')
calculate(*main(pointer))
pointer.close()
'''
#usnig readlines function
"""
def main(pointer):
    roll,name,marks =list(),list(),list()
    for count in pointer.readlines():
        count=count.split()
        roll.append(count[0])
        name.append(count[1])
        marks.append(int(count[2]))
    return roll,name,marks
def calculate(roll,name,marks):
    topper=marks.index(max(marks))
    print('the highest ranker is \n roll :- ',roll[topper],'\n name :- ',name[topper],'\nmarks :- ',marks[topper])

pointer=open('sample.txt','r')
calculate(*main(pointer))
pointer.close()
"""
#using read funtion
'''
def main(pointer):
    roll,name,marks =list(),list(),list()
    for count in pointer.read().split('\n'):
        count=count.split()
        roll.append(count[0])
        name.append(count[1])
        marks.append(int(count[2]))
    return roll,name,marks
def calculate(roll,name,marks):
    topper=marks.index(max(marks))
    print('the highest ranker is \n roll :- ',roll[topper],'\n name :- ',name[topper],'\nmarks :- ',marks[topper])

pointer=open('sample.txt','r')
calculate(*main(pointer))
pointer.close()
'''