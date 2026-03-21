import json
import requests

response = requests.get("https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/picture/image_info.json")
image_info = response.json()

castles_list = {
    "北海道・東北地方": {"castle": [], "visited": 0, "unvisited": 0},
    "関東地方": {"castle": [], "visited": 0, "unvisited": 0},
    "中部地方": {"castle": [], "visited": 0, "unvisited": 0},
    "近畿地方": {"castle": [], "visited": 0, "unvisited": 0},
    "中国地方": {"castle": [], "visited": 0, "unvisited": 0},
    "四国地方": {"castle": [], "visited": 0, "unvisited": 0},
    "九州・沖縄地方": {"castle": [], "visited": 0, "unvisited": 0}
}

area_list = [
    ["北海道・東北地方", ["北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県"]],
    ["関東地方", ["茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県"]],
    ["中部地方", ["新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県"]],
    ["近畿地方", ["三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県"]],
    ["中国地方", ["鳥取県", "島根県", "岡山県", "広島県", "山口県"]],
    ["四国地方", ["徳島県", "香川県", "愛媛県", "高知県"]],
    ["九州・沖縄地方", ["福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"]]
]

unvisited_castle_cnt = 0
with open("castles/100castles.txt", "r", encoding="utf-8") as f:
    for line in f:
        castle_info = line.split("\t")

        # 城が何地方に属するかを判定
        for area_idx in range(len(area_list)):
            if castle_info[2] in area_list[area_idx][1]:
                area = area_list[area_idx][0]
                break

        # 城の写真を取得
        image_list = []
        for key in image_info.keys():
            if castle_info[2] in key:
                for marker in image_info[key]["markers"]:
                    if castle_info[1] in marker["title"]:
                        image_list.append(marker["photo"])

        # 訪問済みか判定 未訪問の場合はダミー画像を追加
        if len(image_list) > 0:
            castles_list[area]["visited"] += 1
        else:
            castles_list[area]["unvisited"] += 1
            unvisited_castle_cnt += 1

            image_list.append("https://placehold.jp/ffffff/000000/400x300.jpg?text=未訪問")

        # 城の情報をリストに追加
        for image in image_list:
            castles_list[area]["castle"].append({"title": castle_info[0] + " " + castle_info[1] + "(" + castle_info[2] + castle_info[3] + ")",
                                                 "photo": image})

    # 地方ごとの訪問済み・未訪問の数を表示
    for area, data in castles_list.items():
        print(f"{area}: 訪問済み {data['visited']} 城, 未訪問 {data['unvisited']} 城")

    # 未訪問の城の数をリストに追加
    castles_list["unvisited_castle_cnt"] = unvisited_castle_cnt
    print("未訪問の城の数:", unvisited_castle_cnt)

with open("castles/castles.json", "w", encoding="utf-8") as f:
    json.dump(castles_list, f, ensure_ascii=False, indent=4)
