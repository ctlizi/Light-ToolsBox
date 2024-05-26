# GUI框架
import tkinter as tk
# 右侧栏
import rights
# base 解/编码 GUI文件
import base as bs
# 加/解密 GUI文件
import cryption as cpt
# 读取用户数据文件
import json


# 将主文件窗口封装成一个类
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Light-ToolsBox")
        self.geometry("1000x600")
        self.resizable(False, False)
        # 选择语言窗口语言
        self.langs = []
        # 选择主题窗口语言
        self.themes = []
        # base 解/编码 窗口语言
        self.based = []
        # 加/解密 窗口语言
        self.cpd = []
        # 所有窗口主题
        self.bg = ""
        self.fg = ""
        # 按钮主题
        self.button = []
        # 右侧栏主类
        self.rs = rights.Rights(self, self.langs,
                                self.themes, [self.bg, self.fg, self.button])
        self.fresh()

    # 窗口刷新，为了能在选择语言/主题之后刷新窗口，更新窗口语言/主题
    def fresh(self):
        with open("./data/user_data.json", "r", encoding="utf-8") as f:
            # 读取用户数据文件
            user_data = json.load(f)
        with open(f"./Languages/{user_data['language']}.lbg", "r", encoding="utf-8") as f:
            # 读取语言文件
            language_data = f.readlines()
        # 标题大字
        title = ""
        # 工具栏
        boxes = []
        # 右侧栏
        right = []
        # 命令哈希
        command = []
        # 语言文件读取
        for i in language_data:
            sp = [j.strip() for j in i.split(": ")]
            if sp[0] == "TITLE":
                title = sp[1].split(", ")
            elif sp[0] == "BOXES":
                boxes = sp[1].split(", ")
            elif sp[0] == "RIGHT":
                right = sp[1].split(", ")
            elif sp[0] == "Languages":
                self.langs = sp[1].split(", ")
            elif sp[0] == "Themes":
                self.themes = sp[1].split(", ")
            elif sp[0] == "Base":
                self.based = sp[1].split(", ")
            elif sp[0] == "Cryption":
                self.cpd = sp[1].split(", ")
            elif sp[0] == "Command":
                command = [j.split("-") for j in sp[1].split(", ")]
        command = {j[0]: j[1] for j in command}
        with open(f"./Themes/{user_data['theme']}.lbe", "r", encoding="utf-8") as f:
            # 读取主题文件
            theme_data = f.readlines()
        for i in theme_data:
            sp = [j.strip() for j in i.split(": ")]
            if sp[0] == "Background":
                self.bg = sp[1]
            elif sp[0] == "Foreground":
                self.fg = sp[1]
                # 按钮样式
            elif sp[0] == "Button":
                self.button = sp[1].split(", ")
        # 窗口背景色更新
        self.config(bg=self.bg)
        # 右侧栏主类更新
        self.rs = rights.Rights(self, self.langs, self.themes,
                                [self.bg, self.fg, self.button])
        # 标题大字更新
        tk.Label(self, text=title, font=("cmdysj", 50),
                 bg=self.bg, fg=self.fg).place(x=400, y=20)
        y = 50
        # 工具栏更新
        for box in boxes:
            b = tk.Button(
                self, text=box, font=("cmdysj", 20), relief="flat", bg=self.button[0], width=17,
                fg=self.fg, activebackground=self.button[2], activeforeground=self.fg,
                command=eval("self."+command[box])
            )
            b.bind("<Enter>", self.enter)
            b.bind("<Leave>", self.leave)
            b.place(x=20, y=y)
            y += 100
        y = 150
        # 右侧栏更新
        for r in right:
            r = tk.Button(
                self, text=r, font=("cmdysj", 20), relief="flat", bg=self.button[0], width=17,
                fg=self.fg, activebackground=self.button[2], activeforeground=self.fg,
                command=eval("self."+command[r])
            )
            r.bind("<Enter>", self.enter)
            r.bind("<Leave>", self.leave)
            r.place(x=500, y=y)
            y += 100

    def enter(self, event):
        event.widget.config(bg=self.button[1])

    def leave(self, event):
        event.widget.config(bg=self.button[0])

    # 语言切换
    def lang(self):
        self.rs.set_lang()

    # 主题切换
    def theme(self):
        self.rs.set_theme()

    # base 编/解码
    def base(self):
        bs.Base(self, [self.bg, self.fg, self.button], self.based)

    # 加/解密
    def cryption(self):
        cpt.Cryption(self, [self.bg, self.fg, self.button], self.cpd)


if __name__ == "__main__":
    root = App()
    root.mainloop()
