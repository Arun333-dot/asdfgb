with DAG():
    model_pipeline123123213_Join_1 = Task(
        task_id = "model_pipeline123123213_Join_1", 
        component = "Model", 
        modelName = "model_pipeline123123213_Join_1"
    )
    model_pipeline123123213_Filter_1 = Task(
        task_id = "model_pipeline123123213_Filter_1", 
        component = "Model", 
        modelName = "model_pipeline123123213_Filter_1"
    )
    model_pipeline123123213_FlattenSchema_1 = Task(
        task_id = "model_pipeline123123213_FlattenSchema_1", 
        component = "Model", 
        modelName = "model_pipeline123123213_FlattenSchema_1"
    )
    model_pipeline123123213_WindowFunction_1 = Task(
        task_id = "model_pipeline123123213_WindowFunction_1", 
        component = "Model", 
        modelName = "model_pipeline123123213_WindowFunction_1"
    )
    model_pipeline123123213_Aggregate_1 = Task(
        task_id = "model_pipeline123123213_Aggregate_1", 
        component = "Model", 
        modelName = "model_pipeline123123213_Aggregate_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
