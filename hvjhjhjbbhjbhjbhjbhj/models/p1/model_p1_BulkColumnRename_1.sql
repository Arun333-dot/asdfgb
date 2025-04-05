{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_p1_post_BulkColumnRename_1_0",
    "database": "hive_metastore",
    "schema": "arun123"
  })
}}

WITH BulkColumnRename_1 AS (

  {{ DatabricksSqlBasics.BulkColumnRename('', [], '', '', '', "") }}

)

SELECT *

FROM BulkColumnRename_1
