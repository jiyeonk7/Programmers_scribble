# def solution(participant, completion):
#     answer = ''
#     # if len(participant) <= 0 or len(participant) > 100000:
#     #     return
#     # else:
#     for c in completion:
#         participant.remove(c)
#     answer = participant[0]       
#     return answer

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
    
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer