# リスト内包表記で各行をタブでスライスして、１列目と２列目をリスト化
col1 = [line.split('\t')[0] for line in open('./hightemp.txt')]
col2 = [line.split('\t')[1] for line in open('./hightemp.txt')]

# 書き込みモードでファイルオープン
f1 = open('./col1.txt','w')
f2 = open('./col2.txt','w')

# 改行コードでjoin
f1.write('\n'.join(col1))
f2.write('\n'.join(col2))

# 確認用コマンド
# $ cat ./hightemp.txt  | cut -f 1
# $ cat ./hightemp.txt  | cut -f 2
