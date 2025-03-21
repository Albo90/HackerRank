SELECT res FROM (
SELECT N, Concat(N, " Root") as res  FROM BST where P IS NULL
UNION
SELECT N, Concat(N, " Leaf") as res FROM BST b WHERE b.P IS NOT NULL AND NOT EXISTS(SELECT N FROM BST b1 WHERE b.N = b1.P)
UNION
SELECT N, Concat(N, " Inner") as res FROM BST b WHERE b.P IS NOT NULL AND EXISTS(SELECT N FROM BST b1 WHERE b.N = b1.P)
) AS Final
ORDER BY N ASC