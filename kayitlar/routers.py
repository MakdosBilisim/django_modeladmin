import random

### Veritabanları arası balance
class OrnekRouter(object):
    def db_for_read(self, model, **hints):
        ### Veri okumayı rastgele yap
        return random.choice(['master', 'balancebir', 'balanceiki'])

    def db_for_write(self, model, **hints):
        ### Veri yazma yalnızca master adlı veritabanına
        return 'master'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('master', 'balancebir', 'balanceiki')
        ### Veritabanları arası nesnelere (obje) ilişkilere izin verir.
        ###
        if obj1.state.db in db_list and obj2.state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        ### Tüm yetkisiz modeller için de kullanılır
        return True



### Tüm projeler için ortak kullanıcı tablosu
### Bir proje ait tüm kullanıcılar diğer projelerde de aynı bilgiler giriş işlem yapabilir.
class AuthRouter(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'auth':
            return 'auth_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'auth_db':
            return app_label == 'auth'
        elif app_label == 'auth':
            return False
        return None
