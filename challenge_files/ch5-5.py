musician = {"BTS": "Not today",
            "TWICE": "BDZ",
            "Red Velvet": "Russian Roulette"
            }

key = input("言葉を入力してください：")

if key in musician:
    song = musician[key]
    print(song)
else:
    print("見つかりません。")