# Write a python program to open and then close a file
file_object=open('today.txt')
file_object.close()


# Write a python program to open a user defined file(user must give relative path of the file)
file_object=open(str(input('Enter the relative file path : ')))
print('file successfully opened')
file_object.close()


# Write a python program to open a user defined file(user must give absolute path of the file)
file_object=open(str(input('Enter the absolute file path : ')))
print('file successfully opened')
file_object.close()



# advanced

# Write a python program to open a user defined file(user must give absolute path of the file)
def pathprovider(n=int(input('press 1. for relative path \npress 2. for absolute paht\nEnter the option : '))):
	if n in (1,2):
		if n==1:
			return input('Enter the path : ')
		else :
			return input('Enter the path : ').replace('\\',r'\\')
	else: print('invalid input')

file_object=open(pathprovider())
print('file exists')
file_object.close()
