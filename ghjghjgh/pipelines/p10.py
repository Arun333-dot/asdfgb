with DAG():
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    empty_output_csv = SourceTask(
        task_id = "empty_output_csv", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{"type" : "literal", "properties" : {"value" : "ghjghjhgjghjghjhjghjghjghjghjghjghjhg_on_prophecy"}}]
          }
        }
    )
