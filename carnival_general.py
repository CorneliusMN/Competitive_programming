from collections import deque
from math import ceil

n = int(input())

rankings = deque([i for i in range(2)])
not_used = input()
dict_disliked = {0: [None], 1: [None]}

for general in range(2, n):
    pref = list(map(int, input().split()))
    dict_disliked[general] = [pref[-1]]
    if len(pref) <= 3:
        if pref[-1] != rankings[-1]:
            rankings.append(general)
        elif pref[-1] != rankings[0]:
            rankings.appendleft(general)
    
    else:
        disliked = pref[ceil(len(pref)/2):]
        dict_disliked[general] = disliked
        if rankings[-1] not in disliked and general not in dict_disliked[rankings[-1]]:
            rankings.append(general)
        elif rankings[0] not in disliked and general not in dict_disliked[rankings[0]]:
            rankings.appendleft(general)
        else:
            for k in range(2, n-1):
                a = dict_disliked[rankings[k-1]]
                b = rankings[k-1]
                c = dict_disliked[general]
                d = dict_disliked[rankings[k]]
                e = rankings[k]
                if general not in a and b not in c and general not in d and e not in c:
                #if general not in dict_disliked[rankings[k-1]] and rankings[k-1] not in dict_disliked[general] and general not in dict_disliked[rankings[k]] and rankings[k] not in dict_disliked[general]:
                    rankings.insert(k, general)
                    break

print(" ".join(map(str,rankings)))