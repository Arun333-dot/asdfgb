with DAG():
    model_p77_WindowFunction_2 = Task(
        task_id = "model_p77_WindowFunction_2", 
        component = "Model", 
        modelName = "model_p77_WindowFunction_2"
    )
    model_p77_Deduplicate_2 = Task(
        task_id = "model_p77_Deduplicate_2", 
        component = "Model", 
        modelName = "model_p77_Deduplicate_2"
    )
    model_p77_Aggregate_1 = Task(
        task_id = "model_p77_Aggregate_1", 
        component = "Model", 
        modelName = "model_p77_Aggregate_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    Email_1 = Task(task_id = "Email_1", component = "Email", to = None, subject = "", body = "", includeData = False)
    model_p77_Join_1 = Task(task_id = "model_p77_Join_1", component = "Model", modelName = "model_p77_Join_1")
    model_p77_Deduplicate_3 = Task(
        task_id = "model_p77_Deduplicate_3", 
        component = "Model", 
        modelName = "model_p77_Deduplicate_3"
    )
    model_p77_Filter_1 = Task(task_id = "model_p77_Filter_1", component = "Model", modelName = "model_p77_Filter_1")
    model_p77_Aggregate_2 = Task(
        task_id = "model_p77_Aggregate_2", 
        component = "Model", 
        modelName = "model_p77_Aggregate_2"
    )
    model_p77_Deduplicate_1 = Task(
        task_id = "model_p77_Deduplicate_1", 
        component = "Model", 
        modelName = "model_p77_Deduplicate_1"
    )
    model_p77_Join_2 = Task(task_id = "model_p77_Join_2", component = "Model", modelName = "model_p77_Join_2")
    model_p77_Aggregate_3 = Task(
        task_id = "model_p77_Aggregate_3", 
        component = "Model", 
        modelName = "model_p77_Aggregate_3"
    )
    model_p77_Join_3 = Task(task_id = "model_p77_Join_3", component = "Model", modelName = "model_p77_Join_3")
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p77_Filter_2 = Task(task_id = "model_p77_Filter_2", component = "Model", modelName = "model_p77_Filter_2")
    model_p77_WindowFunction_1 = Task(
        task_id = "model_p77_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p77_WindowFunction_1"
    )
