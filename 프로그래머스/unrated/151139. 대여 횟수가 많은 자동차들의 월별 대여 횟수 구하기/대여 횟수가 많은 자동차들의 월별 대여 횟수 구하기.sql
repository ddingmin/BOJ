-- 코드를 입력하세요

-- 날짜 조건이 일치한 가상 테이블
WITH correct_date AS (
    SELECT month(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE year(START_DATE) = '2022'
    and month(START_DATE) between 8 AND 10
    GROUP BY CAR_ID, month(START_DATE)
)

SELECT *
FROM correct_date
WHERE CAR_ID in (
    SELECT CAR_ID
    FROM correct_date
    GROUP BY CAR_ID
    HAVING sum(RECORDS) >= 5
)
ORDER BY 1, 2 DESC