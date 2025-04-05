Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    notify_pipeline_success = Task(
        task_id = "notify_pipeline_success", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "Without include data", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Customer contact information, enabling effective communication and relationship management.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "utf8"}, 
                          "description": "The first name of the individual", 
                          "name": "first_name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The last name of the individual", 
                          "name": "last_name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The residential address of the individual", 
                          "name": "address"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "tanmay", "name" : "m1", "schema" : "default"}
    )
    notify_pipeline_success_1_1 = Task(
        task_id = "notify_pipeline_success_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = False, 
        fileName = "sdfsdfsdfsdfsdfsd", 
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
        fileName = "sdfsdfsdfsdfsdfsd", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/testing_template_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    notify_pipeline_success_1_1_1 = Task(
        task_id = "notify_pipeline_success_1_1_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "pipeline success", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/testing_template.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    notify_pipeline_success_1 = Task(
        task_id = "notify_pipeline_success_1", 
        component = "Email", 
        body = "this is aruns pipeline", 
        subject = "This is with csv", 
        includeData = True, 
        fileName = "sdfsdfsdfsdfsdfsd", 
        to = ["arunsharma@prophecy.io", "soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = True
    )
    (
        DatabricksSource_1.out0
        >> [notify_pipeline_success.in0, notify_pipeline_success_1.in0, notify_pipeline_success_1_1.in0,
              notify_pipeline_success_1_1_1.in0, notify_pipeline_success_1_1_1_1.in0]
    )
