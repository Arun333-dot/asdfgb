WITH all_type_databricks AS (

  SELECT * 
  
  FROM {{ source('qa_team.qa_database', 'all_type_databricks') }}

)

SELECT *

FROM all_type_databricks
