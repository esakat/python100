# １列目のデータを取り出し
col1 = [line.split('\t')[0] for line in open('./hightemp.txt')]
output = []

# 別リストに追加していく、重複した値は入れない
for c in col1:
    if c not in output:
        output.append(c)

print(output)

# $ cat hightemp.txt | cut -f 1 | sort -k1  | uniq
