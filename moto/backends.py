from __future__ import unicode_literals
from moto.swf import swf_backend

BACKENDS = {
    'swf': swf_backend,
}


def get_model(name):
    for backend in BACKENDS.values():
        models = getattr(backend.__class__, '__models__', {})
        if name in models:
            return list(getattr(backend, models[name])())
