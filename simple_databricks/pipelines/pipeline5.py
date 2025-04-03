Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    seeeeeeed = Task(
        task_id = "seeeeeeed", 
        component = "Dataset", 
        table = {"name" : "seeeeeeed", "sourceType" : "Seed", "alias" : ""}
    )
    MSSQLSource_1 = SourceTask(
        task_id = "MSSQLSource_1", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "qa_database", "name" : "test_table", "schema" : "qa_schema"}
    )
    SFTPSource_5 = SourceTask(
        task_id = "SFTPSource_5", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = XMLFormat(), 
        filePath = "/prophecy-sftp/rohit/genericTarget.xml"
    )
    SFTPSource_3 = SourceTask(
        task_id = "SFTPSource_3", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = "/prophecy-sftp/aruns/test_results.csv"
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(
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
                          "description": "An array containing multiple arrays of integers", 
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
                          "description": "Structured data containing a name and an array of integer values", 
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
                          "description": "Structured data containing arrays of key-value pairs", 
                          "name": "struct_of_array_of_structs"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    all_type_databricks = Task(
        task_id = "all_type_databricks", 
        component = "Dataset", 
        table = {"name" : "all_type_databricks", "sourceType" : "Source", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    SFTPSource_1 = SourceTask(
        task_id = "SFTPSource_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = "/prophecy-sftp/aruns/valid_data_100.csv"
    )
    fetch_name_country = Task(
        task_id = "fetch_name_country", 
        component = "RestAPI", 
        method = "GET", 
        body = "", 
        url = "https://api.nationalize.io", 
        params = "name=john&country_id=US", 
        headers = ""
    )
    SFTPSource_2 = SourceTask(
        task_id = "SFTPSource_2", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    SFTPSource_4 = SourceTask(
        task_id = "SFTPSource_4", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = "/prophecy-sftp/rohit/customers.csv"
    )
    Reformat_1 = Task(task_id = "Reformat_1", component = "Reformat", columnsSelector = [], expressions = [])
    seeeeeeed.out >> [Reformat_1.in0, fetch_name_country.in0]
