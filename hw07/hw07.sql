CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name,size FROM dogs,sizes WHERE height>min AND height<=max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d1.name FROM dogs AS d1,parents,dogs AS d2 WHERE d1.name=child AND parent=d2.name ORDER BY d2.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT d1.name AS s1,d2.name AS s2 FROM dogs AS d1,parents AS p1,dogs AS d2,parents AS p2 WHERE d1.name=p1.child AND d2.name=p2.child AND p1.parent=p2.parent AND d1.name<d2.name;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT s1||" and "||s2||" are "||sd1.size||" siblings" FROM siblings,size_of_dogs AS sd1,size_of_dogs AS sd2 WHERE s1=sd1.name AND s2=sd2.name AND sd1.size=sd2.size;

-- Total size for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur,SUM(height) FROM dogs GROUP BY fur HAVING height>0.7*AVG(height) AND height<1.3*AVG(height);
