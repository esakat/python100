import re # 正規表現の利用
from collections import defaultdict # 文字数カウント用

string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# ,と.を削除後に単語でリスト化
words_list = re.sub('[,.]','',string).split()

# カウンターの初期化
counter = defaultdict(int)

# 先頭の単語・文字からカウントしていく
for word in words_list:
	for c in word:
		counter[c] += 1

# 辞書型なので(文字,カウント数)のタプルリスト型に変換
count_list = dict(counter).items()

print(count_list)
