import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

# SEEDS_PATH = 'seeds/'
#
# # Order matters
# SEEDS_TOPICS = [
#     'layer_type',
#     'layer',
#     'dashboard',
# ]



model_link = os.getenv('model_link', 'http://127.0.0.1:8000/')
