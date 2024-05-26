import json
import os
import tkinter as tk
import tkinter.ttk as ttk


# 语言窗口主类
class Lang(tk.Toplevel):
    def __init__(self, root, lang, theme):
        super().__init__(root)
        self.bg = theme[0]
        self.fg = theme[1]
        self.button = theme[2]
        # 窗口语言
        self.lang = lang
        self.root = root
        # 窗口主题
        self.theme = theme
        self.title(lang[0])
        self.geometry("400x200")
        self.resizable(False, False)
        self.config(bg=self.bg)
        self.value = []
        # 获取语言包
        for i in os.listdir("./Languages"):
            if i.endswith(".lbg"):
                self.value.append(i.replace(".lbg", ""))
        tk.Label(self, text=lang[1], bg=self.bg, fg=self.fg,
                 font=("cmdysj", 20)).place(x=25, y=10)
        self.select = ttk.Combobox(self, values=self.value,
                                   font=("cmdysj", 15), state="readonly")
        self.select.set(self.value[int(lang[2])])
        # 语言选择
        self.select.place(x=25, y=70)
        self.ok = tk.Button(self, text=lang[3], bg=self.button[0],
                            fg=self.fg, font=("cmdysj", 15), relief="flat",
                            activebackground=self.button[2], activeforeground=self.fg,
                            command=self.save)
        self.ok.bind("<Enter>", self.enter)
        self.ok.bind("<Leave>", self.leave)
        self.ok.place(x=25, y=120)
        self.cancel = tk.Button(self, text=lang[4], bg=self.button[0],
                                fg=self.fg, font=("cmdysj", 15), relief="flat",
                                activebackground=self.button[2], activeforeground=self.fg,
                                command=lambda: self.destroy())
        self.cancel.bind("<Enter>", self.enter)
        self.cancel.bind("<Leave>", self.leave)
        self.cancel.place(x=260, y=120)

    def enter(self, event):
        event.widget.config(bg=self.button[1])

    def leave(self, event):
        event.widget.config(bg=self.button[0])

    def save(self):
        # 写入用户数据
        with open("./data/user_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        data["language"] = self.select.get()
        with open("./data/user_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        # 刷新父窗口，销毁自身
        self.root.fresh()
        self.destroy()


# 主题窗口主类
class Theme(tk.Toplevel):
    def __init__(self, root, themes, theme):
        super().__init__(root)
        self.bg = theme[0]
        self.fg = theme[1]
        self.button = theme[2]
        self.root = root
        # 窗口语言
        self.themes = themes
        self.title(themes[0])
        self.geometry("400x250")
        self.resizable(False, False)
        self.config(bg=self.bg)
        # 浅色/深色主题选择
        tk.Label(
            self, text=themes[1], bg=self.bg, fg=self.fg,
            font=("cmdysj", 20)).place(x=25, y=10)
        self.value = themes[2:4]
        self.select = ttk.Combobox(self, values=self.value,
                                   font=("cmdysj", 15), state="readonly")
        # 浅色/深色主题对于的子主题
        self.value2 = []
        # 获取子主题
        with open("./data/user_data.json", "r", encoding="utf-8") as f:
            t = json.load(f)["theme"].split("-")
            # 浅色
            if t[0] == "light":
                t2 = 0
                for i in os.listdir("./Themes"):
                    if i.startswith("light-") and i.endswith(".lbe"):
                        self.value2.append(i.replace(".lbe", ""))
            # 深色
            else:
                t2 = 1
                for i in os.listdir("./Themes"):
                    if i.startswith("dark-") and i.endswith(".lbe"):
                        self.value2.append(i.replace(".lbe", ""))
            self.select2 = ttk.Combobox(self, values=self.value2,
                                        font=("cmdysj", 15), state="readonly")
            self.select2.set(self.value2[self.value2.index(t[0]+"-"+t[1])])
            self.select.set(self.value[t2])
        self.select.bind("<<ComboboxSelected>>", self.the)
        # 选择子主题
        self.select.place(x=25, y=70)
        self.select2.place(x=25, y=120)
        self.ok = tk.Button(self, text=self.themes[4], bg=self.button[0],
                            fg=self.fg, font=("cmdysj", 15), relief="flat",
                            activebackground=self.button[2], activeforeground=self.fg,
                            command=self.save)
        self.ok.bind("<Enter>", self.enter)
        self.ok.bind("<Leave>", self.leave)
        self.ok.place(x=25, y=170)
        self.cancel = tk.Button(self, text=self.themes[5], bg=self.button[0],
                                fg=self.fg, font=("cmdysj", 15), relief="flat",
                                activebackground=self.button[2], activeforeground=self.fg,
                                command=lambda: self.destroy())
        self.cancel.bind("<Enter>", self.enter)
        self.cancel.bind("<Leave>", self.leave)
        self.cancel.place(x=260, y=170)

    def the(self, event):
        # 更新子主题选项
        self.value2 = []
        if event.widget.get() == self.value[0]:
            for i in os.listdir("./Themes"):
                # 浅色
                if i.startswith("light-") and i.endswith(".lbe"):
                    self.value2.append(i.replace(".lbe", ""))
            self.select2.config(values=self.value2)
            self.select2.set(self.value2[0])
        else:
            for i in os.listdir("./Themes"):
                # 深色
                if i.startswith("dark-") and i.endswith(".lbe"):
                    self.value2.append(i.replace(".lbe", ""))
            self.select2.config(values=self.value2)
            self.select2.set(self.value2[0])

    def save(self):
        # 写入用户数据文件
        with open("./data/user_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        data["theme"] = self.select2.get()
        with open("./data/user_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        # 更新主题，销毁自身
        self.root.fresh()
        self.destroy()

    def enter(self, event):
        event.widget.config(bg=self.button[2])

    def leave(self, event):
        event.widget.config(bg=self.button[0])


# 右侧栏主类
class Rights:
    def __init__(self, root, langs, themes, theme):
        self.root = root
        self.langs = langs
        self.themes = themes
        self.theme = theme

    def set_lang(self):
        Lang(self.root, self.langs, self.theme)

    def set_theme(self):
        Theme(self.root, self.themes, self.theme)
