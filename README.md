## class_materials_sort

講義資料を自動で整理・分類するPythonツールです。

Downloadsフォルダ内のファイルを解析し、

- 科目ごと
- 拡張子ごと

に自動で分類して、デスクトップへ整理します。

さらに、

- PDFテキスト解析
- OCR（画像文字認識）
- 重複ファイルスキップ
- ログ出力
- 日付フィルタ
- GUI操作

にも対応しています。

---

# 主な機能

## 科目ごとの自動整理

Downloadsフォルダ内の資料を：

```txt
数学A/
 ├─ pdf/
 ├─ png/
 ├─ pptx/

コンピュータ数学/
 ├─ pdf/
 ├─ jpg/
```

のように自動整理します。

---

## 拡張子ごとの整理

対応拡張子：

- pdf
- docx
- pptx
- png
- jpg
- jpeg

---

## PDFテキスト解析

PDFの1ページ目から文字を抽出し、
ファイル名に科目名が無い場合でも分類できます。

使用ライブラリ：

- pdfplumber

---

## OCR対応（画像文字認識）

画像内の文字を読み取り、
スクリーンショットや画像資料も自動分類します。

対応画像：

- png
- jpg
- jpeg

使用ライブラリ：

- pytesseract
- Pillow

OCRエンジン：

- Tesseract OCR

---

## 重複ファイルスキップ

既にコピー済みのファイルが存在する場合は、
重複コピーを防ぐためスキップします。

これにより、
同じ資料を何度実行しても
ファイルが増殖しません。

---

## 日付フィルタ

指定した日付以降のファイルのみ整理できます。

例：

```python
days_limit = 7
```

↓

「7日以内に追加されたファイルのみ整理」

---

## ログ出力

整理結果を：

```txt
log.txt
```

へ保存します。

例：

```txt
lecture1.pdf を コンピュータ数学/pdf にコピーしました。
```

---

## GUI対応

Tkinterを使用したGUIで、
ボタン操作のみで整理できます。

---

# 使用ライブラリ

## インストール

```bash
pip install pdfplumber pytesseract pillow
```

---

# Tesseract OCR インストール

Windows版Tesseract OCRをインストールしてください。

インストール後、
コード内でOCRエンジンのパスを指定します。

例：

```python
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Users\YOUR_NAME\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
)
```

---

# 使用方法

## 1. Downloadsフォルダへ資料を入れる

対応ファイル：

- pdf
- docx
- pptx
- png
- jpg
- jpeg

---

## 2. プログラム実行

```bash
python main.py
```

---

## 3. GUIで「整理開始」を押す

整理済みファイルが：

```txt
Desktop/class_materials_sort
```

へ出力されます。

---

# ディレクトリ構成

```txt
class_materials_sort/
├─ main.py
├─ file_presort.py
├─ README.md
├─ requirements.txt
```

出力例：

```txt
class_materials_sort/
├─ 数学A/
│   ├─ pdf/
│   └─ png/
│
├─ コンピュータ数学/
│   ├─ pdf/
│   └─ jpg/
│
└─ log.txt
```

---

# 対応機能

- [x] 科目別整理
- [x] 拡張子別整理
- [x] PDF解析
- [x] OCR
- [x] GUI
- [x] ログ出力
- [x] 日付フィルタ
- [x] 重複ファイルスキップ

---

# 今後追加予定

- JSON設定ファイル
- ドラッグ＆ドロップ対応
- exe化
- AIによる自動分類
- PDF全文検索
- 自動バックアップ

---

# 開発環境

- Python 3.13
- Windows 11

---

# License

MIT License

# Third-Party Libraries

This project uses the following libraries and tools:

- Tesseract OCR (Apache License 2.0)
- pytesseract
- Pillow
- pdfplumber
