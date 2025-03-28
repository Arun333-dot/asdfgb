with DAG():
    empty_output_csv = SourceTask(
        task_id = "empty_output_csv", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = {
          "type": "concat_operation", 
          "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "dfgdfgdfgdfg_on_prophecy345"}}]}
        }
    )
