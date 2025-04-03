with DAG():
    model_p4_Deduplicate_1 = Task(
        task_id = "model_p4_Deduplicate_1", 
        component = "Model", 
        modelName = "model_p4_Deduplicate_1"
    )
    model_p4_WindowFunction_0 = Task(
        task_id = "model_p4_WindowFunction_0", 
        component = "Model", 
        modelName = "model_p4_WindowFunction_0"
    )
