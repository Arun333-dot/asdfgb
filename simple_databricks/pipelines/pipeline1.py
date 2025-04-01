Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_pipeline1_FlattenSchema_1 = Task(
        task_id = "model_pipeline1_FlattenSchema_1", 
        component = "Model", 
        modelName = "model_pipeline1_FlattenSchema_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_pipeline1_Deduplicate_1 = Task(
        task_id = "model_pipeline1_Deduplicate_1", 
        component = "Model", 
        modelName = "model_pipeline1_Deduplicate_1"
    )
    model_pipeline1_Aggregate_1 = Task(
        task_id = "model_pipeline1_Aggregate_1", 
        component = "Model", 
        modelName = "model_pipeline1_Aggregate_1"
    )
    OrchestrationSource_3 = SourceTask(
        task_id = "OrchestrationSource_3", 
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
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
