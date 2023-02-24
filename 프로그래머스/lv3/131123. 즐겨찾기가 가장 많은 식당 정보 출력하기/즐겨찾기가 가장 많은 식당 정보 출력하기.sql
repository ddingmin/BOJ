-- 코드를 입력하세요
# SELECT FOOD_TYPE, REST_ID, REST_NAME, (FAVORITES)
# FROM REST_INFO
# WHERE FAVORITES in (
#     SELECT MAX(FAVORITES)
#     FROM REST_INFO
#     GROUP BY FOOD_TYPE
# )
# -- GROUP BY FOOD_TYPE
# ORDER BY 1 DESC
SELECT MAX(FAVORITES)
FROM REST_INFO
GROUP BY FOOD_TYPE