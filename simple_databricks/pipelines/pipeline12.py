Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    DatabricksSource_0 = SourceTask(
        task_id = "DatabricksSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(), 
        tableFullName = {"database" : "tanmay", "name" : "m1", "schema" : "default"}
    )
    send_email_with_attachment = Task(
        task_id = "send_email_with_attachment", 
        component = "Email", 
        body = "", 
        subject = "", 
        includeData = True, 
        fileName = "abcd.docx", 
        to = ["soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = False
    )
    DatabricksSource_0.out0 >> send_email_with_attachment.in0
