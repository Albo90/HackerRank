SELECT hacker_id, name
FROM
(SELECT hacker_id, name, COUNT(*) as count_val
FROM
(SELECT h.hacker_id, h.name, s.challenge_id
FROM Submissions s
JOIN Challenges c
  ON s.challenge_id = c.challenge_id
JOIN Difficulty d
  ON d.difficulty_level = c.difficulty_level AND s.score = d.score
JOIN Hackers h
  ON h.hacker_id = s.hacker_id) AS full_view
GROUP BY hacker_id, name) AS res
WHERE count_val > 1
ORDER BY count_val DESC, hacker_id ASC