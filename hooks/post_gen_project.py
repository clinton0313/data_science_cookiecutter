import os
import subprocess
import shutil

from cookiecutter.main import cookiecutter

if "{{ cookiecutter.cookiecutter_type }}" == "lite":
    shutil.rmtree("/data", ignore_errors=True)
    shutil.rmtree(os.path.join("tests", "data"), ignore_errors=True)
    os.remove("LICENSE")
    os.remove("mkdocs.yml")
    shutil.rmtree("docs", ignore_errors=True)


subprocess.check_call(["git", "init"])
subprocess.check_call(["git", "add", "."])
subprocess.check_call(["git", "commit", "-m", "'Initial commit'"])
