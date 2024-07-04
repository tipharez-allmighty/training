
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

/*
1075. Project Employees I
*/
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project AS p
LEFT OUTER JOIN Employee AS e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id;
/*
1633. Percentage of Users Attended a Contest
*/
SELECT r.contest_id,
    ROUND(COUNT(DISTINCT r.user_id)/(SELECT COUNT(u.user_id) FROM Users As u)*100,2) AS percentage
FROM Register AS r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;

/*
1211. Queries Quality and Percentage
*/
SELECT 
    query_name,
    ROUND(SUM(rating / position) / NULLIF(COUNT(DISTINCT result), 0), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / NULLIF(COUNT(DISTINCT result), 0), 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;

/*
2356. Number of Unique Subjects Taught by Each Teacher
*/
SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;

/*
1141. User Activity for the Past 30 Days I
*/
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;

/*
596. Classes More Than 5 Students
*/
SELECT Class
FROM Courses
GROUP BY Class
HAVING COUNT(student) >= 5;

/*
1729. Find Followers Count
*/
SELECT user_id, COUNT(DISTINCT follower_id) AS followers_count
FROM Followers
GROUP BY user_id;

/*
619. Biggest Single Number
*/
SELECT MAX(num) as num
FROM (SELECT num
     FROM MyNumbers
     GROUP BY num
     HAVING COUNT(num) = 1)
     AS unique_nums;

/*
1731. The Number of Employees Which Report to Each Employee
*/
SELECT e1.employee_id, e1.name, COUNT(e2.employee_id) AS reports_count, ROUND(AVG(e2.age), 0) AS average_age
FROM Employees AS e1
JOIN Employees AS e2 ON
    e1.employee_id = e2.reports_to
GROUP BY e1.employee_id
ORDER BY e1.employee_id ASC;

/*
1789. Primary Department for Each Employee
*/
SELECT employee_id,department_id
FROM Employee
GROUP BY employee_id, primary_flag
HAVING primary_flag = 'Y' OR employee_id in (SELECT employee_id
    FROM Employee
    Group by employee_id
    having count(employee_id)=1)

/*
610. Triangle Judgement
*/
SELECT x, y, z, 
    (CASE WHEN x + y > z and x + z > y and y + z > x THEN 'Yes' ELSE 'No' END) AS triangle
FROM Triangle;

/*
1978. Employees Whose Manager Left the Company
*/
SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id ASC;

/*
1667. Fix Names in a Table
*/

SELECT user_id, CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id ASC;

/*
1527. Patients With a Condition
*/
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions REGEXP '(^| )DIAB1';

/*
196. Delete Duplicate Emails
*/
DELETE p1
FROM Person AS p1, Person as p2
WHERE p1.email = p2.email AND p1.id > p2.id;

/*
1484. Group Sold Products By The Date
*/
SELECT sell_date, 
       COUNT(DISTINCT product) AS num_sold,
       GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date;


/*
1327. List the Products Ordered in a Period
*/
SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders as o
LEFT JOIN Products AS p ON o.product_id = p.product_id
WHERE o.order_date < '2020-03-1' AND o.order_date >= '2020-02-1'
GROUP BY o.product_id
HAVING unit >= 100;


/*
517. Find Users With Valid E-Mails
*/
SELECT *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$';
