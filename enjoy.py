age = input("お前の年齢を入力しろ！")
if int(age) <= 17:
    print("未成年です。")
elif int(age) <= 64 :
    print("成人です。")
else:
    print("高齢者です。")