from left_recursion import *

def create_first_follow_matrix(): # creates and return it
    first_follow_matrix = {}
    for nonterminal in input_dict["Grammar"]["Nonterminal"]:
        first_set = set()
        follow_set = set()
        verified_nonterminal_list = [] #will contain nonterminals for which we should not find the follow_set because we already started finding it
        find_first(first_set,nonterminal)
        verified_nonterminal_list.append(nonterminal)
        find_follow(follow_set,nonterminal,verified_nonterminal_list)
        first_follow_matrix[nonterminal] = {"first": list(first_set),"follow": list(follow_set)}
    return first_follow_matrix

def find_first(first_set,nonterminal): # finds all firsts refering to a nonterminal
    for production in input_dict["Grammar"]["Productions"]:
        for left, right in production.items(): #left and right side of production
            if(left == nonterminal):
                if(right != ""):
                    extract_first_from_right(first_set,right[0])
                else:
                    first_set.add("")

def extract_first_from_right(first_set,symbol): #finds a first from first symbol of the right part
    if symbol in input_dict["Grammar"]["Terminal"]:
        first_set.add(symbol) #symbol should be terminal
    elif symbol in input_dict["Grammar"]["Nonterminal"]:
        find_first(first_set,symbol) #symbol should be nonterminal

def find_follow(follow_set,nonterminal,verified_nonterminal_list):
    if(nonterminal==input_dict["Grammar"]["Start"]): # adds $ to follow for start nonterminal
        follow_set.add("$")
    for production in input_dict["Grammar"]["Productions"]:
        for left,right in production.items():
            n = find_index_nonterminal_in_right(nonterminal,right)
            if(n != -1): #if true then nonterminal found and n represents its first index
                char_to_jump = 0
                while(True):
                    right_after_nonterminal = right[n+len(nonterminal)+char_to_jump:]
                    # print(left,right,right_after_nonterminal)
                    # print(follow_set, nonterminal, verified_nonterminal_list)
                    if(right_after_nonterminal != ""): #testing string after nonterminal finding follow of the nonterminal
                        first_symbol = find_first_symbol_from_right(right_after_nonterminal)
                        # print("first symbol",first_symbol)
                        epsilon_test = extract_first_from_right2(follow_set,first_symbol)
                        # print("epsilon_test",epsilon_test)
                        # print(follow_set)
                        if(epsilon_test):
                            char_to_jump += len(first_symbol)
                        else:
                            break
                    elif left not in verified_nonterminal_list: #this check is used to exit the posible infinite loop
                        verified_nonterminal_list.append(left)
                        find_follow(follow_set,left,verified_nonterminal_list)
                        # print(follow_set)
                        break
                    else:
                        break

def find_index_nonterminal_in_right(nonterminal,right):
    n = right.find(nonterminal)
    if(n != -1):
        test_nonterminal_list = [elem for elem in input_dict["Grammar"]["Nonterminal"] if elem!=nonterminal]
        for test_nonterminal in test_nonterminal_list:
            n2 = right.find(test_nonterminal,n)
            if n2 == n and len(test_nonterminal) > len(nonterminal):
                return -1
    return n

def find_first_symbol_from_right(right):
    for terminal in input_dict["Grammar"]["Terminal"]:
        if(right.startswith(terminal)):
            return terminal
    len_of_nonterminal = 0
    for nonterminal in input_dict["Grammar"]["Nonterminal"]:
        if right.startswith(nonterminal) and len(nonterminal)>len_of_nonterminal:
            len_of_nonterminal = len(nonterminal)
            nonterm = nonterminal
    return nonterm

def extract_first_from_right2(follow_set,first_symbol): #finds a follow from first symbol of the right part
    epsilon_test = False
    if first_symbol in input_dict["Grammar"]["Terminal"]:
        follow_set.add(first_symbol) #symbol should be terminal
    elif first_symbol in input_dict["Grammar"]["Nonterminal"]:
        epsilon_test = find_first_for_follow(follow_set,first_symbol) #symbol should be nonterminal
    return epsilon_test

def find_first_for_follow(follow_set,nonterminal): # finds all firsts refering to a nonterminal
    epsilon_test = False
    for production in input_dict["Grammar"]["Productions"]:
        for left, right in production.items(): #left and right side of production
            if(left == nonterminal):
                if(right != ""):
                    first_symbol = find_first_symbol_from_right(right)
                    extract_first_from_right2(follow_set,first_symbol)
                else:
                    epsilon_test = True
    return epsilon_test

print("\nThe first follow matrix")
pprint(create_first_follow_matrix())
