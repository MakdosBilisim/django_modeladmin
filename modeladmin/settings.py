import os

tarih                              =   "26.01.2019"

### Proje yolu
### Ör: /home/musluyuksektepe/PycharmProjects/modeladmin
### Veritabanı, Static yolu vs.. gibi tanımlamalarda kullanılacak tanımlama
BASE_DIR                           =   os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


########### Models
## Default: {}
### get_absolute_url() geçersiz kılıp yeni url yolu tanımlamak
ABSOLUTE_URL_OVERRIDES             =   {
                                         'kayitlar.kullanicilar': lambda kayit: f'/{kayit.isim}/{kayit.soyisim}/',
                                         'kayitlar.aylar': lambda kayit: f'/{kayit.id}/{kayit.ay_ismi}/',
                                       }


########### Email
## Default: []
### DEBUG=False iken kod hatalarında bilgi verilecek kişi listesi
### LOGGING ve EMAIL ayarları yapılmış olmalı.
ADMINS                             =   [('Muslu', 'muslu.yuksektepe@makdos.com'), ('Murat', 'murat.yuksektepe@makdos.com')]


## Default: []
### HTTP Host Header saldırılarına karşı izin verilen HOST adresleri
### Mutlaka tanımlanmalı
### Ör: ['*'] ['localhost', '192.168.1.35', '[2001:0db8:85a3:0000:0000:8a2e:0370:7334]']
### Ör: ['.alanadi.com'] = ['alanadi.com', 'www.alanadi.com']
### DEBUG=True ve ALLOWED_HOSTS=[] ise ['localhost', '127.0.0.1', '[::1]'] geçerli olur.
ALLOWED_HOSTS                      =   ["*"]


########### URLs
## Default: True
### True ise istek yollarının (Ör: /anasayfa/, /talepformu/, /urunler/ ) sonlarına otomatik / ekler
### True iken istek yolu urls.py dosyalarında eşleşen bir koşul yoksa ve / ile bitmiyorsa aynı istek yolunu / ile bitene eşleştirmeyi dener.
### POST isteklerinde istek yolu / ile biten ile bitmeyen arasında veri kaybı yaşatabilir.
### Aktif olması için Middleware de CommonMiddleware aktif olmalı.
APPEND_SLASH                       =   True


########### AUTH - Kimlik Doğrulama
## Default: 'django.contrib.auth.backends.ModelBackend'
### Kimlik doğrulama için kullanılacak backend sınıf
### https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#writing-an-authentication-backend
AUTHENTICATION_BACKENDS            =   ['django.contrib.auth.backends.ModelBackend']


########### AUTH - Kimlik Doğrulama
## Default: None
"""
UserAttributeSimilarityValidator   = Kullanıcı adı ve parola arasındaki benzerlik
MinimumLengthValidator             = Parolanın olması gereken en az karakter sayısı
CommonPasswordValidator            = Bilinen 20.000 parola ile karşılaştırır.
NumericPasswordValidator           = Parolanın sadece numaralardan oluşup oluşmadığını kontrol eder. 
"""
AUTH_PASSWORD_VALIDATORS           =   [
                                            {
                                                'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
                                            },
                                            {
                                                'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                                                'OPTIONS': {
                                                    'min_length': 9,
                                                }
                                            },
                                            {
                                                'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
                                            },
                                            {
                                                'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
                                            },
                                        ]

########### AUTH - Kimlik Doğrulama
## Default: 'auth.User'
### Kullanıcıları temsil eden tablo.
### Djangonun User tablosu yetmez ise özel bir tablo kullanılabilir. Ör: email hesabı ile giriş yapılması istenirse
### Proje ürün haline gelip yayına açıldıktan sonra değiştirilmemeli
AUTH_USER_MODEL                    =   'auth.User' ###  uyeler.Kullanicilar


########### Security - Güvenlik
## Default: 31449600 (1 Yıl)
### CSRF = XSRF = Siteler Arası İstek Sahtekarlığı
### Oturum açılmış bir siteye dışarıda bir siteden istek yapılarak habersiz şekilde işlem yaptırılması.
### facebook.com da oturum açmış biri yan sekmede kotusite.com daki bir linki tıklayarak facebook.com daki oturumunu sildirebilir ya da habersiz şekilde yazı paylaştırılabilir.
###
### CSRF (Cross Site Request Forgery) çerezin saniye olarak geçerlilik süresi
### Sürenini uzun belirlemenin sebebi, ziyaretçinin tarayıcıyı kapatması veya yer imine koyması ve sonradan önbellekten yüklemesi durumunda sorun çıkmaması
### Internet Explorer gibi bazı tarayıcılar bu kadar uzun süreye izin vermeyebilir. Değeri None yapıp oturum bazlı kayıt tutmak (session) daha iyi olur.
CSRF_COOKIE_AGE                    =   31449600


########### Security - Güvenlik
## Default: None
### CSRF = XSRF = Siteler Arası İstek Sahtekarlığı
### Oturum açılmış bir siteye dışarıdan bir siteden istek yapılarak habersiz şekilde işlem yaptırılması.
### facebook.com da oturum açmış biri yan sekmede kotusite.com daki bir linki tıklayarak facebook.com daki oturumunu sildirebilir ya da habersiz şekilde yazı paylaştırılabilir.
###
### CSRF koruması yapılacak yani projenin kullanıldığı alan adı.
### alanadi.com kullanılınca diğer alt alan adları arasında da istek yapılabilir.
CSRF_COOKIE_DOMAIN                 =   None ## makdos.com


########### Security - Güvenlik
## Default: False
### CSRF = XSRF = Siteler Arası İstek Sahtekarlığı
### Oturum açılmış bir siteye dışarıdan bir siteden istek yapılarak habersiz şekilde işlem yaptırılması.
### facebook.com da oturum açmış biri yan sekmede kotusite.com daki bir linki tıklayarak facebook.com daki oturumunu sildirebilir ya da habersiz şekilde yazı paylaştırılabilir.
###
### True yapılınca HttpOnly bayrağı ekler. Böylelikle çereze javascriptler erişemez.
CSRF_COOKIE_HTTPONLY               =   False


########### Security - Güvenlik
## Default: 'csrftoken'
### CSRF için çerezdeki kimlik doğrulama adı. Çakışmayacak bir isim verilerek değiştirilebilir.
CSRF_COOKIE_NAME                   =   'csrftoken'


########### Security - Güvenlik
## Default: '/'
### Aynı alan adında birden çok proje yayınlanıyor ise kullanışlıdır.
### urls.py de olan bir path yolu olmalıdır.
CSRF_COOKIE_PATH                   =   '/'


########### Security - Güvenlik
## Default: 'Lax'
###
### CSRF çerezine SameSite bayrağı ekler. Yani çapraz siteler arası çerez transferini, CSRF saldırılarını ve oturum çerezini çalma yöntemlerini önler.
### Her tarayıcı SameSite etiketini dikkate almayabilir.
### Strict  :   Sitedeki hiç bir çerez bilgisine dışarıdan erişilememesine izin verilmez. Ama sayfanızda bir sosyal ağ linki veya kodu var ise link tıklandığında yeniden oturum açılması istenir.
### Lax     :   Siteye yalnızca GET (image, javascript, iframe vs..) ile yapılan sorgularda çerez bilgileri gönderilir.  Dış siteden form POST ile gelen isteklere cevap verilmez.
CSRF_COOKIE_SAMESITE               =   'Lax'


########### Security - Güvenlik
## Default: False
### Tarayıcılar çerezin yalnızca HTTPS bağlantısı ile gönderilmesini sağlar.
### localde runserver veya SSL kullanılmıyor ise False yapılmalı
### admin paneli girişinde CSRF hatası varsa False edilmeli
CSRF_COOKIE_SECURE                 =   False


########### Security - Güvenlik
## Default: 'django.views.csrf.csrf_failure'
### CSRF hatası olduğunda kullanılacak özel fonksiyon.
### def csrf_failure(request, reason=""):
CSRF_FAILURE_VIEW                  =   'django.views.csrf.csrf_failure'


########### Security - Güvenlik
## Default: 'HTTP_X_CSRFTOKEN'
### Bir API ile ya da dışarıdan herhangi bir istek ile CSRF kontrolü gerektiğinde kullanılacak istek başlığı
CSRF_HEADER_NAME                   =   'HTTP_X_CSRFTOKEN'


########### Security - Güvenlik
## Default: []
### CSRF için güvenilir adresler listesi
### Host başlığı ile Referer başlığı tutması gerekir.
CSRF_TRUSTED_ORIGINS               =   ['*'] #['.makdos.biz']


########### Security - Güvenlik
## Default: False
### Çerezin oturumda tutulup tutulmayacağı.
### Oturumda tutulması yararlıdır ayrıca diğer frameworkler (Flask gibi) de bilgilere erişebilir..
CSRF_USE_SESSIONS                  =   False


## Default: 2621440 (2.5MB)
### request.body (Ör: Web sitesi içeriği) ve request.POST (Ör: html form ile yüklenen dosyalar, JSON içerik ve metin içerikleri-yorum- gibi) yüklenmesinden önce belirlenen bellek boyutu
### Bu limit şüpheli işlem kontrolünden önce kullanılır. (SuspiciousOperation (RequestDataTooBig))
### None olarak tanımlanırsa DDOS a maruz kalınabilir.
DATA_UPLOAD_MAX_MEMORY_SIZE        =   2621440


########### HTTP
## Default: 1000
### POST ve GET isteklerindeki en fazla parametre sayısı
### Şüpheli işlem (SuspiciousOperation (TooManyFields)) öncesi kullanılır.
### Örneğin: admin panelden toplu kayıt silerken limitin artırılması gerekecek.
### None olarak tanımlanırsa DDOS a maruz kalınabilir.
DATA_UPLOAD_MAX_NUMBER_FIELDS      =   1000






























########### Database - Veritabanı
## Default: {}
### Veritabanı ayarları
### Mutlaka tanımlanmalı
### postgresql, mysql, sqlite3 veya oracle
DATABASES                          =   {
                                                            'default': {
                                                                'ENGINE': 'django.db.backends.sqlite3',
                                                                ### Windowsda da / kullanılmalı Ör: C:/projeler/deneme//sqlite3.db
                                                                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                                            },
                                                           # 'default': {
                                                           #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
                                                           #     'NAME': 'dbadi',           ## Veritabanı adı
                                                           #     'USER': 'dbuser',          ## Veritabanında işlem yetkili kullanıcı adı
                                                           #     'PASSWORD': 'dbpass',      ## Veritabanı bağlantı parolasu
                                                           #     'HOST': '192.168.101.202', ## Veritabanının bulunduğu sunucu adresi
                                                           #     'PORT': '5432',            ## Veritabanı servisine bağlantı portu
                                                           #     'CONN_MAX_AGE': 600,       ## Veritabanına bağlantı süresi. 0 kullanılır ise her sorgu sonrası bağlantı kapatılır
                                                           # }
                                                           #  'master': {
                                                           #      'ENGINE': 'django.db.backends.mysql',
                                                           #      'NAME': 'dbadi',
                                                           #      'USER': 'dbuser',
                                                           #      'PASSWORD': 'dbpass',
                                                           #      'HOST': '192.168.1.1',
                                                           #      'PORT': '',
                                                           #  },
                                                           #  'balancebir': {
                                                           #      'ENGINE': 'django.db.backends.mysql',
                                                           #      'NAME': 'dbadi',
                                                           #      'USER': 'dbuser',
                                                           #      'PASSWORD': 'dbpass',
                                                           #      'HOST': '192.168.1.2',
                                                           #      'PORT': '',
                                                           #  },
                                                           #  'balanceiki': {
                                                           #      'ENGINE': 'django.db.backends.mysql',
                                                           #      'NAME': 'dbadi',
                                                           #      'USER': 'dbuser',
                                                           #      'PASSWORD': 'dbpass',
                                                           #      'HOST': '192.168.1.3',
                                                           #      'PORT': '',
                                                           #  },
                                                        }


########### Database - Veritabanı
## Default: []
### Birden çok veritabanı bağlantısı gerektiğinde hangi veritabanının kullanılacağının belirleyecek liste
### postgresql.conf ==> listen_addresses = '*'
# DATABASE_ROUTERS                   =   ['kayitlar.routers.OrnekRouter']


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'N j, Y' (e.g. Oca. 24, 2019)
### Sistemin herhangi bir yerinde kullanılacak gün formatı.
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### Kullanılabilir formatlar: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
DATE_FORMAT                        =   'F j, Y'


########### Globalization (i18n/l10n) - Küreselleşme
#Default:
#[
#    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2019-10-25', '10/25/2019', '10/25/06'
#    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2019', 'Oct 25, 2019'
#    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2019', '25 Oct, 2019'
#    '%B %d %Y', '%B %d, %Y',            # 'October 25 2019', 'October 25, 2019'
#    '%d %B %Y', '%d %B, %Y',            # '25 October 2019', '25 October, 2019'
#]
### Sistemin herhangi bir yerinde date alanları için kullanılacak gün format listesi.
### Listenin ilk sırasından itibaren uygunlouk kontrolü yapar
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### Kullanılabilir formatlar: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
DATE_INPUT_FORMATS                 =   ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y', '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y', '%d %B, %Y']


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'N j, Y, P' (e.g. Oca. 24, 2019, 4 p.m.)
### Sistemin herhangi bir yerinde kullanılacak zaman (gün ve saat) formatı.
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### Panelde kullanılacak DatetimeField formatı
### Kullanılabilir formatlar: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
DATETIME_FORMAT                    =   'N j, Y, P'


########### Globalization (i18n/l10n) - Küreselleşme
#Default:
# [
#     '%Y-%m-%d %H:%M:%S',     # '2019-10-25 14:30:59'
#     '%Y-%m-%d %H:%M:%S.%f',  # '2019-10-25 14:30:59.000200'
#     '%Y-%m-%d %H:%M',        # '2019-10-25 14:30'
#     '%Y-%m-%d',              # '2019-10-25'
#     '%m/%d/%Y %H:%M:%S',     # '10/25/2019 14:30:59'
#     '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2019 14:30:59.000200'
#     '%m/%d/%Y %H:%M',        # '10/25/2019 14:30'
#     '%m/%d/%Y',              # '10/25/2019'
#     '%m/%d/%y %H:%M:%S',     # '10/25/19 14:30:59'
#     '%m/%d/%y %H:%M:%S.%f',  # '10/25/19 14:30:59.000200'
#     '%m/%d/%y %H:%M',        # '10/25/19 14:30'
#     '%m/%d/%y',              # '10/25/19'
# ]
### Sistemin herhangi bir yerinde date alanları için kullanılacak zaman (gün ve saat) format listesi.
### Listenin ilk sırasından itibaren uygunluk kontrolü yapar
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### Kullanılabilir formatlar: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
DATETIME_INPUT_FORMATS             =   ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%m/%d/%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S.%f', '%m/%d/%Y %H:%M', '%m/%d/%Y', '%m/%d/%y %H:%M:%S', '%m/%d/%y %H:%M:%S.%f', '%m/%d/%y %H:%M', '%m/%d/%y']




########### Debugging - Hata Ayıklama
## Default: False
### Hatalarda hata ve açıklamaların ekranda gösterilmesi.
### ÖNEMLİ: Sunucuya yükleme yapıldıktan sonra yani product zamanı ASLA True olarak bırakmayın.
### False edildiğinde ALLOWED_HOSTS tanımlanmış olması gerekir. Aksi takdirde Bad Request (400) hatası alınır.
### startproject ile proje oluşturunca otomatik True olarak gelir.
### Debug=True olduğunda Django her SQL sorgusunu hatırlar. Sunucuda iken bu boşa bellek tükettirir.
### Debug=False iken LOGGING ve EMAIL tanımlamaları aktif edilir. Hatalar mail ile gönderilebilir.
### urls.py (uygulamalara ait urls.py de çalışmaz) handler400, handler403, handler404 ve handler500 tanımlayarak özel 404 ve 500 sayfası gösterilebilir.
### True iken API, KEY, PASS, SECRET, SIGNATURE, TOKEN gibi değerler (ve bunlarla başlayan Ör: PASSWORD) güvenlik sebebiyle gösterilmez.
DEBUG                              =   True


########### Debugging - Hata Ayıklama
## Default: False
### True yapılırsa Django'nun handler500, http500 loggingve DEBUG=True olması dikkate alınmadan HTTP servisinin (Apache, Nginx, Litespeed vs.) hata ekranı gösterilir.
### Önemli bilgilerin gösterilmemesi için HTTP servisinin hata gösterme ayarları gözden geçirilmeli.
DEBUG_PROPAGATE_EXCEPTIONS         =   False


########### Globalization (i18n/l10n) - Küreselleşme
## Default: '.' NOKTA
### Ondalık sayı ayracı
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
DECIMAL_SEPARATOR                  =   ','


########### Serialization
########### HTTP
########### Email
## Default: 'utf-8'
### HttpResponse objeleri için karakter kümesi. MIME türleri (Ör: application/json, text/html) özel olarak ayarlanabilir.
DEFAULT_CHARSET                    =   'utf-8'


########### File uploads - Dosya Yükleme
## Default: 'django.core.files.storage.FileSystemStorage'
### Yüklenen dosyalar (html form upload gibi) için özellikle yer belirtilmez ise kullanılacak default ayar sınıfı. Defualt: MEDIA_ROOT ve MEDIA_URL
DEFAULT_FILE_STORAGE               =   'django.core.files.storage.FileSystemStorage'


########### Email
## Default: 'webmaster@localhost'
### Otomatik gönderilen mailler için kullanılacak varsayılan gönderne e-posta adresi.
### Hata mesajlarını ADMINS ve MANAGERS de tanımlananlara göndermez.
DEFAULT_FROM_EMAIL                 =   'projeadi@alanadi.com'


########### DATABASE
## Default: ''
### PostgreSQL ve Oracle veritabanlarında indexler için default tablespace tanımlaması.
### Tablespace tablo ve indexleri aynı yerde tutmaya çalışan böylelikle hızlı sorgu yaptıran bir alt yapıdır.
### Oracle system adında bir tablespace kullanıyor.
### SQLite ve MySQL (MariaDB) desteklenmez.
DEFAULT_INDEX_TABLESPACE           =   ''


########### DATABASE
## Default: ''
### PostgreSQL ve Oracle veritabanlarında tablolar (model) için default tablespace tanımlaması.
### Tablespace tablo ve indexleri aynı yerde tutmaya çalışan böylelikle hızlı sorgu yaptıran bir alt yapıdır.
### Oracle  system adında bir tablespace kullanıyor.
### SQLite ve MySQL (MariaDB) desteklenmez.
DEFAULT_TABLESPACE                 =   ''


########### HTTP
## Default: []
## Tarayıcı ve botların sitedeki herhangi bir sayfayı ziyaret etmesinin engellenmesi
### Aktif olması için Middleware de CommonMiddleware aktif olmalı.
### Regex ile içerenler kontrol ettirilir.
import re
DISALLOWED_USER_AGENTS             =   (
                                            # re.compile('Chrome', re.IGNORECASE), ## Chrome
                                            # re.compile('Firefox', re.IGNORECASE), ## Firefox
                                            re.compile('Trident', re.IGNORECASE), ## IE
                                            re.compile('OPR', re.IGNORECASE), ## Opera
                                        )
########### Email
## Default: 'django.core.mail.backends.smtp.EmailBackend'
### Mail gönderimi için kullanılacak backend sınıf.
EMAIL_BACKEND                      =   'django.core.mail.backends.smtp.EmailBackend'


########### Email
## Default: Tanımlanmaz
### Mail dosyalarının saklanacağı fiziksel yol.
### EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend' ile kullanılırsa geçerli olur
### Örn: os.path.join(PROJECT_ROOT, 'tmp')
EMAIL_FILE_PATH                    =   ''


########### Email
## Default: 'localhost'
### Mail hesabının bulunduğu SMTP host adresi
EMAIL_HOST                         =   'smtp.gmail.com'


########### Email
## Default: ''
### SMTP sunucusu için kullanılacak kullanıcı adı
EMAIL_HOST_USER                    =   'musluyuksektepe@gmail.com'


########### Email
## Default: ''
### SMTP sunucusu için kullanılacak kullanıcı parolas
EMAIL_HOST_PASSWORD                =   ''




########### Email
## Default: 25
### Mail hesabının bulunduğu SMTP hostunun bağlantı portu
EMAIL_PORT                         =   587


########### Email
## Default: False
### SMTP sunucusuna güvenli bağlantı seçeneği.
### Genelde 587 portu kullanılır.
### Sunucu TLS gerektiriyor ise True edilmeli.
EMAIL_USE_TLS                      =   True


########### Email
## Default: '[Django] '
### django.core.mail.mail_admins veya django.core.mail.mail_managers ile gönderilen maillerde konu başlığı
EMAIL_SUBJECT_PREFIX               =   '[Django] '


########### Email
## Default: False
### SMTP Header da Date başlığında gönderilecek saat dilimi
### True ise local False ise UTC bilgilerini gönderir
EMAIL_USE_LOCALTIME                =   False


########### Email
## Default: False
### SMTP sunucusu SSL ile bağlantı gerektiriyor ise True edilmeli.
### Aktif edildiğinde EMAIL_PORT = 465 olarak değiştirilmeli. (Genelde bu port kullanılır.)
### EMAIL_USE_TLS False ise aktif olabilir.
EMAIL_USE_SSL                      =   False


########### Email
## Default: None
### EMAIL_USE_SSL veya EMAIL_USE_TLS aktif ise sertifika dosyasının (PEM formatlı olmalı) yolu
EMAIL_SSL_CERTFILE                 =   None


########### Email
## Default: None
### EMAIL_USE_SSL veya EMAIL_USE_TLS aktif ise private key dosyasının (PEM formatlı olmalı) yolu
EMAIL_SSL_KEYFILE                  =   None


########### Email
## Default: None
### Bağlantı zaman aşımı süresi.
### Ör: 5 (5 saniye)
EMAIL_TIMEOUT                      =   None


########### File uploads - Dosya Yükleme
## Default : ['django.core.files.uploadhandler.MemoryFileUploadHandler', 'django.core.files.uploadhandler.TemporaryFileUploadHandler']
### Dosya yükleme sırasında kullanılan işleyiciler sırası.
### Değiştirilmesi tavsiye edilmez
FILE_UPLOAD_HANDLERS               =   [
                                                            ### Küçük dosyalar için belleği kullanmak
                                                            'django.core.files.uploadhandler.MemoryFileUploadHandler',
                                                            ### Verileri geçici bir dosyaya aktarmak
                                                            'django.core.files.uploadhandler.TemporaryFileUploadHandler',
                                                        ]


########### File uploads - Dosya Yükleme
## Default: Default: 2621440 (i.e. 2.5 MB)
### Yüklemenin sunucuya aktarılmadan önce alacağı en fazla bellek boyut.
### html form üzerinden yüklenmesine izin verilen dosya boyutu
FILE_UPLOAD_MAX_MEMORY_SIZE        =   10 * 1024 * 1024 # 10MB


########### File uploads - Dosya Yükleme
## Default: None
### Dosya yüklenirken oluşturulan kalsör yetkileri
### 0 ile başlaması önemli
FILE_UPLOAD_DIRECTORY_PERMISSIONS  =   0o755


########### File uploads - Dosya Yükleme
## Default: None
### FILE_UPLOAD_MAX_MEMORY_SIZE ile belirlenen dosya boyutuna kadar yüklemelerin geçici bulundurulduğu klasör
### None kullanılırsa Django işletim sisteminin standart temporary klasörünü kullanır. Ör: *nix lerde /tmp
FILE_UPLOAD_TEMP_DIR               =   '/tmp'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 0 (Pazar)
### Takvim seçeneklerinde haftanın ilk günün seçilmesi
### 0 = Pazar, 1 = Pazartesi
FIRST_DAY_OF_WEEK                  =   1


########### Models
## Default: []
### manage.py dumpdata veya el ile oluşturulan hazır kayıt içerik dosyalarının (json, xml, yaml) tutulacağı klasör yolu
### manage.py dumpdata ile veriler dışarıya aktarılır ve daha sonra otomatik içeri alınabilir.
### SQL dump ve load gibi manage.py dumpdata ve manage.py loaddata
### Klasör yolu uzun yazılacak ise Windows dahil / kullanılmalı. Ör: C:/projeler/deneme/fixtures/
FIXTURE_DIRS                       =  (os.path.join(BASE_DIR, 'fixtures'),)


########### Error reporting - Hata raporlama
## Default: None
### Özel yerelleştirme formatlarının tutulduğu klasör
### Klasörler altında __init__.py yi unutmayın
FORMAT_MODULE_PATH                 =   ['kayitlar.formatlar']




## Default: []
### Listedeki yollar bulunamaz ise MANAGERS listesindekilere mail gönderir.
### NOT: APPEND_SLASH=True ise url sonuna / ekleneceği için sorun çıkabilir.
### middleware django.middleware.common.BrokenLinkEmailsMiddleware eklendi ise geçerli olur
IGNORABLE_404_URLS                 =   [
                                            re.compile(r'^wp-login$'),
                                            re.compile(r'^/favicon\.ico$'),
                                            re.compile(r'^/robots\.txt$'),
                                        ]


########### Models
## Default: []
### Kullanılacak uygulamalar listesi
### Mutlaka tanımlanmalı
### Liste olduğu için sıralama önemli.
### Uygulama isim (name) ve etiketleri (label) ayrı ayrı olmalı.
### django.contrib.auth var iken projem.auth kullanılamaz
INSTALLED_APPS                     =   [
                                            'django.contrib.admin',
                                            'django.contrib.auth',
                                            'django.contrib.contenttypes',
                                            'django.contrib.sessions',
                                            'django.contrib.messages',
                                            'django.contrib.staticfiles',
                                            'django.contrib.humanize',
                                            'kayitlar.apps.KayitlarConfig',
                                        ]


########### HTTP
## Default: []
### DEBUG=True iken izin verilen IP adreslerine template içind eiken debug yapma hakkı verir
### request.META['REMOTE_ADDR']) da gelen IP adresi önemli
### django-debug-toolbar da kullanılıyor.
INTERNAL_IPS                       =   ('127.0.0.1', '78.187.60.13', '192.168.1.52')


########### Globalization (i18n/l10n) - Küreselleşme
## Default: en-us
### USE_I18N=True olmalı
### Site genelinde kullanılacak default dil.
### Yönetim paneli dahil seçilen dil ile gösterilir.
LANGUAGE_CODE                      =   'tr'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: None
### Dil seçiminin saniye olarak geçerlilik süresi
### None seçilirse tarayıcı kapatıldığında geçerliliği biter
LANGUAGE_COOKIE_AGE                =   600


########### Globalization (i18n/l10n) - Küreselleşme
## Default None
### Çoklu alan adı kullanımında geçişler arası dil seçimi için çerez bilgisi
### Bir kere ayarlanması ve değişiklik yapılmaması gerekir.
### LANGUAGE_COOKIE_NAME değeri önemli
LANGUAGE_COOKIE_DOMAIN             =   '.makdos.com'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'django_language'
### Tarayıcı çerezinde tutulan dil ayarı adı
### Çoklu dil seçiminde ortak çerez adı
LANGUAGE_COOKIE_NAME               =   'site_dili'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: /
### Çerez Dil seçiminin tutulduğu yol
### Çoklu site yayını yapılıyor ise yol değiştirilip seçim sadece o yol ve altına tanımlanabilir
LANGUAGE_COOKIE_PATH               =   '/'


########### Globalization (i18n/l10n) - Küreselleşme
from django.utils.translation import gettext_lazy as _
## Default: None
### Sitede kullanılacak dil listesi.
LANGUAGES                          =   [
                                            ('tr', _('Türkçe')),
                                            ('en', _('English')),
                                        ]

########### Globalization (i18n/l10n) - Küreselleşme
## Default: None
### Sağdan Sola yazım dilleri listesi
LANGUAGES_BIDI                     =   ["he", "ar", "fa", "ur"]


########### Globalization (i18n/l10n) - Küreselleşme
# ## Default: []
# ### Çoklu dil kullanımında dil dosyalarının bulunacağı klasör listesi
LOCALE_PATHS                       =   (os.path.join(os.path.dirname(__file__), "locale"),)


## Default: '/accounts/profile/'
### Giriş ypaıldıktan sonra yönlendirilecek adres
LOGIN_REDIRECT_URL                 =   '/panel/hesabim'


## Default: '/accounts/login/'
### Giriş için yönlendirilecek adres
LOGIN_URL                          =   '/giris/'


## Default: None
### Çıkış sonrası yönlendirilecek adres
LOGOUT_REDIRECT_URL                =   '/cikis-yapildi/'



########### Logging - Günlükleme
## DEBUG=False iken çalışır
### Loglama işlemleri için ayarlar
### Mail gönderim, print(yerine dosyaya çıktı yazdırmak, mail gönderimi sağlamak vs..)
import codecs
import logging
import sys
########### Logging - Günlükleme
########### Error reporting - Hata raporlama
### Proje klasörü altında djangoLog.log dosyası oluşturulmalı ve 777 yazma yetkisi verilmeli.
logging.basicConfig(level=logging.INFO, format='%(message)s', handlers=[logging.FileHandler(os.path.join(BASE_DIR, "djangoLog.log"), 'w', 'utf-8')])
sys.stdout                         = codecs.getwriter("utf-8")(sys.stdout.detach())
LOGGING                            =   {
                                            'version': 1,
                                            'disable_existing_loggers': False,
                                            'handlers': {
                                                'mail_admins': {
                                                    'level': 'ERROR',
                                                    'class': 'django.utils.log.AdminEmailHandler',
                                                    'include_html': True,
                                                },
                                                'log_to_stdout': {
                                                    'level': 'DEBUG',
                                                    'class': 'logging.StreamHandler',
                                                    'stream': sys.stdout,
                                                },
                                            },
                                            'loggers': {
                                                'main': {
                                                    'handlers': ['mail_admins', 'log_to_stdout'],
                                                    'level': 'DEBUG',
                                                    'propagate': True,
                                                }
                                            }
                                        }


########### Email
########### Error reporting - Hata raporlama
## Default: []
### ADMINS gibi ama MANAGERS listesindekilere bozuk linkler mail ile gönderilir.
### middleware django.middleware.common.BrokenLinkEmailsMiddleware eklendi ise geçerli olur
MANAGERS                           =   [('Muslu', 'muslu.yuksektepe@makdos.com')]


########### File uploads - Dosya Yükleme
## Default: ''
### Siteye dışarıdan yüklenen dosyalar için klasör yolu
### STATIC_ROOT ile aynı adda klasör yazılamaz
### Ziyaretçilerin html form ile dosya yüklemesi, admin panelinden yükleme vs..
MEDIA_ROOT                         =   os.path.join(BASE_DIR, 'media')


########### File uploads - Dosya Yükleme
## Default: ''
### Siteye dışarıdan yüklenen dosyaların gösterilmesi için url yolu
### Tanımlama yapılacak ise / işareti ile bitmeli
### STATIC_URL ile aynı değer yazılamaz
### Dışarıdan yüklemelere karşı dikkatli olunmalı. Klasör izinlerine dikkat edilmeli.
### TEMPLATES context_processors de django.template.context_processors.media aktif edilmeli
MEDIA_URL                          =   '/media/'


## Default: messages.INFO
### django.contrib.messages ile gönderilen mesajların en düşük seviyesi.
### En az INFO bilgileri mesaj olarak gönderilebilir.
# MESSAGE_LEVEL                      =   'messages.INFO'


########### HTTP
### Middleware: Djangonun tüm istekleri ve cevapları (request/response) kontrol edip işlem yaptırımasını sağlayan katman
### Yazım sırası önemli. Önce yazılan alt katmana ne gönderirse alt katmandaki ancak o kadar bilgi ile işlem yapabilir.
### Özel bir katman yazılarak tüm gelen sorguları loglama yapabilir ya da mail ile gönderebiliriz.
### Özel katman ile ziyaretçinin request bilgisi ile kullanılan aygıt tespit edilebilir.
### Özel katman ile tüm sayfalara tek yerden IP giriş izni verilmeyebilir.
### Bu katmanda tüm views.py deki fonskiyonlar takip edilebilecğei için çok detaylı loglama ypaılabilir.
MIDDLEWARE                         =   [
                                            'django.middleware.security.SecurityMiddleware',
                                            'django.contrib.sessions.middleware.SessionMiddleware',
                                            'django.middleware.common.CommonMiddleware',
                                            'django.middleware.csrf.CsrfViewMiddleware',
                                            'django.contrib.auth.middleware.AuthenticationMiddleware',
                                            'django.contrib.messages.middleware.MessageMiddleware',
                                            'django.middleware.clickjacking.XFrameOptionsMiddleware',
                                        ]


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'F j'
## Kayıt sayfası ve tüm sistemde ay ve günün kullanılacağı format.
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### Formatlar için: https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
MONTH_DAY_FORMAT                   = 'F j'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 0
### Tam sayı (İnteger) kısmın gruplanmasını sağlar
### Ör: 12,34,56,000
### 0 dan büyük bir değer yazılırsa THOUSAND_SEPARATOR kullanılır.
NUMBER_GROUPING                    =   1


########### Security - Güvenlik
## Default: 3
### Parola sıfırlama linkinin geçerlilik süresi (3 gün)
PASSWORD_RESET_TIMEOUT_DAYS        =   5





########### Security - Güvenlik
## Default:
"""
[
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
"""
### Parolaların hashlenmesi için kullanılan algoritmalar
### <algorithm>$<iterations>$<salt>$<hash>
PASSWORD_HASHERS                   =   [
                                            'django.contrib.auth.hashers.PBKDF2PasswordHasher',
                                            'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
                                            'django.contrib.auth.hashers.Argon2PasswordHasher',
                                            'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
                                        ]


########### URLs
## Default: False
### URL sorgusuna otomatik www. ekler.
### Aktif olması için Middleware de CommonMiddleware aktif olmalı.
PREPEND_WWW                        =   False


########### URLs
## Default: Tanımlanmaz
### Projenin url path yönlendirmelerinin bulunduğu dosya
### /home/musluyuksektepe/PycharmProjects/modeladmin/modeladmin/urls.py
### Mutlaka tanımlanmadlı
ROOT_URLCONF                       =   'modeladmin.urls'


########### Security - Güvenlik
## Default = ''
### sessions, messages, password reset ve tüm cryptographic singing imzalamalarda kullanılır.
### Parola ve geri getirme işlemlerinde kullanılmaz.
### Mutlaka tanımlanmalı
SECRET_KEY                         =   'GizliKey'


########### HTTP
## Default: False
### SecurityMiddleware aktif olmalı.
### XSS korumasını tarayıcı tarafında da yaptırmak için filtre
### True yapılırsa tüm HTTP Header başlıklarına X-XSS-Protection: 1; mode=block eklenir.
### Çoğu tarayıcı POST ve GET leri sunucudan döndürülünce de kontrol eder. Böylelikle XSS saldırısını kontrol eder.
"""
# Nginx
add_header X-Frame-X-XSS-Protection 1;
# Apache
Header always append X-XSS-Protection 1
# IIS
<httpProtocol>
<customHeaders>
  <add name="X-XSS-Protection" value="1" />
</customHeaders>
</httpProtocol>
"""
SECURE_BROWSER_XSS_FILTER          =   True


########### HTTP
## Default: False
### SecurityMiddleware aktif olmalı.
### HTTP Header başlığına X-Content-Type-Options: nosniff ekler
### Tarayıcılara yüklenen dosyanın türünü (MIME Type sniffing) hakkında karar vermesi engeller
"""
# Nginx
add_header X-Content-Type-Options nosniff;
# Apache
Header always X-Content-Type-Options nosniff
# IIS
<httpProtocol>
<customHeaders>
  <add name="X-Content-Type-Options" value="nosniff" />
</customHeaders>
</httpProtocol>
"""
SECURE_CONTENT_TYPE_NOSNIFF        =   True


########### HTTP
## Default: False
### SecurityMiddleware aktif olmalı.
### HSTS (HTTP Strict Transport Security) ile tüm sorguların zorunlu olarak HTTPS üzerinden yapılmasına zorlanır.
### HSTS hem sunucu hem de tarayıcı da ki sertifikaların eşleşmesi için kullanılır. Böylelikle hatalı sertifika ya da saldırganın sertifikası karşılaştırılır ve tarayıcı uyarı verir.
### SECURE_HSTS_PRELOAD ile sertifika tarayıcıların kullandığı HSTS veritabanına eklenmelidir.
### NOT: Tüm alanadına ait ve alt alan adlarına ait sorgular HTTPS üzerinden geçeeği için sorun yaşanabilir. Örn: Panel portları artık sadece HTTPS portundan çalışır.
### Strict-Transport-Security: max-age=16070400; includeSubDomains
"""
# Apache
LoadModule headers_module modules/mod_headers.so
 
<VirtualHost *:443>
    ...
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains"
</VirtualHost>

# NGINX
add_header Strict-Transport-Security max-age=63072000; includeSubdomains

# IIS web.config
<system.webServer>
    <httpProtocol><customHeaders><add name="Strict-Transport-Security" value="max-age=31536000"/></customHeaders></httpProtocol>
</system.webServer>
"""
SECURE_HSTS_INCLUDE_SUBDOMAINS     =   False


########### HTTP
## Default: False
### SecurityMiddleware aktif olmalı.
### Modern tarayıcılara güvenli olmayan bir bağlantıyla (SECURE_HSTS_SECONDS süresi dahilinde) alan adına bağlanmayı reddetmeleri bildirilir.
### https://hstspreload.org/ adresinden alan adının tarayıcı listesine eklenme talep edilebilir.
### https://hstspreload.org/removal/ adresinden silme talebi oluşturulur
SECURE_HSTS_PRELOAD                =   False


########### HTTP
## Default: 0
### SecurityMiddleware aktif olmalı.
### Sertifikaların karşılaştırılma süresi.
### Strict-Transport-Security: max-age=0 ile iptal edilebilir.
SECURE_HSTS_SECONDS                =   10886400 ## 18 hafta


########### HTTP
## Default: None
### Projemiz bir proxy (loadbalancer, reverse-proxy vs.. gibi) arkasaında ise ve SSL i proxy yönetiyor ise
### Proxy üzerinden gelen tüm sorgular HTTPS e yönlendirilir. Bu güvenliği tam sağlamaz. 3. parti kütüphane kullanılıyor ise çalışmayabilir.
# SECURE_PROXY_SSL_HEADER            =   ('HTTP_X_FORWARDED_PROTO', 'https') ### ('HTTP_X_FORWARDED_SCHEME', 'https')


########### HTTP
## Default= []
### HTTPS e yönlendirilmeyecek yollarr
### SECURE_SSL_REDIRECT=True olmalı.
### Bazı tarayıcılar (Ör: Firefox) admin paneline yönlendirmede sorun yaşatırsa
SECURE_REDIRECT_EXEMPT             =   [r'^(?!admin/).*']


########### HTTP
## Default: None
### SecurityMiddleware aktif olmalı.
### SECURE_SSL_REDIRECT=True olmalı.
### Trafiğin yönlendirileceği HTTPS adresi.
# SECURE_SSL_HOST                    =   'guvenlibolge.alanadi.com'


########### HTTP
## Default: False
### SecurityMiddleware aktif olmalı.
### Tüm trafiği HTTPS e yönlendirir
SECURE_SSL_REDIRECT                =   False


########### Email
## Default: 'root@localhost'
### ADMINS ve MANAGERS listesine mail gönderen hesap
SERVER_EMAIL                       =   'hatavar@alanadi.com'


## Default: 'default'
### Oturumlarda CACHES backend de çoklu barındırma kullanılıyorsa hangi depolamanın kullanılacağı
SESSION_CACHE_ALIAS                =   'default'


## Default: Default: 1209600 (2 hafta)
### Oturum için kullanılan çerezlerin geçerlilik süresi
SESSION_COOKIE_AGE                 =   1209600


## Default: None
### Oturum çerezlerinin  hangi alan adına ait olduğu
### Aynı çerez çoklu alan adı için kullanılacaksa 'alanadi.com' gibi kullanılabilir. Böylelikle alt alanadlarında da aynı çerez ile giriş yaptırılmış olur.
### Ayrıca; django.contrib.messages içinde bu ayarlar kullanılır.
SESSION_COOKIE_DOMAIN              =   None #'.makdos.biz' ## tüm alt alan adları dahil


## Default: True
### Çereze HTTPOnly bayrağı ekler.
### True yapılırsa oturum çerezlerine javascript üzerinden erişilemez. Böylelikle saldırganlar oturum çerezlerini malmasını önlemeye yardımcı olur.
SESSION_COOKIE_HTTPONLY            =   False


## Default: 'sessionid'
### Oturum çerezlerinde ortak çerez adı.
### Çok sayıda sitenin tek çerez ile oturum açılması istenirse burası aktif edilmeli.
SESSION_COOKIE_NAME                =   'sessionid'


## Default: '/'
### Aynı alan adında birden çok Djang oprojesi çalıştırılıyor ise farklı çerez yolları kullanılmalı. Böylelikle her proje kendi oturum çerezine ulaşır.
SESSION_COOKIE_PATH                =   '/'


## Default: 'Lax'
### Oturum çerezine SameSite bayrağı ekler. Yani çapraz siteler arası çerez transferini, CSRF saldırılarını ve oturum çerezini çalma yöntemlerini önler.
### Her tarayıcı SameSite etiketini dikkate almayabilir.
### Strict  :   Sitedeki hiç bir çerez bilgisine dışarıdan erişilememesine izin verilmez. Ama sayfanızda bir sosyal ağ linki veya kodu var ise link tıklandığında yeniden oturum açılması istenir.
### Lax     :   Siteye yalnızca GET (image, javascript, iframe vs..) ile yapılan sorgularda çerez bilgileri gönderilir.  Dış siteden form POST ile gelen isteklere cevap verilmez.
### GET ile sorgu her ne kadar çözüm olsa bile tarayıcı geçmişinde gözükmesi, parametrelerin server loglarında tutulması gibi sebeplerden dolayı dikkat edilmeli.
SESSION_COOKIE_SAMESITE            =   'Lax'


## Default: False
### Tarayıcılar çerezin yalnızca HTTPS bağlantısı ile gönderilmesini sağlar.
### localde runserver veya SSL kullanılmıyor ise False yapılmalı
### admin paneli girişinde CSRF hatası varsa False edilmeli
SESSION_COOKIE_SECURE              =   False


## Default: 'django.contrib.sessions.backends.db'
"""
'django.contrib.sessions.backends.db'               ## Veritabanında bir tabloda tutar. Veritabanı bağlantısı yavaş ise oturum kaybı yaşanabilir.
'django.contrib.sessions.backends.file'             ## SESSION_FILE_PATH yolunda saklanır. tempfile.gettempdir() ile klasör kontrol edilebilir. Bu yola okuma/yazma yetkilerinin verildiğinden emin olun.
'django.contrib.sessions.backends.cache'            ## Önbellekte tutulur. Önbellek dolarsa veya önbellek sunucusu yeniden başlatılırsa, önbellekteki veriler kaybolur.
'django.contrib.sessions.backends.cached_db'        ## Önbellekte tutular oturumlar her yazma işleminde veritabanına taşınır. Oturum önbellekte yoksa veritabanına bakar.
'django.contrib.sessions.backends.signed_cookies'   ## Oturum bilgileri tarayıcı çerezlerinde tutulur. SECRET_KEY önemli. Değiştirilirse oturumlar düşer. SESSION_COOKIE_HTTPONLY=True yapılması iyi olur. ORTAK site oturumu kullanılmayacak ise tavsiye edilmez.
"""

### Django'nun oturum bilgileri nerede saklayacağı
SESSION_ENGINE                     =   'django.contrib.sessions.backends.db'



## Default: False
### Tarayıcı kapatılınca oturumun süresini bitir.
### Chrome sorun yaşanabilir. Chrome sürekli oturum açılmaması için çerezleri saklamaya devam eder.
### False yapılırsa SESSION_COOKIE_AGE dikkate alınır.
SESSION_EXPIRE_AT_BROWSER_CLOSE    =   False


## Default: None
### Oturum bilgileri dosya tabanlı saklanacaksa, dosyaların tutulacağı klasör.
### None bırakılırsa Django sistemin standart geçici klasörlerini kullanır. (*nix : /tmp/)
SESSION_FILE_PATH                  =   None


## Default: False
### Her sorgu yapıldığında yeniden oturum bilgileri güncellemek
### False bırakılırsa sadece oturum bilgileri değişirse saklanır.
### Oturum cache den dolayı düşüyor ise True yapılmalı
SESSION_SAVE_EVERY_REQUEST         =   False


## Default: Tanımlanmaz
### django.contrib.sites ayarları
### Tek bir veritabanının birden çok sitenin içeriğini yönetebilmesi
SITE_ID                            =   1


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'm/d/Y' (Ör: 01/31/2019)
### Templatelerde gün alanlarında gösterilecek format
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
SHORT_DATE_FORMAT                  =   'm/d/Y'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'm/d/Y P' (Ör: 01/31/2019 9 p.m.)
### Templatelerde gün saat alanlarında gösterilecek format
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
SHORT_DATETIME_FORMAT              =   'm/d/Y P'


########### HTTP
## Default: 'django.core.signing.TimestampSigner'
### Çerezleri ve diğer bilgileri imzalamak için kullanılan fonksiyonlar
SIGNING_BACKEND                    =   'django.core.signing.TimestampSigner'


########### Error reporting - Hata raporlama
## Defualt: None
### Sistem hata ve uyarılarını gizlemek
### Örn: The value of list_filter must be a list or tuple uyarısını görmemek için admin.E112 yazılabilir.
### security.W018 = You should not have DEBUG set to True in deployment.
### https://docs.djangoproject.com/en/2.2/ref/checks/
SILENCED_SYSTEM_CHECKS             =   ['admin.E112', 'security.W018']


### Default: Tanımlanmaz
### STATIC_ROOT klasör yolunda kullanılacak dosyalar (css,js,pdf,mp3 vs..) için URL yolu.
### Tanımlama yapılacak ise / işareti ile bitmeli
### SAdece DEBUG=True iken çalışır.
### Tanımlama yapılırsa ModelAdmin ve ModelForm class MEdia da ki css ve js yolları otomatik /static/css/ gibi olur.
STATIC_URL                         =   '/static/'


# STATIC_URL                         = 'https://dosyalar.alanadi.com' ### Debug=True iken çalışmaz


### Default: Tanımlanmaz
### Static dosyalarının bulunduğu fiziksel yol.
### INSTALLED_APPS de 'django.contrib.staticfiles' tanımlanmış olmalı
### Mutlaka tanımlanmalı
### collectstatic ile kullanılan uygulamaların static dosyalarının kopyalanacağı yol
# STATIC_ROOT                        = os.path.join(BASE_DIR, 'static') #### Sunucuda çalışır. ### COLLECTSTATIC için aktif edilmeli
STATIC_ROOT                        =   '' #### Lokalde runserver ile çalışır  ###COLLECTSTATIC için pasif edilmeli


## Default: []
### Lokalde runserver ile çalışır
STATICFILES_DIRS                   =   [
                                            ('imajlar', os.path.join(BASE_DIR, 'static/imajlar/')), ### <img src="{% static "imajlar/logo.png" %}">
                                            ('videolar', os.path.join(BASE_DIR, 'static/videolar/'))
                                        ]
























########### Templates - Şablonlar - HTML
## Default: []
### Tüm html dosyalarının yorumlanacağı özel ayarlar
TEMPLATES                          =   [
                                            {
                                                ### Template dosyalarında kullanılacak html yorumlama motoru
                                                ### Döngü, koşul, template tags gibi Djangoya özel fonksiyonların html dosyası içinde yorumlanması için backend seçimi
                                                ### .backends.django.DjangoTemplates veya .backends.jinja2.Jinja2
                                                'BACKEND': 'django.template.backends.django.DjangoTemplates',

                                                ## Default: []
                                                ### Standart html dosyalarının bulunduğu yol
                                                'DIRS': [os.path.join(BASE_DIR, 'templates')],
                                                ## Default: False
                                                ### startproject ile oluşturulursa True gelir.
                                                'APP_DIRS': True, ### INSTALLED_APPS daki Uygulamalara (Ör: kayitlar/templates/) özel html dosyaları
                                                'OPTIONS': {
                                                    'context_processors': [
                                                        'django.template.context_processors.debug',
                                                        'django.template.context_processors.request',
                                                        'django.contrib.auth.context_processors.auth',
                                                        'django.contrib.messages.context_processors.messages',
                                                        'django.template.context_processors.media',  ### Kullanıcıların yüklediği dosyalar için MEDIA tanımlaması
                                                    ],
                                                },
                                            },
                                        ]


########### Globalization (i18n/l10n) - Küreselleşme
## Default: ',' Virgül
### Binlik ayracı
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
THOUSAND_SEPARATOR                 =   '.'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'P' (4 p.m.)
### Sistemin herhangi bir alanında ki zaman alanlarının formatı
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
TIME_FORMAT                        =   'P'


########### Globalization (i18n/l10n) - Küreselleşme
"""
Default:
[
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
]
"""
### Sistemdeki saat giriş alanları için kabul edilen formlat listesi
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### USE_TZ=True olmalı.
### https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
TIME_INPUT_FORMATS                 =   ['%H:%M:%S', '%H:%M:%S.%f','%H:%M']


########### Globalization (i18n/l10n) - Küreselleşme
## Default:
### Sistemin geneli için uygulanacak saat dilimi
### https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
### Windows da alternatif saat dilimleri güvenilir şekilde kullanılamayabilir. Sistem saat dilimi ile aynı olmalı.
TIME_ZONE                          =   'Europe/Istanbul'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: True
### Djangon sistemi translate edip etmeyeceği. Tek dil kullanılacak ise False ypaılması performans sağlar.
### False iken Django boş yere translate etmek için zaman harcamaz
USE_I18N                           =   True


########### Globalization (i18n/l10n) - Küreselleşme
## Default: False
### Yerelleştirmenin aktfi olup olmayacağı
### True yapılırsa Django tüm sayı, zaman ve saat formatlarını yerel ayarlara (LANGUAGE_CODE) göre yapar
### startproject ile proje oluşturunca True olarak gelir.
USE_L10N                           =   True


########### Globalization (i18n/l10n) - Küreselleşme
## Default: False
### Sayılarda binlik ayracını göstermek
### True yapılırsa ve USE_L10N=True olursa ve yerel ayarlarda binlik ayracı yoksa Django THOUSAND_SEPARATOR ve NUMBER_GROUPING ayarlarını etkinleştirir.
USE_THOUSAND_SEPARATOR             =   True

########### Globalization (i18n/l10n) - Küreselleşme
## Default: False
### True seçilirse Django saat dilimi ayarlarını kullanır.
### startproject ile proje oluşturunca True olarak gelir.
USE_TZ                             =   False

########### HTTP
## Default: False
### Bir proxy server (Nginx, Apache, Haproxy vs..) ile trafik yönlendiriliyor ise Django ilk gelen host bilgilerini kullanır.
### Proxy ninde aynı şekilde ayarlanması gerekir. Ayarlanmaz ise Proxy sunucu bilgileri kullanılır.
### Genelde iç IP ye yönlendirmek yapılacağı zaman sorun çıkar. Apache için proxy ayarları yapılarak içeriye yönlednirme yapılır
### İç IP ye SSL ile yönlenecek ise SECURE_PROXY_SSL_HEADER=True olmalı
"""
<VirtualHost *:443>
    ...
    RequestHeader set X-Forwarded-Proto 'https' env=HTTPS

    ProxyPass / http://192.168.101.200/
    ProxyPassReverse / http://192.168.101.200/
    ...
</VirtualHost>
"""
USE_X_FORWARDED_HOST               =   False


########### HTTP
## Default: False
### USE_X_FORWARDED_HOST ile aynı kullanım ama gelen portu da yönlendirmek için
USE_X_FORWARDED_PORT               =   False


########### HTTP
## Default: None
### runserver ile çalıştırmada WSGI uygulamasının (Ör: wsgi.py) fiziksel tam yolu.
### startproject proje klasörü altında wsgi.py adında bir dosya oluşturur.
### Tanımlanmaz ise django.core.wsgi.get_wsgi_application() değeri kullanılır.
### Apache için Ör:
"""
WSGIScriptAlias / /home/makdos/django/proje/proje/wsgi.py
WSGIDaemonProcess proje threads=5 python-path=/usr/local/lib/python3.6/dist-packages/:/home/makdos/django/proje/
WSGIProcessGroup proje
WSGIApplicationGroup %{GLOBAL}

<Directory /home/makdos/django/proje/proje/>
  <Files wsgi.py>
        Require all granted
  </Files>
</Directory>
"""
WSGI_APPLICATION                   =   'modeladmin.wsgi.application'


########### Globalization (i18n/l10n) - Küreselleşme
## Default: 'F Y'
### Sistem genelinde yıl ve ay kullanılacak alanalrda (Ör: admin paneli filtreleme) gösterilecek format
### USE_L10N=True olursa yerelleştirme formatı öncelikli olarak kullanılır.
### https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#std:templatefilter-date
YEAR_MONTH_FORMAT                  =   'F Y'


########### Security - Güvenlik
## Default: 'SAMEORIGIN'
### Sitenin başka bir yerde IFrame içinde çalıştırılıp çalıştırmamasına izin verme (clickjacking koruması)
### 'DENY' = Engelle
### 'SAMEORIGIN' = Sadece kendi alt alan adlarında izin ver
### Bazı tarayıcılarda çalışmayabilir.
"""
# Apache
Header always set X-Frame-Options "sameorigin"
Header set X-Frame-Options "deny"
Header set X-Frame-Options "allow-from https://makdos.com/"
# Haproxy
http-response set-header X-Frame-Options sameorigin
# Nginx
add_header X-Frame-Options sameorigin;
# IIS
<system.webServer>
  ...
  <httpProtocol>
    <customHeaders>
      <add name="X-Frame-Options" value="sameorigin" />
    </customHeaders>
  </httpProtocol>
</system.webServer>
"""
X_FRAME_OPTIONS                    =   'DENY'