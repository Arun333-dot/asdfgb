Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    S3Source_0_1 = SourceTask(
        task_id = "S3Source_0_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "_c0", 
                          "dataType": {"type" : "int64"}, 
                          "description": "First column representing a unique identifier or key."
                        },                         {
                          "name": "_c1", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record."
                        },                         {
                          "name": "_c2", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record in the dataset"
                        },                         {
                          "name": "_c3", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record."
                        },                         {
                          "name": "_c4", 
                          "dataType": {"type" : "float64"}, 
                          "description": "A numerical value representing a key metric or measurement."
                        },                         {
                          "name": "_c5", 
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates a true or false condition related to the data."
                        },                         {
                          "name": "_c6", 
                          "dataType": {"type" : "float64"}, 
                          "description": "A numerical value representing a specific metric or measurement."
                        },                         {
                          "name": "_c7", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "A string value representing a specific attribute or detail."
                        },                         {
                          "name": "_c8", 
                          "dataType": {"type" : "date64"}, 
                          "description": "Date associated with the record"
                        },                         {
                          "name": "_c9", 
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created or last updated"
                        }]
          }
        ), 
        filePath = "/orch_dataset/csv_data/csv_all_type_dataset_normal_colnames.csv"
    )
    model_s3_pipeline_sorted_filter_1 = Task(
        task_id = "model_s3_pipeline_sorted_filter_1", 
        component = "Model", 
        modelName = "model_s3_pipeline_sorted_filter_1"
    )
    S3Source_0 = Task(
        task_id = "S3Source_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_s3_pipeline_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_s3_pipeline_source", 
          "alias": ""
        }
    )
    S3Source_0_1 = Task(
        task_id = "S3Source_0_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_s3_pipeline_pre_Reformat_1_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_s3_pipeline_source", 
          "alias": ""
        }
    )
    S3Source_0 = SourceTask(
        task_id = "S3Source_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "_c0", 
                          "dataType": {"type" : "int64"}, 
                          "description": "First column representing a unique identifier or key."
                        },                         {
                          "name": "_c1", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record."
                        },                         {
                          "name": "_c2", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record in the dataset"
                        },                         {
                          "name": "_c3", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique identifier for a specific record."
                        },                         {
                          "name": "_c4", 
                          "dataType": {"type" : "float64"}, 
                          "description": "A numerical value representing a key metric or measurement."
                        },                         {
                          "name": "_c5", 
                          "dataType": {"type" : "bool"}, 
                          "description": "Indicates a true or false condition related to the data."
                        },                         {
                          "name": "_c6", 
                          "dataType": {"type" : "float64"}, 
                          "description": "A numerical value representing a specific metric or measurement."
                        },                         {
                          "name": "_c7", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "A string value representing a specific attribute or detail."
                        },                         {
                          "name": "_c8", 
                          "dataType": {"type" : "date64"}, 
                          "description": "Date associated with the record"
                        },                         {
                          "name": "_c9", 
                          "dataType": {"type" : "timestamp"}, 
                          "description": "Timestamp indicating when the record was created or last updated"
                        }]
          }
        ), 
        filePath = "/orch_dataset/csv_data/csv_all_type_dataset_normal_colnames.csv"
    )
    S3Source_0.out0 >> S3Source_0.input_port_0_1
    S3Source_0_1.out0 >> S3Source_0_1.input_port_1_1
    S3Source_0.output_port_0_1 >> model_s3_pipeline_sorted_filter_1.in_1
    S3Source_0_1.output_port_1_1 >> model_s3_pipeline_sorted_filter_1.in_1
