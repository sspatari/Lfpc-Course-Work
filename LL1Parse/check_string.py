from read_input import *
from ll1_parse_table import *

stack = [input_dict['Grammar']['Start']]
string = input_dict['string'] + '$'
all_symbols = input_dict['Grammar']['Nonterminal'] + input_dict['Grammar']['Terminal']

def combine_2symbols_elements(array, start):
    array[start:start + 2] = [''.join(array[start:start + 2])]

def prepare_production_for_stack(prod):
    array = [*prod]
    index = 0
    for i in array:
        if i not in all_symbols:
            combine_2symbols_elements(array, index - 1)
        index += 1
    return array

def change_stack_string(stack, string, action):
    if action == 'Terminal':
        stack = stack[1:]       # delete first element of stack
        string = string[1:]     # delete first element of string
    elif action == '':          # Epsilon
        stack = stack[1:]
    else:
        prod_array = prepare_production_for_stack(action)
        stack = prod_array + stack[1:]  # change first element of stack with action's production
    return stack, string

def check_string(ll1_table, stack, string):
    k = True
    stack_first_element = stack[0]
    string_first_element = string[0]
    if stack_first_element in input_dict['Grammar']['Nonterminal'] and string_first_element in ll1_table[stack_first_element]:
        stack, string = change_stack_string(stack, string, ll1_table[stack_first_element][string_first_element][0])    # Modify stack and string
    elif stack_first_element in input_dict['Grammar']['Terminal'] and stack_first_element == string_first_element:
        stack, string = change_stack_string(stack, string, 'Terminal')
    else:
        print('Bad string')
        k = False
    print(stack, string[:len(string) - 1])    # show stack and string after change (string without last char)
    if k and (stack != [] or string != '$'):
        check_string(ll1_table, stack, string)

ll1_table = creat_ll1_table()

print('\nCheck string\n')
print(stack, string[:len(string) - 1])    # (string without last char)
check_string(ll1_table, stack, string)
