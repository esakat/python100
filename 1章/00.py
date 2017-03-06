string = "stressed"
print(string[::-1])
# スライスで実装
# string[開始位置:終了位置:ステップ数]
# 開始、終了位置は負の数指定で末尾から数える
# 以下のようにもできる
print(string[-1::-1])
