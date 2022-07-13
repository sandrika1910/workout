def can_see_stage(lst):
	lst_length = len(lst)
	each_lst_length = len(lst[0])

	indicator = {'return': 'True'}
	for i in range(each_lst_length):
		for j in range(lst_length - 1):
			if lst[j][i] >= lst[j+1][i]:
				indicator['return'] = 'False'
	
	if indicator['return'] == 'True':
		return True
	else:
		return False
				

# print(can_see_stage([[1, 2, 3, 2, 1, 1], 
# [2, 4, 4, 3, 2, 2], 
# [5, 5, 5, 4, 4, 4], 
# [6, 6, 8, 6, 5, 5]])) # True

# print(can_see_stage([
#   [0, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
#   ])) # True

# print(can_see_stage([
# 	[2, 0, 0], 
#   	[1, 1, 1], 
#   	[2, 2, 2]
# ])) # False 
