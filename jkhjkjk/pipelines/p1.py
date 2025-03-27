with DAG():
    model_p1_Deduplicate_1 = Task(
        task_id = "model_p1_Deduplicate_1", 
        component = "Model", 
        modelName = "model_p1_Deduplicate_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {}}, 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p1_Aggregate_1 = Task(
        task_id = "model_p1_Aggregate_1", 
        component = "Model", 
        modelName = "model_p1_Aggregate_1"
    )
