{{
  config({    
    "materialized": "table",
    "alias": "prophecy__temp_share_point_pipelien_post_Limit_1_0",
    "database": "tanmay",
    "schema": "default"
  })
}}

WITH SharepointSource_0_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_share_point_pipelien_source', 'prophecy__temp_share_point_pipelien_pre_Reformat_1_1_0') }}

),

Reformat_1_1 AS (

  SELECT 
    Name AS Name,
    `Engagement category` AS `Engagement category`,
    `Engagement score` AS `Engagement score`,
    `Salesforce Account Account Name` AS `Salesforce Account Account Name`,
    `Salesforce Account Crossbeam Databricks Account Status` AS `Salesforce Account Crossbeam Databricks Account Status`,
    `Salesforce Account Account ID` AS `Salesforce Account Account ID`,
    `Salesforce Account Industry` AS `Salesforce Account Industry`,
    `Salesforce Account Account Type` AS `Salesforce Account Account Type`,
    `Salesforce Account Number Of Opportunities` AS `Salesforce Account Number Of Opportunities`,
    `Salesforce Account Open To Low Code` AS `Salesforce Account Open To Low Code`,
    `Hubspot Company Last Touch Converting Campaign` AS `Hubspot Company Last Touch Converting Campaign`,
    `Hubspot Company First Touch Converting Campaign` AS `Hubspot Company First Touch Converting Campaign`,
    `Salesforce Account Last MQL Date` AS `Salesforce Account Last MQL Date`
  
  FROM SharepointSource_0_1 AS in0

),

SharepointSource_0 AS (

  SELECT * 
  
  FROM {{ source('prophecy__temp_share_point_pipelien_source', 'prophecy__temp_share_point_pipelien_pre_Reformat_1_0') }}

),

Reformat_1 AS (

  SELECT 
    Name AS Name,
    `Engagement category` AS `Engagement category`,
    `Engagement score` AS `Engagement score`,
    `Salesforce Account Account Name` AS `Salesforce Account Account Name`,
    `Salesforce Account Crossbeam Databricks Account Status` AS `Salesforce Account Crossbeam Databricks Account Status`,
    `Salesforce Account Account ID` AS `Salesforce Account Account ID`,
    `Salesforce Account Industry` AS `Salesforce Account Industry`,
    `Salesforce Account Account Type` AS `Salesforce Account Account Type`,
    `Salesforce Account Number Of Opportunities` AS `Salesforce Account Number Of Opportunities`,
    `Salesforce Account Open To Low Code` AS `Salesforce Account Open To Low Code`,
    `Hubspot Company Last Touch Converting Campaign` AS `Hubspot Company Last Touch Converting Campaign`,
    `Hubspot Company First Touch Converting Campaign` AS `Hubspot Company First Touch Converting Campaign`,
    `Salesforce Account Last MQL Date` AS `Salesforce Account Last MQL Date`
  
  FROM SharepointSource_0 AS in0

),

engagement_data_summary AS (

  SELECT 
    in0.Name AS Name,
    in0.`Engagement category` AS `Engagement category`,
    in0.`Engagement score` AS `Engagement score`,
    in0.`Salesforce Account Account Name` AS `Salesforce Account Account Name`,
    in0.`Salesforce Account Crossbeam Databricks Account Status` AS `Salesforce Account Crossbeam Databricks Account Status`,
    in0.`Salesforce Account Account ID` AS `Salesforce Account Account ID`,
    in0.`Salesforce Account Industry` AS `Salesforce Account Industry`,
    in0.`Salesforce Account Account Type` AS `Salesforce Account Account Type`,
    in0.`Salesforce Account Number Of Opportunities` AS `Salesforce Account Number Of Opportunities`,
    in0.`Salesforce Account Open To Low Code` AS `Salesforce Account Open To Low Code`,
    in0.`Hubspot Company Last Touch Converting Campaign` AS `Hubspot Company Last Touch Converting Campaign`,
    in0.`Hubspot Company First Touch Converting Campaign` AS `Hubspot Company First Touch Converting Campaign`,
    in0.`Salesforce Account Last MQL Date` AS `Salesforce Account Last MQL Date`
  
  FROM Reformat_1 AS in0
  INNER JOIN Reformat_1_1 AS in1
     ON true

),

OrderBy_1 AS (

  SELECT * 
  
  FROM engagement_data_summary AS in0
  
  ORDER BY Name ASC NULLS FIRST

),

Limit_1 AS (

  SELECT * 
  
  FROM OrderBy_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
