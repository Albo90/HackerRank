CREATE VIEW vw_order AS
SELECT
DENSE_RANK() OVER (ORDER BY LAT_N DESC) as rank_val,
LAT_N
FROM STATION;

CREATE VIEW vw_final AS
(SELECT *,
 FLOOR((max(rank_val) OVER ())/2) as median_index_lower,
 CEIL((max(rank_val) OVER ())/2)  as median_index_upper
 FROM vw_order);

SELECT
CASE
 WHEN median_index_lower <> median_index_upper THEN ROUND(LAT_N, 4)
 ELSE ROUND((SUM(LAT_N) OVER ()), 4)
END
FROM vw_final
WHERE (median_index_lower = median_index_upper AND rank_val IN (median_index_lower, median_index_upper+1)) OR (median_index_lower <> median_index_upper AND rank_val = median_index_upper)