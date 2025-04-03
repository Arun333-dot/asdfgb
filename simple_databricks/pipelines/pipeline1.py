Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    OrchestrationSource_1 = Task(
        task_id = "OrchestrationSource_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline1_pre_Deduplicate_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline1_source", 
          "alias": ""
        }
    )
    model_pipeline1_FlattenSchema_1 = Task(
        task_id = "model_pipeline1_FlattenSchema_1", 
        component = "Model", 
        modelName = "model_pipeline1_FlattenSchema_1"
    )
    OrchestrationSource_1 = SourceTask(
        task_id = "OrchestrationSource_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(header = True, separator = ",")
    )
    DatabricksSource_3 = SourceTask(
        task_id = "DatabricksSource_3", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Comprehensive dataset capturing various data types and attributes, enabling detailed analysis of user profiles and behaviors.", 
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
                          "description": "A floating-point value representing a measurement", 
                          "name": "float_value"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "A double precision value for more accurate measurements", 
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
                          "description": "Numeric representation of the interval in seconds", 
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
                          "description": "Array of decimal values representing precise measurements", 
                          "name": "decimal_array"
                        },                         {
                          "dataType": {"dataType" : {"type" : "timestamp"}, "type" : "Array"}, 
                          "description": "Array of timestamps marking specific events or records", 
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
                          "description": "Array containing multiple arrays of integers", 
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
                                                            "description": "Value associated with a specific key in a structured array of details.", 
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
                          "description": "Structured data containing arrays of key-value pairs", 
                          "name": "struct_of_array_of_structs"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    OrchestrationSource_5 = SourceTask(
        task_id = "OrchestrationSource_5", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_7 = SourceTask(
        task_id = "OrchestrationSource_7", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    OrchestrationSource_2 = SourceTask(
        task_id = "OrchestrationSource_2", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(header = True, separator = ",")
    )
    OrchestrationSource_6 = SourceTask(
        task_id = "OrchestrationSource_6", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True)
    )
    model_pipeline1_Aggregate_2 = Task(
        task_id = "model_pipeline1_Aggregate_2", 
        component = "Model", 
        modelName = "model_pipeline1_Aggregate_2"
    )
    OrchestrationTarget_2 = Task(
        task_id = "OrchestrationTarget_2", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        properties = {}, 
        format = {"properties" : {"separator" : ",", "header" : True}, "kind" : "csv", "category" : "file"}
    )
    OrchestrationSource_4 = Task(
        task_id = "OrchestrationSource_4", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline1_pre_Deduplicate_2_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline1_source", 
          "alias": ""
        }
    )
    OrchestrationSource_4 = SourceTask(
        task_id = "OrchestrationSource_4", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(header = True, separator = ",")
    )
    DatabricksSource_2 = SourceTask(
        task_id = "DatabricksSource_2", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Customer demographic and account information, aiding in understanding customer profiles and preferences.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "float64"}, 
                          "description": "Unique identifier for each customer in the system", 
                          "name": "C_CUSTOMER_SK"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Unique identifier for each customer", 
                          "name": "C_CUSTOMER_ID"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "Current customer demographic key for tracking customer details.", 
                          "name": "C_CURRENT_CDEMO_SK"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The current household demographic key for the customer", 
                          "name": "C_CURRENT_HDEMO_SK"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The unique identifier for the customer's current address", 
                          "name": "C_CURRENT_ADDR_SK"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The key representing the date of the customer's first shipment.", 
                          "name": "C_FIRST_SHIPTO_DATE_SK"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The date when the customer made their first purchase.", 
                          "name": "C_FIRST_SALES_DATE_SK"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The salutation used for the customer", 
                          "name": "C_SALUTATION"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The first name of the customer", 
                          "name": "C_FIRST_NAME"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The last name of the customer", 
                          "name": "C_LAST_NAME"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Indicates whether the customer is a preferred customer.", 
                          "name": "C_PREFERRED_CUST_FLAG"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The day of the customer's birth", 
                          "name": "C_BIRTH_DAY"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The month in which the customer was born", 
                          "name": "C_BIRTH_MONTH"
                        },                         {
                          "dataType": {"type" : "float64"}, 
                          "description": "The year of birth of the customer", 
                          "name": "C_BIRTH_YEAR"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Country of birth of the customer", 
                          "name": "C_BIRTH_COUNTRY"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The login identifier for the customer", 
                          "name": "C_LOGIN"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Email address of the customer", 
                          "name": "C_EMAIL_ADDRESS"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The date when the customer last reviewed their account", 
                          "name": "C_LAST_REVIEW_DATE"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "customer", "schema" : "qa_database"}
    )
    model_pipeline1_Deduplicate_1 = Task(
        task_id = "model_pipeline1_Deduplicate_1", 
        component = "Model", 
        modelName = "model_pipeline1_Deduplicate_1"
    )
    model_pipeline1_Aggregate_1 = Task(
        task_id = "model_pipeline1_Aggregate_1", 
        component = "Model", 
        modelName = "model_pipeline1_Aggregate_1"
    )
    OrchestrationSource_3 = SourceTask(
        task_id = "OrchestrationSource_3", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(header = True, separator = ",")
    )
    OrchestrationSource_0 = Task(
        task_id = "OrchestrationSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline1_pre_Aggregate_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline1_source", 
          "alias": ""
        }
    )
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        format = CSVFormat(separator = ",", header = True)
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connection"), 
        format = DATABRICKSFormat(), 
        tableFullName = {"database" : "qa_team", "name" : "customer", "schema" : "qa_database"}
    )
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {}
    )
    OrchestrationSource_0.out >> OrchestrationSource_0.input_port_0_1
    OrchestrationSource_1.output_port_2_1 >> model_pipeline1_Deduplicate_1.in_1
    OrchestrationSource_4.output_port_5_1 >> model_pipeline1_Aggregate_2.in_1
    OrchestrationSource_0.output_port_0_1 >> model_pipeline1_Aggregate_1.in_1
    OrchestrationSource_1.out >> OrchestrationSource_1.input_port_2_1
    OrchestrationSource_4.out >> OrchestrationSource_4.input_port_5_1
