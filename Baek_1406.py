# Time Rimmit Error
import sys
stack = list(map(str, sys.stdin.readline()))
point = len(stack)
n = int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if point > 0:
            point -= 1
    elif command[0] == 'D':
        if point < len(stack):
            point += 1
    elif command[0] == 'B':
        if point > 0:
            stack.pop(point-1)
    elif command[0] == 'P':
        stack.insert(point, command[1])
print("".join(stack))

# Why Error?
import sys
stack_1 = list(map(str, sys.stdin.readline()))
stack_2 = []

for __ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == 'L':
        if len(stack_1) != 0:
            stack_2.append(stack_1.pop())
            
    elif command[0] == 'D':
        if len(stack_2) != 0:
            stack_1.append(stack_2.pop())
            
    elif command[0] == 'B':
        if len(stack_1) != 0:
            stack_1.pop()
            
    elif command[0] == 'P':
        stack_1.append(command[1])

stack_1.extend(reversed(stack_1))
print("".join(stack_1))