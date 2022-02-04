def solution(d, budget):
    d.sort()
    count = 0
  
    for i in range(len(d)):
        if budget >= d[i]:
            count += 1
            budget -= d[i]
        else:
            break
    return count