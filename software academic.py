# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup

# 定义目标网页的URL
url = "https://example.com"  # 替换为实际的网页URL

# 发起HTTP请求并获取网页内容
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(html_content, "html.parser")

# 根据网页结构和标签，定位学术软件相关的信息
software_elements = soup.find_all("div", class_="software")  # 替换为实际的标签和类名

# 统计学术软件的数量
num_software = len(software_elements)

# 打印学术软件的数量
print("网页中的学术软件数量：", num_software)
