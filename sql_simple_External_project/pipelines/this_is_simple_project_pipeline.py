with DAG():
    all_type_databricks = Task(
        task_id = "all_type_databricks", 
        component = "Dataset", 
        table = {"name" : "all_type_databricks", "sourceType" : "Source", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
