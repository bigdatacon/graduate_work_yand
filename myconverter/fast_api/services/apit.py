from functools import lru_cache
from typing import List, Optional



class ApiTesting:
    def __init__(self):
        pass

    async def get_list(self):

        return {'Hello' : 'World'}


@lru_cache()
def get_apitesting_service() -> ApiTesting:
    return ApiTesting()