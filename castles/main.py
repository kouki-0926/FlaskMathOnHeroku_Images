import json

castles_list = {}
with open('castles/100castles.txt', 'r', encoding='utf-8') as f:
    for line in f:
        tmp = line.split("\t")

        castles_list[tmp[1]] = {"location": tmp[2] + tmp[3],
                                "coords": [tmp[4], tmp[5]],
                                "photo": "https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/" + tmp[2] + "/" + tmp[1] + ".jpg"}

with open("castles/castles.json", "w", encoding='utf-8') as f:
    json.dump(castles_list, f, ensure_ascii=False, indent=4)
