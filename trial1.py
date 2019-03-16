def sum_for(arr):
	# start sum at 0
	sum = 0
		
	# for each num in the list, add it to sum
	for num in arr:
		sum += num


	return sum

def sum_while(arr):
	# start sum at 0
	sum = 0

	# while the list length is not 0, we're going to pop
	# the very first number and add it to sum
	while len(arr) != 0:
		sum += arr.pop()

	return sum

def sum_recursion(arr):
	# if the length of the list is 0, we just stop
	if (len(arr) == 0):
		return 0
	else:
		# otherwise we pop a value from the list
		running_sum = arr.pop()

		# and recurse with the remaining values
		return running_sum + sum_recursion(arr) 

def concat_lists(arr1, arr2):
	# assuming these 2 lists might not be the same length
	
	# iterator for arr1 and arr2
	i = 0
	j = 0
	final = []

	# while the iterators of arr1 and arr2
	# are not bigger than the lengths
	# append alternatingly to final
	while (i < len(arr1)) or (j < len(arr2)):
		if (i < len(arr1)):
			final.append(arr1[i])
			i += 1
		if (j < len(arr2)):
			final.append(arr2[j])
			j += 1

	return final

def fibo():
	# start with definition
	arr = [0,1]

	while (len(arr) != 100):
		arr.append(arr[len(arr)-1] + arr[len(arr)-2])

	return arr


# print(sum_recursion([1,2,3,4]))
#print(concat_lists(['a','b','c','d'], [1,2,3]))
thing = fibo()
print(len(thing))
