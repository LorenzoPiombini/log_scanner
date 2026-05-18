#!/bin/python3

# import get_file_contet() and write_file()
from file_operation import get_file_line_nr,write_file,filter_file_content,START_ASAN_STRING,END_ASAN

def main():
    write_file("memory_issue.log",filter_file_content("e.txt",START_ASAN_STRING,END_ASAN),"a")
    write_file("e.txt","","w") # this truncate the file to 0! aka empty, maintain the log file small
    print("scan completed!")
    if get_file_line_nr("memory_issue.log") > 500:
        if filter_file_content("memory_issue.log",START_ASAN_STRING,END_ASAN) == "nothing found\n":
            write_file("memory_issue.log","w")






if __name__ == "__main__":
    main()
