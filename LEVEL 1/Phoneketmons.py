def solution(nums):
    thresh = len(nums)/2
    unique = len(set(nums))
    if unique >= thresh:
        answer = thresh
    else:
        answer = unique
    # answer = 0
    return answer

# More Concise
def solution(nums):
    return min(len(nums)/2, len(set(nums)))