with DAG():
    book_inventory_csv_1 = Task(
        task_id = "book_inventory_csv_1", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {
          "category": "file", 
          "kind": "xlsx", 
          "properties": {"header" : True, "ignoreCellFormatting" : True, "sheetName" : "Sheet1"}
        }, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/resutlst_outoput.xlsx"}}]
            }
          }
        }
    )
    SFTPSource_2 = Task(
        task_id = "SFTPSource_2", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p2_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p2_source", 
          "alias": ""
        }
    )
    book_inventory_csv_2 = Task(
        task_id = "book_inventory_csv_2", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {"id" : "sftp"}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/resutlst_outoput.csv"}}]
            }
          }
        }, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    model_p2_Reformat_1 = Task(task_id = "model_p2_Reformat_1", component = "Model", modelName = "model_p2_Reformat_1")
    SFTPSource_2 = SourceTask(
        task_id = "SFTPSource_2", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "providerType": "arrow", 
            "fields": [{
                          "name": "@id", 
                          "dataType": {"type" : "String"}, 
                          "description": "Unique identifier for the record"
                        },                         {
                          "name": "author", 
                          "dataType": {"type" : "String"}, 
                          "description": "Name of the author of the book"
                        },                         {
                          "name": "title", 
                          "dataType": {"type" : "String"}, 
                          "description": "The title of the book or publication"
                        },                         {
                          "name": "genre", 
                          "dataType": {"type" : "String"}, 
                          "description": "Category of the book or publication"
                        },                         {
                          "name": "price", 
                          "dataType": {"type" : "Double"}, 
                          "description": "The selling price of the item"
                        },                         {
                          "name": "publish_date", 
                          "dataType": {"type" : "Date"}, 
                          "description": "The date when the item was published"
                        },                         {
                          "name": "data_type", 
                          "dataType": {"type" : "String"}, 
                          "description": "The type of data represented in the record"
                        },                         {
                          "name": "data_value", 
                          "dataType": {
                            "type": "Struct", 
                            "fields": [{
                                          "name": "id", 
                                          "dataType": {"type" : "Bigint"}, 
                                          "description": "Unique identifier for the data entry"
                                        },                                         {
                                          "name": "category", 
                                          "dataType": {"type" : "String"}, 
                                          "description": "Category of the data item"
                                        },                                         {
                                          "name": "item", 
                                          "dataType": {"type" : "Array", "dataType" : {"type" : "String"}}, 
                                          "description": "List of items associated with the data value"
                                        }]
                          }, 
                          "description": "Structured data containing detailed information about the item"
                        },                         {
                          "name": "description", 
                          "dataType": {"type" : "String"}, 
                          "description": "A brief overview of the item or content"
                        }]
          }
        ), 
        filePath = "/prophecy-sftp/aruns/book_catalog_with_data_types.xml"
    )
    book_inventory_csv = Task(
        task_id = "book_inventory_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "xml", "properties" : {"rootName" : "root", "rowTag" : "row"}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/resutlst_outoput.xml"}}]
            }
          }
        }
    )
    book_inventory_csv_3 = Task(
        task_id = "book_inventory_csv_3", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "json", "properties" : {}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/resutlst_outoput.json"}}]
            }
          }
        }
    )
    (
        SFTPSource_2.out0
        >> [book_inventory_csv_1.in0, book_inventory_csv_2.in0, book_inventory_csv_3.in0, SFTPSource_2.input_port_0_1]
    )
    SFTPSource_2.output_port_0_1 >> model_p2_Reformat_1.in_1
    model_p2_Reformat_1.out_1 >> book_inventory_csv.in0
