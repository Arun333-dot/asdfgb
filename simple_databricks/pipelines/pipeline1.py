Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    OrchestrationSource_1 = Task(
        task_id = "OrchestrationSource_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline1_pre_Deduplicate_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline1_source", 
          "alias": ""
        }
    )
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
        format = CSVFormat(header = True, separator = ",")
    )
    OrchestrationSource_5 = SourceTask(
        task_id = "OrchestrationSource_5", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_7 = SourceTask(
        task_id = "OrchestrationSource_7", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(header = True, separator = ",")
    )
    OrchestrationSource_6 = SourceTask(
        task_id = "OrchestrationSource_6", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_pipeline1_Aggregate_2 = Task(
        task_id = "model_pipeline1_Aggregate_2", 
        component = "Model", 
        modelName = "model_pipeline1_Aggregate_2"
    )
    OrchestrationTarget_2 = Task(
        task_id = "OrchestrationTarget_2", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    OrchestrationSource_4 = SourceTask(
        task_id = "OrchestrationSource_4", 
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
        format = CSVFormat(header = True, separator = ",")
    )
    OrchestrationSource_0 = Task(
        task_id = "OrchestrationSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline1_pre_Aggregate_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline1_source", 
          "alias": ""
        }
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
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {}
    )
    OrchestrationSource_0.out >> OrchestrationSource_0.input_port_0_1
    OrchestrationSource_1.out >> OrchestrationSource_1.input_port_2_1
    OrchestrationSource_0.output_port_0_1 >> model_pipeline1_Aggregate_1.in_1
    OrchestrationSource_1.output_port_2_1 >> model_pipeline1_Deduplicate_1.in_1
