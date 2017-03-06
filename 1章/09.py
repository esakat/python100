import random # 乱数処理の利用

def rand_str(str):
    # スペースで区切ってリスト化
    str = str.split(' ')
    re_str = []
    for i,s in enumerate(str):
        if len(s) > 4:
            re_str.append(s[0]+"".join(random.sample(s[1:-1],len(s)-2))+s[-1])
        else:
            re_str.append(s)
    # 返り値は単語をスペースで付け直す
    return " ".join(re_str)

test_str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
test_str2 = "さいしょ と さいご の もじ さえ あっていれば じゅんばん は めちゃくちゃ でも ちゃんと よめる という けんきゅう に もとづいて わざと もじの じゅんばん を いれかえて あります どうです？ ちゃんと よめちゃう でしょ ？"

print(rand_str(test_str))
# 結果: I cnlu'dot belevie that I colud allctauy udeatsnnrd what I was radineg : the pehnomanel pwoer of the huamn mind .
print(rand_str(test_str2))
# 結果: さいしょ と さいご の もじ さえ あっていれば じんばゅん は めちゃちくゃ でも ちゃんと よめる という けゅきんう に もづといて わざと もじの じんばゅん を いかえれて あります どすでう？ ちゃんと よゃちめう でしょ ？
