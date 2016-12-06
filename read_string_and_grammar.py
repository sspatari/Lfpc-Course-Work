import json
from pprint import pprint

#Returns the read base_string
def read_json_file(file_name):
    fo = open(file_name,"r") #Open base_string.json for reading
    data_string = fo.read() #obtain string from file
    data = json.loads(data_string) #from string to data
    fo.close()
    return data

def creat_grammar_variable():
    string_json = read_json_file("base_string.json")
    grammar_json = read_json_file("grammar.json")
    print(string_json)
    print(grammar_json)

creat_grammar_variable()
