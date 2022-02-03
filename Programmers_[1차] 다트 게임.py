def solution(dartResult):
    n = ''
    result = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() == True:
            n += dartResult[i]
        elif dartResult[i] == 'S':
            n = int(n)**1
            result.append(n)
            n = ''
        elif dartResult[i] == 'D':
            n = int(n)**2
            result.append(n)
            n = ''
        elif dartResult[i] == 'T':
            n = int(n)**3
            result.append(n)
            n = ''
        elif dartResult[i] == '*':
            if len(result) > 1:
                result[-2] = result[-2] * 2
                result[-1] = result[-1] * 2
            else:
                result[-1] = result[-1] * 2
        elif dartResult[i] == '#':
            result[-1] = result[-1] * -1
    
    return sum(result)