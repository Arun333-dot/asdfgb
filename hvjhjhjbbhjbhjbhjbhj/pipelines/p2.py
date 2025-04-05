Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_p2_BulkColumnExpressions_1 = Task(
        task_id = "model_p2_BulkColumnExpressions_1", 
        component = "Model", 
        modelName = "model_p2_BulkColumnExpressions_1"
    )
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {}}, 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_p2_Intersect_1 = Task(
        task_id = "model_p2_Intersect_1", 
        component = "Model", 
        modelName = "model_p2_Intersect_1"
    )
    model_p2_Filter_1 = Task(task_id = "model_p2_Filter_1", component = "Model", modelName = "model_p2_Filter_1")
