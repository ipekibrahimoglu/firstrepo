# -- Trakya Ünviersitesi, Bilgisayar Mühendisliği Bölümü, Programlama Dillerine Giriş Dersi --
# Bir iskmabil destesinin 4 oyuncuya rastgele dağıtılması ve Batak (Spades) oyunu için temel
# kuralların tanımlı olduğu bir program kodu verilmiştir. Oyunu oynamamış olan öğrenciler
# çeşitli internet sitelerinden veya videolardan kuralları öğrenebilirler.

# Program kodunun aşağıdaki yönlerden eksiklerinin öğrenciler tarafından giderilmesi beklenmektedir:
# + Bu kodda sadece 1 tur oynanmaktadır. Önceden belirlenen sayıda tur adedi ile oynanması sağlanmalıdır.
# + Her oyuncunun tur başında kaç el alacağını tahmin etmesi eklenmelidir. Bu 3 farklı şekilde yapılabilir:
#   1) Her oyuncu için rastgele belirlenebilir (mantıklı değil)
#   2) Oyuncunun kartlarına göre bilgisayar karar vermeye çalışabilir (yapması zor)
#   3) Kullanıcı her oyuncu için bu değeri girebilir (yapması kolay)
# + Puanlama sistemi eklenmeli ve her tur sonunda güncel puan tablosu gösterilmelidir:
#   - Oyuncu tahmin ettiği eli alırsa "tahmin x 10" puan kazanır (3 tahmin edip tam 3 el almışsa 30 puan)
#   - Fazladan aldığı her el için 1 puan eklenir (3 tahmin edip 5 aldıysa: 32)
#   - Tahmininden az el alırsa "tahmin x 10" puan kaybeder (3 tahmin edip 2 aldıysa: -30)
# + Oyuncular bu kodda genel olarak elindeki o tipten en büyük kartı atmaktadır (sadece Maça kartını bir koz
#   olarak kullanacağı zaman en küçüğünü atmaktadır). Çoğu durumda bu mantıklı bir seçim değildir (Kod içinde
#   bununla ilgili bir NOT yazılmıştır). Oyuncuların daha mantıklı kart atmaları için kontroller eklenmelidir.





def kart_önerisi (benim_kartlarim, yerdeki_kartlar):#tekrarı olacak durumlar için fonksiyon

    kart_bilgisi = {'♠': False, '♣': False, '♥': False, '♦': False} #hata vermemesi için başta değer atandı
    kart_sayisi_el = {'♠': 0, '♣': 0, '♥': 0, '♦': 0}
    kart_sayisi_yer = {'♠': 0, '♣': 0, '♥': 0, '♦': 0} #kart sayısı bizde tek, yerde (atılmış olan) çok olan durum için (aynı kart tipi)

    a_yerdemi = kart_bilgisi.copy() #orijinal liste değişmeden kopya alındı
    k_bendemi = kart_bilgisi.copy()

    
    for eldeki_kart_tipi in benim_kartlarim:# Elimizdeki tüm kart tipleri dıştaki döngüde, yerdeki kart tipleri için içteki döngüde kontrol edilir

        kart_sayisi_el[eldeki_kart_tipi] = len(benim_kartlarim[eldeki_kart_tipi])

        for kart in yerdeki_kartlar:

            tip_yer = kart[1] # yerdeki kartlar listesine tek tek oyuncu_kartlar append edildi. her oyuncu_karttaki 1 indisli kart tipi tip_yere 
            numara_yer = kart[2]# atandı. 2 indisli kart numarası, yerdeki kartlardan olduğu için numara_yer e atandı.

            if tip_yer != eldeki_kart_tipi:# eldeki kart tipi ve yerdeki tip eşit değilse aramaya devam eder, eşitse aşağı devam eder.
                continue

            kart_sayisi_yer[eldeki_kart_tipi] += 1 # (elimizde ve önceki kartlarda yere atılan tip aynı) kart_sayısı o tipte 1 artırılır

            
            if numara_yer == 'A':# yerdeki kart as ise
                a_yerdemi[tip_yer] = True #yerde as olmasına true verir
                continue   # kod yorumunda önerilen K ve A durumu için
            
        
    for eldeki_kart_tipi in benim_kartlarim:#benim_kartlarım her seferinde oyunuclar[oyuncu] ile çağrılır bu da 4 kart tipinin key olduğu ve bu key lerin value ları onlan
        
        for kart in benim_kartlarim[eldeki_kart_tipi]:#bir sözlük olur.Eldeki_kart_tipi her bir key e ulaşır.Kart ise o key in değerlerini dolaşır 1,2,K...
            
            if kart == 'K':#eğer oyuncuda yukarda bahsettiğim kısımda K varsa k bende demek için k_bendemi de false olan value değerini true yapar
                k_bendemi[eldeki_kart_tipi] = True

   

    for eldeki_kart_tipi in benim_kartlarim:

        if eldeki_kart_tipi == '♠': 
            continue


        if (k_bendemi[eldeki_kart_tipi] and a_yerdemi[eldeki_kart_tipi]): # her iki değer de true is durum gerçekleşmiş ve yerde aynı tip kartın ası oyuncuda papzazı vardır
            return eldeki_kart_tipi, 'K' # bu durumda önerilen , return edilen kart papaz olur




        if kart_sayisi_el[eldeki_kart_tipi] == 1 and kart_sayisi_yer[eldeki_kart_tipi] <= 4 and kart_sayisi_el['♠'] >= 0:
            print( eldeki_kart_tipi)
            print("yukarıdaki karttan oyuncuda 1 tane var, atılmış halde 4 veya daha az var ve oyuncuda koz var") #bu kozu kullanmak için bir strateji olabilir
            return eldeki_kart_tipi, benim_kartlarim[eldeki_kart_tipi][0] #zaten elimizde 1 tane var bu kart tipinden

    return None, None #eğer durum gerçekleşmemişse atacagim kart ve atacagim kart numarası için ayrı ayrı none verir

import random
A = ['♠', '♣', '♥', '♦']
B = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for k in range(int(input(" tur sayısı giriniz : "))):

    deste = []
    for i in A:
        for j in B:
            deste.append(i+j)


    el_tahmini = {} #oyuncuların oyun başlamadan yaptıkları tahminleri tutar
    yerdeki_kartlar = []

    oyuncular = {}
    oyuncu_sira = []
    for i in range(4):
        girilen_isim = input("Oyuncu " + str(i+1) + ": ")
        oyuncular.setdefault( girilen_isim , {}.fromkeys(A))
        girilen_tahmin = int(input( girilen_isim + " için el tahminini giriniz : "))
        el_tahmini.setdefault( girilen_isim , girilen_tahmin )
    for oyuncu in oyuncular:
        oyuncu_sira.append(oyuncu)
        for i in A:
            oyuncular[oyuncu][i] = []
        for i in range(13):
            kart = random.choice(deste)
            oyuncular[oyuncu][kart[0]].append(kart[1:])
            deste.remove(kart)

    print("\nDAĞITILAN KARTLAR:")
    for oyuncu in oyuncular:
        print(oyuncu + ":")
        for karttip in oyuncular[oyuncu]:
            oyuncular[oyuncu][karttip].sort(key=B.index)  # kartlar B listesindeki sıraya göre dizilir
            print(karttip, oyuncular[oyuncu][karttip])

    print("\nOYUN BAŞLADI...")  # Oyun sadece 1 tur (13 el) oynanacak
    oyun_skor = dict()
    macaAtildi = False
    sira = random.randrange(4)  # oyuna başlayacak oyuncu rastgele belirleniyor
    for el in range(13):  # 13 el oynanacak
        print(str(el+1) + ". el:")
        oynayan = 0
        oynanan_kartlar = []  # bu liste içine kimin hangi kartı attığı yazılacak
        while oynayan < 4:
            oyuncu = oyuncu_sira[sira]
            if oynayan == 0:  # ilk kart atacak oyuncu ise kart tipi belirlenecek (rastgele)
                while True:
                    if macaAtildi:  # Maça önceki bir elde koz olarak kullanıldı ise oyuncu Maça ile başlayabilir
                        kart_tipi = random.choice(A)
                    else:  # Maça önceki bir elde koz olarak kullanılmadı ise diğer üç kart tipinden atabilir
                        kart_tipi = random.choice(A[1:])
                    if len(oyuncular[oyuncu_sira[sira]][kart_tipi]):  # o tipte kartı yoksa döngü devam edecek
                        break

                
                # oyuncu lehine bir durum bulamazsa None döner ve en büyük kartın atılması devam eder
                # lehimize olacak bir durum bulursa oynanacak kartı döner
                atacagim_kart_tipi, atacagim_kart_numarasi = kart_önerisi (oyuncular[oyuncu], yerdeki_kartlar)
                # kart_önerisi  fonksiyonu oyuncu yerine bazı mantıklı kararlar verir
                if atacagim_kart_tipi is not None : # fonksiyondakine uygun duurum bulunur ise return değerini kullanacak
                    for kart_numarasi in oyuncular[oyuncu][atacagim_kart_tipi]:
                        if kart_numarasi == atacagim_kart_numarasi:
                            break
                    oyuncu_kart = (oyuncu, atacagim_kart_tipi, oyuncular[oyuncu][atacagim_kart_tipi].pop(oyuncular[oyuncu][atacagim_kart_tipi].index(kart_numarasi)))
                    yerdeki_kartlar.append(oyuncu_kart)
                else: #yazılan durumlara girmezse kod aynen devam eder
                    oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())  # o tipteki en büyük kartı atıyor
                    yerdeki_kartlar.append(oyuncu_kart)

                # NOT: Oyuncunun o tipteki en büyük kartı atması çoğu durumda mantıklı değil. Rastgele olarak seçilmesi veya
                # en küçüğü atmak da mantıklı olmaz. Oyuncunun mantıklı bir kart atmasını sağlamak için birçok ilave kontrol
                # eklenmesi gerekir (Önceki bir elde 'A' çıktı ise 'K' ile başlamak mantıklı olabilir vb.). Bu programda o 
                # elin ilk kartı atılırken de, sonraki kartlar için de mantıklı olmasına yönelik kontroller bulunmamaktadır.
            else:  # diğer oyuncular ilk oyuncunun belirlediği kart tipinde kart atacak
                if len(oyuncular[oyuncu][kart_tipi]):  # o kart tipinde kartı varsa en büyük olanı atacak
                    oyuncu_kart = (oyuncu, kart_tipi, oyuncular[oyuncu][kart_tipi].pop())
                    yerdeki_kartlar.append(oyuncu_kart)
                elif len(oyuncular[oyuncu]['♠']):  # o kart tipinde kartı yoksa en küçük maça kartını atacak
                    oyuncu_kart = (oyuncu, '♠', oyuncular[oyuncu]['♠'].pop(0))
                    yerdeki_kartlar.append(oyuncu_kart)
                    macaAtildi = True  # Maça koz olarak oynandığı için sonraki ellerde doğrudan Maça atılabilecek
                else:  # maça kartı da yoksa, diğer tiplerin birinden en küçük kartı atacak
                    kart_tipleri = A[1:].copy()  # maça hariç diğer 3 kart tipi kopyalandı
                    for tip in kart_tipleri:
                        if len(oyuncular[oyuncu][tip]):
                            oyuncu_kart = (oyuncu, tip, oyuncular[oyuncu][tip].pop(0))
                            yerdeki_kartlar.append(oyuncu_kart)
                            break
            print(oyuncu_kart[0], oyuncu_kart[1] + oyuncu_kart[2])
            oynanan_kartlar.append(oyuncu_kart)
            oynayan += 1
            sira += 1
            if sira >= 4:
                sira -= 4
        # atılan 4 karta göre eli kazananı bulma:
        en_buyuk = oynanan_kartlar[0]   # ilk atılanı en büyük kart kabul et
        for kart in oynanan_kartlar[1:]:
            if kart[1] == en_buyuk[1] and B.index(kart[2]) > B.index(en_buyuk[2]):
                en_buyuk = kart  # en büyük ile aynı kart tipinde daha büyük atıldı ise en büyük kart kabul et
            elif en_buyuk[1] != '♠' and kart[1] == '♠':
                en_buyuk = kart  # en büyük maça değilken maça atıldı ise en büyük kart kabul et
        print("eli kazanan:", en_buyuk[0])
        sira = oyuncu_sira.index(en_buyuk[0])
        oyun_skor[en_buyuk[0]] = oyun_skor.setdefault(en_buyuk[0], 0) + 1

    for i in oyun_skor:
        if oyun_skor[i] == 0:
            print( i + " skoru 0. ")

    print("SKOR:", oyun_skor)  # oyuncuların kaçar el adığını gösterir (gerçek kurallara göre bir puanlama sistemi yok)
    puan_listesi = {}

    for i in oyun_skor: #oyuncuların el tahminleri ve skor bilgileri ile puan hesaplayan kısım
        if el_tahmini.get(i) == oyun_skor[i]:
            puan_listesi.setdefault(i,el_tahmini[i]*10)
        elif oyun_skor[i] == 0:
            puan_listesi.setdefault(i , el_tahmini[i] *10 * (-1))
        elif el_tahmini.get(i) > oyun_skor[i]:
            puan_listesi.setdefault(i,((-1)* 10 * el_tahmini[i]))
        else:
            puan_listesi.setdefault(i, (oyun_skor[i] - el_tahmini[i]) * 1 + el_tahmini[i] * 10)

    print("el tahmini : " ,el_tahmini)
    print("puanlar : " ,puan_listesi)
    



