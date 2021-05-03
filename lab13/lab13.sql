.read su19data.sql

CREATE TABLE obedience AS
  SELECT seven,instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time,smallest FROM students WHERE smallest>2 ORDER BY smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT s1.pet,s1.song,s1.color,s2.color FROM students AS s1,students AS s2 WHERE s1.pet=s2.pet AND s1.song=s2.song AND s1.time<s2.time;

CREATE TABLE smallest_int_having AS
  SELECT time,smallest FROM students GROUP BY smallest HAVING COUNT(smallest)=1;
