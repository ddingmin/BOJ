-- 코드를 입력하세요
SELECT year(sales_date), month(sales_date), GENDER, 
count(distinct ONLINE_SALE.USER_ID) AS USERS
from USER_INFO, ONLINE_SALE
WHERE GENDER is not NULL AND USER_INFO.user_id = ONLINE_SALE.user_id
group by year(sales_date), month(sales_date), GENDER
-- where
order by 1, 2, 3