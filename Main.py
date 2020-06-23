#yapan kişi : Yiğit Kağan Kılıç

import time as t
import fonk as f

print("phyton ile yazılmış basit konsol sistemine hoşgeldiniz")

print("yükleniyor...")
t.sleep(2.5)

ka = str(input("Kullanıcı adınızı giriniz : "))
oka = str(input("kullanıcı adınızı onaylayınız : "))

s = str(input("Şifrenizi giriniz : "))
os = str(input("Şifrenizi onaylayınız : "))

while(True):

    if ka != oka:
        print("kullanıcı adı onayı başarısız Lütfen tekrar deneyiniz")
        continue

    elif s != os:
        print("Şifre onayınız başarısız lütfen tekrar deneyiniz")
        continue

    elif ka != oka and s != os:
        print("tekrar deneyin")
        continue
    elif ka == oka and s == os:
        print("yükleniyor...")
        t.sleep(3)

        while(True):
            komut = str(input(ka + ">>"))
            if komut == "selam":
                print("selam")
                continue

            elif komut == "bitir":
                print("Sistem kapatılıyor...")
                t.sleep(3)
                break

            elif komut == "dosya olustur":
                dadi = str(input("dosyanın adı ve uzantısını giriniz : "))
                open(dadi,"a")
                continue

            elif komut == "dosya yaz":
                giris = input("Dosyaya ne yazacaksınız : ")
                dadi.write(giris)

            elif komut == "dosya oku":
                try:
                    dosyaadi = str(input("dosyanın adı ve uzantısını giriniz : "))
                    open(dosyaadi,"r")

                except(FileNotFoundError):
                    print("dosya bulunamadı")

                finally:
                    continue

            elif komut == "topla":
                a = int(input("bir sayı giriniz : "))
                b = int(input("ikinci bir sayı giriniz : "))
                f.topla(a,b)
                continue

            elif komut == "cikar":
                c = int(input("bir sayı giriniz : "))
                d = int(input("ikinci bir sayı giriniz : "))
                f.cikar(c,d)
                continue

            elif komut == "carp":
                e =  int(input("bir sayı giriniz : "))
                g = int(input("ikinci bir sayı giriniz : "))
                f.carp(e,g)
                continue

            elif komut == "bol" :
                h = int(input("bir sayı giriniz : "))
                i = int(input("ikinci bir sayı giriniz : "))
                f.bol(h,i)
                continue

            else:
                print("!!!böyle bir komut yoktur!!!")
                continue