import re

import os


# def read(file_path):
#     with open(file_path, "r", encoding="ansi") as f:
#         f = f.readlines()
#         return f

def new_text():
    """重新定制题库"""
    file_path = os.getcwd() + "\\tiku.txt"
    print(file_path)
    i = 0
    new_f = open(os.getcwd() + "\\new.txt", 'w', encoding="utf8")
    with open(file_path, "r", encoding="ansi") as f:
        while True:
            if t := f.readline():
                if not t.startswith("Q(") and not t.startswith("A("):
                    continue
                pattern = r'="([^"]*)"'
                matches = re.findall(pattern, t)
                if not matches:
                    continue
                new_t = matches[0]
                if t.startswith("Q("):
                    new_t_l = new_t.split("-")
                    new_f.write(f"Q({i}):{new_t_l[-1]}-{new_t_l[0]}\n")
                else:
                    new_f.write(f"A({i}):{new_t}\n")
                    i += 1
            else:
                break
    print(i)
    new_f.close()


if __name__ == "__main__":
    file_path = os.getcwd() + "\\tiku.txt"
    data = {}
    result = []
    i = 0
    with open(file_path, "r", encoding="ansi") as f:
        while True:
            if t := f.readline():
                if not t.startswith("Q(") and not t.startswith("A("):
                    continue
                pattern = r'="([^"]*)"'
                matches = re.findall(pattern, t)
                if not matches:
                    continue
                new_t = matches[0]
                if t.startswith("Q("):
                    new_t_l = new_t.split("-")
                    data[i] = f"Q({i}):{new_t_l[-1]}-{new_t_l[0]}"
                else:
                    result.append(f"{data[i]}|A({i}):{new_t}")
                    i += 1
            else:
                break
    import json

    with open(os.getcwd() + "\\ht.txt", "w", encoding="utf8") as f:
        f.write("\n".join(result))
