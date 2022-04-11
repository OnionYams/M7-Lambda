
import csv
from functools import reduce

f = open("911_Calls_for_Service_(Last_30_Days).csv", newline='')
reader = csv.DictReader(f)
    
filteredCalls = list(filter(lambda row: row["zip_code"] != "" and row["neighborhood"] != "" 
                            and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "", reader))

avgResponse = reduce(lambda val, dict: val + float(dict["totalresponsetime"]), filteredCalls, 0)
print("Response time avg: " + str(avgResponse/len(filteredCalls)))
avgDispatch = reduce(lambda val, dict: val + float(dict["dispatchtime"]), filteredCalls, 0)
print("Response time avg: " + str(avgDispatch/len(filteredCalls)))
avgTotal = reduce(lambda val, dict: val + float(dict["totaltime"]), filteredCalls, 0)
print("Response time avg: " + str(avgTotal/len(filteredCalls)))


""" #for i in range(len(calls)):
#filteredCalls = filter(lambda dict: dict.get("neighborhood") if dict.get("neighborhood") != "" else "" for dict in calls) 
res = list(filter(None, ({key : val for key, val in dict.items() if val} for dict in calls)))

print(res[0])
#filteredCalls = filter(lambda zip_code: zip_code != "", filteredCalls)

total_time = reduce(lambda val, dict: )

print(total_time/len(list(calls)))

print(type(filteredCalls))
print(list(filteredCalls[0])) """
#print(calls[1])
#print(calls[2])"""
