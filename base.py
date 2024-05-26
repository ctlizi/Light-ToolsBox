import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
# 复制
import pyperclip
import base64


class Base(tk.Toplevel):
    def __init__(self, root, theme, lang):
        super().__init__(root)
        self.root = root
        self.bg = theme[0]
        self.fg = theme[1]
        self.button = theme[2]
        self.lang = lang
        self.title(self.lang[0])
        self.geometry("450x300")
        self.resizable(False, False)
        self.config(bg=self.bg)
        tk.Label(self, text=self.lang[0], font=("cmdysj", 18),
                 bg=self.bg, fg=self.fg).place(x=10, y=10)
        # 选择base85/64/32/16
        self.base_set = ttk.Combobox(self, values=["base85", "base64", "base32", "base16"],
                                     state="readonly", font=("cmdysj", 14))
        self.base_set.set("base64")
        self.base_set.place(x=10, y=50)
        # 输入
        tk.Label(self, text=self.lang[1], font=("cmdysj", 14),
                 bg=self.bg, fg=self.fg).place(x=10, y=100)
        self.input_str = ttk.Entry(self, font=("cmdysj", 14))
        self.input_str.place(x=100, y=100)
        # 输出
        tk.Label(self, text=self.lang[2], font=("cmdysj", 14),
                 bg=self.bg, fg=self.fg).place(x=10, y=150)
        self.output_str = ttk.Entry(self, font=("cmdysj", 14),
                                    state="readonly")
        self.output_str.place(x=100, y=150)
        # 编码按钮
        self.encode = tk.Button(self, text=self.lang[3], bg=self.button[0], fg=self.fg,
                                font=("cmdysj", 14), activebackground=self.button[2],
                                activeforeground=self.fg, relief="flat", command=self.encode)
        self.encode.bind("<Enter>", self.enter)
        self.encode.bind("<Leave>", self.leave)
        self.encode.place(x=10, y=200)
        # 解码按钮
        self.decode = tk.Button(self, text=self.lang[4], bg=self.button[0], fg=self.fg,
                                font=("cmdysj", 14), activebackground=self.button[2],
                                activeforeground=self.fg, relief="flat", command=self.decode)
        self.decode.bind("<Enter>", self.enter)
        self.decode.bind("<Leave>", self.leave)
        self.decode.place(x=150, y=200)
        # 复制按钮
        self.copy = tk.Button(self, text=self.lang[5], bg=self.button[0], fg=self.fg,
                              font=("cmdysj", 14), activebackground=self.button[2],
                              activeforeground=self.fg, relief="flat", command=self.copy)
        self.copy.bind("<Enter>", self.enter)
        self.copy.bind("<Leave>", self.leave)
        self.copy.place(x=290, y=200)

    def enter(self, event):
        event.widget.config(bg=self.button[1])

    def leave(self, event):
        event.widget.config(bg=self.button[0])

    # 编码
    def encode(self):
        make = "error"
        # 判断
        if self.base_set.get() == "base85":
            make = base64.b85encode(self.input_str.get().encode("utf-8"))
        elif self.base_set.get() == "base64":
            make = base64.b64encode(self.input_str.get().encode("utf-8"))
        elif self.base_set.get() == "base32":
            make = base64.b32encode(self.input_str.get().encode("utf-8"))
        elif self.base_set.get() == "base16":
            make = base64.b16encode(self.input_str.get().encode("utf-8"))
        # 写入输出
        self.output_str.config(state="normal")
        self.output_str.delete(0, tk.END)
        self.output_str.insert(0, make)
        self.output_str.config(state="readonly")

    # 解码
    def decode(self):
        make = "error"
        # 编码格式是否规范
        try:
            # 判断
            if self.base_set.get() == "base85":
                make = base64.b85decode(self.input_str.get().encode("utf-8"))
            elif self.base_set.get() == "base64":
                make = base64.b64decode(self.input_str.get().encode("utf-8"))
            elif self.base_set.get() == "base32":
                make = base64.b32decode(self.input_str.get().encode("utf-8"))
            elif self.base_set.get() == "base16":
                make = base64.b16decode(self.input_str.get().encode("utf-8"))
        except ValueError:
            # 报错
            make = "error"
            msg.showerror(self.lang[6], self.base_set.get() + " " + self.lang[7])
        # 写入输出
        self.output_str.config(state="normal")
        self.output_str.delete(0, tk.END)
        self.output_str.insert(0, make)
        self.output_str.config(state="readonly")

    # 复制
    def copy(self):
        pyperclip.copy(self.output_str.get())
        msg.showinfo(self.lang[8], self.lang[9])
