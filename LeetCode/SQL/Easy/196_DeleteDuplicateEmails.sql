-- DeleteDuplicateEmails
DELETE p2
FROM Person p1 JOIN Person p2
    ON p1.email = p2.email
WHERE p2.id > p1.id;