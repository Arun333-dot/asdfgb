with DAG():
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "SharepointTarget", 
        connector = Connection(kind = "sharepoint"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {}
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
            "elements": [{
                            "type": "literal", 
                            "properties": {"value" : "/jsndjnasjdnajksdnajksdnajksdnaksjdnaskddoes_not_Exist_this_does_not_exist_2"}
                          }]
          }
        }
    )
    model_p13_WindowFunction_1 = Task(
        task_id = "model_p13_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p13_WindowFunction_1"
    )
    model_p13_WindowFunction_1.out_1 >> OrchestrationTarget_0.in0
