m, n = map(int, input().split())
for i in range(m, n+1):
    if i == 1:
        continue
    # 에라토스테네스의 체: 약수는 해당 수의 대칭이기에 해당 수의 제곱근까지만 확인하면 된다!
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        print(i)