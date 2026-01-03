import os
import piexif
import termcolor


def remove_exif_folder(folder_path):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        _, ext = os.path.splitext(file_name)
        if ext.lower() in [".jpg", ".jpeg"] and os.path.isfile(file_path):
            try:
                piexif.remove(file_path)
                print(termcolor.colored("Success:" + file_name, "green"))
            except Exception as e:
                print(termcolor.colored("Error:" + file_name, "red"))


if __name__ == "__main__":
    for folder_name in os.listdir("ticket"):
        if os.path.isdir(os.path.join("ticket", folder_name)):
            print("Processing folder: " + folder_name)
            remove_exif_folder(os.path.join("ticket", folder_name))
