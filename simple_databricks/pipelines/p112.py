Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    send_email_with_attachment = Task(
        task_id = "send_email_with_attachment", 
        component = "Email", 
        body = "mail", 
        subject = "this is a email", 
        includeData = True, 
        fileName = "email", 
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/abcd.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    DatabricksSource_0 = SourceTask(
        task_id = "DatabricksSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(
          schema = {
            "fields": [{"name" : "id", "dataType" : {"type" : "int32"}},                         {"name" : "tiny_value", "dataType" : {"type" : "int8"}},                         {"name" : "small_value", "dataType" : {"type" : "int16"}},                         {"name" : "big_value", "dataType" : {"type" : "int64"}},                         {"name" : "name", "dataType" : {"type" : "utf8"}},                         {"name" : "is_active", "dataType" : {"type" : "bool"}},                         {"name" : "salary", "dataType" : {"type" : "utf8"}},                         {"name" : "float_value", "dataType" : {"type" : "float32"}},                         {"name" : "double_value", "dataType" : {"type" : "float64"}},                         {"name" : "binary_data", "dataType" : {"type" : "binary"}},                         {"name" : "created_at", "dataType" : {"type" : "timestamp"}},                         {"name" : "created_at_ntz", "dataType" : {"type" : "timestamp"}},                         {"name" : "birth_date", "dataType" : {"type" : "date32"}},                         {"name" : "interval_value", "dataType" : {"type" : "utf8"}},                         {"name" : "interval_seconds", "dataType" : {"type" : "utf8"}},                         {
                          "name": "metadata", 
                          "dataType": {"type" : "Map", "keyType" : {"type" : "utf8"}, "valueType" : {"type" : "utf8"}}
                        },                         {"name" : "int_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "int32"}}},                         {"name" : "float_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "float32"}}},                         {"name" : "boolean_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "bool"}}},                         {"name" : "decimal_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "decimal"}}},                         {"name" : "timestamp_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "timestamp"}}},                         {"name" : "date_array", "dataType" : {"type" : "Array", "dataType" : {"type" : "date32"}}},                         {
                          "name": "struct_array", 
                          "dataType": {
                            "type": "Array", 
                            "dataType": {
                              "type": "Struct", 
                              "fields": [{"name" : "type", "dataType" : {"type" : "utf8"}},                                           {"name" : "value", "dataType" : {"type" : "int32"}}]
                            }
                          }
                        },                         {
                          "name": "array_of_arrays", 
                          "dataType": {"type" : "Array", "dataType" : {"type" : "Array", "dataType" : {"type" : "int32"}}}
                        },                         {
                          "name": "struct_of_array", 
                          "dataType": {
                            "type": "Struct", 
                            "fields": [{"name" : "name", "dataType" : {"type" : "utf8"}},                                         {"name" : "values", "dataType" : {"type" : "Array", "dataType" : {"type" : "int32"}}}]
                          }
                        },                         {
                          "name": "struct_of_array_of_structs", 
                          "dataType": {
                            "type": "Struct", 
                            "fields": [{"name" : "id", "dataType" : {"type" : "int32"}},                                         {
                                          "name": "details", 
                                          "dataType": {
                                            "type": "Array", 
                                            "dataType": {
                                              "type": "Struct", 
                                              "fields": [{"name" : "key", "dataType" : {"type" : "utf8"}},                                                           {"name" : "val", "dataType" : {"type" : "int32"}}]
                                            }
                                          }
                                        }]
                          }
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    send_email_with_attachment_1 = Task(
        task_id = "send_email_with_attachment_1", 
        component = "Email", 
        body = "mail", 
        subject = "this is a email", 
        includeData = True, 
        fileName = "email", 
        to = ["arunsharma@prophecy.io"], 
        attachmentPath = "attachments/abcd.xlsx", 
        fileFormat = "xlsx", 
        hasTemplate = True
    )
    DatabricksSource_0.out0 >> [send_email_with_attachment.in0, send_email_with_attachment_1.in0]
