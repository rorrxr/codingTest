-- 평균을 구한 후, 세 번째 자리에서 반올림
SELECT RI.REST_ID AS REST_ID, RI.REST_NAME AS REST_NAME, 
RI.FOOD_TYPE AS FOOD_TYPE, RI.FAVORITES AS FAVORITES, 
RI.ADDRESS AS ADDRESS, ROUND(AVG(RR.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO RI 
JOIN REST_REVIEW RR
ON RI.REST_ID = RR.REST_ID
WHERE ADDRESS LIKE "서울%"
-- 식당별 평균 리뷰 점수(SCORE)를 계산하기 위해서 GROUP BY
-- 식당 단위로 묶기 위해 REST_ID 기준
GROUP BY RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS
ORDER BY SCORE DESC, FAVORITES DESC