WITH seed1 AS (

  SELECT * 
  
  FROM {{ ref('seed1_github')}}

)

SELECT *

FROM seed1
