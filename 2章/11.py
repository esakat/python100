# リスト内包表記で各行のタブを１文字スペースに変換
space_text = [line.expandtabs(1) for line in open('./hightemp.txt')]

# python3からのprint関数では第２引数にend=""で""内の文字を終端文字として扱える
# end=""だと改行なしとなる
print(''.join(space_text),end='')

# 確認用コマンド
# $ cat ./hightemp.txt | tr '\t' ' '
