from read_input import *
from create_first_follow_matrix import *

first_follow_obj = create_first_follow_matrix()

def creat_ll1_table():
    ll1_table = {}
    for prod in input_dict['Grammar']['Productions']:
        for key, value in prod.items():
            if key not in ll1_table:
                ll1_table[key] = {}
            if value != '': # check if not epsilon
                first_symbol = find_first_symbol_from_right(value)
                if first_symbol in input_dict['Grammar']['Terminal']:
                    if first_symbol not in ll1_table[key]:
                        ll1_table[key][first_symbol] = [value]
                    else:
                        ll1_table[key][first_symbol].append(value)
                else: # if else the first_symbol is nonterminal
                    for first_elem in first_follow_obj[first_symbol]['first']:
                        if first_elem!='':
                            if first_elem in ll1_table[key]:
                                ll1_table[key][first_elem].append(value)
                            else:
                                ll1_table[key][first_elem] = [value]
                        else:
                            for follow_elem in first_follow_obj[first_symbol]['follow']:
                                if follow_elem in ll1_table[key]:
                                    ll1_table[key][follow_elem].append('')
                                else:
                                    ll1_table[key][follow_elem] = ['']

                # for n in first_follow_obj[key]['first']:
                #     if n in ll1_table[key]:             #
                #         ll1_table[key][n].append(value) # add production value to key in ll1_table for each element in first of key
                #     else:                               #
                #         ll1_table[key][n] = [value]     #
            else:
                for nn in first_follow_obj[key]['follow']:
                    if nn not in ll1_table[key]:
                        ll1_table[key][nn] = [value]
                    else:
                        ll1_table[key][nn].append(value)

    # for key, value in ll1_table.items(): # delete '' epsilon from dict value
    #    value = value.pop('', None)


    return ll1_table

print('\nLL1 Table\n')
pprint(creat_ll1_table())
