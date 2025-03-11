{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_dgfgdfgdfg_post_model1_0_0",
    "database": "database",
    "schema": "default"
  })
}}

WITH model1_0 AS (

  {{ sql_advanced_project.model1() }}

)

SELECT *

FROM model1_0
