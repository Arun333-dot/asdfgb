Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    notify_pipeline_success = Task(
        task_id = "notify_pipeline_success", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "Without include data", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd.csv", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(), 
        tableFullName = {"database" : "tanmay", "name" : "m1", "schema" : "default"}
    )
    notify_pipeline_success_1_1 = Task(
        task_id = "notify_pipeline_success_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    notify_pipeline_success_1_1_1_1 = Task(
        task_id = "notify_pipeline_success_1_1_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/template_final.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    notify_pipeline_success_1_1_1 = Task(
        task_id = "notify_pipeline_success_1_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/template_final_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    notify_pipeline_success_1 = Task(
        task_id = "notify_pipeline_success_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "This is with csv", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.csv", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    (
        DatabricksSource_1.out0
        >> [notify_pipeline_success.in0, notify_pipeline_success_1.in0, notify_pipeline_success_1_1.in0,
              notify_pipeline_success_1_1_1.in0, notify_pipeline_success_1_1_1_1.in0]
    )
