#reading a file's first 30 bytes and printing it to stdout
file_pointer=open('sample.txt','r')
print(file_pointer.read())
file_pointer.close()


# make a python code to read data from student database where the content is stored as 
# roll name marks
# then display the highest marks obtained
f=open('school.txt','r')
data=f.readline()
data=data.split()
h=0
d=0
hna=" "
while (data):
    if int(data[2])>h:
        h=int(data[2])
        hna=data[1]
    data=f.readline()
    data=data.split()
print('name=',hna)
print('highest marks =',h)
f.close()

# Write a python program to find the longest word in the file
file=open('sample.txt','r')
content=file.read().split()
flag=''
for count in content:
    if len(count)>len(flag):
        flag=count
print('the longest word is :-',flag)
file.close()

# Write a python program to find the longest word in the file
file=open('sample.txt','r')
content=file.read().split()
flag=''
for count in content:
    if count.isalpha():
        if len(count)>len(flag):flag=count
print('the longest word is :-',flag)
file.close()