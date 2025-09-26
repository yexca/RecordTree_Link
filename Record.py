import os
import json
from datetime import datetime

AUTHOR_NAME=""
COMPARE_DATE="2025-09-01"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RECORD_PATH = os.path.join(BASE_DIR, 'Record Tree.json')

OUTPUT_NAME = ""

DOWNLOAD_LINKS = []

# search
def search_author(recordData):
    for authorData in recordData:
        if AUTHOR_NAME in authorData["author"]:
            return authorData
    return False

# get download link
def get_download_link(propertys):
    for property in propertys:
        DOWNLOAD_LINKS.append(property["Link"])
        print(property["Link"])
    return

# compare
def compare_date(compareDate, fileDate):
    return fileDate >= compareDate

# init
if AUTHOR_NAME == "":
    print("未输入作者名称")
    raise SystemExit
if os.path.exists(RECORD_PATH) == False:
    print("未找到数据文件")
    raise SystemExit

with open(RECORD_PATH, "r", encoding="utf-8") as file:
    recordData = json.load(file)
    # search
    if authorData := search_author(recordData):
        # record
        records = authorData["records"]
        # compare date?
        if COMPARE_DATE:
            print("输出大于日期 " + COMPARE_DATE + " 的下载链接")
            DOWNLOAD_LINKS.append(AUTHOR_NAME + " 在 " + COMPARE_DATE + " 之后的下载链接")
            OUTPUT_NAME = AUTHOR_NAME + " 在 " + COMPARE_DATE + " 之后的下载链接"

            compareDate = datetime.strptime(COMPARE_DATE, "%Y-%m-%d").date()
            for record in records:
                filename = record["FileNames"]
                fileDateOrigin = filename.split("]")[1][1:]
                fileDate = datetime.strptime(fileDateOrigin, "%Y-%m-%d").date()
                if compare_date(compareDate, fileDate):
                    get_download_link(record["property"])
        else:
            print("输出全部下载链接")
            DOWNLOAD_LINKS.append(AUTHOR_NAME + " 全部的下载链接")
            OUTPUT_NAME = AUTHOR_NAME + " 全部的下载链接"

            for record in records:
                get_download_link(record["property"])
    else:
        print(AUTHOR_NAME + " 不存在")

OUTPUT_PATH = os.path.join(BASE_DIR, OUTPUT_NAME + ".txt")
with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
    for link in DOWNLOAD_LINKS:
        file.write(str(link) + "\n")