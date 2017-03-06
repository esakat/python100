import re # 正規表現の利用

# シーケンスとして文字列とリスト用意
X = "paraparaparadise"
Y = "paragraph"

# n-gram関数 05の再利用
def n_gram(n,sequence):

    ngram = []

    if isinstance(sequence, str):
        sequence = list(re.sub('[,. ]','',sequence))

    for i in range(len(sequence)-n+1):
        # 05と変えた箇所、リスト内リストだと後述のset型に変換できなかったので
        # タプル型に変換処理を入れている
        ngram.append(tuple(sequence[i:i+n]))

    return ngram

# X,Y のbi-gram作成
# 集合計算のためにset型で定義
X = set(n_gram(2,X))
Y = set(n_gram(2,Y))

# 和集合
print(X | Y)
# 積集合
print(X & Y)
# 差集合
print(X - Y)
print(Y - X)
# 'se'が含まれるかチェック
if ('s','e') in X & Y:
    print("'se'はX及びYに含まれます")
else:
    print("'se'はXもしくはYに含まれていません")
