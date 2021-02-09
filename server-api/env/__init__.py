import os

__all__ = [
    'BACKEND_ADDRESS',
    'FRONTEND_ADDRESS',
]


def dev():
    import env.dev as config
    return config


def prod():
    import env.prod as config
    return config


mode = os.getenv('MODE')
configs = {
    'DEV': dev,
    'PROD': prod,
}
try:
    config = configs[mode]()
    BACKEND_ADDRESS = config.BACKEND_ADDRESS
    FRONTEND_ADDRESS = config.FRONTEND_ADDRESS
except:
    print(f"environment variable $MODE should have been either "
          f"{', '.join(configs.keys())}. got: {mode}")
    exit(1)
