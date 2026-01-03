import os
from PIL import Image


def remove_exif_folder(folder_path):
    # フォルダ内のすべてのファイルを取得
    file_list = os.listdir(folder_path)

    for file_name in file_list:
        try:
            # ファイルの拡張子をチェックして画像ファイルか確認
            _, file_ext = os.path.splitext(file_name)
            if file_ext.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
                # 画像読み込み
                image_path = os.path.join(folder_path, file_name)
                image = Image.open(image_path)

                # # 縦長の場合90度回転させる
                # width, height = image.size
                # if height > width:
                #     image = image.rotate(90, expand=True)

                # Exifメタデータを削除
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(list(image.getdata()))

                # 元のファイルを上書き保存
                image_without_exif.save(image_path)

                print("Success: " + file_name)
        except:
            print("Error: " + file_name)


if __name__ == "__main__":
    for folder_name in os.listdir("ticket"):
        if os.path.isdir(os.path.join("ticket", folder_name)):
            print("Processing folder: " + folder_name)
            remove_exif_folder(os.path.join("ticket", folder_name))
