
# Otomatik Kapı Açma Projesi
> Bu Proje herhangi bir elektronik mekanizmayla çalışan kapının röle tetiklemesi ile kolayca açılabilmesi için yapılmıştır.
### Çalışma Prensibi
Sistem kapının çevresine kurulur, yaklaşan kullanıcı wifi alanının içerisine girer ve telefonu otomatik bağlanır. Bağlanma işlemi ile bilikte röle tetiklenir ve kapı kilidi açılır.
## Devre Şeması
![](https://i.hizliresim.com/rr4tz0i.png)

## Kurulum
1. mikrodenetleyici kullanımı destekleyen bir IDE yükleyin 
 -[Thonny](https://thonny.org/)
2. Esp8266 Karta [micropython](https://micropython.org/download/esp8266/) .bin dosyasını yazdırın.
3. [boot.py](https://github.com/nerawn/Automatic-Door-Opener/blob/main/boot.py) Dosyasını karta kaydedin ve cihazın üzerindeki RST Butonuna bir kez basın.

![](https://github.com/nerawn/Automatic-Door-Opener/blob/main/giphy.gif)


## Uygulama
STL Klasörü içersindeki dosyaları 3D yazıcı ile üretebilirsiniz. İçerikte 2 Röle kartı için tasarlanmış fakat tekli röle kartı için de uygun.
>Tasarım,sadece Esp8266 cp2102 modeli için uygundur.

![](https://github.com/nerawn/Automatic-Door-Opener/blob/main/project.jpg)
