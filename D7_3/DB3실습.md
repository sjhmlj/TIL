###  1. 흡연 여부(smoking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT smoking, COUNT(*) FROM healthcare GROUP BY smoking;
```

```sql
smoking  COUNT(*)
-------  --------
1        626138  
2        189808  
3        183711  
         343 
```



###  2. 음주 여부(is_drinking)로 구분한 각 그룹의 컬렴명과 그룹의 사람의 수를 출력하시오.

```sql 
SELECT is_drinking, COUNT(*) FROM healthcare GROUP BY is_drinking;
```
```sql 
is_drinking  COUNT(*)
-----------  --------
0            415119  
1            584685  
             196 
```

### 3. 음주 여부로 구분한 각 그룹에서 혈압(blood_pressure)이 200이상인 사람의 수를 출력하시오.

```sql
SELECT is_drinking, COUNT(*) FROM healthcare WHERE blood_pressure >= 200 GROUP BY is_drinking;
```
```sql 
is_drinking  COUNT(*)
-----------  --------
0            6064    
1            1770    
```

### 4. 시도(sido)에 사는 사람의 수가 50000명 이상인 시도의 코드와 그 시도에 사는 사람의 수를 출력하시오.

```sql
SELECT sido, COUNT(*) '사람수' FROM healthcare GROUP BY sido HAVING COUNT(*) >= 50000;

```
```sql 
sido  사람수   
----  ------
11    166231
26    69025 
28    58345 
41    247369
47    54438 
48    68530 
```

### 5. 키(height)를 기준으로 구분하고, 각 키와 사람의 수를 출력하시오.

> 단, 사람의 수를 기준으로 내림차순으로 5개까지 출력하시오.

```sql
SELECT height, COUNT(*) FROM healthcare GROUP BY height ORDER BY COUNT(*) DESC LIMIT 5;
```
```sql 
height  COUNT(*)
------  --------
160     184993  
155     181306  
165     179352  
170     152585  
150     128555  
```

### 6. 키(height)와 몸무게(weight)를 기준으로 구분하고, 몸무게와, 키, 해당 그룹의 사람의 수를 출력하시오. 

> 단, 사람의 수를 기준으로 내림차순 5개까지 출력하시오.

```sql
SELECT height, weight, COUNT(*) FROM healthcare GROUP BY height, weight ORDER BY COUNT(*) DESC LIMIT 5;
```
```sql 
height  weight  COUNT(*)
------  ------  --------
155     55      45866   
160     60      42454   
165     65      40385   
155     50      38582   
160     55      38066   
```

### 7. 음주여부에 따라 평균 허리둘레(waist)와 사람의 수를 출력하시오.

```sql 
SELECT AVG(waist), COUNT(*), is_drinking FROM healthcare WHERE is_drinking <> '' GROUP BY is_drinking;
```
```sql 
AVG(waist)        COUNT(*)  is_drinking
----------------  --------  -----------
81.2128249971711  415119    0          
83.1541594191841  584685    1          
```

### 8. 각 성별(gender)의 평균 왼쪽 시력(va_left)과 평균 오른쪽 시력(va_right)를 출력하시오.

> 단, 평균 왼쪽 시력과 평균 오른쪽 시력의 컬럼명을 '평균 왼쪽 시력' '평균 오른쪽 시력'로 표시하고, 평균 시력은 소수점 둘째 자리까지 출력하시오.

```sql
SELECT AVG(va_left), AVG(va_right), gender FROM healthcare GROUP BY gender;
```
```sql 
AVG(va_left)       AVG(va_right)      gender
-----------------  -----------------  ------
0.982933448735036  0.98803371523777   1     
0.880487563125815  0.879241116591859  2     
```

### 9. 각 나이대(age)의 평균 키와 평균 몸무게를 출력하시오.

> 단, 평균 키와 평균 몸무게의 컬럼명을 '평균 키' '평균 몸무게'로 표시하고, 평균키가 160 이상 평균 몸무게가 60 이상인 데이터만 출력하시오.

```sql
SELECT age, AVG(height) AS '평균 키', AVG(weight) AS '평균 몸무게' FROM healthcare GROUP BY age HAVING AVG(height) >= 160 and AVG(weight) >= 60;
```
```sql 
age  평균 키              평균 몸무게          
---  ----------------  ----------------
9    165.66545300972   67.2402208898302
10   164.119689244962  65.677140776194 
11   162.111550610398  63.9036737713782
12   160.653006214415  62.5955563062588
```

### 10. 음주 여부(is_drinking)와 흡연 여부(smoking)에 따른 평균 BMI를 출력하시오.

> 단, 음주 여부 또는 흡연 여부가 공백이 아닌 행만 사용하세요.

```sql
SELECT is_drinking, smoking, AVG(weight / (height*height*0.0001)) AS 'AVG BMI' FROM healthcare WHERE is_drinking <> '' and smoking <> '' GROUP BY is_drinking, smoking;
```
```sql 
is_drinking  smoking  AVG BMI         
-----------  -------  ----------------
0            1        23.8724603942955
0            2        24.6073677352564
0            3        24.3193273448558
1            1        23.9341328992508
1            2        25.0333550564281
1            3        24.6363247421328
```