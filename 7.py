dramas = ["ウォーキング・デッド", "アントラージュ", "サ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for drama in dramas:
    print(drama)

#for i in range(25, 51):
    #print(i)
    
for i, drama in enumerate(dramas):
    print(i, drama)

answer = [2, 43, 26, 86, 31, 56, 67, 98, 15, 77]
while True:
    a = input("1から100までの数字を一つ入力してください。やめたい場合はqを入力してください:")
    if a == "q":
        break
    try:
        a = int(a)
    except ValueError:
            print("数字を入力するか、qで終了します。")
            continue
    if a in answer:
        print("正解です！")
    else:
        print("不正解です!")
        

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
b = []
for i in list1:
    for j in list2:
        b.append(i * j)

print(b)
