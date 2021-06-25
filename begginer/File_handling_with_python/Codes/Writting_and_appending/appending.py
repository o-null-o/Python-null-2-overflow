#python to accept roll no, name and class of 5 student in a class store it in a file student.
def main():
    count=1
    while count<=5:
        stud_name=input('Enter the name : ')
        stud_class=input('Enter the class : ')
        stud_roll=input('Enter the roll : ')
        record=[stud_roll,' ',stud_name,' ',stud_class,' ','\n']
        pointer.writelines(record)
        count+=1

with open('school.txt','a') as pointer :
    main()