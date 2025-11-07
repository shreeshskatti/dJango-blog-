from pathlib import Path

# -----------------------------------------------------------------------------
# BASE PATHS
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
# SECURITY
# -----------------------------------------------------------------------------
SECRET_KEY = 'replace-this-in-production'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# -----------------------------------------------------------------------------
# APPLICATIONS
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'django_summernote',

    # Local apps
    'blog',
]

# -----------------------------------------------------------------------------
# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Allow Summernote iframes inside admin
X_FRAME_OPTIONS = 'SAMEORIGIN'

# -----------------------------------------------------------------------------
# URLS & TEMPLATES
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Optional project-level templates folder
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,  # looks in blog/templates/ automatically
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # admin + Summernote need this
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# -----------------------------------------------------------------------------
# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------------------------------------------
# AUTH PASSWORD VALIDATION
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------------------------------------------
# I18N / TIMEZONE
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# STATIC & MEDIA FILES
# -----------------------------------------------------------------------------
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'        # optional for collectstatic
STATICFILES_DIRS = [BASE_DIR / 'static']      # optional for your own assets

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'               # Summernote uploads go here

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------
# DJANGO SUMMERNOTE CONFIGURATION
# -----------------------------------------------------------------------------
SUMMERNOTE_CONFIG = {
    'summernote': {
        'toolbar': [
            ['style', ['style']],
            ['font', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol', 'paragraph']],
            ['insert', ['link', 'picture', 'video']],  # video embed button
            ['view', ['codeview']],
        ],
        'height': 350,
        'width': '100%',
    },
}

# Allow YouTube & Vimeo embeds (iframe sanitizer whitelist)
SUMMERNOTE_ALLOWED_IFRAMES = [
    r'^https://www\.youtube\.com/embed/.*',
    r'^https://www\.youtube-nocookie\.com/embed/.*',
    r'^https://player\.vimeo\.com/video/.*',
]

# Allow iframe tags and attributes so embeds aren’t stripped
SUMMERNOTE_ALLOWED_TAGS = [
    'p', 'br', 'span', 'div', 'a', 'img', 'ul', 'ol', 'li', 'strong', 'em', 'u', 's',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'pre', 'code', 'hr',
    'table', 'thead', 'tbody', 'tr', 'th', 'td',
    'iframe'
]

SUMMERNOTE_ALLOWED_ATTRIBUTES = {
    '*': ['style', 'class', 'id'],
    'a': ['href', 'title', 'target', 'rel'],
    'img': ['src', 'alt', 'width', 'height'],
    'iframe': [
        'src', 'width', 'height', 'title', 'frameborder',
        'allow', 'allowfullscreen', 'referrerpolicy'
    ],
}
