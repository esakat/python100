input = int(input())

lines = [line for line in open('./hightemp.txt')]

sublist = [''.join(lines[i:i+input]) for i in range(0,len(lines),input)]

# python結果確認用
for i in sublist:
    print(i)

# 確認用コマンド
# $ split -l N ./hightemp.txt 
