Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_pipeline2_Deduplicate_2 = Task(
        task_id = "model_pipeline2_Deduplicate_2", 
        component = "Model", 
        modelName = "model_pipeline2_Deduplicate_2"
    )
