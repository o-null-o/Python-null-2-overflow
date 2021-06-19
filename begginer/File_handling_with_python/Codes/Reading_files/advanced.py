# write a python programm to count the frequecy of words in a pointer.

def main(pointer):
    all_words=pointer.read().split()
    words=list()
    for i in all_words:
        if i in words:
            pass
        else: 
            words.append(i)   
    for i in words:
        print(f'\'{i}\'','has been repeated',all_words.count(i),'times')    
    return words
pointer=open(r'begginer\File_handling_with_python\Codes\Reading_files\sample.txt','r')
main(pointer)
pointer.close()


#Write a Python program that allows you to group in a list the words common for two text files: file1.txt and file2.txt.
def compare(content1,content2):
    '''This funciton will help you to compare two files, just you had to pass the file handler to the function in reading mode'''
    content1=content1.read().split()
    # print(content1)
    content2=content2.read().split()
    # print(content2)
    common_words=list()
    for count in range(len(content1)-1):
        for flag in range(len(content2)-1):
            if content1[count]==content2[flag]:
                if content2[flag] not in common_words:
                    common_words.append(content1[count])
    print('the common words are : - ')
    for count in common_words:print(count)
compare(open('file1.txt'),open('file2.txt'))