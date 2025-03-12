SELECT * FROM
((SELECT
Concat(Name, CONCAT('(', SUBSTR(Occupation, 1, 1), ')')) as work_name
FROM OCCUPATIONS)
UNION(
SELECT
    CONCAT('There are a total of ', count , " ", lower(occupation), "s.") as work_name
    FROM(SELECT
    occupation, count(*) as count
    FROM OCCUPATIONS
    GROUP BY occupation
) AS T_1)
) AS fin
ORDER BY work_name ASC