import random
import csv
#単語データ
words = {}
with open("words.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        words[row[0]] = row[1]
missed = []
score = 0
while True:
    try:
        num_questions = int(input("問題数を入力してください: "))
        if num_questions > 0:
            break
    except:
        pass
        print("無効な入力です。もう一度入力してください。")
#問題に出す英単語をランダムに選ぶ
asked_words = random.sample(list(words.keys()), min(num_questions, len(words)))
for i, word in enumerate(asked_words):
    #正解の選択肢を入れる
    correct = words[word]
    #間違いの選択肢を選んで入れる
    choices =  list(words.values())
    choices.remove(correct)
    wrong_count = min(3, len(choices))
    wrong = random.sample(choices, wrong_count)
    #選択肢を作る
    options = wrong + [correct]
    random.shuffle(options)

    #問題表示
    print(f"\n--- 問題 {i + 1}/ {len(asked_words)} ---")
    print("単語：", word)

    for j, opt in enumerate(options):
            print(f"{j + 1}. {opt}")

    # 入力
    while True:
        try:
            ans = int(input("番号で教えて"))
            if 1 <= ans <= len(options):
                break
        except ValueError:
            print("無効な入力です。もう一度入力してください。")

    #判定
    if options[ans - 1] == correct:
        print("正解！")
        score += 1
    else:
        if word not in missed:
            missed.append(word)
        print("不正解:", correct)


print(f"最終スコア: {score}/{len(asked_words)}")
print("間違えた単語:")
for w in missed:
    print(w, ":", words[w])