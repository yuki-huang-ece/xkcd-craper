from main import fetch_xkcd
import os

def test_fetch_xkcd_creates_image():
    fetch_xkcd()
    # 確認 images 資料夾有檔案
    assert len(os.listdir("images")) > 0
