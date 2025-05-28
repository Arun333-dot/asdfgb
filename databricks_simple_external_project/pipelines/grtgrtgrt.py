with DAG():
    fetch_invalid_url = Task(
        task_id = "fetch_invalid_url", 
        component = "RestAPI", 
        method = "GET", 
        body = "", 
        url = "this_is_invalid_url", 
        params = "", 
        headers = ""
    )
    model_grtgrtgrt_m1_1 = Task(
        task_id = "model_grtgrtgrt_m1_1", 
        component = "Model", 
        modelName = "model_grtgrtgrt_m1_1"
    )
