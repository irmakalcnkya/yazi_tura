import random

print("Yazı mı Tura mı? (yazı/tura)")
seçim = input("Seçiminizi yapın: ").lower()

sonuç = random.choice(["yazı", "tura"])

print("Zar atılıyor...")
print("Sonuç:", sonuç)

if seçim == sonuç:
    print("Tebrikler! Doğru tahmin ettiniz ")
else:
    print("Üzgünüm, yanlış tahmin ")
