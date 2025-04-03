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
            "providerType": "Arrow", 
            "fields": [{
                          "name": "id", 
                          "dataType": {"type" : "int64"}, 
                          "description": "Unique identifier for each individual in the dataset"
                        },                         {"name" : "name", "dataType" : {"type" : "utf8"}, "description" : "The full name of the individual"},                         {
                          "name": "email", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Email address of the individual"
                        },                         {"name" : "age", "dataType" : {"type" : "int64"}, "description" : "The age of the individual"},                         {
                          "name": "city", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city where the individual resides"
                        },                         {
                          "name": "country", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The country where the individual resides"
                        }]
          }, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          header = True
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    notify_pipeline_success = Task(
        task_id = "notify_pipeline_success", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd.csv", 
        to = ["arunsharma@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    notify_pipeline_success_1_1 = Task(
        task_id = "notify_pipeline_success_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd.xlsx", 
        to = ["arunsharma@prophecy.io"], 
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
        to = ["arunsharma@prophecy.io"], 
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
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/template_final_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    notify_pipeline_success_1 = Task(
        task_id = "notify_pipeline_success_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd.csv", 
        to = ["arunsharma@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    (
        SFTPSource_0.out0
        >> [notify_pipeline_success.in0, notify_pipeline_success_1.in0, notify_pipeline_success_1_1.in0,
              notify_pipeline_success_1_1_1.in0, notify_pipeline_success_1_1_1_1.in0]
    )
