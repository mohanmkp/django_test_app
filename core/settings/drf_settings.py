

DRF_APPS = [
    'rest_framework',
    'corsheaders',

]

# CORS_ALLOWED_ORIGINS = [
#     "https://localhost:3000",
#     "https://127.0.0.1:3000",
#     "http://localhost:3000",
#     "http://127.0.0.1:3000",
# ]

CORS_ORIGIN_ALLOW_ALL = True



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}



