
# リスト内包表記使ってみる
num_lines = len([line for line in open('./hightemp.txt')])
print(num_lines)

# 結果確認用
import subprocess
output = subprocess.check_output(['wc','-l','./hightemp.txt'])
print(output)
