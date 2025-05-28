Config = {
    "string": "'Name'", 
    "Array": array("'arun'", "'varun'", "'sumit'"), 
    "date": Date("'2025-04-11'"), 
    "boolean": True, 
    "Int": 123, 
    "Double": 1311515623612, 
    "Long": 9007199254740991, 
    "Float": 9.22, 
    "sql_Expression": expr(select * from date(expr))
}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    million_records = Task(
        task_id = "million_records", 
        component = "Dataset", 
        table = {"name" : "million_records", "sourceType" : "Table", "sourceName" : "hive_metastore.arun123", "alias" : ""}
    )
    model_pipeline23_selected_records = Task(
        task_id = "model_pipeline23_selected_records", 
        component = "Model", 
        modelName = "model_pipeline23_selected_records"
    )
    million_records.out >> model_pipeline23_selected_records.in_1
