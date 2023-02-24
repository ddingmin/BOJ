-- 코드를 입력하세요
SELECT BOOK.AUTHOR_ID, AUTHOR.AUTHOR_NAME, CATEGORY, SUM(SALES * PRICE) AS TOTAL_SALES
from book, author, book_sales as sales
where year(sales.sales_date) = '2022' and month(sales.sales_date) = '01' and
book.author_id = author.author_id and book.book_id = sales.book_id
GROUP BY AUTHOR.AUTHOR_NAME, CATEGORY
ORDER BY 1, 3 DESC