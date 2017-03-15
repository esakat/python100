# リスト内包表記で各行のタブを１文字スペースに変換
space_text = [line.expandtabs(1) for line in open('./hightemp.txt')]
[print(line) for line in space_text]

# 確認用コマンド
# $ cat ./hightemp.txt | tr '\t' ' '
