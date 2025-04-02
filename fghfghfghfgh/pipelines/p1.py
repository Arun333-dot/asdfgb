with DAG():
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          nullValue = "USA", 
          schema = {
            "fields": [{"dataType" : {"type" : "int64"}, "name" : "id"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "utf8"}, "name" : "email"},                         {"dataType" : {"type" : "utf8"}, "name" : "age"},                         {"dataType" : {"type" : "utf8"}, "name" : "city"},                         {"dataType" : {"type" : "utf8"}, "name" : "country"}], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records_nullvalue.csv"
    )
    user_information_csv = Task(
        task_id = "user_information_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {"value" : "/prophecy-sftp/aruns/results_output_target.csv"}
                            }]
            }
          }
        }
    )
    SFTPSource_0.out0 >> user_information_csv.in0
