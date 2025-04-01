with DAG():
    MSSQLSource_0 = SourceTask(
        task_id = "MSSQLSource_0", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(
          schema = {
            "fields": [{
                          "dataType": {"type" : "Integer"}, 
                          "description": "Unique identifier for each record", 
                          "name": "id"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The name associated with the record", 
                          "name": "name"
                        }], 
            "providerType": "arrow"
          }
        ), 
        tableFullName = {"database" : "qa_database", "name" : "test_table_rohit", "schema" : "qa_schema"}
    )
    MSSQLSource_1 = SourceTask(
        task_id = "MSSQLSource_1", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "qa_database", "name" : "test_table", "schema" : "qa_schema"}
    )
    MSSQLSource_2 = SourceTask(
        task_id = "MSSQLSource_2", 
        component = "OrchestrationSource", 
        kind = "MSSQLSource", 
        connector = Connection(kind = "mssql", id = "dasadsads"), 
        format = MSSQLFormat(), 
        tableFullName = {"database" : "qa_database", "name" : "pg", "schema" : "qa_schema"}
    )
