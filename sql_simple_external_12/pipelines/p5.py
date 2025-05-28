with DAG():
    SFTPSource_0 = Task(
        task_id = "SFTPSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p5_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p5_source", 
          "alias": ""
        }
    )
    user_information_databricks = Task(
        task_id = "user_information_databricks", 
        component = "OrchestrationTarget", 
        kind = "DatabricksTarget", 
        connector = Connection(kind = "databricks", id = ""), 
        format = {"category" : "table", "kind" : "databricks", "properties" : {"kind" : "databricks", "properties" : {}}}, 
        properties = {"tableFullName" : {}}
    )
    input_stream_csv = Task(
        task_id = "input_stream_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/test_20records.csv"}}]
            }
          }
        }
    )
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{
                          "dataType": {"type" : "Bigint"}, 
                          "description": "Unique identifier for each individual in the dataset", 
                          "name": "id"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The full name of the individual", 
                          "name": "name"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Email address of the individual", 
                          "name": "email"
                        },                         {"dataType" : {"type" : "Bigint"}, "description" : "The age of the individual", "name" : "age"},                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The city where the individual resides", 
                          "name": "city"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The country where the individual resides", 
                          "name": "country"
                        }], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    model_p5_Reformat_1 = Task(task_id = "model_p5_Reformat_1", component = "Model", modelName = "model_p5_Reformat_1")
    SFTPSource_0.out0 >> [user_information_databricks.in0, SFTPSource_0.input_port_0_1]
    SFTPSource_0.output_port_0_1 >> model_p5_Reformat_1.in_1
    model_p5_Reformat_1.out_1 >> input_stream_csv.in0
