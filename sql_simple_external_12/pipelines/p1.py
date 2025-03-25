Config = {"cvxcvxcvxvxcvx" : "'cdsccc'", "dfsdfsddfsddfs" : "sqrt('4')", "dsfdfsdfsdfsdfs" : "'age'"}

with DAG(Config = Config):
    SFTPSource_2 = SourceTask(
        task_id = "SFTPSource_2", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = JSONFormat(
          inferenceDataSamplingLimit = 0, 
          multiDoc = False, 
          schema = {
            "fields": [{
                          "dataType": {"type" : "String"}, 
                          "description": "Identifier for the custom object in the dataset", 
                          "name": "CUSTOM_OBJECT"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Indicates the presence of a null value in the dataset", 
                          "name": "NULL_VALUE"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Unique identifier for each record", 
                          "name": "ID"
                        },                         {"dataType" : {"type" : "Double"}, "description" : "The age of the individual", "name" : "AGE"},                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The salary amount of the individual", 
                          "name": "SALARY"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "List of hobbies that the individual enjoys", 
                          "name": "HOBBIES"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The residential address of the individual", 
                          "name": "ADDRESS"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The current balance in the user's bank account", 
                          "name": "BANK_BALANCE"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Indicates whether the individual possesses a credit card", 
                          "name": "HAS_CREDIT_CARD"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "Indicates whether the individual is currently employed", 
                          "name": "IS_EMPLOYED"
                        },                         {
                          "dataType": {"type" : "Date"}, 
                          "description": "The date when the individual joined the organization", 
                          "name": "JOIN_DATE"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "The date and time when the user last logged into the system", 
                          "name": "LAST_LOGIN"
                        },                         {
                          "dataType": {"type" : "String"}, 
                          "description": "User's preferred colors", 
                          "name": "FAVORITE_COLORS"
                        }], 
            "providerType": "arrow"
          }
        ), 
        filePath = "/prophecy-sftp/aruns/formatted_json_data_10.json"
    )
    SFTPSource_2 = Task(
        task_id = "SFTPSource_2", 
        component = "Dataset", 
        table = {
          "name": "prophecy__temp_p1_pre_custom_object_data_0", 
          "sourceType": "Source", 
          "sourceName": "prophecy__temp_p1_source", 
          "alias": ""
        }
    )
    fetch_posts_by_id = Task(
        task_id = "fetch_posts_by_id", 
        component = "RestAPI", 
        method = "GET", 
        body = "", 
        url = "https://jsonplaceholder.typicode.com/posts/1", 
        params = "", 
        headers = ""
    )
    model_p1_custom_object_data = Task(
        task_id = "model_p1_custom_object_data", 
        component = "Model", 
        modelName = "model_p1_custom_object_data"
    )
    SFTPSource_2.out0 >> [fetch_posts_by_id.in0, SFTPSource_2.input_port_0_1]
    SFTPSource_2.output_port_0_1 >> model_p1_custom_object_data.in_1
