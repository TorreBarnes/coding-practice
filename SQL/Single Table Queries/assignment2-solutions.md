SELECT*
FROM employees;
----------------------------------------------------------------------------------------------
SELECT first_name, last_name
FROM employees;
----------------------------------------------------------------------------------------------
SELECT DISTINCT(title)
FROM titles;
----------------------------------------------------------------------------------------------
SELECT emp_no, from_date, salary
FROM salaries;
----------------------------------------------------------------------------------------------
SELECT emp_no
FROM salaries
WHERE $60000 < salary < $71000;
----------------------------------------------------------------------------------------------
SELECT*
FROM employees
WHERE ‘Demeyer’ IN (last_name, first_name);
----------------------------------------------------------------------------------------------
SELECT emp_no, from_date, to_date
FROM titles
WHERE title IN (‘Senior Engineers’, ’Assistant Engineers’, ‘Engineers’, ‘Technique Leaders’);
----------------------------------------------------------------------------------------------
SELECT emp_no, hire_date
FROM employees
WHERE first_name, last_name NOT IN (‘Facello’, ‘Zielinski’, ‘Haddadi’, ‘Berztiss’, ‘Demeyer’)
----------------------------------------------------------------------------------------------
