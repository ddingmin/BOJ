-- 코드를 입력하세요
# 5월인 식품의 총 판매량
WITH OD AS
(
    SELECT OD.PRODUCT_ID, SUM(AMOUNT) AS TOTAL_AMOUNT
    FROM FOOD_ORDER AS OD
    WHERE (PRODUCE_DATE) LIKE '2022-05%'
    GROUP BY PRODUCT_ID
)



SELECT DISTINCT OD.PRODUCT_ID, PD.PRODUCT_NAME, (OD.TOTAL_AMOUNT * PD.PRICE) AS TOTAL_SALES
FROM OD
JOIN FOOD_PRODUCT AS PD ON OD.PRODUCT_ID = PD.PRODUCT_ID
ORDER BY 3 DESC, 1

