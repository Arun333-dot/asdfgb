Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    send_email_with_attachment = Task(
        task_id = "send_email_with_attachment", 
        component = "Email", 
        body = "", 
        subject = "This is 4th gem", 
        includeData = True, 
        fileName = "hello", 
        to = ["soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/template_final_1.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    send_email_notification_2 = Task(
        task_id = "send_email_notification_2", 
        component = "Email", 
        body = "", 
        subject = "This is without include data CSV", 
        includeData = False, 
        fileName = "hi", 
        to = ["soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = False
    )
    send_email_notification_3 = Task(
        task_id = "send_email_notification_3", 
        component = "Email", 
        body = "", 
        subject = "", 
        includeData = False, 
        fileName = "hey", 
        to = ["soni.vaibhav@prophecy.io"], 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    send_email_notification = Task(
        task_id = "send_email_notification", 
        component = "Email", 
        body = "", 
        subject = "This is first gem", 
        includeData = True, 
        fileName = "avbcd", 
        to = ["soni.vaibhav@prophecy.io"], 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    DatabricksSource_0 = SourceTask(
        task_id = "DatabricksSource_0", 
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
    notify_email_recipients = Task(
        task_id = "notify_email_recipients", 
        component = "Email", 
        body = "", 
        subject = "This is second gem", 
        includeData = True, 
        fileName = "xyz.csv", 
        to = ["soni.vaibhav@prophecy.io"], 
        fileFormat = "csv", 
        hasTemplate = False
    )
    send_email_notification_1 = Task(
        task_id = "send_email_notification_1", 
        component = "Email", 
        body = "", 
        subject = "This is third gem", 
        includeData = True, 
        fileName = "myFile", 
        to = ["soni.vaibhav@prophecy.io"], 
        attachmentPath = "attachments/template_final.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = False
    )
    (
        DatabricksSource_0.out0
        >> [send_email_notification.in0, notify_email_recipients.in0, send_email_notification_1.in0,
              send_email_with_attachment.in0, send_email_notification_2.in0, send_email_notification_3.in0]
    )
