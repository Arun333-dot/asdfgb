Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_p1_Intersect_1 = Task(
        task_id = "model_p1_Intersect_1", 
        component = "Model", 
        modelName = "model_p1_Intersect_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {}}, 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p1_BulkColumnRename_1 = Task(
        task_id = "model_p1_BulkColumnRename_1", 
        component = "Model", 
        modelName = "model_p1_BulkColumnRename_1"
    )
    model_p1_Filter_1 = Task(task_id = "model_p1_Filter_1", component = "Model", modelName = "model_p1_Filter_1")
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    TableauWrite_1 = Task(task_id = "TableauWrite_1", component = "TableauWrite")
