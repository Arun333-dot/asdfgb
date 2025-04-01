with DAG():
    model_p2_Aggregate_1 = Task(
        task_id = "model_p2_Aggregate_1", 
        component = "Model", 
        modelName = "model_p2_Aggregate_1"
    )
    model_p2_Deduplicate_1 = Task(
        task_id = "model_p2_Deduplicate_1", 
        component = "Model", 
        modelName = "model_p2_Deduplicate_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
