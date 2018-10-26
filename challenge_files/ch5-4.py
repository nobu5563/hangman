my_dic = {"height": "176cm",
          "age": "22",
          "weight": "58",
          }

key = input("言葉を入力してください：")

if key in my_dic:
    info = my_dic[key]
    print(info)
else:
    print("見つかりません。")