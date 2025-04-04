Config = {"config1" : "'config1'", "config2" : "'config2'", "config3" : "'config3'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Comprehensive dataset capturing various data types and structures, useful for detailed analysis and insights across multiple dimensions.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "int32"}, 
                          "description": "Unique identifier for each record", 
                          "name": "id"
                        },                         {
                          "dataType": {"type" : "int8"}, 
                          "description": "A small integer value representing a specific metric", 
                          "name": "tiny_value"
                        },                         {
                          "dataType": {"type" : "int16"}, 
                          "description": "A small integer value used for various calculations", 
                          "name": "small_value"
                        },                         {
                          "dataType": {"type" : "int64"}, 
                          "description": "A large numerical value representing significant data", 
                          "name": "big_value"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name associated with the record", 
                          "name": "name"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether the record is currently active", 
                          "name": "is_active"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The salary amount of the individual", 
                          "name": "salary"
                        },                         {
                          "dataType": {"type" : "float32"}, 
                          "description": "A floating-point number representing a specific measurement", 
                          "name": "float_value"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "A double-precision number used for more accurate calculations", 
                          "name": "double_value"
                        },                         {
                          "dataType": {"type" : "binary"}, 
                          "description": "Raw binary data associated with the record", 
                          "name": "binary_data"
                        },                         {
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created", 
                          "name": "created_at"
                        },                         {
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created without timezone information", 
                          "name": "created_at_ntz"
                        },                         {
                          "dataType": {"type" : "date64"}, 
                          "description": "The date of birth of the individual", 
                          "name": "birth_date"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "A string representation of a time interval", 
                          "name": "interval_value"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The duration of the interval expressed in seconds", 
                          "name": "interval_seconds"
                        },                         {
                          "dataType": {"keyType" : {"type" : "utf8"}, "type" : "utf8", "valueType" : {"type" : "utf8"}}, 
                          "description": "Additional information related to the record", 
                          "name": "metadata"
                        },                         {
                          "dataType": {"dataType" : {"type" : "int32"}, "type" : "Array"}, 
                          "description": "Array of integer values associated with the record", 
                          "name": "int_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "float32"}, "type" : "Array"}, 
                          "description": "Array of float values associated with the record", 
                          "name": "float_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "bool"}, "type" : "Array"}, 
                          "description": "Array of boolean values indicating various conditions", 
                          "name": "boolean_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "decimal"}, "type" : "Array"}, 
                          "description": "Array of decimal values for precise numerical data", 
                          "name": "decimal_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "timestamp"}, "type" : "Array"}, 
                          "description": "Array of timestamps representing specific moments in time", 
                          "name": "timestamp_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "date64"}, "type" : "Array"}, 
                          "description": "Array of dates associated with the record", 
                          "name": "date_array"
                        },                         {
                          "dataType": {
                            "dataType": {
                              "fields": [{
                                            "dataType": {"type" : "utf8"}, 
                                            "description": "Type field within each structure in the struct_array", 
                                            "name": "type"
                                          },                                           {
                                            "dataType": {"type" : "int32"}, 
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
                          "dataType": {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "type" : "Array"}, 
                          "description": "A collection of integer arrays", 
                          "name": "array_of_arrays"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "utf8"}, 
                                          "description": "Name associated with the structured array", 
                                          "name": "name"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "int32"}, "type" : "Array"}, 
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
                                          "dataType": {"type" : "int32"}, 
                                          "description": "Unique identifier for the struct containing an array of structs.", 
                                          "name": "id"
                                        },                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{
                                                            "dataType": {"type" : "utf8"}, 
                                                            "description": "Key value within each detail struct.", 
                                                            "name": "key"
                                                          },                                                           {
                                                            "dataType": {"type" : "int32"}, 
                                                            "description": "Value associated with each key in the structured array of details.", 
                                                            "name": "val"
                                                          }], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "description": "Array of details associated with the struct.", 
                                          "name": "details"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structured data containing an array of key-value pairs", 
                          "name": "struct_of_array_of_structs"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_p10_Limit_1 = Task(task_id = "model_p10_Limit_1", component = "Model", modelName = "model_p10_Limit_1")
    all_type_databricks = Task(
        task_id = "all_type_databricks", 
        component = "Dataset", 
        table = {"name" : "all_type_databricks", "sourceType" : "Table", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    employees = Task(
        task_id = "employees", 
        component = "Dataset", 
        table = {"name" : "employees", "sourceType" : "Table", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    DatabricksSource_0 = Task(
        task_id = "DatabricksSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p10_pre_full_data_extraction_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p10_source", 
          "alias": ""
        }
    )
    DatabricksSource_0 = SourceTask(
        task_id = "DatabricksSource_0", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Diverse dataset capturing various data types and structures, useful for comprehensive analysis and insights across multiple dimensions.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "int32"}, 
                          "description": "Unique identifier for each record", 
                          "name": "id"
                        },                         {
                          "dataType": {"type" : "int8"}, 
                          "description": "A small integer value for specific categorization", 
                          "name": "tiny_value"
                        },                         {
                          "dataType": {"type" : "int16"}, 
                          "description": "A small integer value used for additional metrics", 
                          "name": "small_value"
                        },                         {
                          "dataType": {"type" : "int64"}, 
                          "description": "A large numerical value representing significant data", 
                          "name": "big_value"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name associated with the record", 
                          "name": "name"
                        },                         {
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates whether the record is currently active", 
                          "name": "is_active"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The salary amount of the individual", 
                          "name": "salary"
                        },                         {
                          "dataType": {"type" : "float32"}, 
                          "description": "A floating-point value representing a measurement", 
                          "name": "float_value"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "A double-precision value representing a measurement", 
                          "name": "double_value"
                        },                         {
                          "dataType": {"type" : "binary"}, 
                          "description": "Raw binary data associated with the record", 
                          "name": "binary_data"
                        },                         {
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created", 
                          "name": "created_at"
                        },                         {
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created without timezone information", 
                          "name": "created_at_ntz"
                        },                         {
                          "dataType": {"type" : "date64"}, 
                          "description": "The date of birth of the individual", 
                          "name": "birth_date"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Descriptive value representing a time interval", 
                          "name": "interval_value"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Numeric representation of the time interval in seconds", 
                          "name": "interval_seconds"
                        },                         {
                          "dataType": {"keyType" : {"type" : "utf8"}, "type" : "utf8", "valueType" : {"type" : "utf8"}}, 
                          "description": "Additional information related to the record", 
                          "name": "metadata"
                        },                         {
                          "dataType": {"dataType" : {"type" : "int32"}, "type" : "Array"}, 
                          "description": "Array of integer values associated with the record", 
                          "name": "int_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "float32"}, "type" : "Array"}, 
                          "description": "Array of float values associated with the record", 
                          "name": "float_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "bool"}, "type" : "Array"}, 
                          "description": "Array of boolean values representing various flags", 
                          "name": "boolean_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "decimal"}, "type" : "Array"}, 
                          "description": "Array of decimal values for precise numerical data", 
                          "name": "decimal_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "timestamp"}, "type" : "Array"}, 
                          "description": "Array of timestamps indicating specific events or records", 
                          "name": "timestamp_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "date64"}, "type" : "Array"}, 
                          "description": "Array of dates associated with the record", 
                          "name": "date_array"
                        },                         {
                          "dataType": {
                            "dataType": {
                              "fields": [{
                                            "dataType": {"type" : "utf8"}, 
                                            "description": "Type field within the structured data array", 
                                            "name": "type"
                                          },                                           {
                                            "dataType": {"type" : "int32"}, 
                                            "description": "Value associated with each entry in the structured array.", 
                                            "name": "value"
                                          }], 
                              "type": "Struct"
                            }, 
                            "type": "Array"
                          }, 
                          "description": "Array of structured data containing type and value", 
                          "name": "struct_array"
                        },                         {
                          "dataType": {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "type" : "Array"}, 
                          "description": "Array containing multiple arrays of integers.", 
                          "name": "array_of_arrays"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "utf8"}, 
                                          "description": "Name associated with the structured array", 
                                          "name": "name"
                                        },                                         {
                                          "dataType": {"dataType" : {"type" : "int32"}, "type" : "Array"}, 
                                          "description": "Values contained within the structured array", 
                                          "name": "values"
                                        }], 
                            "type": "Struct"
                          }, 
                          "description": "Structure containing a name and an array of integer values.", 
                          "name": "struct_of_array"
                        },                         {
                          "dataType": {
                            "fields": [{
                                          "dataType": {"type" : "int32"}, 
                                          "description": "Unique identifier for the structure containing an array of structs.", 
                                          "name": "id"
                                        },                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{
                                                            "dataType": {"type" : "utf8"}, 
                                                            "description": "Key value within each detail struct.", 
                                                            "name": "key"
                                                          },                                                           {
                                                            "dataType": {"type" : "int32"}, 
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
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    DatabricksSource_0.out0 >> DatabricksSource_0.input_port_0_1
    DatabricksSource_0.output_port_0_1 >> model_p10_Limit_1.in_1
