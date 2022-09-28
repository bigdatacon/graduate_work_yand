import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

SEEDS_PATH = 'seeds/'

# Order matters
SEEDS_TOPICS = [
    'layer_type',
    'layer',
    'dashboard',
]

AUTH_REQUIRED = os.getenv('AUTH_REQUIRED', 'True').lower() in ('true', '1')

POSTGRES_DB = os.getenv('POSTGRES_DB', 'interactive_map')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5432')

KEYCLOAK_HOST = os.getenv('KEYCLOAK_HOST', 'https://keycloak.dev.imap20.tn.p13.space')
KEYCLOAK_PATH = os.getenv('KEYCLOAK_PATH', '/realms/saturn/protocol/openid-connect/userinfo')

CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split()
