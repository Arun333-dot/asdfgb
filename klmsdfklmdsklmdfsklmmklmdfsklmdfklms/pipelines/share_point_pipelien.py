Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_share_point_pipelien_Limit_1 = Task(
        task_id = "model_share_point_pipelien_Limit_1", 
        component = "Model", 
        modelName = "model_share_point_pipelien_Limit_1"
    )
    SharepointSource_0_1 = Task(
        task_id = "SharepointSource_0_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_share_point_pipelien_pre_Reformat_1_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_share_point_pipelien_source", 
          "alias": ""
        }
    )
    SharepointSource_0 = SourceTask(
        task_id = "SharepointSource_0", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint", id = "sharepoint"), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "Name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name of the entity or individual being engaged."
                        },                         {
                          "name": "Engagement category", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Category representing the level of engagement with the account"
                        },                         {
                          "name": "Engagement score", 
                          "dataType": {"type" : "float64"}, 
                          "description": "Score indicating the level of engagement with the account"
                        },                         {
                          "name": "Salesforce Account Account Name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name of the Salesforce account associated with the engagement."
                        },                         {
                          "name": "Salesforce Account Crossbeam Databricks Account Status", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Status of the account in relation to Crossbeam and Databricks"
                        },                         {
                          "name": "Salesforce Account Account ID", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the Salesforce account."
                        },                         {
                          "name": "Salesforce Account Industry", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The industry classification of the Salesforce account"
                        },                         {
                          "name": "Salesforce Account Account Type", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Type of the Salesforce account indicating its classification."
                        },                         {
                          "name": "Salesforce Account Number Of Opportunities", 
                          "dataType": {"type" : "int64"}, 
                          "description": "Total number of opportunities associated with the Salesforce account"
                        },                         {
                          "name": "Salesforce Account Open To Low Code", 
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether the Salesforce account is receptive to low-code solutions"
                        },                         {
                          "name": "Hubspot Company Last Touch Converting Campaign", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The last marketing campaign that converted the company in Hubspot"
                        },                         {
                          "name": "Hubspot Company First Touch Converting Campaign", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The campaign that first engaged the company in Hubspot."
                        },                         {
                          "name": "Salesforce Account Last MQL Date", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The date when the account was last marked as a Marketing Qualified Lead."
                        }]
          }
        ), 
        filePath = "/csv_files/accounts_final.csv"
    )
    SharepointSource_0_1 = SourceTask(
        task_id = "SharepointSource_0_1", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint", id = "sharepoint"), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "Name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name of the entity or individual being engaged."
                        },                         {
                          "name": "Engagement category", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Category representing the level of engagement with the account"
                        },                         {
                          "name": "Engagement score", 
                          "dataType": {"type" : "float64"}, 
                          "description": "Score indicating the level of engagement with the account"
                        },                         {
                          "name": "Salesforce Account Account Name", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name of the Salesforce account associated with the engagement."
                        },                         {
                          "name": "Salesforce Account Crossbeam Databricks Account Status", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Status of the account in relation to Crossbeam and Databricks"
                        },                         {
                          "name": "Salesforce Account Account ID", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for the Salesforce account."
                        },                         {
                          "name": "Salesforce Account Industry", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The industry classification of the Salesforce account"
                        },                         {
                          "name": "Salesforce Account Account Type", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Type of the Salesforce account indicating its classification."
                        },                         {
                          "name": "Salesforce Account Number Of Opportunities", 
                          "dataType": {"type" : "int64"}, 
                          "description": "Total number of opportunities associated with the Salesforce account"
                        },                         {
                          "name": "Salesforce Account Open To Low Code", 
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether the Salesforce account is receptive to low-code solutions"
                        },                         {
                          "name": "Hubspot Company Last Touch Converting Campaign", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The last marketing campaign that converted the company in Hubspot"
                        },                         {
                          "name": "Hubspot Company First Touch Converting Campaign", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The campaign that first engaged the company in Hubspot."
                        },                         {
                          "name": "Salesforce Account Last MQL Date", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The date when the account was last marked as a Marketing Qualified Lead."
                        }]
          }
        ), 
        filePath = "/csv_files/accounts_final.csv"
    )
    SharepointSource_0 = Task(
        task_id = "SharepointSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_share_point_pipelien_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_share_point_pipelien_source", 
          "alias": ""
        }
    )
    SharepointSource_0_1.out0 >> SharepointSource_0_1.input_port_0_1
    SharepointSource_0.out0 >> SharepointSource_0.input_port_1_1
    SharepointSource_0_1.output_port_0_1 >> model_share_point_pipelien_Limit_1.in_1
    SharepointSource_0.output_port_1_1 >> model_share_point_pipelien_Limit_1.in_1
