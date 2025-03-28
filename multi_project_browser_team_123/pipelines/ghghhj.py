with DAG():
    TableauWrite_1 = Task(task_id = "TableauWrite_1", component = "TableauWrite")
    model_ghghhj_Deduplicate_1 = Task(
        task_id = "model_ghghhj_Deduplicate_1", 
        component = "Model", 
        modelName = "model_ghghhj_Deduplicate_1"
    )
    model_ghghhj_SetOperation_1 = Task(
        task_id = "model_ghghhj_SetOperation_1", 
        component = "Model", 
        modelName = "model_ghghhj_SetOperation_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint"), 
        format = CSVFormat(separator = ",", header = True)
    )
    RestAPI_1 = Task(
        task_id = "RestAPI_1", 
        component = "RestAPI", 
        method = "", 
        body = "", 
        url = "", 
        params = "", 
        headers = ""
    )
    model_ghghhj_Aggregate_1 = Task(
        task_id = "model_ghghhj_Aggregate_1", 
        component = "Model", 
        modelName = "model_ghghhj_Aggregate_1"
    )
