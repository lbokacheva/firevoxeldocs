# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'FireVoxelDocs'
copyright = '2020, Artem Mikheev and Henry Rusinek'
author = 'FireVoxel'

# The full version, including alpha/beta/rc tags
release = '0.0.6'


master_doc = 'index'

# -- General configuration ---------------------------------------------------

import sphinx_rtd_theme

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autosectionlabel',
              "sphinx_rtd_theme",
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'sphinx.ext.imgmath',
              'sphinx.ext.jsmath',
 #             'rst2pdf.pdfbuilder'
]

html_math_renderer = 'imgmath'
imgmath_image_format = 'png'
imgmath_font_size = 14

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

todo_include_todos = True

numfig = True

# -- Options for HTML output -------------------------------------------------

def setup(app):
    app.add_stylesheet('css/custom.css')

html_show_sourcelink = False

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    'sticky_navigation': True,
    'collapse_navigation': True,
    'includehidden': True,
    'titles_only': True
}

html_logo = '_static/fvlogo.png'

html_favicon = '_static/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output -------------------------------------------------

latex_documents = [('contents', 'firevoxeldocs.tex', 'FireVoxel: User Manual', 'FireVoxel Team', 'manual', False)]

pdf_documents = [('index', u'rst2pdf', u'FireVoxel Documentation', u'FireVoxel Team')]

latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'preamble': '',
    'releasename':"Release ",
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    'figure_align':'htbp',
}

latex_logo = '_static/fvlogo.png'

