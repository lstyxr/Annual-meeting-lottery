# 格式化姓名，两个字的中间补充空格对齐
def name_format(name):
    if len(name) == 2:
        name = name[0] + f"{chr(12288)}" + name[1]
    return name