import json

with open("content.json", "r", encoding="utf-8") as f:
    content = json.load(f)

horses = content["Horses"]

#各データの次に続くものをひたすら探す
for i in range(len(horses)):
    search_start = horses[i]

    for horse in horses:
        if horse["Joint"][0] == search_start["Joint"][1]:
            print(search_start["Name"] +"->" +horse["Name"])