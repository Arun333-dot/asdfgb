Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    fetch_employees = Task(
        task_id = "fetch_employees", 
        component = "RestAPI", 
        method = "GET", 
        body = "", 
        url = "https://postman-echo.com/get", 
        params = "name={{First Name}}&job={{Job Title}}", 
        headers = ""
    )
    DatabricksSource_1 = SourceTask(
        task_id = "DatabricksSource_1", 
        component = "OrchestrationSource", 
        kind = "DatabricksSource", 
        connector = Connection(kind = "databricks", authType = "pat", id = "connnection"), 
        format = DATABRICKSFormat(
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          description = "Contact information for individuals, aiding in outreach and relationship management efforts.", 
          schema = {
            "fields": [{
                          "dataType": {"type" : "utf8"}, 
                          "description": "The first name of the individual", 
                          "name": "First Name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The surname of the individual", 
                          "name": "Last Name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The street address of the individual", 
                          "name": "Street Address"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The name of the city where the individual resides.", 
                          "name": "City Name"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Abbreviation representing the state of residence.", 
                          "name": "State Code"
                        },                         {
                          "dataType": {"type" : "int64"}, 
                          "description": "Postal code for the address location", 
                          "name": "Zip Code"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Contact phone number of the individual", 
                          "name": "Phone Number"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The email address of the individual", 
                          "name": "Email Address"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "The title of the individual's job position", 
                          "name": "Job Title"
                        },                         {
                          "dataType": {"type" : "utf8"}, 
                          "description": "Name of the company where the individual is employed", 
                          "name": "Company Name"
                        }], 
            "providerType": "Arrow"
          }
        ), 
        tableFullName = {"database" : "qa_team", "name" : "data_with_spaces", "schema" : "qa_database"}
    )
    DatabricksSource_1.out0 >> fetch_employees.in0
