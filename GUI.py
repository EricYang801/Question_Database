import tkinter as tk
from tkinter import ttk

# 建立主窗口
root = tk.Tk()
root.title("題庫系統")

# 設置窗口大小
root.geometry("400x300")
root.resizable(False, False)

# 題型選擇框架
frame_type = ttk.LabelFrame(root, text="選擇題型")
frame_type.pack(pady=10, padx=10, fill="x")

# 題型選擇
question_type = tk.StringVar()
types = ["單選題", "多選題", "是非題", "混合題"]
ttk.Combobox(frame_type, textvariable=question_type,
             values=types, state="readonly").pack(padx=10, pady=5, fill="x")

# 冊數選擇框架
frame_volume = ttk.LabelFrame(root, text="選擇冊數")
frame_volume.pack(pady=10, padx=10, fill="x")

# 創建冊數選擇
volume = tk.StringVar()
volumes = ["第一冊", "第二冊", "第三冊", "第四冊", "第五冊", "第六冊"]
ttk.Combobox(frame_volume, textvariable=volume, values=volumes,
             state="readonly").pack(padx=10, pady=5, fill="x")

# 單元選擇框架
frame_unit = ttk.LabelFrame(root, text="選擇單元")
frame_unit.pack(pady=10, padx=10, fill="x")

unit_entry = tk.Entry(frame_unit)
unit_entry.pack(padx=10, pady=5, fill="x")

""" # 單元選擇
unit = tk.StringVar()
units = ["單元一", "單元二", "單元三", "單元四"]
ttk.Combobox(frame_unit, textvariable=unit, values=units).pack(
    padx=10, pady=5, fill="x") """

# 確定按鈕
submit_button = ttk.Button(root, text="確定")
submit_button.pack(pady=10)

# 運行主循環
root.mainloop()
