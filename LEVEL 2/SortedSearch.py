# count_numbers: accepts a sorted list of unique integers and counts the number of list elements that are less_than

# def count_numbers(sorted_list, less_than):
#     for n in reversed(sorted_list):
#       if n < less_than:
#         return sorted_list.index(n)+1

from bisect import bisect_left

def count_numbers(sorted_list, less_than):
    return bisect_left(sorted_list, less_than)

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2
