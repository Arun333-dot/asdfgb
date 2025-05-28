with DAG():
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "DatabricksVolumeTarget", 
        connector = Connection(kind = "databricks"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p1_Aggregate_1 = Task(
        task_id = "model_p1_Aggregate_1", 
        component = "Model", 
        modelName = "model_p1_Aggregate_1"
    )
    model_p1_Filter_1 = Task(task_id = "model_p1_Filter_1", component = "Model", modelName = "model_p1_Filter_1")
