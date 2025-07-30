-- 1세대 : ID 1, ID 2,
-- 2세대 : ID 3, ID 4, ID 5
-- 3세대 : ID 6, ID 7
-- 4세대 : ID 8

-- 세대별 자식이 없는 대장균의 ID
-- 1세대 : ID 1
-- 2세대 : ID 3, ID 5
-- 3세대 : ID 7
-- 4세대 : ID 8

WITH RECURSIVE gen AS (
    -- 1세대: 부모가 없는 개체들
    SELECT
        id,
        parent_id,
        1 AS generation
    FROM ECOLI_DATA
    WHERE parent_id IS NULL

    UNION ALL

    -- 다음 세대: 부모의 세대 + 1
    SELECT
        e.id,
        e.parent_id,
        g.generation + 1 AS generation
    FROM ECOLI_DATA e
    JOIN gen g
      ON e.parent_id = g.id
)
SELECT
    COUNT(*) AS COUNT,
    generation AS GENERATION
FROM gen g
LEFT JOIN ECOLI_DATA c
  ON c.parent_id = g.id      -- g가 부모인 자식이 존재하는지 확인
WHERE c.id IS NULL           -- 자식이 없으면 리프
GROUP BY generation
ORDER BY generation;
