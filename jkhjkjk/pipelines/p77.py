with DAG():
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p77_Aggregate_1 = Task(
        task_id = "model_p77_Aggregate_1", 
        component = "Model", 
        modelName = "model_p77_Aggregate_1"
    )
