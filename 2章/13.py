# とりあえず読み込み
col1 = [line for line in open('./col1.txt')]
col2 = [line for line in open('./col2.txt')]

new_file = open('./new_file.txt','w')

# zipで２つのリストを連結して処理
# 2つのリストをタブで連結、改行コードを削除を１行として
# 最後に改行いれて次の行へ
for col in zip(col1, col2):
    new_file.write('\t'.join(col).replace('\n',''))
    new_file.write('\n')

# 確認用コマンド
# $ paste ./col1.txt ./col2.txt
