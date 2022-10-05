# When passed a list and a target sum, returns two distinct zero-based indices of any two of the numbers, 
# whose sum is equal to the target sum. If there are no two numbers, the function should return None.


# def find_two_sum(numbers, target_sum):
#     """
#     :param numbers: (list of ints) The list of numbers.
#     :param target_sum: (int) The required target sum.
#     :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
#     """
#     numList = sorted(numbers, reverse=True)
#     for num in numList:
#       if num <= target_sum:
#         rest = target_sum-num
#         if rest in numList:
#           return numbers.index(num), numbers.index(rest)
#     return None

def find_two_sum(numbers, target_sum):
	"""
	:param numbers: (list of ints) The list of numbers.
	:param target_sum: (int) The required target sum.
	:returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
	"""
	taken = {}
	for i, num in enumerate(numbers):												# i: index, num: value
			diff = target_sum - num
			if diff in taken:
					return i, taken[diff]
			taken[num] = i
	return None


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
