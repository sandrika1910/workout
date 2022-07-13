def is_disarium(num):
	str_num = str(num)
	lst = [int(a) for a in str_num]

	sum_items = 0
	for decriment,(item) in enumerate(lst):
		decriment += 1
		sum_items += item**decriment

	if sum_items == num:
		return True
	else:
		return False

if is_disarium(int(input('number: '))):
	print('number is disarium. ')
else:
	print('number is not disarium. ')