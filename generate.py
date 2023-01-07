# -*- coding: utf-8 -*-
# @Time    : 2022/12/8 12:33
# @Author  : AI悦创
# @FileName: generate.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import os
from urllib.parse import urljoin

TEMPLATE = '<VideoPlayer src="{url}" />'


def save(urls: list):
    html = """# 人均老师
"""
    code = """```url
{}
```
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(html)
        for url in sorted(urls):
            content = code.format(url)
            f.write(content + "\n")


def generate_path():
    BASE = "https://github.aiyc.top/teacher-per-capita"
    target = ["mp4", "ts"]
    result = []
    for root, _, filenames in os.walk("."):
        for name in filenames:
            suffix = name.split(".")[-1].lower()
            # print(suffix)
            if suffix not in target:
                continue
            url = urljoin(BASE, os.path.join(root, name))
            url = TEMPLATE.format(url=url)
            yield url


if __name__ == '__main__':
    url = generate_path()
    # for i in r:
    #     print(i)
    save(url)
    print("生成成功！继续上传，同步。")
