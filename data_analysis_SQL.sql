SELECT bank_id, bank_name, city, state, cert, acquired_by, closed_date, fund
FROM fdic_bank_failures;

#States with the highest number of bank failures since 2000
SELECT state, COUNT(state) AS number_of_state
FROM fdic_bank_failures
GROUP BY state
ORDER BY COUNT(state) DESC;

#Companies with the highest number of acquisitions since 2000
SELECT acquired_by, COUNT(acquired_by) AS number_of_acquistions
FROM fdic_bank_failures
GROUP BY acquired_by
ORDER BY number_of_acquistions DESC;

#Year with the highest number of bank failures
SELECT EXTRACT(YEAR FROM closed_date) AS year, COUNT(*) AS year_count
FROM fdic_bank_failures
GROUP BY year
ORDER BY year_count DESC;

#Average number of bank failures per year
SELECT AVG(num_failures) AS avg_num_per_year
FROM (
	  SELECT EXTRACT(YEAR FROM closed_date) AS year, COUNT(*) AS num_failures
	  FROM fdic_bank_failures
	  GROUP BY year
) y;

#Average number of bank failures per month
SELECT EXTRACT(MONTH FROM closed_date) AS month, COUNT(*) AS month_count
FROM fdic_bank_failures
GROUP BY month
ORDER BY month_count DESC;

