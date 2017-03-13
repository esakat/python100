# 14と同じ感じ
input = int(input())

lines = [line for line in open('./hightemp.txt')]

# スライスおさらい
# 負の数与えると末尾からの順番で扱える
print(''.join(lines[-input:]))

# 確認用コマンド
# $ tail ./hightemp.txt -n
