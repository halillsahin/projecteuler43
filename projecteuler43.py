import itertools

numaralar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tüm_sayılar = list(itertools.permutations(numaralar))
a=[]
for i in tüm_sayılar:
    sayı=int("".join(map(str,i)))
    if int(str(sayı)[1:4])%2==0 and int(str(sayı)[2:5])%3==0 and int(str(sayı)[3:6])%5==0 and int(str(sayı)[4:7])%7==0 and int(str(sayı)[5:8])%11==0 and int(str(sayı)[6:9])%13==0 and int(str(sayı)[7:10])%17==0:
        a.append(sayı)
print(sum(a))