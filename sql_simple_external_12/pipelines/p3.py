with DAG():
    book_inventory_csv_2 = Task(
        task_id = "book_inventory_csv_2", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = {"kind" : "sftp", "type" : "connector", "properties" : {"id" : "sftp"}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {"value" : "/prophecy-sftp/aruns/resutlst_outdfsdfdfsdfsoput.csv"}
                            }]
            }
          }
        }, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    SFTPSource_2 = SourceTask(
        task_id = "SFTPSource_2", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(
          schema = {
            "fields": [{
                          "dataType": {"type" : "String"}, 
                          "description": "Unique identifier for the record", 
                          "name": "@id"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Name of the author of the book", 
                          "name": "author"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The title of the book or publication", 
                          "name": "title"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Category of the book or publication", 
                          "name": "genre"
                        },                         {
                          "dataType": {"type" : "Double"}, 
                          "description": "The selling price of the item", 
                          "name": "price"
                        },                         {
                          "dataType": {"type" : "Date"}, 
                          "description": "The date when the item was published", 
                          "name": "publish_date"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The type of data represented in the record", 
                          "name": "data_type"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "Bigint"}, 
                                          "description": "Unique identifier for the data entry", 
                                          "name": "id"
                                        },                                         {
                                          "dataType": {"type" : "String"}, 
                                          "description": "Category of the data item", 
                                          "name": "category"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "String"}, "type" : "Array"}, 
                                          "description": "List of items associated with the data value", 
                                          "name": "item"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structured data containing detailed information about the item", 
                          "name": "data_value"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "A brief overview of the item or content", 
                          "name": "description"
                        }], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/book_catalog_with_data_types.xml"
    )
    SFTPSource_2.out0 >> book_inventory_csv_2.in0
