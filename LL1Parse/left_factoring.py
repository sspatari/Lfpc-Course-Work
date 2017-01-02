from read_input import *
from itertools import zip_longest
from pprint import pprint

def left_factoring(nonterminal_list,production_list):
	left_part = [] # left part of productions list
	right_part = [] # right part of productions list
	remove_nonterminal_index_list = [] #index of productions to be removed
	new_productions = [] #new productions to be added,will contain object
	new_productions_final = [] #all new productions to be added,will contain object
	new_nonterminal_list = [] #new nonterminal to be added
	new_nonterminal_list_final = [] #all new nonterminal to be added
	for production in production_list:
		for left,right in production.items():
			left_part.append(left)
			right_part.append(right)

	for nonterminal in nonterminal_list:
		nonterminal_index_list = [i for i,x in enumerate(left_part) if x == nonterminal and right_part[i] != ""] #list of indexes of production that derive from same nonterminal and that do not derive to epsilon/null string
		if len(nonterminal_index_list) != 1:
			right_part_list = [right_part[index] for index in nonterminal_index_list]
			# print(nonterminal,right_part_list)
			prefixes_list = find_prefixes(right_part_list)
			# print(prefixes_list)
			if (len(prefixes_list) != len(right_part_list)):
				remove_nonterminal_index_list += nonterminal_index_list
				prefix_sufixes_dict = find_prefix_suffixes(right_part_list, prefixes_list)
				# print("prefix_sufixes_dict",nonterminal,prefix_sufixes_dict)
				new_nonterminal_list, new_productions = create_new_productions_and_nonterminal(nonterminal, prefix_sufixes_dict)
				# print("new_nonterminal_list before",new_nonterminal_list)
				# print("new_productions before",new_productions)
				new_nonterminal_list, new_productions = left_factoring(new_nonterminal_list,new_productions) #recursion
				# print("new_nonterminal_list after",new_nonterminal_list)
				# print("new_productions after",new_productions)
				new_nonterminal_list_final += new_nonterminal_list
				new_productions_final += new_productions

	# print("Index of nonterminal to remove",remove_nonterminal_index_list)
	# print("Productions",production_list)
	production_list = [elem for index,elem in enumerate(production_list) if index not in remove_nonterminal_index_list]
	# print("Productions",production_list)
	# print("New Productions",new_productions_final)
	production_list += new_productions_final
	# print("New nonterminals",new_nonterminal_list_final)
	nonterminal_list += new_nonterminal_list_final
	# print("Nonterminals",nonterminal_list)
	# print("Productions",production_list)
	return nonterminal_list,production_list

def find_prefixes(strings):
	zipped = zip_longest(*strings, fillvalue='')
	for index, letters in enumerate(zipped):
		if index == 0:
			prefixes = letters  # assumes there will always be a prefix
		else:
			poss_prefixes = [prefix + letters[i] for i, prefix in enumerate(prefixes)]
			prefixes = [prefix if poss_prefixes.count(prefix) == letters.count(prefix) or poss_prefixes.count(prefix)==prefixes.count(prefix[:-1]) else prefixes[i] for i, prefix in enumerate(poss_prefixes)]
	return list(set(prefixes))

def find_prefix_suffixes(strings, prefixes):
	prefix_suffix = {}
	for s in strings:
		for prefix in prefixes:
			if s.startswith(prefix):
				if prefix in prefix_suffix:
					prefix_suffix[prefix].append(s.replace(prefix, '', 1))
					break
				else:
					prefix_suffix[prefix] = list([s.replace(prefix, '', 1)])
					break
	return prefix_suffix

def create_new_productions_and_nonterminal(nonterminal, prefix_sufixes_dict):
	new_productions = []
	new_nonterminal_list = []
	counter = 0
	for key, value_list in prefix_sufixes_dict.items():
		if len(value_list) == 1:
			if value_list[0] == "":
				new_productions.append({nonterminal:key})
			else:
				new_productions.append({nonterminal:key+value_list[0]})
		else:
			counter+=1
			new_nonterminal = nonterminal+str(counter)
			new_productions.append({nonterminal:key+new_nonterminal})
			for value in value_list:
				new_productions.append({new_nonterminal:value})
			new_nonterminal_list.append(new_nonterminal)
	return new_nonterminal_list, new_productions

input_dict["Grammar"]["Nonterminal"],input_dict["Grammar"]["Productions"] = left_factoring(input_dict["Grammar"]["Nonterminal"],input_dict["Grammar"]["Productions"])
print("Data after left factoring")
pprint(input_dict)
