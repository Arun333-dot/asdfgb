Config = {"ID" : "'\"ID\"'", "Name" : "'\"Name\"'", "Age" : "'\"Age\"'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    million_records = Task(
        task_id = "million_records", 
        component = "Dataset", 
        table = {"name" : "million_records", "sourceType" : "Table", "sourceName" : "hive_metastore.arun123", "alias" : ""}
    )
    model_pipeline5_Reformat_1 = Task(
        task_id = "model_pipeline5_Reformat_1", 
        component = "Model", 
        modelName = "model_pipeline5_Reformat_1"
    )
    million_records.out >> model_pipeline5_Reformat_1.in_1
