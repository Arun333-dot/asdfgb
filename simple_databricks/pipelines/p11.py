Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          description = "Demographic information of individuals, aiding in understanding customer profiles and geographic distribution.", 
          separator = ",", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "int64"}, 
                          "description": "Unique identifier for each individual in the dataset", 
                          "name": "id"
                        },                         {"dataType" : {"type" : "utf8"}, "description" : "The full name of the individual", "name" : "name"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Email address of the individual", 
                          "name": "email"
                        },                         {"dataType" : {"type" : "int64"}, "description" : "The age of the individual", "name" : "age"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city where the individual resides", 
                          "name": "city"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The country where the individual resides", 
                          "name": "country"
                        }], 
            "providerType": "Arrow"
          }, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          header = True
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    notify_pipeline_success_1_1_1_1 = Task(
        task_id = "notify_pipeline_success_1_1_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/template_final.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    Email_1 = Task(
        task_id = "Email_1", 
        component = "Email", 
        body = "", 
        subject = "", 
        includeData = False, 
        fileName = "", 
        to = None, 
        fileFormat = "", 
        hasTemplate = False
    )
    notify_pipeline_success_1_1_1 = Task(
        task_id = "notify_pipeline_success_1_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/template_final_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    notify_pipeline_success_1_1_1_2 = Task(
        task_id = "notify_pipeline_success_1_1_1_2", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/template_final_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    (
        SFTPSource_0.out0
        >> [notify_pipeline_success_1_1_1.in0, notify_pipeline_success_1_1_1_1.in0,
              notify_pipeline_success_1_1_1_2.in0]
    )
