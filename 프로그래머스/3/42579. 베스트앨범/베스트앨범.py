def solution(genres, plays):
    dic = {}
    genre_total = {}
    answer = []
    
    for i, genre in enumerate(genres):
        if genre not in dic:
            dic[genre] = [] #초기에 장르가 dic에 없으면 장르 추가
        if genre not in genre_total :
            genre_total[genre] = 0
        dic[genre].append((i,plays[i]))#장르에 튜플값 추가
        genre_total[genre] += plays[i]
    
    sorted_genre = sorted(genre_total.items(),key=lambda x: x[1],reverse=True)

    for i in genre_total:
        #장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다. 조건
        dic[i] = sorted(dic[i],key=lambda x: (-x[1], x[0])) 
        
    for genre, total in sorted_genre:
        for song in dic[genre][:2]:
            answer.append(song[0])

    return answer