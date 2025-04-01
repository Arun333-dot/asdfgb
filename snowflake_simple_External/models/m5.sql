WITH GRADES AS (

  SELECT * 
  
  FROM {{ source('BLACKROCK.TEST', 'GRADES') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM GRADES AS in0

)

SELECT *

FROM Reformat_1
