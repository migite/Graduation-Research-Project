import json

with open("content.json", "r", encoding="utf-8") as f:
    content = json.load(f)

horses = content["Horses"]
search_1st = []

#各データの次に続くものをひたすら探す
for i in range(len(horses)):
    search_start = horses[i]

    #一つ目の一致を探す
    for horse in horses:
        if horse["Joint"][0] == search_start["Joint"][1]:
            if(horse["Name"] != search_start["Name"]):
                search_1st.append((search_start["Name"] +"->" +horse["Name"]))
                print(search_start["Name"] +"->" +horse["Name"])

        
