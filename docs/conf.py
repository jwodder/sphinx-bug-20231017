project = "sphinx-bug-20231017"
author = "John Thorvald Wodder II"
version = "0.0.0"
release = version

extensions = ["sphinx.ext.autodoc", "sphinx.ext.intersphinx"]

autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

exclude_patterns = ["build"]
source_suffix = ".rst"
source_encoding = "utf-8"
master_doc = "index"
today_fmt = "%Y %b %d"
default_role = "py:obj"
pygments_style = "sphinx"

html_theme = "alabaster"
html_last_updated_fmt = "%Y %b %d"
html_show_copyright = False
