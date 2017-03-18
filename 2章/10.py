# リスト内包表記使ってみる
# num_lines = len(list(open('./hightemp.txt')))

# ジェネレータ内包表記
# 1行づつ読み込み、行数カウント
# リスト内包表記のようにリストを作成しないためメモリ使用量が減る
num_lines = sum(1 for line in open('./hightemp.txt'))
print(num_lines)

# 結果確認用
import subprocess
output = subprocess.check_output(['wc','-l','./hightemp.txt'])
print(output)
