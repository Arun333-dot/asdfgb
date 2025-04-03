Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_pipeline4_Filter_1 = Task(
        task_id = "model_pipeline4_Filter_1", 
        component = "Model", 
        modelName = "model_pipeline4_Filter_1"
    )
    model_pipeline4_Intersect_1 = Task(
        task_id = "model_pipeline4_Intersect_1", 
        component = "Model", 
        modelName = "model_pipeline4_Intersect_1"
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "SharepointSource", 
        connector = Connection(kind = "sharepoint"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_pipeline4_WindowFunction_1 = Task(
        task_id = "model_pipeline4_WindowFunction_1", 
        component = "Model", 
        modelName = "model_pipeline4_WindowFunction_1"
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(), 
        filePath = "/prophecy-sftp/aruns/valid_data_records.xml"
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
    Email_1 = Task(task_id = "Email_1", component = "Email", to = None, subject = "", body = "", includeData = False)
    MSSQLSource_1 = SourceTask(
        task_id = "MSSQLSource_1", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "orchestrator", "name" : "tushartg", "schema" : "dbo"}
    )
