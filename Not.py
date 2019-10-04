ab = int(input("B1 Kuru Ortalamanız:"))
if ab >= 80:
    print("Geçme Notu 55 Olarak Hesaplanacaktır")
    cevap1 = input("Kabul Ediyor Musunuz? (Evet veya Hayır Olarak Cevaplayınız):")
    if cevap1 == "Evet":
        z = 55
    elif cevap1 == "Hayır":
        z = int (input("Geçme Notu Kaç Olsun:"))

elif ab <= 80:
    z = 65


# Watlar: Z = Geçme Notu
a = float(input("Wat 1:"))
b = float(input("Wat 2:"))
c = float(input("Wat 3:"))
d = float(input("Wat 4:"))
e = float(input("Wat 5:"))
# Writing:
f = float(input("Writing 1:"))
g = float(input("Writing 2:"))
# Collab
h = float(input("Collabrative Task:"))
# English Central
i = float(input("English Central Ortalamaniz:"))
# Midterm
j = float(input("Midterm:"))
# Speaking
k = float(input("Speaking:"))
# Wat Ortalamasi:
l = ((a + b + c + d + e) / 5)
# Writing Ortalamasi:
m = ((f + g) / 2)
# Eomsuz Ortalama:
eomsuz = (m * 10 / 100 + l * 15 / 100 + h * 5 / 100 + i * 5 / 100 + j * 20 / 100 + k * 10 / 100)
# Temel islem:
n = (100 * (z - (m * 10 / 100 + l * 15 / 100 + h * 5 / 100 + i * 5 / 100 + j * 20 / 100 + k * 10 / 100))) / 35

Ortalamalar = [l, m, eomsuz]

print("================================================")

print("Wat Ortalamanız:{}\nWriting Ortalamanız:{}\nE.O.M'suz Ortalamanız:{}".format(Ortalamalar[0], Ortalamalar[1],
                                                                                    Ortalamalar[2]))

if eomsuz <= z:
    print("End Of Moduleden Alman Gereken %s 'dir" % int(n))

elif eomsuz >= z:
    print("End Of Module Girmenize Gerek Yoktur")



print("Created By Yunus Elci")

print("================================================")




