from collections import Counter

# １列目のデータを取り出し
# col1 = [line.split('\t')[0] for line in open('./hightemp.txt')]
# collections.Counterを利用
# counter = Counter(col1)

# １行にまとめてジェネレータ内包表記のほうが良い？
counter = Counter(line.split('\t')[0] for line in open('./hightemp.txt'))
for word,count in counter.most_common():
    print(word+', '+str(count))

# 確認用コマンド
# $ cat ./hightemp.txt  | cut -f 1 | sort | uniq -c | sort -r
