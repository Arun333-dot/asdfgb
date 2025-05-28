with DAG():
    OrchestrationTarget_0 = Task(
        task_id = "OrchestrationTarget_0", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
