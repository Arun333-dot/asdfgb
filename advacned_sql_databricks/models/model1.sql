WITH seed AS (

  SELECT * 
  
  FROM {{ ref('seed_github')}}

)

SELECT *

FROM seed
