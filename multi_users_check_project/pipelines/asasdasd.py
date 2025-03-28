with DAG():
    model_asasdasd_Filter_1 = Task(
        task_id = "model_asasdasd_Filter_1", 
        component = "Model", 
        modelName = "model_asasdasd_Filter_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    Email_1 = Task(task_id = "Email_1", component = "Email", to = None, subject = "", body = "", includeData = False)
    model_asasdasd_Aggregate_1 = Task(
        task_id = "model_asasdasd_Aggregate_1", 
        component = "Model", 
        modelName = "model_asasdasd_Aggregate_1"
    )
    model_asasdasd_Aggregate_2 = Task(
        task_id = "model_asasdasd_Aggregate_2", 
        component = "Model", 
        modelName = "model_asasdasd_Aggregate_2"
    )
    model_asasdasd_Join_1 = Task(
        task_id = "model_asasdasd_Join_1", 
        component = "Model", 
        modelName = "model_asasdasd_Join_1"
    )
    model_asasdasd_Filter_2 = Task(
        task_id = "model_asasdasd_Filter_2", 
        component = "Model", 
        modelName = "model_asasdasd_Filter_2"
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_asasdasd_WindowFunction_1 = Task(
        task_id = "model_asasdasd_WindowFunction_1", 
        component = "Model", 
        modelName = "model_asasdasd_WindowFunction_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "SharepointTarget", 
        connector = Connection(kind = "sharepoint"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
