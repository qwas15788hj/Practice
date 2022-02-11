def solution(numbers, target):
    # 앞에는 [50, 1], 2 같은 경우
    # 뒤에는 다 더한게 target보다 작을 때
    if max(numbers) > sum(numbers[:numbers.index(max(numbers))]) + sum(numbers[numbers.index(max(numbers))+1:]) + target or sum(numbers) < target:
        return 0
    
    # 예2 같은 경우
    elif target == max(numbers) and sum(numbers[:numbers.index(max(numbers))]) + sum(numbers[numbers.index(max(numbers))+1:]) == max(numbers):
        return 2
    
    else:
        num_list = []
        num_list.append(numbers[0])
        num_list.append(-1*numbers[0])

        for i in range(1, len(numbers)):
            for j in range(2**i):
                num_list.append(num_list[j] + numbers[i])
                num_list.append(num_list[j] - numbers[i])

            for r in range(2**i):
                num_list.pop(0)

        print(num_list)
        print(num_list.count(target))

        return num_list.count(target)