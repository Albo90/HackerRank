CREATE VIEW view_occ AS
SELECT Name, occupation,
       DENSE_RANK() OVER (PARTITION BY occupation ORDER BY Name ASC) AS rank_val
FROM OCCUPATIONS;

CREATE VIEW view_doc AS
SELECT Name, rank_val FROM view_occ WHERE occupation = 'Doctor';
CREATE VIEW view_prof AS
SELECT Name, rank_val FROM view_occ WHERE occupation = 'Professor';
CREATE VIEW view_act AS
SELECT Name, rank_val FROM view_occ WHERE occupation = 'Actor';
CREATE VIEW view_sin AS
SELECT Name, rank_val FROM view_occ WHERE occupation = 'Singer';

CREATE VIEW view_first_two AS (
SELECT d.Name AS doc_name, p.Name AS prof_name, d.rank_val as rank_val
FROM view_doc d
LEFT JOIN view_prof p ON d.rank_val = p.rank_val
UNION
SELECT d.Name AS doc_name, p.Name AS prof_name, p.rank_val as rank_val
FROM view_doc d
RIGHT JOIN view_prof p ON d.rank_val = p.rank_val
);

CREATE VIEW view_first_three AS (
SELECT d.doc_name AS doc_name, d.prof_name AS prof_name, p.Name AS sin_name, d.rank_val as rank_val
FROM view_first_two d
LEFT JOIN view_sin p ON d.rank_val = p.rank_val
UNION
SELECT d.doc_name AS doc_name, d.prof_name AS prof_name, p.Name AS sin_name, p.rank_val as rank_val
FROM view_first_two d
RIGHT JOIN view_sin p ON d.rank_val = p.rank_val
);


SELECT d.doc_name, d.prof_name, d.sin_name, a.Name AS act_name
FROM view_first_three d
LEFT JOIN view_act a ON d.rank_val = a.rank_val
UNION
SELECT d.doc_name, d.prof_name, d.sin_name, a.Name AS act_name
FROM view_first_three d
RIGHT JOIN view_act a ON d.rank_val = a.rank_val;
