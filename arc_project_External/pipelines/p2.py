with DAG():
    model_p2_WindowFunction_1 = Task(
        task_id = "model_p2_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p2_WindowFunction_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p2_Aggregate_1 = Task(
        task_id = "model_p2_Aggregate_1", 
        component = "Model", 
        modelName = "model_p2_Aggregate_1"
    )
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "DatabricksVolumeTarget", 
        connector = Connection(kind = "databricks"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p2_Aggregate_2 = Task(
        task_id = "model_p2_Aggregate_2", 
        component = "Model", 
        modelName = "model_p2_Aggregate_2"
    )
    OrchestrationSource_3 = SourceTask(
        task_id = "OrchestrationSource_3", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p2_WindowFunction_2 = Task(
        task_id = "model_p2_WindowFunction_2", 
        component = "Model", 
        modelName = "model_p2_WindowFunction_2"
    )
