with DAG():
    MSSQLSource_0 = SourceTask(
        task_id = "MSSQLSource_0", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "qa_database", "name" : "test_table", "schema" : "qa_schema"}
    )
    MSSQLSource_1 = SourceTask(
        task_id = "MSSQLSource_1", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "qa_database", "name" : "pg", "schema" : "qa_schema"}
    )
