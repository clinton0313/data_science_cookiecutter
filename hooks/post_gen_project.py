import os
import sys

from cookiecutter.main import cookiecutter

if "{{ cookiecutter.cookiecutter_type }}" == "lite":
    try:
        os.removedirs("data")
        os.removedirs(os.path.join("tests", "data"))
        os.remove("LICENSE")
        os.remove("mkdocs.yml")
        os.removedirs("docs")
    except:
        sys.exit(1)