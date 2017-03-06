import re # 正規表現の利用

elements = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
mono_words = [1, 5, 6, 7, 8, 9, 15, 16, 19]
shortened_elements = {}

# .を削除後に単語でリスト化
elements_list = elements.replace('.','').split()

# 元素単語リストを1つずつ探査しながら
# 定義しておいた1文字表現かどうかのチェック
# 元素の辞書に省略元素名と先頭から何番目かを入れる
# enumerate使えばイテレータ取得できる
for i,e in enumerate(elements_list):
    count = i + 1
    if(count in mono_words):
        shortened_elements[e[:1]] = count
    else:
        shortened_elements[e[:2]] = count

print(shortened_elements)
