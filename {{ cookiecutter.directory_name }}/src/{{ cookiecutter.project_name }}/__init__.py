try:
    import importlib.metadata as importlib_metadata
except ModuleNotFoundError:
    import importlib_metadata

__author__ = "{{ cookiecutter.author }}"
__version__ = importlib_metadata.version(__name__)
