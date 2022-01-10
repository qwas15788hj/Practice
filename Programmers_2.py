def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    a = []
    b = []

    # 2단계
    for i in range(len(new_id)):
        if new_id[i].islower() == True or new_id[i].isdigit() == True or new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            a.append(new_id[i])
    
    a = "".join(a)

    # 3단계        
    for i in range(len(a)-1):
        count = 0
        if a[i] == '.' and a[i+1] == '.':
            count += 1
        if count == 0:
            b.append(a[i])
            
    b.append(a[len(a)-1])

    # 4단계
    if not b:
        pass
    else:
        if b[0] == '.':
            b.pop(0)
    if not b:
        pass
    else:
        if b[len(b)-1] == '.':
            b.pop(-1)

    # 5단계
    if not b:
        b.append("a")
    
    # 6단계
    if len(b) > 15:
        while len(b) > 15:
            b.pop(-1)
    
    if b[len(b)-1] == '.':
        b.pop(-1)
        
    # 7단계
    if len(b) == 1:
        b.append(b[0])
        b.append(b[0])
    elif len(b) == 2:
        b.append(b[1])

    
    answer = "".join(b)
    return answer