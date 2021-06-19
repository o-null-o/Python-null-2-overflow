#WAPP to create a file with roll and name for all the student in you class in a file recurd.txt .
#Write a function to delete roll no 7 from the record and display new list.
# this is to create the file record.txt
def create_file(file_pointer):
    data=list()
    while True:
        data.append(str(input('\nEnter the roll : '))+' '+input('Enter the name :')+'\n')
        if input('\nTo add more press(Enter) or (n|N) to exit :') in tuple('nN'):
            break
    file_pointer.writelines(data)
    print('\nData is succesfully written\n')
    file_pointer.close()
# this function is for data sorting
def data_sorting(file_pointer):
    # reading data from the file
    file_data=file_pointer.readlines()
    # creating two flags to use
    new=list()
    flag=list()
    # iterating through the file to sort the names with roll 7
    roll_to_del=int(input('Enter the roll no to deleate : '))
    for count in range (0,len(file_data)-1):
        # appending the roll no into the flag file
        flag.append((file_data[count].split())[0])
        # checking for roll 7
        if int(flag[count])==roll_to_del:
            pass
        else:
            # appending all the records that doesnot have roll 7
            new.append(file_data[count])
    # returning the new list
    return new
# this function is for writting the data 
def write_data(data_to_write,file_handler):
    file_handler.writelines(data_to_write)
    file_handler.close()
    print('\nData modified successfully!!')
# This is to call the fucntions 
if __name__=='__main__':
    create_file(open('school.txt','w'))
    write_data(data_sorting(open('school.txt','r')),open('school.txt','w'))

# '''''''''''''''''''''''''''''''''''''''''''''''''' END OF PROGRAM ''''''''''''''''''''''''''''''''''''''''''''''''''