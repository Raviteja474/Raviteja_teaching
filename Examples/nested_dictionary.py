# Nested dictionary
college = {"GTNN": [{"Engineeering":{"ECE":{1:"Ramya",2:"Ramya1",3:"Ramya2",4:"Ramya3"},
                                         "EEE":{1:"Ramya4",2:"Ramya15",3:"Ramya6",4:"Ramya7"},
                                         "CSE":{1:"Ramya8",2:"Ramya9",3:"Ramya10",4:"Ramya11"},
                                         "IT":{1:"Ramya12",2:"Ramya13",3:"Ramya14",4:"Ramya15"}
                                          }},
                {"polytechnic": {"ECE": {1:"Ramya16",2:"Ramya17",3:"Ramya18"},
                                  "EEE": {1:"Ramya20",2:"Ramya21",3:"Ramya22"},
                                  "CSE": {1:"Ramya24",2:"Ramya25",3:"Ramya26"},
                                  "IT": {1:"Ramya28",2:"Ramya29",3:"Ramya30"}
                                 }}]
                        }


print(len(college["GTNN"][0]["Engineeering"]["ECE"][1]))

# 2nd year class toppers
print(college["GTNN"][0]["Engineeering"])

# 19@@ take out hardcode
entries = [0,1]
print(entries)
divisions = ["Engineeering", "polytechnic"]
branches = ["ECE", "EEE", "CSE", "IT"]
classes = [1,2,3,4]

for entry in entries:
    for division in divisions:
        for branch in branches:
            for class1 in classes:
                if entry == 0 and division == "Engineeering":
                    if class1 == 2:
                        print(f"entry : {entry}, division: {division}, branch :{branch}, class: {class1}")
                        print(college["GTNN"][entry][division][branch][class1])
                if entry == 1 and division == "polytechnic":
                    if class1 == 2:
                        print(f"entry : {entry}, division: {division}, branch :{branch}, class: {class1}")
                        print(college["GTNN"][entry][division][branch][class1])
