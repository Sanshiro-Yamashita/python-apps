import time
import random 
import math
while True:
    li = []
    n = random.randint(5,15)
    print("反射神経テストを始めます。　! ! ! ! !　と表示されたらEnterを押して下さい。")
    time.sleep(n)
    print("! ! ! ! !")
    start_time = time.time()
    input()
    end_time = time.time()
    k = end_time - start_time
    k = math.floor(k * 10000) / 10000
    li.append(k)
    if k < 0.01:
        print("早すぎです。連打などは不正になります。")
    else:
        print(f"あなたの反応速度は{k}秒です。")
    d = input("もう1度プレイする場合は'yes'を終了する場合は'no'を入力してください")
    if d == "no":
        z = min(li)
        print(f"最高記録は{z}秒でした。")
        print("終わります。ありがとうございました!")
        break