import re # 正規表現の利用

# シーケンスとして文字列とリスト用意
sentence_string = "I am an NLPer"
sentence_list = sentence_string.split()

# 数字nとシーケンスを引数にするn-gram関数
def n_gram(n,sequence):

    # 返り値用のリスト
    ngram = []

    # 文字列、リストで共通処理にするために
    # 文字列が引数に与えられた場合は1文字ごとのリストに変換
    # ,と.とスペースを削除
    if isinstance(sequence, str):
        sequence = list(re.sub('[,. ]','',sequence))

    # n-gram作成処理
    # for文でiの位置+引数のnをスライスする
    # forの終了はリスト長からnを引いて1足した箇所まで
    for i in range(len(sequence)-n+1):
        ngram.append(sequence[i:i+n])

    return ngram

# 単語bi-gram
print(n_gram(2,sentence_list))
# 文字bi-gram
print(n_gram(2,sentence_string))
