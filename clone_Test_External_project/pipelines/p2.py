with DAG():
    model_p2_WindowFunction_1 = Task(
        task_id = "model_p2_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p2_WindowFunction_1"
    )
    model_p2_Filter_1 = Task(task_id = "model_p2_Filter_1", component = "Model", modelName = "model_p2_Filter_1")
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint"), 
        format = CSVFormat(separator = ",", header = True)
    )
