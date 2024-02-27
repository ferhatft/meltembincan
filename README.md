# Ferhat Tuğrul

## Kurulum

Projenin çalışması için aşağıdaki adımları izleyin.

### Gereksinimlerin Kurulması

Proje bağımlılıklarını yüklemek için aşağıdaki komutu kullanın:

```bash  
pip install -r requirements.txt
```

### Veritabanı Ayarları

Veritabanı ayarlarını `settings.py` dosyasında yapılandırın. Örneğin, PostgreSQL kullanmak istiyorsanız:


```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Migrasyonlar

Veritabanı tablolarını oluşturmak için aşağıdaki komutları sırasıyla çalıştırın:

```python
python manage.py makemigrations
python manage.py migrate

```

## Katkıda Bulunma

1. Bu depoyu (`fork`) edin.
2. Yeni bir özellik dalı (`branch`) oluşturun: `git checkout -b yeni-özellik`
3. Değişikliklerinizi yapın ve bunları (`commit`) ile işaretleyin: `git commit -am 'Yeni özellik ekle'`
4. Dalınızı ana depoya (`remote`) gönderin: `git push origin yeni-özellik`
5. Bir Birleştirme İsteği (`Pull Request`) gönderin.
