"""Sphinx configuration."""
project = "Telegram Hq Builder"
author = "Luiz Sena"
copyright = "2025, Luiz Sena"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
