# # 예제 03. [오류해결] 입력 받기
# # numbers = input().split()
# numbers = map(int, input().split())
# print(sum(numbers))

# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# # 원인 : sum 함수는 컨테이너 내의 요소들이 int 타입을 가지고 있어야 작동한다.
# # 해결 : 기존의 numbers의 요소는 str 타입이었기 때문에 map()을 통해 요소들을 int로 형변환 시켰다.

# # 예제 04. [오류 해결] 입력 받기 -2
# # words =  list(map(int, input().split()))
# words =  list(input().split())
# print(words)

# # ValueError : invalid literal for int() with base 10: "i'm"
# # 원인 : int()는 알파벳을 int 타입으로 바꿔주지 못한다. 
# # 해결 : 그냥 str 그대로 나눠서 리스트에 넣는다. 

# # 예제 05. [오류 해결] 숫자의 길이 구하기
# # number = 22020718
# number = str(22020718)
# print(len(number))

# # TypeError: object of type 'int' has no len()
# # 원인 : len()은 int 타입의 개수를 헤아릴 수 없다. 
# # 해결 : str으로 형변환해서 len()을 한다. 

# # 예제 06.[오류 해결] 1부터 N까지의 2의 곱 저장하기

# N = 10
# answer = []
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# # AttributeError: 'tuple' object has no attribute 'append'
# # 원인 : tuple은 immutable 하기 때문에 값 추가가 안된다.
# # 해결 : mutable 한 리스트에 값을 추가한다. 

# # 예제 07. [오류 해결] 평균 구하기

# number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# total = 0
# count = 0

# for number in number_list:
#     total += number
#     count += 1

# print(total // count)

# # 원인 : indentation이 안되어서 카운트가 한번만 되었다. 
# # 해결 : indentation을 한다. 

# # 예제 08. [오류 해결] 모음의 개수 찾기

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char in ['a', 'e', 'i', 'o', 'u'] :
#         count += 1
       

# print(count)

# # 원인 : 연산자 우선순위에서 '=='가 'or'보다 먼저이기 때문에 오류가 발생했다. 
# # 해결 시도_1. if char == ("a" or "e" or "i" or "o" or "u" or "y"): 이 코드는 제대로 작동을 하지 않는다. 
# # 해결 : 모음으로 이루어진 리스트를 만들어서, word의 요소들과 비교한다. 

# # 예제 09. [오류 해결] 과일 개수 구하기

# from pprint import pprint

# fruits = [
#     "Soursop",
#     "Grapefruit",
#     "Apricot",
#     "Juniper berry",
#     "Feijoa",
#     "Blackcurrant",
#     "Cantaloupe",
#     "Salal berry",
# ]

# fruit_count = {}

# for fruit in fruits:
#     if fruit not in fruit_count:
#         fruit_count[fruit] = 1
#     else:
#         fruit_count[fruit] += 1

# pprint(fruit_count)

# # 원인 :  fruit_count = {fruit: 1} 이 문장은 값을 더하는 게 아니라 초기화를 시켜버린다. 
# # 해결 :  fruit_count[fruit] = 1 

# 예제 10. [오류 해결] 더 큰 최댓값 찾기

# number_list = [1, 23, 9, 6, 91, 59, 29]
# max1 = max(number_list)

# number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
# max2 = max(number_list2)

# if max1 > max2:
#     print("첫 번째 리스트의 최댓값이 더 큽니다.")

# elif max1 < max2:
#     print("두 번째 리스트의 최댓값이 더 큽니다.")

# else:
#     print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 원인 : max() 는 내장함수인데, 여기서는 변수로 사용을 해서 에러가 난 거였다. 
# 해결 : 첫번째 리스트의 최대값을 max1에 할당한다. 

# # 예제 11. [오류 해결] 영화 정보 찾기

# from pprint import pprint


# def movie_info(movie, genres):
#     genres_names = []
#     genre_ids = movie["genre_ids"]
#     for genre_id in genre_ids:
#         for genre in genres:
#             if genre_id == genre["id"]:
#                 genre_name = genre["name"]
#                 genres_names.append(genre_name)

#     new_movie_info = {
#         "genre_names": genres_names,
#         "id": movie["id"],
#         "overview": movie["overview"],
#         "title": movie["title"],
#         "vote_average": movie["vote_average"],
#     }
#     return new_movie_info



# if __name__ == "__main__":
#     movie = {
#         "adult": False,
#         "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
#         "genre_ids": [18, 80],
#         "id": 278,
#         "original_language": "en",
#         "original_title": "The Shawshank Redemption",
#         "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
#         "popularity": 67.931,
#         "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
#         "release_date": "1995-01-28",
#         "title": "쇼생크 탈출",
#         "video": False,
#         "vote_average": 8.7,
#         "vote_count": 18040,
#     }

#     genres_list = [
#         {"id": 28, "name": "Action"},
#         {"id": 12, "name": "Adventure"},
#         {"id": 16, "name": "Animation"},
#         {"id": 35, "name": "Comedy"},
#         {"id": 80, "name": "Crime"},
#         {"id": 99, "name": "Documentary"},
#         {"id": 18, "name": "Drama"},
#         {"id": 10751, "name": "Family"},
#         {"id": 14, "name": "Fantasy"},
#         {"id": 36, "name": "History"},
#         {"id": 27, "name": "Horror"},
#         {"id": 10402, "name": "Music"},
#         {"id": 9648, "name": "Mystery"},
#         {"id": 10749, "name": "Romance"},
#         {"id": 878, "name": "Science Fiction"},
#         {"id": 10770, "name": "TV Movie"},
#         {"id": 53, "name": "Thriller"},
#         {"id": 10752, "name": "War"},
#         {"id": 37, "name": "Western"},
#     ]

#     pprint(movie_info(movie, genres_list))

#     # 원인 : 함수는 return 값을 반환한다.
#     # 해결 : new_movie_info를 return 한다. 

# 문제 19. 숫자의 길이 구하기

n = 123
test = 10
cnt = 1
while n > test :
    test = test *10
    cnt += 1

print(cnt)

# 해결 : 자리수는 10의 자리수를 기준으로 판별하기 때문에 10, 100, 1000 ... 을 비교했다. 