WITH million_records AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.arun123', 'million_records') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM million_records AS in0

),

ordered_reformat_1 AS (

  {#Organizes chronic patient records in ascending order by ID.#}
  SELECT * 
  
  FROM Reformat_1 AS in0
  
  ORDER BY id ASC NULLS FIRST

),

Limit_1 AS (

  SELECT * 
  
  FROM ordered_reformat_1 AS in0
  
  LIMIT 10

),

all_type_databricks AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'all_type_databricks') }}

),

Filter_1 AS (

  SELECT * 
  
  FROM Limit_1 AS in0
  
  WHERE true

)

SELECT *

FROM Filter_1
