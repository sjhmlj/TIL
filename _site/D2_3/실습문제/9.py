students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt = 0
for i in students :
    if i == '이영희' :
        cnt += 1
print(cnt)
while '이영희' in students : 
    students.remove('이영희')
    cnt += 1
print(cnt)