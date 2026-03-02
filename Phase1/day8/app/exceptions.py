class LLMError(Exception):
    pass
class AuthenticationError(LLMError):
    pass
class RateLimitError(LLMError):
    pass
class APIResponseError(LLMError):
    pass