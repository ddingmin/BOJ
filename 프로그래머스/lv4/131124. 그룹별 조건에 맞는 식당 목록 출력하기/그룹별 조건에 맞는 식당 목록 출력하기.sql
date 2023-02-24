-- 코드를 입력하세요
WITH MOST AS (
    SELECT MEMBER_ID, COUNT(MEMBER_ID)
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY 2 DESC
    LIMIT 1
)

SELECT MEMBER_PROFILE.MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM REST_REVIEW, MOST, MEMBER_PROFILE
WHERE REST_REVIEW.MEMBER_ID = MOST.MEMBER_ID 
AND MEMBER_PROFILE.MEMBER_ID = REST_REVIEW.MEMBER_ID
ORDER BY 3, 2