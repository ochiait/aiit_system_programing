def fb(i):
    return (i % 3 == 0) * "fizz" + (i % 5 == 0) * "buzz"

i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1

'''
＜工夫した箇所＞
・比較演算子'=='が真の時に1を返し、偽の時は0を返す性質を利用した
・なるべく簡潔に、可読性が高くなるよう工夫した
・コーディング規約に合っているか再度見直した
'''