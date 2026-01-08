import requests
import os
from datetime import datetime

# XKCD API 網址
URL = "https://xkcd.com/info.0.json"

def fetch_xkcd():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch XKCD: {response.status_code}")
    data = response.json()
    
    # 取得漫畫資訊
    num = data["num"]
    title = data["title"]
    img_url = data["img"]
    
    # 確保 images 資料夾存在
    os.makedirs("images", exist_ok=True)
    
    # 存檔名稱：漫畫編號 + 原始檔名
    img_name = f"images/{num}_{os.path.basename(img_url)}"
    
    # 下載圖片
    img_data = requests.get(img_url).content
    with open(img_name, "wb") as f:
        f.write(img_data)
    
    print(f"Downloaded XKCD #{num} - {title} -> {img_name}")

if __name__ == "__main__":
    fetch_xkcd()
