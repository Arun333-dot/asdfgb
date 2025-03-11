WITH model1 AS (

  SELECT * 
  
  FROM {{ ref('model1')}}

),

model3 AS (

  SELECT * 
  
  FROM {{ ref('model3')}}

)

SELECT *

FROM model1
