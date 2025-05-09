WITH all_type_databricks AS (

  SELECT * 
  
  FROM {{ source('hive_metastore.qa_database', 'all_type_databricks') }}

)

SELECT *

FROM all_type_databricks
