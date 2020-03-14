from django.contrib import admin
from django.conf import settings
import meyer.models as mod

Models = dict([(name, cls) for name, cls in mod.__dict__.items() if isinstance(cls, type)])

for Name, Model in Models.items():
    admin.site.register(Model)

