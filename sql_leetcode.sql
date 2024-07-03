
/*
1757. Recyclable and Low Fat Products
*/
SELECT product_id
FROM Products
WHERE (low_fats = 'Y' AND recyclable = 'Y')

/*
584. Find Customer Referee
*/
SELECT name
FROM Customer
WHERE (referee_id IS NULL) OR (referee_id != 2);

/*
595. Big Countries
*/
SELECT name, population, area
FROM World
WHERE (area >= 3000000) OR (population >= 25000000);

/*
1148. Article Views I
*/
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;

/*
1683. Invalid Tweets
*/
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;

/*
1378. Replace Employee ID With The Unique Identifier
*/
SELECT 
       EmployeeUNI.unique_id AS unique_id,
       Employees.name AS name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id=EmployeeUNI.id
;

/*
1068. Product Sales Analysis I
*/
SELECT
    Sales.year,
    Sales.price,
    Product.product_name
FROM
    Sales
JOIN Product ON Sales.product_id=Product.product_id
;

/*
1581. Customer Who Visited but Did Not Make Any Transactions
*/
SELECT
    Visits.customer_id,
    COUNT(customer_id) AS count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.visit_id IS NULL
GROUP BY customer_id
;

/*
197. Rising Temperature
*/
SELECT 
    w1.id
FROM Weather w1
JOIN Weather w2 ON (DATEDIFF(w1.recordDate,w2.recordDate) = 1)
WHERE w1.temperature > w2.temperature
;

/*
1661. Average Time of Process per Machine
*/
SELECT a.machine_id,
round(
    (SELECT AVG(a1.timestamp) FROM Activity a1 WHERE a1.activity_type = 'end' and a1.machine_id = a.machine_id) -
    (SELECT AVG(a1.timestamp) FROM Activity a1 WHERE a1.activity_type = 'start' and a1.machine_id = a.machine_id),
    3) AS processing_time
FROM Activity a
GROUP BY a.machine_id;

/*
577. Employee Bonus
*/
SELECT employee.name, Bonus AS bonus
FROM Employee
LEFT JOIN Bonus ON Employee.empID = Bonus.empID
WHERE bonus is NULL or bonus < 1000;

/*
577. Employee Bonus
*/
SELECT  s.student_id, s.student_name, sb.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS sb
LEFT JOIN Examinations AS e ON s.student_id = e.student_id AND e.subject_name = sb.subject_name
GROUP BY s.student_id, s.student_name, sb.subject_name
ORDER BY s.student_id ASC, s.student_name ASC;

/*
620. Not Boring Movies
*/
SELECT *
FROM Cinema
WHERE description != 'boring' And id % 2 = 1
ORDER BY rating DESC;

/*
1251. Average Selling Price
*/
SELECT product_id, ROUND(CASE WHEN total_units = 0 THEN 0 ELSE total_price / total_units END, 2) AS average_price
FROM (
    SELECT p.product_id, SUM(p.price*s.units) AS total_price, COALESCE(SUM(s.units), 0) AS total_units
    FROM Prices AS p
    LEFT JOIN UnitsSold AS s 
    ON p.product_id = s.product_id
    AND s.purchase_date BETWEEN p.start_date AND p.end_date
    GROUP BY p.product_id
) AS subquery;
