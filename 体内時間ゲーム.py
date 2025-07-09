import time
import random


def body_clock_game(rounds=3):  # 体内時間ゲームの処理をまとめた関数
    # print("🎮 体内時間当てゲーム（全{}回）".format(rounds))
    print(f"🎮 体内時間当てゲーム（全{rounds}回）")
    total_diff = 0
    for i in range(1, rounds + 1):
        # print("\n--- {}回目 ---".format(i))
        print(f"--- {i}回目 ---")
        target = random.randint(5, 15)
        print(f"目標時間: {target}秒です。")
        input(f"{target}秒経ったと思ったら Enter を押してください\nEnterキーでスタート")
        start = time.time()
        input()
        end = time.time()

        elapsed = end - start
        diff = abs(elapsed - target)
        total_diff += diff

        # print("経過時間：{:.2f}秒".format(elapsed))
        # print("差：{:.2f}秒".format(diff))
        print(f"目標: {target}秒")
        print(f"経過時間：{elapsed:.2f}秒")
        print(f"差：{diff:.2f}秒")

    avg_diff = total_diff / rounds
    print("\n✅ 全体の平均誤差：{:.2f}秒".format(avg_diff))

    if avg_diff < 0.5:
        print("🎉 とても正確な体内時計です！")
    elif avg_diff < 1.5:
        print("🙂 なかなか良いです！")
    else:
        print("😅 要練習ですね。")


body_clock_game()
