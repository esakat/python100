# 3列目のリストと、行ごとのリストをとる
values = [line.split('\t')[2] for line in open('./hightemp.txt')]
keys = [line for line in open('./hightemp.txt')]

dic = dict(zip(keys,values))

# ３列目の値でソート
sort_dic = sorted(dic.items(), key=lambda x:x[1])

for k,v in sort_dic:
    print(k,end='')

# 確認用コマンド
# $ cat hightemp.txt |  sort -k3
