import time
import random


def single_player_game(rounds=3):
    print("🎮 体内時間当てゲーム（1人プレイ）")
    total_diff = 0

    for i in range(1, rounds + 1):
        print(f"\n--- {i}回目 ---")
        target = random.randint(5, 15)
        print(f"⏱ これから {target} 秒 数えてください！")
        input("✅ 準備ができたら Enter を押してスタート 🎬")
        start = time.time()
        input("🖐 数え終わったと思ったら Enter を押してストップ ⏹")
        end = time.time()

        elapsed = end - start
        diff = abs(elapsed - target)
        total_diff += diff

        print(f"目標：{target}秒")
        print(f"実際：{elapsed:.2f}秒")
        print(f"誤差：{diff:.2f}秒")

    avg = total_diff / rounds
    print(f"\n✅ 平均誤差：{avg:.2f}秒")

    if avg < 0.5:
        print("🎉 とても正確な体内時計です！")
    elif avg < 1.5:
        print("🙂 なかなか良いです！")
    else:
        print("😅 要練習ですね。")


def player_turn(player_name):
    print(f"\n🎲 {player_name} のターン！")
    target = random.randint(5, 15)
    print(f"⏱ {player_name} さん、これから {target} 秒 数えてください！")
    input("✅ 準備ができたら Enter を押してスタート 🎬")
    start = time.time()
    input("🖐 数え終わったと思ったら Enter を押してストップ⏹")
    end = time.time()

    elapsed = end - start
    diff = abs(elapsed - target)

    print(f"目標：{target}秒")
    print(f"実際：{elapsed:.2f}秒")
    print(f"誤差：{diff:.2f}秒")
    return diff


def two_player_bo_game():
    print("🎮 体内時計ゲーム（2人・BOモード）")

    name1 = input("👤 プレイヤー1の名前：")
    name2 = input("👤 プレイヤー2の名前：")

    while True:
        try:
            bo = int(input("🎯 勝負形式を選んでください（1, 3, 5）: "))
            if bo in [1, 3, 5]:
                break
            else:
                print("⚠️ 1, 3, 5 のいずれかを選んでください。")
        except ValueError:
            print("⚠️ 数字で入力してください。")

    wins_needed = (bo // 2) + 1
    score1 = 0
    score2 = 0
    round_num = 1

    while score1 < wins_needed and score2 < wins_needed:
        print(f"\n🏁 第 {round_num} ラウンド！")
        diff1 = player_turn(name1)
        diff2 = player_turn(name2)

        print(f"\n🧮 結果：")
        print(f"{name1} の誤差：{diff1:.2f}秒")
        print(f"{name2} の誤差：{diff2:.2f}秒")

        if diff1 < diff2:
            print(f"✅ {name1} の勝ち！")
            score1 += 1
        elif diff2 < diff1:
            print(f"✅ {name2} の勝ち！")
            score2 += 1
        else:
            print("🤝 引き分け！このラウンドはノーカウント")
            continue  # 引き分けはラウンド数にカウントしない

        print(f"📊 現在のスコア → {name1}：{score1}勝 ／ {name2}：{score2}勝")
        round_num += 1

    print("\n🎉 最終結果 🎉")
    if score1 > score2:
        print(f"🏆 勝者：{name1}！！")
    else:
        print(f"🏆 勝者：{name2}！！")


def main():
    print("🕹 体内時計ゲームへようこそ！")

    while True:
        mode = input("1人で遊ぶ → 1\n2人で対戦 → 2\n選んでください：")
        if mode == "1":
            single_player_game()
            break
        elif mode == "2":
            two_player_bo_game()
            break
        else:
            print("⚠️ 1 か 2 を入力してください。")


while True:
    main()  # ゲーム本体を呼び出す
    again = input("\n🔁 もう一回プレイしますか？（y/n）：").strip().lower()
    if again != "y":
        print("👋 遊んでくれてありがとう！またね！")
        break
