import random

def yazitura_oyunu():
    print("Yazı Tura Oyununa Hoşgeldiniz!")
    oyuncu_adi = input("Adınızı Giriniz: ")

    tur_sayisi = int(input("Kaç tur oynamak istersiniz? "))
    puan = 0
    geçmiş = []

    for tur in range(1, tur_sayisi + 1):
        print(f"\n-- {tur}. Tur ---")
        tahmin = input("Yazı mı Tura mı? ").lower()
        sonuc = random.choice(["yazı", "tura"])

        if tahmin == sonuc:
            print(f"Doğru! Bilgisayar da '{sonuc}' dedi.")
            puan += 1
            durum = "Doğru"
        else:
            print(f"Yanlış! Bilgisayar '{sonuc}' dedi.")
            durum = "Yanlış"

        geçmiş.append({
            "tur": tur,
            "tahmin": tahmin,
            "bilgisayar": sonuc,
            "sonuc": durum
        })

    print(f"\nOyun bitti, {oyuncu_adi}!")
    print(f"Toplam Puan: {puan} / {tur_sayisi}")
    print("\nOyun Geçmişi:")
    for kayit in geçmiş:
        print(f"{kayit['tur']}. Tur: Sen -> {kayit['tahmin']} | Bilgisayar -> {kayit['bilgisayar']} | Sonuç: {kayit['sonuc']}")

if __name__ == "__main__":
    yazitura_oyunu()
    
