import json

with open("content.json", "r", encoding="utf-8") as f:
    content = json.load(f)

horses = content["Horses"]
search_1st = []

# 1段目だけなら、全ペアを総当たりで確認する
for search_start in horses:
    for horse in horses:
        if horse["Name"] == search_start["Name"]:
            continue
        if horse["Joint"][1] == search_start["Joint"][0]:
            pair = horse["Name"] + "->" + search_start["Name"]
            search_1st.append(pair)
            print(pair)