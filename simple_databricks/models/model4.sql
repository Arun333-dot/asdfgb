WITH seed1 AS (

  SELECT * 
  
  FROM {{ ref('seed1')}}

),

Reformat_1 AS (

  SELECT * 
  
  FROM seed1 AS in0

)

SELECT *

FROM seed1
