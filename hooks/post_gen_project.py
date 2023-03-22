import os
import subprocess
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

subprocess.check_call("cd", "{{ cookiecutter.directory_name }}")
subprocess.check_call("git", "init")
subprocess.check_call("git", "add", ".")
subprocess.check_call("git", "commit", "-m", "'Initial commit'")
