import json
from pprint import pprint

#Returns the read base_string
def read_json_file(file_name):
    fo = open(file_name,"r") #Open file json
    data_string = fo.read() #obtain string from file
    data = json.loads(data_string) #from string to data
    fo.close()
    return data

input_dict = read_json_file("input.json")
