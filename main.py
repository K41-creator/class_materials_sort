from pathlib import Path
import shutil
import pdfplumber
import file_presort
import datetime
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\kaiy2\OCR\tesseract.exe"
)
#downloadフォルダ
download_path = Path.home() / "Downloads" / "pdf"
#desktopフォルダ
desktop_path = Path.home() / "OneDrive" / "Desktop"
#出力フォルダ
output_folder = desktop_path / "class_materials_sort"

output_folder.mkdir(exist_ok=True)

log_file = output_folder / "log.txt"
with open(log_file, "w", encoding="utf-8") as log:
    log.write("ファイルの整理を開始します。\n")

allowed_extensions = [
    "pdf",
    "docx",
    "pptx",
    "png",
    "jpg"
]


def extract_text_from_pdf(file_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            first_page = pdf.pages[0]

            text = first_page.extract_text()

            if text:
                return text.lower()
            
            return text
        
    except Exception as e:
        print(f"PDFのテキスト抽出に失敗しました: {e}")
        return ""
    

def extract_text_from_image(image_path):

    try:

        image = Image.open(image_path)

        text = pytesseract.image_to_string(
            image,
            lang="jpn"
        )

        return text.lower()

    except Exception as e:

        print(f"OCR失敗: {e}")

        return ""


file_presort.presort()

subjects = {
    "数学A": "数学A",
    "数学B": "数学B",
    "知的力学システム": "知的力学システム",
    "システム力学": "知的力学システム",
    "コンピュータ基礎演習": "コンピュータ基礎演習",
    "コンピュータ基礎": "コンピュータ基礎",
    "万 偉偉": "コンピュータ基礎",
    "コンピュータ数学": "コンピュータ数学",
    "基礎工学PBL": "基礎工学PBL",
    "フランス語中級": "フランス語中級",
    "第一外国語": "第一外国語",
    "E-larning": "E-larning",
    "その他": "その他"
}
#downloadフォルダ内のファイルを確認して、科目ごとに整理する
def sort_files_by_subject():
    for file in download_path.iterdir():
         #期間条件
         target_date = datetime.datetime(2026, 4, 1)
         modified_time = file.stat().st_mtime
         modified_date = datetime.datetime.fromtimestamp(modified_time)

         if modified_date < target_date:
             continue
         
         if file.is_file():

            file_name = file.name.lower()
            search_text = file_name

            if file.suffix.lower() == ".pdf":
                pdf_text = extract_text_from_pdf(file)
                if pdf_text:
                    search_text += " " + pdf_text
            elif file.suffix.lower() in [".png", ".jpg", ".jpeg"]:
                ocr_text = extract_text_from_image(file)
                if ocr_text:
                    search_text += " " + ocr_text
            subject = "その他"

            for keyword, subject_name in subjects.items():
                if keyword.lower() in search_text:
                    subject = subject_name
                    break

            extension = file.suffix.lower().replace(".", "")
            if extension == "":
                extension = "no_extension"

            if extension not in allowed_extensions:
                continue

            subject_folder = output_folder / subject
            subject_folder.mkdir(exist_ok=True)

            extension_folder = subject_folder / extension
            extension_folder.mkdir(exist_ok=True)


            target_file = extension_folder / file.name

            counter = 1

            if target_file.exists():

                 print(f"{target_file} は既に存在しています。")
                 with open(log_file, "a", encoding="utf-8") as log:
                    log.write(f"{target_file} は既に存在しています。\n")
                    log_area.insert(tk.END, f"{target_file} は既に存在しています。\n")
                    log_area.see(tk.END)
                 continue
         

            shutil.copy2(str(file), str(target_file))
        

            print(f"{file.name} を {subject}/{extension} にコピーしました。")
            with open(log_file, "a", encoding="utf-8") as log:
                log.write(f"{file.name} を {subject}/{extension} にコピーしました。\n")
                log_area.insert(tk.END, f"{file.name} を {subject}/{extension} にコピーしました。\n")
                log_area.see(tk.END)




#ダウンロード内容を確認

for file in download_path.iterdir():

    if file.is_file():

        file_name = file.name.lower()

        subject = "その他"

        for keyword, subject_name in subjects.items():
            if keyword.lower() in file_name:
                subject = subject_name
                break

        extension = file.suffix.lower().replace(".", "")

        print(extension)

        if extension not in allowed_extensions:
            continue




    




#guiを作成
import tkinter as tk

root = tk.Tk()
root.title("Class Materials Sorter")
root.geometry("700x500")

log_area = tk.Text(root,
                   height=20, 
                   width=80
                   )
log_area.pack(pady=20)

button = tk.Button(root, 
                   text="整理開始",
                   command=sort_files_by_subject
                   )
button.pack(pady=20)
root.mainloop()
