import json
import requests

response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
image_info = response.json()

castles_list = {}
with open("castles/100castles.txt", "r", encoding="utf-8") as f:
    for line in f:
        castle_info = line.split("\t")

        tmp_list = []
        for key in image_info.keys():
            if castle_info[2] in key:
                for marker in image_info[key]["markers"]:
                    if castle_info[1] in marker["title"]:
                        tmp_list.append({"title": castle_info[1] + "(" + castle_info[3] + ")",
                                         "photo": marker["photo"]})

        if len(tmp_list) > 0:
            castles_list[castle_info[2]] = tmp_list
        else:
            castles_list[castle_info[2]] = [{"title": castle_info[1] + "(" + castle_info[3] + ")",
                                             "photo": "https://placehold.jp/ffffff/000000/400x300.jpg?text=未訪問"}]

with open("castles/castles.json", "w", encoding="utf-8") as f:
    json.dump(castles_list, f, ensure_ascii=False, indent=4)
