with DAG():
    DatabricksSource_0 = SourceTask(
        task_id = "DatabricksSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(), 
        tableFullName = {"database" : "qa_team", "name" : "call_center", "schema" : "qa_database"}
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(
          schema = {
            "fields": [{
                          "dataType": {"type" : "Integer"}, 
                          "description": "Unique identifier for each record", 
                          "name": "id"
                        },                         {
                          "dataType": {"type" : "TinyInt"}, 
                          "description": "A small integer value representing a specific metric", 
                          "name": "tiny_value"
                        },                         {
                          "dataType": {"type" : "SmallInt"}, 
                          "description": "A small integer value used for categorization or ranking", 
                          "name": "small_value"
                        },                         {
                          "dataType": {"type" : "Bigint"}, 
                          "description": "A large integer value representing significant data", 
                          "name": "big_value"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The name associated with the record", 
                          "name": "name"
                        },                         {
                          "dataType": {"type" : "Boolean"}, 
                          "description": "Indicates whether the record is currently active", 
                          "name": "is_active"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The salary amount of the individual", 
                          "name": "salary"
                        },                         {
                          "dataType": {"type" : "Float"}, 
                          "description": "A floating-point value representing a measurement", 
                          "name": "float_value"
                        },                         {
                          "dataType": {"type" : "Double"}, 
                          "description": "A double-precision value representing a measurement", 
                          "name": "double_value"
                        },                         {
                          "dataType": {"type" : "Binary"}, 
                          "description": "Raw binary data associated with the record", 
                          "name": "binary_data"
                        },                         {
                          "dataType": {"type" : "Timestamp"}, 
                          "description": "Timestamp indicating when the record was created", 
                          "name": "created_at"
                        },                         {
                          "dataType": {"type" : "Timestamp"}, 
                          "description": "Timestamp indicating when the record was created without timezone information", 
                          "name": "created_at_ntz"
                        },                         {
                          "dataType": {"type" : "Date"}, 
                          "description": "The date of birth of the individual", 
                          "name": "birth_date"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "A string representation of a time interval", 
                          "name": "interval_value"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The duration of the interval measured in seconds", 
                          "name": "interval_seconds"
                        },                         {
                          "dataType": {"keyType" : {"type" : "utf8"}, "type" : "String", "valueType" : {"type" : "utf8"}}, 
                          "description": "Additional information related to the record", 
                          "name": "metadata"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Integer"}, "type" : "Array"}, 
                          "description": "Array of integer values associated with the record", 
                          "name": "int_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Float"}, "type" : "Array"}, 
                          "description": "Array of float values associated with the record", 
                          "name": "float_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Boolean"}, "type" : "Array"}, 
                          "description": "Array of boolean values representing various flags", 
                          "name": "boolean_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Decimal"}, "type" : "Array"}, 
                          "description": "Array of decimal values for precise numerical data", 
                          "name": "decimal_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Timestamp"}, "type" : "Array"}, 
                          "description": "Array of timestamps indicating specific moments in time", 
                          "name": "timestamp_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "Date"}, "type" : "Array"}, 
                          "description": "Array of dates associated with the record", 
                          "name": "date_array"
                        },                         {
                          "dataType": {
                            "dataType": {
                              "fields": [{
                                            "dataType": {"type" : "String"}, 
                                            "description": "Type field within the structured data array", 
                                            "name": "type"
                                          },                                           {
                                            "dataType": {"type" : "Integer"}, 
                                            "description": "Value associated with each entry in the structured array", 
                                            "name": "value"
                                          }], 
                              "type": "Struct"
                            }, 
                            "type": "Array"
                          }, 
                          "description": "Array of structured data containing type and value", 
                          "name": "struct_array"
                        },                         {
                          "dataType": {"dataType" : {"dataType" : {"type" : "Integer"}, "type" : "Array"}, "type" : "Array"}, 
                          "description": "An array containing multiple arrays of integers", 
                          "name": "array_of_arrays"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "String"}, 
                                          "description": "Name associated with the structured array", 
                                          "name": "name"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "Integer"}, "type" : "Array"}, 
                                          "description": "Values contained within the structured array", 
                                          "name": "values"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structure containing a name and an array of integer values", 
                          "name": "struct_of_array"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "Integer"}, 
                                          "description": "Unique identifier for the structure containing an array of structs.", 
                                          "name": "id"
                                        },                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{
                                                            "dataType": {"type" : "String"}, 
                                                            "description": "Key value within each detail struct.", 
                                                            "name": "key"
                                                          },                                                           {
                                                            "dataType": {"type" : "Integer"}, 
                                                            "description": "Value associated with a specific key in a structured array of details.", 
                                                            "name": "val"
                                                          }], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "description": "Array of details associated with the structure.", 
                                          "name": "details"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structured data containing an array of key-value pairs", 
                          "name": "struct_of_array_of_structs"
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
