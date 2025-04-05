with DAG():
    library_items_catalogue_xml = SourceTask(
        task_id = "library_items_catalogue_xml", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = XMLFormat(
          schema = {
            "providerType": "arrow", 
            "fields": [{
                          "name": "@id", 
                          "dataType": {"type" : "String"}, 
                          "description": "Unique identifier for the record"
                        },                         {
                          "name": "description", 
                          "dataType": {"type" : "String"}, 
                          "description": "A brief overview of the content or subject matter."
                        },                         {
                          "name": "author", 
                          "dataType": {"type" : "String"}, 
                          "description": "Name of the author of the item"
                        },                         {
                          "name": "title", 
                          "dataType": {"type" : "String"}, 
                          "description": "The title of the item or publication"
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
                          "description": "Type of data represented in the record"
                        },                         {
                          "name": "data_value", 
                          "dataType": {
                            "type": "Struct", 
                            "fields": [{
                                          "name": "id", 
                                          "dataType": {"type" : "Bigint"}, 
                                          "description": "Unique identifier for the data item"
                                        },                                         {
                                          "name": "category", 
                                          "dataType": {"type" : "String"}, 
                                          "description": "Category of the item represented in the data structure"
                                        },                                         {
                                          "name": "item", 
                                          "dataType": {"type" : "Array", "dataType" : {"type" : "String"}}, 
                                          "description": "List of items associated with the data entry"
                                        }]
                          }, 
                          "description": "Structured data containing detailed information about the item, including its ID, category, and associated attributes."
                        }]
          }
        ), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{
                            "type": "literal", 
                            "properties": {"value" : "/prophecy-sftp/aruns/book_catalog_with_data_types.xml"}
                          }]
          }
        }
    )
    book_inventory_csv = Task(
        task_id = "book_inventory_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/resuklts_outpuottt.csv"}}]
            }
          }
        }
    )
    library_items_catalogue_xml.out >> book_inventory_csv.in0
