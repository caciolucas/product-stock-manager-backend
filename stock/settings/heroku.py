# https://www.youtube.com/watch?v=f6PVDxCB08A&ab_channel=FabioRuicci
import environ

from stock.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}
