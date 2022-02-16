n = input()
array = [0]*26

for i in n:
    array[ord(i)%97] += 1

print(*array)