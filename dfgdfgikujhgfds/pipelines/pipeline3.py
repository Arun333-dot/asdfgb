Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_pipeline3_Aggregate_1 = Task(
        task_id = "model_pipeline3_Aggregate_1", 
        component = "Model", 
        modelName = "model_pipeline3_Aggregate_1"
    )
    model_pipeline3_Deduplicate_1 = Task(
        task_id = "model_pipeline3_Deduplicate_1", 
        component = "Model", 
        modelName = "model_pipeline3_Deduplicate_1"
    )
    model_pipeline3_Except_1 = Task(
        task_id = "model_pipeline3_Except_1", 
        component = "Model", 
        modelName = "model_pipeline3_Except_1"
    )
    empty_output_csv = SourceTask(
        task_id = "empty_output_csv", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True), 
        filePath = {
          "type": "concat_operation", 
          "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "randompath"}}]}
        }
    )
