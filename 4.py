





def df(x=24, y=2, z):
    """
    3つの引数をプラスする
    """

    return x + y + z

print(df(234))

def dv(x):
    """"
    受け取った引数を2で割る
    """
    return x / 2

def add(x):
    """
    受け取った引数に4を掛ける
    """
    return x * 4

z1 = dv(8)
print(add(z1))

def ette(x):
    """
    #引数をfloat型にして返す。
    #引数が数値でない場合は例外を表示
    """
    try:
        return float(x)
    except ValueError:
        print("数字を入力してください。")

print(ette("すうじ"))

