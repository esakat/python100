string1 = "パトカー"
string2 = "タクシー"
string3 = ""
i = 0
while i < len(string1):
    string3 += string1[i] + string2[i]
    i+=1
print(string3)
# スライスとfor文使って作ってみたが美しくない...
