WITH ordersdatabaseinput AS (

  SELECT * 
  
  FROM {{ source('prophecy-field.dataset_two', 'ordersdatabaseinput') }}

)

SELECT *

FROM ordersdatabaseinput
