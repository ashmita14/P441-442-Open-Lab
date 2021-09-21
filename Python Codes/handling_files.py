#Library for handling files and their contents

# READ FILE
def read_matrix(x): #more than one column #parameter = name of file
    f=open(x,'r') #'r' ==> read only
    X=[[float(num) for num in line.split('\t')] for line in f]
    f.close()
    return(X)

##############################################################################

# APPEND FILE
def append_file(x, str): #arguments = name of file, string to append
    f=open(x, 'a') #'a' ==> append file
    f.write(str)
    f.close()
    #

###############################################################################

#WRITE AT BEGINNING (hopefully)
def write_beginning(x, str):
    f=open(x, 'r+')
    old=f.read()
    f.seek(0)
    f.write(str + old)
    f.close()
    # it works :D

# PRINT CONTENTS OF A TEXT FILE
def print_file(x): #argument = name of file
    f=open(x, 'r')
    contents=f.read()
    print(contents)

#################################################################################
