Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_p10_Except_1 = Task(task_id = "model_p10_Except_1", component = "Model", modelName = "model_p10_Except_1")
    model_p10_Filter_0 = Task(task_id = "model_p10_Filter_0", component = "Model", modelName = "model_p10_Filter_0")
