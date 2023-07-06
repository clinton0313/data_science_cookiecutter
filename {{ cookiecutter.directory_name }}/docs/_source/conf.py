# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "{{ cookiecutter.rpoject_name }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    'sphinx_toolbox.more_autodoc.variables',
    "myst_parser",
    "sphinx.ext.githubpages",
]

templates_path = ["_templates"]
exclude_patterns = []

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "myst_parser.sphinx_"
}

modindex_common_prefix = ["{{ cookiecutter.project_name }}."]
add_module_names = False
autodoc_typehints = "description"

# -- AutoDoc Configuration -------------------------------------------------------

autoclass_content = "both"
autodoc_preserve_defaults = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "member-order": "bysource",
    "show-inheritance": True,
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
