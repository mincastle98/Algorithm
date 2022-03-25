-- CombineTwoTables
SELECT firstName, lastName, city, state
FROM Person p left join Address a
    on p.personID = a.personID