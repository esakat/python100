import re # 正規表現の利用

def cipher(str):
    # いったんリストにして、1文字づつ処理
    str = list(str)
    re_str = []
    for s in str:
        if re.search('[a-z]',s):
            # 文字コードで英子文字は97~122 以下の処理でa->z,b->y,c->x...z->aのように変換される
            re_str.append(chr(219-ord(s)))
        else:
            re_str.append(s)
    return "".join(re_str)

test_str = "I am b a esaka!!"

print(cipher(test_str))
# 結果:I zn z vhzpz!!
print(cipher(cipher(test_str)))
# 結果:I am a esaka!!
