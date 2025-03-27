with DAG():
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_first_WindowFunction_1 = Task(
        task_id = "model_first_WindowFunction_1", 
        component = "Model", 
        modelName = "model_first_WindowFunction_1"
    )
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "DatabricksVolumeTarget", 
        connector = Connection(kind = "databricks"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_first_Filter_1 = Task(
        task_id = "model_first_Filter_1", 
        component = "Model", 
        modelName = "model_first_Filter_1"
    )
    model_first_Join_1 = Task(task_id = "model_first_Join_1", component = "Model", modelName = "model_first_Join_1")
