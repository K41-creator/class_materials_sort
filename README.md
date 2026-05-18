# class_materials_sort

講義資料を自動で整理するPythonツールです。

Downloadsフォルダ内のファイルを読み取り、
授業ごとにフォルダ分けし、
さらに拡張子ごとに自動整理します。

整理結果はデスクトップ上の `class_materials_sort` フォルダに出力されます。

---

## 機能

- 授業ごとにフォルダを自動作成
- 拡張子ごとに自動分類
- デスクトップへ整理結果を出力
- PDF / 画像 / Word / PowerPoint などに対応可能

---

## フォルダ構成例

### 整理前

```txt
Downloads/
    線形代数 第3回.pdf
    線形代数 課題.docx
    情報数学 第2回.pdf
    IMG_1823.png
```

### 整理後

```txt
Desktop/
    class_materials_sort/
        線形代数/
            pdf/
                線形代数 第3回.pdf

            docx/
                線形代数 課題.docx

        情報数学/
            pdf/
                情報数学 第2回.pdf

        IMG_1823/
            png/
                IMG_1823.png
```

---

## 使用技術

- Python
- pathlib
- shutil

---

## 実行方法

```bash
python main.py
```

---

## 学んだこと

- pathlibによるパス操作
- shutilによるファイル移動
- for文
- if文
- 辞書(dictionary)
- 文字列処理
- ファイル整理の自動化

---

## 今後追加したい機能

- GUI化
- ドラッグ＆ドロップ対応
- OCRによる授業名自動認識
- 重複ファイル対策
- ファイルコピー対応
- ログ出力機能
- 設定ファイル対応

---

## 注意

現在はファイルを「移動」します。
誤操作防止のため、テスト用フォルダでの実行を推奨します。

---

## ライセンス

MIT License# class_materials_sort
