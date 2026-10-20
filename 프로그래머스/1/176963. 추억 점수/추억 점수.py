def solution(name, yearning, photo):
    #그리운 사람 이름 : name
    #그리움 점수 : yearning
    #사진에 찍힌 인물 : photo
    
    dict = {}
    answer = []
    for i,j in zip(name,yearning):
            dict[i] = dict.get(i,0)+j
    print(dict)
    
    for i in range(len(photo)):
        point = 0
        for j in range(len(photo[i])):
            point+= dict.get(photo[i][j], 0)
        answer.append(point)

    return answer