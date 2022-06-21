"""
Django settings for DjangoBlog project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
"""
__file__は現在のモジュールの絶対パスを取得するもの
resolve()は相対パスを絶対パスに変換するメソッド
"""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k)w1_3wzlad3h6oadao0*-p^be@))qpzq3(x+p=b&@86g2^xi)'
"""
利用するユーザーのパスワードに加えられる文字列が登録されている
"""

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
"""
開発環境の時True
本番環境の時False
"""

ALLOWED_HOSTS = []
"""
ホストサーバーを登録する
"""


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  #テンプレートエンジンとしてDjangoTemplatesモジュールが指定されている
        'DIRS': [], #検索対象のフォルダー
        'APP_DIRS': True, #アプリのテンプレートも検索するかどうか
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', #共通の変数名を指定している。この場合だとdebug,request,auth,messages.
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjangoBlog.wsgi.application' 
#WSGI ウェブサーバーとウェブアプリを接続するための仕組み
#この環境変数はWSGIを実行するための関数を登録するためのもの

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
#パスワードの妥当性をチェックするための仕組みを登録している
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',#ユーザー名と似たパスワード
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',#短すぎるパスワード
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',#よくあるパスワード
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',#数値のみのパスワード
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ja'#ジャンゴの中で使用する言語

TIME_ZONE = 'Asia/Tokyo'#UTCは日本標準時-9h

USE_I18N = True#多言語化機能

USE_L10N = True#日付フォーマットなどを地域ごとに適用する機能

USE_TZ = True#タイムゾーンを変換する機能


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'#静的ファイルを収めたフォルダーのURL

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
