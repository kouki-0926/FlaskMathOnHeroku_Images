import os
import json
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image


def get_gps_data(image_path):
    # 画像からexif情報を取得
    image = Image.open(image_path)
    exif_data = image._getexif()
    exif_data_decoded = {TAGS.get(tag, tag): value for tag, value in exif_data.items()}

    # GPS情報を取得
    gps_info = exif_data_decoded['GPSInfo']
    gps_data = {GPSTAGS.get(tag, tag): value for tag, value in gps_info.items()}

    # 緯度経度を取得
    latitude  = gps_data.get('GPSLatitude', None)
    longitude = gps_data.get('GPSLongitude', None)

    # 60進数から10進数に変換
    latitude  = float( latitude[0] +  latitude[1] / 60 +  latitude[2] / 3600)
    longitude = float(longitude[0] + longitude[1] / 60 + longitude[2] / 3600)
    return latitude, longitude


def get_image_info(pref_name):
    # 画像のファイル名を取得
    path = "blog/" + pref_name + "/"
    file_list = os.listdir(path)
    path_list = [path + fileName for fileName in file_list]

    # 画像の情報を取得
    coordinates_list = [get_gps_data(fileName) for fileName in path_list]
    centerCoordinates = [{"coords": [sum([coordinates_list[i][0] for i in range(len(coordinates_list))]) / len(coordinates_list),
                                     sum([coordinates_list[i][1] for i in range(len(coordinates_list))]) / len(coordinates_list)]}]
    markers = [{"title": file_list[i].split(".")[0],
                "coords": coordinates_list[i],
                "photo": "https://raw.githubusercontent.com/kouki-0926/FlaskMathOnHeroku_Images/main/"+path_list[i]} for i in range(len(path_list))]

    return {"centerCoordinates": centerCoordinates, "markers": markers}


if __name__ == "__main__":
    # 保存ファイルを初期化
    saveFileName = "blog/image_info.json"
    with open(saveFileName, "w", encoding='utf-8') as f:
        f.write("")

    image_info = {}
    for pref_name in sorted(os.listdir("blog")):
        if os.path.isdir("blog/" + pref_name):
            image_info[pref_name] = get_image_info(pref_name)

    # json形式で保存
    with open(saveFileName, "a", encoding='utf-8') as f:
        json.dump(image_info, f, ensure_ascii=False, indent=4)
