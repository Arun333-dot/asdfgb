with DAG():
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{"dataType" : {"type" : "int64"}, "name" : "id"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "utf8"}, "name" : "email"},                         {"dataType" : {"type" : "utf8"}, "name" : "age"},                         {"dataType" : {"type" : "utf8"}, "name" : "city"},                         {"dataType" : {"type" : "utf8"}, "name" : "country"}], 
            "providerType": "arrow"
          }, 
          separator = ","
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records_nullvalue.csv"
    )
