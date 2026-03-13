import aioredis
from functools import wraps

redis = aioredis.from_url('redis://localhost')


async def get_cache(key):
    return await redis.get(key)


async def set_cache(key, value, ttl):
    await redis.set(key, value, ex=ttl)


def redis_cache(ttl=300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f'{func.__name__}:{str(args)}:{str(kwargs)}'
            cached_result = await get_cache(cache_key)
            if cached_result:
                return cached_result
            result = await func(*args, **kwargs)
            await set_cache(cache_key, result, ttl)
            return result
        return wrapper
    return decorator


async def invalidate_cache(key):
    await redis.delete(key)