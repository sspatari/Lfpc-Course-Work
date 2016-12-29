from left_factoring import *

def left_recursion(nonterminal_list,production_list):
    new_production_list = []
    new_nonterminal_list = []
    nonterminal_with_LR_list = [left for production in production_list for
        left,right in production.items() if(right.startswith(left))]

    for nonterminal in nonterminal_with_LR_list:
        counter = 1
        while(1): #this loop is meant to create a proper new_nonterminal that did not exist
            new_nonterminal = nonterminal+str(counter)
            if new_nonterminal in nonterminal_list:
                counter+=1
            else:
                new_nonterminal_list.append(new_nonterminal)
                break
        for production in production_list:
            for left,right in production.items():
                if(left == nonterminal):
                    if(right.startswith(left)):
                        new_production_list.append({new_nonterminal:right[1:]+new_nonterminal})
                        new_production_list.append({new_nonterminal:""})
                    else:
                        new_production_list.append({nonterminal:right+new_nonterminal})
    # print(nonterminal_with_LR_list)
    # print(new_production_list)
    # print(new_nonterminal_list)
    production_list = [production for production in production_list for
        left,right in production.items() if left not in nonterminal_with_LR_list] #removed the changed productions
    production_list += new_production_list #add new productions
    nonterminal_list += new_nonterminal_list #add new nonterminals
    return nonterminal_list, production_list


input_dict["Grammar"]["Nonterminal"],input_dict["Grammar"]["Productions"] = left_recursion(input_dict["Grammar"]["Nonterminal"],input_dict["Grammar"]["Productions"])
print("Data after left recursion")
pprint(input_dict)
