# 🎁 Instagram Çekiliş App

Bu proje, **Streamlit** ve **Selenium** kullanarak Instagram Reels gönderilerindeki yorum yapan kullanıcıları çekip, bu kullanıcılar arasında rastgele çekiliş yapmanızı sağlayan bir web uygulamasıdır.

## Özellikler

- Belirtilen bir Instagram Reels linkinden, giriş yaptıktan sonra yorum yapan kullanıcıların listesini otomatik olarak çeker.
- Kullanıcı arayüzü ile çekilişe katılan kullanıcıları görüntüleyebilirsiniz.
- Rastgele çekiliş yapıp kazanan(lar)ı belirleyebilirsiniz.
- Kullanıcı dostu ve modern bir arayüz ile kolay kullanım.

## Gereksinimler

- Python 3.8+
- [Google Chrome](https://www.google.com/chrome/) yüklü olmalı
- [ChromeDriver](https://chromedriver.chromium.org/downloads) uygun sürümde yüklü olmalı (Python betiği ile aynı dizinde olması önerilir)

### Python Paketleri

- streamlit
- selenium

Kurulum için:

```bash
pip install streamlit selenium
```

> **Not:** `chromedriver`'ın sistem PATH'inde veya proje dizininde olması gerekir.

## Kullanım

1. Projeyi klonlayın veya dosyanızı kaydedin.
2. `chromedriver` dosyasını proje dizinine ekleyin.
3. Uygulamayı başlatın:

   ```bash
   streamlit run insta_draw.py
   ```

4. Tarayıcıda açılan arayüzde:
    - **Reels Linki:** Yorumcuları çekmek istediğiniz Instagram Reels gönderisinin linkini girin.
    - **Instagram Kullanıcı Adı & Şifre:** Giriş bilgilerinizle oturum açın. (Şifreniz güvenli şekilde kullanılır, paylaşılmaz ancak Instagram'ın güvenlik politikalarına dikkat ediniz.)
    - **Yorumcuları Çek** butonuna tıklayın.
    - Yorum yapan kullanıcılar listelenir.
    - Çekiliş bölümünden kazanan sayısını seçin ve **Kazananları Belirle** butonuna tıklayın.
    - Kazananlar listelenir ve kutlama animasyonu gösterilir.



## Uyarılar

- Instagram, üçüncü parti otomasyonlara karşı sınırlamalar getirebilir. Hesabınızın güvenliğini riske atacak şekilde kullanmayınız.
- Hesabınızda iki faktörlü kimlik doğrulama (2FA) açıksa, giriş işlemlerinde sorun yaşayabilirsiniz.
- Bu uygulama sadece eğitim ve eğlence amaçlıdır. Hesap güvenliğinizden siz sorumlusunuz.

## Katkı

Sorunlarınız veya katkı yapmak istedikleriniz için [GitHub Issues](https://github.com/your-repo/issues) bölümünü kullanabilirsiniz.

---

**Yasal Uyarı:** Bu uygulama Instagram tarafından desteklenmemektedir veya onaylanmamıştır. Kullanım tamamen sizin sorumluluğunuzdadır.
