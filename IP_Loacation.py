#Author：赵云香
#Data：2023-06-18
#Version：1.0

import tkinter as tk
import requests
import json
from PIL import ImageTk, Image

# 字段中英文映射关系
field_mapping = {
    "country": "国家",
    "regionName": "地区",
    "city": "城市",
    "zip": "邮编",
    "lat": "纬度",
    "lon": "经度"
}

def convert_coordinate(coordinate, field):
    value = abs(coordinate)
    direction = ""
    
    if field == "lat":
        if coordinate >= 0:
            direction = f"{value}°N"
        else:
            direction = f"{value}°S"
    elif field == "lon":
        if coordinate >= 0:
            direction = f"{value}°E"
        else:
            direction = f"{value}°W"
    
    return direction

def locate_ip():
    ip_address = entry.get()

    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = json.loads(response.content.decode("utf-8"))
    
    if data["status"] == "success":
        result = ""
        for field, value in data.items():
            if field in field_mapping:
                field_name = field_mapping[field]
                if field in ["lat", "lon"]:
                    value = convert_coordinate(value, field)
                result += f"{field_name}：{value}\n"
        
        result_text.set(result)
    else:
        result_text.set("无法定位 IP 地址。")

# 创建 GUI 窗口
window = tk.Tk()
window.title("IP定位-想念初恋版-EarthFamily")

# 设置窗口大小
window.geometry("650x600")

# 添加背景图片
bg_image = ImageTk.PhotoImage(Image.open("background.jpg"))
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# 创建标签和输入框
label = tk.Label(window, text="请输入要定位的 IP 地址：", font=("Helvetica", 15), bg="white")
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

entry = tk.Entry(window, font=("Helvetica", 14))
entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# 创建按钮
button = tk.Button(window, text="点我定位", command=locate_ip, font=("Helvetica", 14), bg="white")
button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# 创建结果显示文本
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text, font=("Helvetica", 18), wraplength=500, bg="white", anchor=tk.W, justify=tk.LEFT)
result_label.place(relx=0.5, rely=0.68, anchor=tk.CENTER)

# 创建工具数据接口支持标签
support_label = tk.Label(window, text="查询接口支持：OpenGPS、北斗全球定位系统", font=("Helvetica", 16), bg="white")
support_label.place(relx=0.16, rely=1.0, anchor=tk.SW)

# 运行 GUI 循环
window.mainloop()
