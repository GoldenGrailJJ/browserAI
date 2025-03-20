import os

def get_key():
    api_key = os.getenv('DEEPSEEK_API_KEY', 'sk-54c2281102c547d6ac1bbd2788a534e4')
    if not api_key:
        raise ValueError('DEEPSEEK_API_KEY is not set')
    return api_key