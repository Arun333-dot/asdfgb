Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    empty_output_csv = SourceTask(
        task_id = "empty_output_csv", 
        component = "OrchestrationSource", 
        kind = "DatabricksVolumeSource", 
        connector = Connection(kind = "databricks"), 
        format = CSVFormat(separator = ",", header = True), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{
                            "type": "literal", 
                            "properties": {"value" : "fghfghfghfghfgfdfsdfsdfsdfsdfs_this_is_propheyc"}
                          }]
          }
        }
    )
