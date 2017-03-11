# input()で標準入力受け付けれる
# int()でinteger型に変換
input = int(input())

lines = [line for line in open('./hightemp.txt')]

print(''.join(lines[:input]))

# 確認用コマンド
# $ head ./hightemp.txt -n
