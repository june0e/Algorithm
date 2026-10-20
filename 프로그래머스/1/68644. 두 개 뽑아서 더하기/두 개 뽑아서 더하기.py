def solution(numbers):

    answer = []
    
    for i in range(len(numbers)): 
        for j in range(i+1,len(numbers)):
                   answer.append(numbers[i]+numbers[j])
    
    return  sorted(set(answer)) #오름차순으로 정렬된 새 리스트 반환