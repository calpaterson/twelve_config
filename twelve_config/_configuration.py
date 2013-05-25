from os import environ
from UserDict import DictMixin

class Configuration(DictMixin):
    def __init__(self, prefix="CONFIG"):
        self._config = {}
        for environment_variable in environ:
            if environment_variable.startswith(prefix):
                name = environment_variable[len(prefix) + 1:].lower()
                self._config[name] = environ[environment_variable]

    def __getitem__(self, name):
        lower = name.lower()
        if name in self._config:
            return self._config[name]

    def __setitem__(self, unused_key, unused_value):
        raise NotImplementedError("Not allowed to mutate configuration")

    def __delitem__(self, unused_key):
        raise NotImplementedError("Not allowed to mutate configuration")

    def keys(self):
        return self._config.keys()
