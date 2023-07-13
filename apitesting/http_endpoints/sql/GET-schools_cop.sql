/* Getting Started:
Enter "USE {database};" before entering your SQL statements.
Type "--your question" + Enter to try out AI-generated SQL queries
Declare a parameter like "Where id = ${arg}".
*/
SELECT *
FROM
  sample_data.global_fortune_500_2018_2022
WHERE
  year = ${year}
