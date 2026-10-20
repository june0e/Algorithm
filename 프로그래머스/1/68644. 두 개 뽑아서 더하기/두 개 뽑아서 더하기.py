def solution(numbers):
    numbers.sort()
    answer = []
    #오름차순 정렬 0,2,5,7 -> 
    for i in range(len(numbers)): 
        for j in range(i+1,len(numbers)):
                   answer.append(numbers[i]+numbers[j])
    
    return sorted(set(answer))