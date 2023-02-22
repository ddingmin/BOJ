-- 코드를 입력하세요
SELECT distinct F.flavor
FROM FIRST_HALF AS F, ICECREAM_INFO AS I
WHERE F.flavor = I.flavor AND F.total_order > 3000 and I.INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER DESC