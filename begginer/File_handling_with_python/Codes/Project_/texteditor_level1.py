# This is level one text editor 
# In this text editor we will mainly focus on terminal based text editing

def show(file_pointer):
    initial_pointer=file_pointer.tell()
    file_pointer.seek(0)
    print(file_pointer.read())
    file_pointer.seek(initial_pointer)
def main():
    with open(r'begginer\File_handling_with_python\Codes\Project_','a+'):
        show()
        pass
    pass

if __name__=='__main__':
#     # print('''
#      ██████╗██╗     ██╗    ████████╗███████╗██╗  ██╗████████╗    ███████╗██████╗ ██╗████████╗ ██████╗ ██████╗ 
# ██╔════╝██║     ██║    ╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝    ██╔════╝██╔══██╗██║╚══██╔══╝██╔═══██╗██╔══██╗
# ██║     ██║     ██║       ██║   █████╗   ╚███╔╝    ██║       █████╗  ██║  ██║██║   ██║   ██║   ██║██████╔╝
# ██║     ██║     ██║       ██║   ██╔══╝   ██╔██╗    ██║       ██╔══╝  ██║  ██║██║   ██║   ██║   ██║██╔══██╗
# ╚██████╗███████╗██║       ██║   ███████╗██╔╝ ██╗   ██║       ███████╗██████╔╝██║   ██║   ╚██████╔╝██║  ██║
#  ╚═════╝╚══════╝╚═╝       ╚═╝   ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═════╝ ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                                                                                          
#     ''')
    try:
        main()
    except KeyboardInterrupt:
        exit()