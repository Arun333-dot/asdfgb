Config = {
    "c1": "'\"erw\"'", 
    "c3": "'\"reerr\"'", 
    "vfg": None, 
    "rtrtrt": None, 
    "rtrt": None, 
    "rtrtrt": None, 
    "rtrtrt": None, 
    "rtrtrt": None, 
    "trtrrt": None, 
    "rtrtrt": None, 
    "trrtrt": None, 
    "rtrtrtrt": None, 
    "rtrttrtr": None
}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
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
    million_records = Task(
        task_id = "million_records", 
        component = "Dataset", 
        table = {"name" : "million_records", "sourceType" : "Table", "sourceName" : "hive_metastore.arun123", "alias" : ""}
    )
    model_pipeline2_Reformat_1 = Task(
        task_id = "model_pipeline2_Reformat_1", 
        component = "Model", 
        modelName = "model_pipeline2_Reformat_1"
    )
    million_records.out >> model_pipeline2_Reformat_1.in_1
    model_pipeline2_Reformat_1.out_1 >> user_metrics_csv.in0
