-- 코드를 입력하세요
SELECT f.FLAVOR as FLAVOR 
FROM  FIRST_HALF as f JOIN ICECREAM_INFO as i ON f.FLAVOR = i.FLAVOR
WHERE f.TOTAL_ORDER >= 3000 AND i.INGREDIENT_TYPE LIKE 'fruit_based'