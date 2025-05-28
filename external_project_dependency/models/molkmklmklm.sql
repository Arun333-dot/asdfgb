WITH weeed AS (

  SELECT * 
  
  FROM {{ ref('weeed')}}

)

SELECT *

FROM weeed
