# input()で標準入力受け付けれる
# int()でinteger型に変換
input_num = int(input())

lines = [line for line in open('./hightemp.txt')]

print(''.join(lines[:input_num]))


# 確認用コマンド
# $ head ./hightemp.txt -n
