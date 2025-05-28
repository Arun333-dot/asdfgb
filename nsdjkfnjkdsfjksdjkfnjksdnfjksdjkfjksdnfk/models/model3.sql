WITH all_type_databricks AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'all_type_databricks') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM all_type_databricks AS in0

),

OrderBy_1 AS (

  {#Organizes chronic patient records in ascending order by ID.#}
  SELECT * 
  
  FROM Reformat_1 AS in0
  
  ORDER BY id ASC

),

Limit_1 AS (

  SELECT * 
  
  FROM OrderBy_1 AS in0
  
  LIMIT 10

),

Filter_1 AS (

  SELECT * 
  
  FROM Limit_1 AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
