Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    SFTPSource_0 = SourceTask(
        task_id = "SFTPSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        connector = Connection(kind = "sftp", authMethod = "password", id = "sftp", port = 22), 
        format = CSVFormat(header = True, separator = ","), 
        filePath = {
          "type": "concat_operation", 
          "properties": {
            "elements": [{
                            "type": "literal", 
                            "properties": {
                              "value": "/prophecy-sftp/aruns/test_20recordssdfklmsdklfmklsdmfklmsdkmfklmsdlkf.csv"
                            }
                          }]
          }
        }
    )
