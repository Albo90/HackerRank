SELECT c.company_code, c.founder, lead.total, sen.total, m.total, e.total FROM (SELECT DISTINCT * FROM Company) as c
JOIN (SELECT company_code, COUNT(DISTINCT lead_manager_code) AS total FROM Lead_Manager GROUP BY company_code) AS lead ON lead.company_code = c.company_code
JOIN (SELECT company_code, COUNT(DISTINCT senior_manager_code) AS total FROM Senior_Manager GROUP BY company_code) AS sen ON sen.company_code = c.company_code
JOIN (SELECT company_code, COUNT(DISTINCT manager_code)AS total FROM Manager GROUP BY company_code) AS m ON m.company_code = c.company_code
JOIN (SELECT company_code, COUNT(DISTINCT employee_code)AS total FROM Employee GROUP BY company_code) AS e ON e.company_code = c.company_code
ORDER BY c.company_code ASC