SELECT 
    ID, 
    CASE 
        -- 크기가 100 이하라면 LOW
        WHEN SIZE_OF_COLONY <= 100 THEN "LOW"
        -- 100 초과 1000 이하라면 MEDIUM
        WHEN SIZE_OF_COLONY <= 1000 THEN "MEDIUM"
        -- 1000 초과라면 HIGH
        ELSE "HIGH"
    END AS SIZE
FROM ECOLI_DATA 
ORDER BY ID