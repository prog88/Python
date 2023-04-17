# define
def Convert_CM_To_M(cmStepsHeight):
    return cmStepsHeight/100    # 1m = 100cm

# minus 2, because he is smart he go to toilet before to start the journey and goes at the end of the journey
def Convert_Up_And_Down_ForA_Week_From(timesByDay):
    upAndDown = 2   # back and forth
    week = 7        # 1 week is 7 days
    return (timesByDay-1) * upAndDown * week

def Eval_Steps(nbSteps, stepHeight):
    timesByDay = 5  # 1 day goes 5 times to WC
    occurenceByWeek = Convert_Up_And_Down_ForA_Week_From(timesByDay)
    nbStepsForWeek = occurenceByWeek * nbSteps
    stepInMeter = Convert_CM_To_M(stepHeight)
    return nbStepsForWeek * stepInMeter

# exec
nbSteps = 10
cmStepsHeight = 10 
nbMeterSteopsByWeek = Eval_Steps(nbSteps, cmStepsHeight)
print("For " + str(nbSteps) + " steps of " + str(cmStepsHeight) + "cm Height, The Guard goes " + str(nbMeterSteopsByWeek) + " meter by week.")