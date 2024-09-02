"""
SQLITE

1. Create/Drop table:
CREATE TABLE shopping (id INTEGER PRIMARY KEY, name TEXT, amount
INTEGER);

DROP TABLE shopping
2. Rename table:
ALTER table shopping RENAME to shopp
ALTER table shopp RENAME to shopping
-- alter changes the table name

3. Insert rows into table:
INSERT INTO shopping VALUES (1, 'Avokado', 5);
INSERT INTO shopping VALUES (2, 'Milk', 2);
INSERT INTO shopping VALUES (3, 'Bread', 3);
INSERT INTO shopping VALUES (4, 'Chocolate', 8);
INSERT INTO shopping VALUES (5, 'Bamba', 5);
INSERT INTO shopping VALUES (6, 'Orange', 10);
4. Display table:
select * from shopping
5. ?
SELECT id, name FROM shopping
6. ?
SELECT * FROM shopping WHERE amount > 5
SELECT * FROM shopping WHERE amount = 2
SELECT * FROM shopping WHERE name LIKE 'Bamba'
7. ?
DELETE from shopping WHERE name like 'Orange';
8. ?
UPDATE shopping SET name = 'Bisli' WHERE name LIKE 'Bamba'
UPDATE shopping SET amount=1 WHERE name LIKE 'Milk'
9. ?
ALTER TABLE shopping ADD COLUMN maavar
10. ?
UPDATE shopping SET maavar=6 WHERE id=1;
UPDATE shopping SET maavar=3 WHERE id=2;
UPDATE shopping SET maavar=12 WHERE id=3;
UPDATE shopping SET maavar=8 WHERE id=4;
UPDATE shopping SET maavar=5 WHERE id=5;
11. ?
SELECT * FROM shopping WHERE amount > 1 AND maavar > 5
SELECT * FROM shopping WHERE maavar BETWEEN 3 AND 5
12. ?
SELECT * FROM shopping ORDER BY maavar
SELECT * FROM shopping ORDER BY maavar DESC
13. ?
CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO books VALUES (1, 'SQL PROGRAMMING');
INSERT INTO books VALUES (2, 'CSHARP PROGRAMMING');
DELETE FROM books;
14. ?
SELECT COUNT(*)from shopping
SELECT MAX(amount) from shopping
SELECT AVG(amount) from shopping
SELECT MIN(amount) from shopping
15. ?
INSERT INTO shopping VALUES (6, 'Onions', 3, 6);
INSERT INTO shopping VALUES (7, 'Orio', 1, 8);
Select maavar, COUNT(*)FROM shopping GROUP BY maavar
16. ?
SELECT id AS "SECRET", name, amount, maavar FROM shopping
17. ?
Select maavar, COUNT(*)FROM shopping GROUP BY maavar HAVING COUNT(*)>1
18. ?
CREATE TABLE prices (id INTEGER PRIMARY KEY, price INTEGER);
INSERT INTO prices VALUES (1, 3);
INSERT INTO prices VALUES (2, 7);
INSERT INTO prices VALUES (3, 12);
INSERT INTO prices VALUES (4, 5);
INSERT INTO prices VALUES (5, 3);
INSERT INTO prices VALUES (6, 2);
INSERT INTO prices VALUES (7, 10);
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id
19. ? SECRET מה מחושב בתוך
SELECT s.id, s.name, s.amount, s.maavar, p.price, s.amount * p.price AS
"SECRET" FROM shopping s JOIN prices p ON s.id=p.id
20. ?
SELECT s.id, s.name, s.amount, s.maavar, p.price FROM shopping s JOIN
prices p ON s.id=p.id WHERE p.price = (SELECT MAX(price) FROM prices)
( 2 ( פתור:
Students
BIRTH (INTEGER)
CITY (TEXT)
NAME (TEXT)
ID (INTEGER)PRIMARY KEY
1974
TEL AVIV
SHALOM
1
1980
RAANANA
YURI
2
1994
RISHON
ANAT
3
1990
REHOVOT
DANA
4
1987
JERUSALEM
OMER
5
GRADE
- כתוב את השאילתות ליצירת הטבלאות )ללא האיכלוס(
___________________________________________________________________
___________________________________________________________________
- כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל
___________________________________________________________________
___________________________________________________________________
- כתוב שאילתא אשר מחשבת את הממוצע הכיתתי
___________________________________________________________________
- כתוב שאילתא להוספת עמודה EXCELLENT . כעת שים YES כאשר הציון גבוה מ- 90 אחרת שים NO
___________________________________________________________________
___________________________________________________________________
- *כתוב שאילתא אשר מדפיסה את כל התלמידים ולכל תלמיד את הציון שהוא קיבל רק עבור
התלמידים אשר קיבלו מעל הממוצע
___________________________________________________________________
___________________________________________________________________
- * כתוב שאילתא אשר מדפיסה את התלמיד ואת ציונו עבור התלמיד אשר קיבל את הציון הגבוה
ביותר_______________________________________________________________
_______________________________________________________________
"""