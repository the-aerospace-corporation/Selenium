# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'selenium'
copyright = '2022, Don Walker'
author = 'Don Walker'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

autoclass_content = 'both'

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,}

autodoc_typehints = "description"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    "sphinx_rtd_theme",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
