import random
while True:
    number = random.randint(1,100)
    b = 4
    c = 0
    print("数当てゲーム！数字を入力して当ててください。チャンスは5回です。")
    for i in range(5):
         a = int(input())
         c += 1
         if number == int(a):
            print("正解です。")
            print(f"{c}回でクリアしました")
            break
         elif a > number+20:
            print(f"不正解!答えよりかなり大きいです。あと{b}回試せます。")
         elif a < number-20:
             print(f"不正解!答えよりかなり小さいです。あと{b}回試せます。")
         elif a < number:
             print(f"不正解!答えより小さいです。あと{b}回試せます。")
         elif a > number:
             print(f"不正解!答えより大きいです。あと{b}回試せます。")
         b -= 1
    print(f"答えは{number}です。")
    d = input("もう1度プレイする場合は'yes'を終了する場合は'no'を入力してください")
    if d == "no":
        print("終わります。ありがとうございました!")
        break



#a = int(input())
#b = 0
#for i in range(5):
    #if number == a:
        #print("正解")
       # break
    #else:
        #print("不正解")
    
#print(f"答えは{number}です")
#while number == a or b == 5:
    #a = int(input())
    #if number == a:


