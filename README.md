This is an MVCE for a bug in [Sphinx](https://www.sphinx-doc.org) in which
`:meta private:` fields are not honored by autodoc when the fields come after a
field containing indented text.

To use this MVCE, install [hatch](https://hatch.pypa.io), run `hatch run
docs:run`, and then open `docs/build/index.html`.
