with DAG():
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "SharepointTarget", 
        connector = Connection(kind = "sharepoint"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_p13_WindowFunction_1 = Task(
        task_id = "model_p13_WindowFunction_1", 
        component = "Model", 
        modelName = "model_p13_WindowFunction_1"
    )
