with DAG():
    all_type_databricks = Task(
        task_id = "all_type_databricks", 
        component = "Dataset", 
        table = {"name" : "all_type_databricks", "sourceType" : "Source", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_this_is_simple_project_pipeline_WindowFunction_1 = Task(
        task_id = "model_this_is_simple_project_pipeline_WindowFunction_1", 
        component = "Model", 
        modelName = "model_this_is_simple_project_pipeline_WindowFunction_1"
    )
