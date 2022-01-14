<img src="images/kapak.jpg"/>

# Association Rule Learning için uygulama kodudur. Daha fazla bilgi ve teorik anlatımına [**Medium Yazısı**](https://medium.com/@alper.tml/öneri-sistemleri-association-rule-learning-1f2e59d086ba) tıklayarak ulaşabilirsiniz.

# Repository Hakkında

Veri olarak online olarak hediyelik eşyalar satan İngiltere'de bulunan bir mağazanın 01/12/2009 - 09/12/2011 arasındaki satışlarını kullanıyoruz.
Bu veri setiyle birlikte müşterilerin geçmiş davranışları ve tercihlerinden yola çıkarak, Öneri sistemlerinin tekniklerinden biri olan Association Rule Learning(Birliktelik Kural Öğrenimi) ile müşterinin sepetine eklediği ürüne göre önerilerde bulunuyoruz. Önerilen bu ürünü alması içinde hangi pazarlama stratejilerini uygulamalıyız, hangi aksiyonları almalıyız gibi bir çok konuyu gerçekleştirebiliyor hale geliyoruz.
Medium yazısı üzerinde Association Rule Learning nedir, nasıl uygulanır, gibi bir çok bilgi baştan sona her şey detaylı şekilde anlatılmıştır.
Sorularınız olursa iletişim adresimden bana ulaşabilirsiniz. İyi çalışmalar.

# Veri

- online_retail_II.xlsx - [**Data source**](https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)

# Veri Detayı

- InvoiceNo: Fatura numarası. Her işleme yani faturaya ait eşsiz numara. Eğer bu kod C ile başlıyorsa işlemin iptal edildiğini ifade eder.
- StockCode: Ürün kodu. Her bir ürün için eşsiz numara.
- Description: Ürün ismi
- Quantity: Ürün adedi. Faturalardaki ürünlerden kaçar tane satıldığını ifade etmektedir.
- InvoiceDate: Fatura tarihi ve zamanı.
- UnitPrice: Ürün fiyatı (Sterlin cinsinden)
- CustomerID: Eşsiz müşteri numarası
- Country: Ülke ismi. Müşterinin yaşadığı ülke.

# Kütüphaneler

- pandas
- numpy
- mlxtend

# Yazar

- Alper Temel [Author](https://github.com/alpertml)

# İletişim

• tml.alper@gmail.com
