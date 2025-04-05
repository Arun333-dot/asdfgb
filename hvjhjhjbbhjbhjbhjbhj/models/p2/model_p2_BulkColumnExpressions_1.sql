{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p2_post_BulkColumnExpressions_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH BulkColumnExpressions_1 AS (

  {{
    DatabricksSqlBasics.BulkColumnExpressions(
      'in0', 
      [], 
      '', 
      '', 
      false, 
      false, 
      false, 
      'Select output type', 
      false, 
      [], 
      'Prefix / Suffix to be added', 
      ''
    )
  }}

)

SELECT *

FROM BulkColumnExpressions_1
