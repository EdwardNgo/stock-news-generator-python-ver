# import numpy as np 
# import random as rd

# # The statespace
# states=["Sleep","Icecream","Run"]

# # Possible sequences of events
# transitionName=[["SS","SR","SI"],["RS","RR","RI"],["IS","IR","II"]]

# # Probabilities matrix (transition matrix)
# transitionMatrix = [[0.2,0.6,0.2],[0.1,0.6,0.3],[0.2,0.7,0.1]]

# if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[1]) != 3:
#     print("Somewhere, something went wrong. Transition matrix, perhaps?")
# else: print("All is gonna be okay, you should move on!! ;)")

# def activity_forecast(days):
    
#     activityToday="sleep"
#     print("Start date"+ activityToday)
    
#     activityList=[activityToday]
#     i=0
#     prob=1
    
#     while i != days:
#         if activityToday =="Sleep":
#             change=np.random.choice(transitionName[0],replace=True, p=transitionMatrix[0])
#             if change == "SS":
#                 prob=prob*0.2
#                 activityList.append("Sleep")
#                 pass
#             elif change == "SR":
#                 prob=prob*0.6
#                 activityToday="Run"
#                 activityList.append("Run")
#             else:
#                 prob=prob*0.2
#                 activityToday = "Icecream"
#                 activityList.append("Icecream")
#         elif activityToday == "Run":
#             change = np.random.choice(transitionName[1],replace=True,p=transitionMatrix[1])
#             if change == "RR":
#                 prob = prob * 0.5
#                 activityList.append("Run")
#                 pass
#             elif change == "RS":
#                 prob = prob * 0.2
#                 activityToday = "Sleep"
#                 activityList.append("Sleep")
#             else:
#                 prob = prob * 0.3
#                 activityToday = "Icecream"
#                 activityList.append("Icecream")
#         elif activityToday == "Icecream":
#             change = np.random.choice(transitionName[2],replace=True,p=transitionMatrix[2])
#             if change == "II":
#                 prob = prob * 0.1
#                 activityList.append("Icecream")
#                 pass
#             elif change == "IS":
#                 prob = prob * 0.2
#                 activityToday = "Sleep"
#                 activityList.append("Sleep")
#             else:
#                 prob = prob * 0.7
#                 activityToday = "Run"
#                 activityList.append("Run")
#         i+=1
#     print("Possible states: " + str(activityList))
#     print("End state after "+ str(days) + " days: " + activityToday)
#     print("Probability of the possible sequence of states: " + str(prob))
    
# activity_forecast(2)
content_blocks=open('/home/viethoang/petproject/OOP/STOCKNEWS_GENERATOR/Vnexpress.CLASSIFIED.VNINDEX.txt','r').read()
import re
pattern_1 = "NHÓM\s\d+-\d+"
pattern_2 = "\d+: " 
pattern_3 = "\n\n"
pattern_vnindex = "NHÓM\s\d+"
pattern_emptyline = "\s*$"
content_blocks = re.sub(pattern_1, "", content_blocks)
content_blocks = re.sub(pattern_2, "", content_blocks)
content_blocks = re.sub(pattern_3, "", content_blocks)
content_blocks = re.sub(pattern_vnindex, "___REMOVE___",content_blocks)
content_blocks = re.sub(pattern_emptyline,"",content_blocks)
with open('/home/viethoang/petproject/OOP/STOCKNEWS_GENERATOR/test.txt','w') as f:
    f.write(content_blocks)
