def solution(s):
    table = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    str = ""
    answer = ""
    
    for i in range(len(s)):
        str += s[i]
        if str == table[0] or str == '0':
            answer += '0'
            str = ""
        elif str == table[1] or str == '1':
            answer += '1'
            str = ""
        elif str == table[2] or str == '2':
            answer += '2'
            str = ""
        elif str == table[3] or str == '3':
            answer += '3'
            str = ""
        elif str == table[4] or str == '4':
            answer += '4'
            str = ""
        elif str == table[5] or str == '5':
            answer += '5'
            str = ""
        elif str == table[6] or str == '6':
            answer += '6'
            str = ""
        elif str == table[7] or str == '7':
            answer += '7'
            str = ""
        elif str == table[8] or str == '8':
            answer += '8'
            str = ""
        elif str == table[9] or str == '9':
            answer += '9'
            str = ""
            
    return int(answer)

# 다른 사람 풀이===========
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)