# import datetime
# now = datetime.datetime.now()
# print(now)

# from datetime import datetime
# now = datetime.now()
# print(now)

# import random

# a = random.sample(range(1, 46), 6)
# print(a)

# with open('test.txt', 'w', encoding = 'utf-8') as f:
#     f.write('Happy Hacking!\n')
#     f.write('sex!\n')
#     for i in range(1, 5) :
#         f.write(f'{i} 번째!\n')
        # f.write('%d'+'번쩨!\n' % i)

# with open('test.txt', 'r', encoding = 'utf-8') as f:
 
#     text = f.read()
#     print(text, type(text))

# with open('test.txt', 'r', encoding = 'utf-8') as f:
 
#     for line in f :
#         print(line, end ='')

## 여기서는json

import json
## 파일을 열고, 
## Json을 파이썬 객체 형식으로 한다. 

kospi_json = open('stocks.json', 'r', encoding = 'utf-8')
json.load(kospi_json)
print(kospi)