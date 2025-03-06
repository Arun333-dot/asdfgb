WITH customers_orders AS (

  SELECT * 
  
  FROM {{ source('prophecy-development.dataset', 'customers_orders') }}

)

SELECT *

FROM customers_orders
