from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_response(question: str):
    return None
