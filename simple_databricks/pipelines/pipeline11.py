Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_pipeline11_Aggregate_1 = Task(
        task_id = "model_pipeline11_Aggregate_1", 
        component = "Model", 
        modelName = "model_pipeline11_Aggregate_1"
    )
    model_pipeline11_Deduplicate_1 = Task(
        task_id = "model_pipeline11_Deduplicate_1", 
        component = "Model", 
        modelName = "model_pipeline11_Deduplicate_1"
    )
