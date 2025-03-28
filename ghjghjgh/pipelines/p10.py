with DAG():
    Email_1 = Task(task_id = "Email_1", component = "Email", to = None, subject = "", body = "", includeData = False)
    TableauWrite_1 = Task(task_id = "TableauWrite_1", component = "TableauWrite")
    model_p10_SetOperation_1 = Task(
        task_id = "model_p10_SetOperation_1", 
        component = "Model", 
        modelName = "model_p10_SetOperation_1"
    )
    model_p10_WindowFunction_1 = Task(
        task_id = "model_p10_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p10_WindowFunction_1"
    )
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_p10_WindowFunction_2 = Task(
        task_id = "model_p10_WindowFunction_2", 
        component = "Model", 
        modelName = "model_p10_WindowFunction_2"
    )
    model_p10_Macro_1 = Task(task_id = "model_p10_Macro_1", component = "Model", modelName = "model_p10_Macro_1")
    model_p10_Join_2 = Task(task_id = "model_p10_Join_2", component = "Model", modelName = "model_p10_Join_2")
    model_p10_Filter_3 = Task(task_id = "model_p10_Filter_3", component = "Model", modelName = "model_p10_Filter_3")
    model_p10_Macro_2 = Task(task_id = "model_p10_Macro_2", component = "Model", modelName = "model_p10_Macro_2")
    model_p10_Filter_2 = Task(task_id = "model_p10_Filter_2", component = "Model", modelName = "model_p10_Filter_2")
    model_p10_Join_1 = Task(task_id = "model_p10_Join_1", component = "Model", modelName = "model_p10_Join_1")
    model_p10_Aggregate_2 = Task(
        task_id = "model_p10_Aggregate_2", 
        component = "Model", 
        modelName = "model_p10_Aggregate_2"
    )
    model_p10_Filter_1 = Task(task_id = "model_p10_Filter_1", component = "Model", modelName = "model_p10_Filter_1")
    model_p10_Aggregate_1 = Task(
        task_id = "model_p10_Aggregate_1", 
        component = "Model", 
        modelName = "model_p10_Aggregate_1"
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
                            "properties": {"value" : "ghjghjhgjghjghjhjghjghjghjghjghjghjhg_on_prophecy"}
                          }]
          }
        }
    )
