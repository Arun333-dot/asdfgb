Config = {"string" : "'\"Name\"'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    all_type_databricks_1 = Task(
        task_id = "all_type_databricks_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_pipeline4_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_pipeline4_source", 
          "alias": ""
        }
    )
    user_metrics_csv = Task(
        task_id = "user_metrics_csv", 
        component = "OrchestrationTarget", 
        kind = "SFTPTarget", 
        connector = Connection(kind = "sftp", id = "sftp"), 
        format = {"category" : "file", "kind" : "csv", "properties" : {"header" : True, "separator" : ","}}, 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{"type" : "literal", "properties" : {"value" : "/prophecy-sftp/aruns/output/output.csv"}}]
            }
          }
        }
    )
    model_pipeline4_Reformat_1 = Task(
        task_id = "model_pipeline4_Reformat_1", 
        component = "Model", 
        modelName = "model_pipeline4_Reformat_1"
    )
    all_type_databricks_1 = SourceTask(
        task_id = "all_type_databricks_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "dartabrikcs2"), 
        format = DATABRICKSFormat(
          schema = {
            "fields": [{"dataType" : {"type" : "int32"}, "name" : "id"},                         {"dataType" : {"type" : "int8"}, "name" : "tiny_value"},                         {"dataType" : {"type" : "int16"}, "name" : "small_value"},                         {"dataType" : {"type" : "int64"}, "name" : "big_value"},                         {"dataType" : {"type" : "utf8"}, "name" : "name"},                         {"dataType" : {"type" : "bool"}, "name" : "is_active"},                         {"dataType" : {"type" : "utf8"}, "name" : "salary"},                         {"dataType" : {"type" : "float32"}, "name" : "float_value"},                         {"dataType" : {"type" : "float64"}, "name" : "double_value"},                         {"dataType" : {"type" : "binary"}, "name" : "binary_data"},                         {"dataType" : {"type" : "timestamp"}, "name" : "created_at"},                         {"dataType" : {"type" : "timestamp"}, "name" : "created_at_ntz"},                         {"dataType" : {"type" : "date32"}, "name" : "birth_date"},                         {"dataType" : {"type" : "utf8"}, "name" : "interval_value"},                         {"dataType" : {"type" : "utf8"}, "name" : "interval_seconds"},                         {
                          "dataType": {"keyType" : {"type" : "utf8"}, "type" : "Map", "valueType" : {"type" : "utf8"}}, 
                          "name": "metadata"
                        },                         {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "name" : "int_array"},                         {"dataType" : {"dataType" : {"type" : "float32"}, "type" : "Array"}, "name" : "float_array"},                         {"dataType" : {"dataType" : {"type" : "bool"}, "type" : "Array"}, "name" : "boolean_array"},                         {"dataType" : {"dataType" : {"type" : "decimal"}, "type" : "Array"}, "name" : "decimal_array"},                         {"dataType" : {"dataType" : {"type" : "timestamp"}, "type" : "Array"}, "name" : "timestamp_array"},                         {"dataType" : {"dataType" : {"type" : "date32"}, "type" : "Array"}, "name" : "date_array"},                         {
                          "dataType": {
                            "dataType": {
                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "type"},                                           {"dataType" : {"type" : "int32"}, "name" : "value"}], 
                              "type": "Struct"
                            }, 
                            "type": "Array"
                          }, 
                          "name": "struct_array"
                        },                         {
                          "dataType": {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "type" : "Array"}, 
                          "name": "array_of_arrays"
                        },                         {
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "utf8"}, "name" : "name"},                                         {"dataType" : {"dataType" : {"type" : "int32"}, "type" : "Array"}, "name" : "values"}], 
                            "type": "Struct"
                          }, 
                          "name": "struct_of_array"
                        },                         {
                          "dataType": {
                            "fields": [{"dataType" : {"type" : "int32"}, "name" : "id"},                                         {
                                          "dataType": {
                                            "dataType": {
                                              "fields": [{"dataType" : {"type" : "utf8"}, "name" : "key"},                                                           {"dataType" : {"type" : "int32"}, "name" : "val"}], 
                                              "type": "Struct"
                                            }, 
                                            "type": "Array"
                                          }, 
                                          "name": "details"
                                        }], 
                            "type": "Struct"
                          }, 
                          "name": "struct_of_array_of_structs"
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "all_type_databricks", "schema" : "qa_database"}
    )
    all_type_databricks_1.out0 >> all_type_databricks_1.input_port_0_1
    all_type_databricks_1.output_port_0_1 >> model_pipeline4_Reformat_1.in_1
    model_pipeline4_Reformat_1.out_1 >> user_metrics_csv.in0
