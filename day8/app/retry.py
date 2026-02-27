import asyncio
import functools

def async_retry(max_retries: int = 3, exponential_wait: float = 2.0): # this gives us a function which will give us wrapped function
    def decorator(func): # this helps to wrap the func by accepting the func
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            delay = 1
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    print(f"Error: {e}")
                    print(f"Retrying in {delay} seconds...")
                    await asyncio.sleep(delay)
                    delay *= exponential_wait
        return wrapper
    return decorator