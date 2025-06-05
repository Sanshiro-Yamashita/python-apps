import time
import random 
import math
n = random.randint(5,15)
print("反射神経テストを始めます。　! ! ! ! !　と表示されたらEnterを押して下さい。")
time.sleep(n)
print("! ! ! ! !")
start_time = time.time()
input()
end_time = time.time()
k = end_time - start_time
k = math.floor(k * 10000) / 10000
if k < 0.01:
    print("早すぎです。連打などは不正になります。")
else:
    print(f"あなたの反応速度は{k}秒です。")


