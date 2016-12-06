#Returns the read base_string
def read_base_string():
    #Open initial_string.txt for reading and read first line
    fo = open("base_string.txt","r")
    base_string = fo.readline().strip() #removes white spaces and splits
    fo.close()
    return base_string
