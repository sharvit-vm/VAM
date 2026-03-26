from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache

def enable_cache():
    set_llm_cache(InMemoryCache())