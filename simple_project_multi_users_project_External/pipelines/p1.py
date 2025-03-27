with DAG():
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p1_WindowFunction_1 = Task(
        task_id = "model_p1_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p1_WindowFunction_1"
    )
