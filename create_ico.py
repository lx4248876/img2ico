import sys
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

try:
    from PIL import Image
except ImportError:
    messagebox.showerror("错误", "未找到 PIL 模块。请安装 Pillow：pip install Pillow")
    sys.exit(1)

def create_icon(input_file, output_file, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    try:
        with Image.open(input_file) as img:
            img.save(output_file, format='ICO', sizes=sizes)
        return True
    except Exception as e:
        return str(e)

def select_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(filetypes=[("图像文件", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    return file_path

def main():
    input_file = select_file()
    if not input_file:
        messagebox.showinfo("提示", "未选择文件，程序退出。")
        return

    output_file = os.path.splitext(input_file)[0] + '.ico'
    result = create_icon(input_file, output_file)
    
    if result is True:
        messagebox.showinfo("成功", f"图标已成功创建: {output_file}")
    else:
        messagebox.showerror("错误", f"创建图标时出错: {result}")

if __name__ == '__main__':
    main()