{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_grtgrtgrt_post_m1_1_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH m1_1 AS (

  {{ databricks_shared_external_project.m1() }}

)

SELECT *

FROM m1_1
