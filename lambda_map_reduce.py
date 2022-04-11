
#took inspiration from Jakob's model

import csv, json
from functools import reduce

calls = open("911_Calls_for_Service_(Last_30_Days).csv", newline='')
callsDict = csv.DictReader(calls)
    
filteredCalls = list(filter(lambda row: row["zip_code"] != "" and row["neighborhood"] != "" 
                            and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "", callsDict))

avgResponse = reduce(lambda val, dict: val + float(dict["totalresponsetime"]), filteredCalls, 0)
#print("Response time avg: " + str(avgResponse/len(filteredCalls)))
avgDispatch = reduce(lambda val, dict: val + float(dict["dispatchtime"]), filteredCalls, 0)
#print("Dispatch time avg: " + str(avgDispatch/len(filteredCalls)))
avgTotal = reduce(lambda val, dict: val + float(dict["totaltime"]), filteredCalls, 0)
#print("Total time avg: " + str(avgTotal/len(filteredCalls)))

neighborhoods = []
for hood in filteredCalls:
    if hood["neighborhood"] not in neighborhoods:
        neighborhoods.append(hood["neighborhood"])
#print(neighborhoods)

jsonOut = []
for hood in neighborhoods: 
    #print(hood)
    #get subset of dicts of each neighborhood
    currentHoodGroup = list(filter(lambda row: row["neighborhood"] == hood, filteredCalls))

    hoodResponse = reduce(lambda val, dict: val + float(dict["totalresponsetime"]), currentHoodGroup, 0)
    #print("Response time avg: " + str(hoodResponse/len(filteredCalls)))
    hoodDispatch = reduce(lambda val, dict: val + float(dict["dispatchtime"]), currentHoodGroup, 0)
    #print("Response time avg: " + str(hoodDispatch/len(filteredCalls)))
    hoodTotal = reduce(lambda val, dict: val + float(dict["totaltime"]), currentHoodGroup, 0)
    #print("Response time avg: " + str(hoodTotal/len(filteredCalls)))
    jsonOut.append({"neighborhood": hood, "Response time avg": hoodResponse/len(currentHoodGroup), 
                "Dispatch time avg": hoodDispatch/len(currentHoodGroup), "Total time avg": hoodTotal/len(currentHoodGroup)})

jsonOut.append({"neighborhood": "Overall", "Response time avg": avgResponse/len(filteredCalls), 
                "Dispatch time avg": avgDispatch/len(filteredCalls), "Total time avg": avgTotal/len(filteredCalls)})
#print(jsonOut[0], type(jsonOut[0]))
with open("hoodOut.json", "w") as outfile:
    json.dump(jsonOut, outfile)


calls.close()

