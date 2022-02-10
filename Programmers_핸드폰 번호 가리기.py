def solution(phone_number):
    answer = '*'*int(len(phone_number)-4) + phone_number[len(phone_number)-4:]
    return answer