import aioredis
from typing import Callable

redis = aioredis.from_url("redis://localhost")

async def redis_cache(ttl: int):
    def decorator(func: Callable):
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{args}:{kwargs}"
            cached_result = await redis.get(cache_key)
            if cached_result:
                return cached_result
            result = await func(*args, **kwargs)
            await redis.set(cache_key, result, ex=ttl)
            return result
        return wrapper
    return decorator

async def invalidate_cache(cache_key: str):
    await redis.delete(cache_key)