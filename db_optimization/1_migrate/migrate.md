## 安装python的MySQL客户端
```
conda install mysqlclient
```

## dump数据
```shell
python manage.py dumpdata > jarvis_all.json
```

## 表结构同步
### 配置slave DB为MySQL DB
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jarvis_applet',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

### 同步命令
```
python manage.py migrate --database slave
```

## load数据到新db

### 配置主数据库为MySQL
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jarvis_applet',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

### load数据
```
python manage.py loaddata jarvis_all.json
```