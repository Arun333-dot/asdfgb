with DAG():
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p17_Aggregate_1 = Task(
        task_id = "model_p17_Aggregate_1", 
        component = "Model", 
        modelName = "model_p17_Aggregate_1"
    )
    model_p17_Filter_1 = Task(task_id = "model_p17_Filter_1", component = "Model", modelName = "model_p17_Filter_1")
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
