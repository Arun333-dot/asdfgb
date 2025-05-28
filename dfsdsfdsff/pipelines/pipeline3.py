Config = {
    "string": "'Name'", 
    "number": 34234, 
    "boolean": true, 
    "double": 234234234234, 
    "Long": 123123123123123, 
    "Float": 123123.556, 
    "array": array("'\"[\\\\\\\'Name\\\\\\\']\"'"), 
    "date": Date(None), 
    "checkbox_boolean1": True, 
    "checkobx_boolean2": False, 
    "radiobutton_boolean1": True, 
    "radiobutton_boolean2": False, 
    "date": Date("'2024-08-28'")
}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    million_records = Task(
        task_id = "million_records", 
        component = "Dataset", 
        table = {"name" : "million_records", "sourceType" : "Table", "sourceName" : "hive_metastore.arun123", "alias" : ""}
    )
    model_pipeline3_Reformat_1 = Task(
        task_id = "model_pipeline3_Reformat_1", 
        component = "Model", 
        modelName = "model_pipeline3_Reformat_1"
    )
    million_records.out >> model_pipeline3_Reformat_1.in_1
