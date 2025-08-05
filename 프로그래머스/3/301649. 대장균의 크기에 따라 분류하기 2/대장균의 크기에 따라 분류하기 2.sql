SELECT ID,
       CASE QUARTILE
           WHEN 1 THEN 'CRITICAL'  -- 상위 0% ~ 25%
           WHEN 2 THEN 'HIGH'      -- 상위 26% ~ 50%
           WHEN 3 THEN 'MEDIUM'    -- 상위 51% ~ 75%
           ELSE 'LOW'              -- 상위 76% ~ 100%
       END AS COLONY_NAME
FROM (
    SELECT ID,
           NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS QUARTILE  -- 크기 기준 4등분
    FROM ECOLI_DATA
) AS quartile_data
ORDER BY ID;