with DAG():
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {}}, 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_p2_Aggregate_1 = Task(
        task_id = "model_p2_Aggregate_1", 
        component = "Model", 
        modelName = "model_p2_Aggregate_1"
    )
