WITH seed1 AS (

  SELECT * 
  
  FROM {{ ref('seed1')}}

),

Aggregate_1 AS (

  SELECT * 
  
  FROM seed1 AS in0

)

SELECT *

FROM Aggregate_1
