Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          schema = {
            "fields": [{
                          "dataType": {"type" : "int64"}, 
                          "description": "Unique identifier for each individual in the dataset", 
                          "name": "id"
                        },                         {"dataType" : {"type" : "utf8"}, "description" : "The full name of the individual", "name" : "name"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Email address of the individual", 
                          "name": "email"
                        },                         {"dataType" : {"type" : "int64"}, "description" : "The age of the individual", "name" : "age"},                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city where the individual resides", 
                          "name": "city"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The country where the individual resides", 
                          "name": "country"
                        }], 
            "providerType": "Arrow"
          }, 
          separator = ","
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    SFTPSource_0 = Task(
        task_id = "SFTPSource_0", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_sftp_pipeline_pre_Reformat_1_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_sftp_pipeline_source", 
          "alias": ""
        }
    )
    model_sftp_pipeline_Filter_1 = Task(
        task_id = "model_sftp_pipeline_Filter_1", 
        component = "Model", 
        modelName = "model_sftp_pipeline_Filter_1"
    )
    SFTPSource_0_1 = Task(
        task_id = "SFTPSource_0_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_sftp_pipeline_pre_Reformat_2_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_sftp_pipeline_source", 
          "alias": ""
        }
    )
    SFTPSource_0_1 = SourceTask(
        task_id = "SFTPSource_0_1", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(
          header = True, 
          separator = ",", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "id", 
                          "dataType": {"type" : "int64"}, 
                          "description": "Unique identifier for each individual in the dataset"
                        },                         {"name" : "name", "dataType" : {"type" : "utf8"}, "description" : "The full name of the individual"},                         {
                          "name": "email", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Email address of the individual"
                        },                         {"name" : "age", "dataType" : {"type" : "int64"}, "description" : "The age of the individual"},                         {
                          "name": "city", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city where the individual resides"
                        },                         {
                          "name": "country", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The country where the individual resides"
                        }]
          }
        ), 
        filePath = "/prophecy-sftp/aruns/test_20records.csv"
    )
    SFTPSource_0_1.out0 >> SFTPSource_0_1.input_port_0_1
    SFTPSource_0.out0 >> SFTPSource_0.input_port_1_1
    SFTPSource_0_1.output_port_0_1 >> model_sftp_pipeline_Filter_1.in_1
    SFTPSource_0.output_port_1_1 >> model_sftp_pipeline_Filter_1.in_1
