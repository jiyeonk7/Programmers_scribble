def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    accuse = [[] for i in range(len(id_list))]
    penalized = [0 for i in range(len(id_list))]
    check = []
    for r in report:
        acc = r.split(' ')[0]
        vic = r.split(' ')[1]
        # print(acc, id_list.index(acc))
        if r not in check:
            acc_idx = id_list.index(acc)
            vic_idx = id_list.index(vic)
            accuse[acc_idx].append(vic)
            penalized[vic_idx] += 1
        check.append(r)
    stopped = []
    for i in range(len(id_list)):
        if penalized[i] >= k:
            stopped.append(id_list[i])
    for i in range(len(id_list)):
        for name in stopped:
            if name in accuse[i]:
                answer[i] += 1
    return answer


### ANSWER ###
def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

