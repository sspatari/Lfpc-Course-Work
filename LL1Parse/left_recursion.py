from left_factoring import *

def left_recursion(nonterminal_list,production_list):
    for production in production_list:
        for left,right in production.items():

left_recursion(input_dict["Grammar"]["Nonterminal"],input_dict["Grammar"]["Productions"])
