Mkdocs Graphviz (for Python 3)
=======================================

This is a continuation of the great job of (from newer to older):

* Rodrigo Schwencke (for all Newer Credits) : [rodrigo.schwencke/mkdocs-graphviz](https://gitlab.com/rodrigo.schwencke/mkdocs-graphviz)
* Cesare Morel [cesaremorel/markdown-inline-graphviz](https://github.com/cesaremorel/markdown-inline-graphviz),
* Steffen Prince in [sprin/markdown-inline-graphviz](https://github.com/sprin/markdown-inline-graphviz), 
* Initially inspired by Jawher Moussa [jawher/markdown-dot](https://github.com/jawher/markdown-dot)

in order to get it work with pip (for python 3). If you use python 2, please use the original extension instead.

A Python Markdown extension for Mkdocs, that renders inline Graphviz definitions with inline SVGs or PNGs out of the box !

Why render the graphs inline? No configuration! Works with any
Python-Markdown-based static site generator, such as [MkDocs](http://www.mkdocs.org/), [Pelican](http://blog.getpelican.com/), and [Nikola](https://getnikola.com/) out of the box without configuring an output directory.

# Installation

`$ pip install mkdocs-graphviz`

or upgrade via pip (if already installed)

`$ pip install --upgrade mkdocs-graphviz`

# Configuration

## Activation

Activate the `mkdocs_graphviz` extension. For example, with **Mkdocs**, you add a
stanza to `mkdocs.yml`:

```yaml
markdown_extensions:
    - mkdocs_graphviz

extra_javascript:
  - https://cdn.jsdelivr.net/gh/rod2ik/cdn@main/mkdocs/javascripts/mkdocs_graphviz.js
```


## Options

**Optionnally**, use any (or a combination) of the following options with all colors being written as **HTML COLORS WITHOUT THE # SIGN** (the default values are written hereafter):

```yaml
markdown_extensions:
    - mkdocs_graphviz:
        ligthcolor: 000000       # HTML Colors Names or any other any other HTML color WITHOUT the '#' sign
        darkcolor: FFFFFF        # HTML Colors Names or any other any other HTML color WITHOUT the '#' sign
        color: 789ABC            # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        bgcolor: none            # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        graph_color: 789ABC      # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        graph_fontcolor: 789ABC  # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        node_color: 789ABC       # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        node_fontcolor: 789ABC   # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        edge_color: 789ABC       # HTML Colors Names or any other HTML color WITHOUT the '#' sign
        edge_fontcolor: 789ABC   # HTML Colors Names or any other HTML color WITHOUT the '#' sign
```

Where:

* `ligthcolor` (default `000000`) is the **default color of the graph (nodes and edges) in Light Theme** in Mkdocs
* `darkcolor` (default `FFFFFF`) is the **default color of the graph (nodes and edges) in Light Theme** in Mkdocs
* `color` (default `789ABC` is a *blueshish average* which modifies **ALL** the following colors **IN BOTH THEMES (Light and Dark)** in just one parameter:
    * All Nodes
    * All Texts inside Nodes
    * All Edges
    * All Labels aside Edges
    FORMAT
* `bgcolor` (default `none`) sets :
    * the background color of the graph (HTML FORMAT WITHOUT THE '#' SIGN)
    * sets the graph to be transparent (`bgcolor: none`)
* `graph_color` (default `789ABC`) sets the color of all Subgraphs/Clusters Roundings (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)
* `graph_fontcolor` (default `789ABC`) sets the color of all Subgraphs/Clusters Titles (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)
* `node_color` (default `789ABC`) sets the color of all Nodes (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)
* `node_fontcolor` (default `789ABC`) sets the color of all Texts inside Nodes (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)
* `edge_color` (default `789ABC`) sets the color of all Edges (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)
* `edge_fontcolor` (default `789ABC`) sets the color of all Labels aside Edges (HTML Standard Names or HTML Hexadecimal FORMAT WITHOUT THE '#' SIGN)

## Color Codes

Color Codes can be :

* a **standard HTML Color Name** as in [this W3C page](https://www.w3schools.com/tags/ref_colornames.asp) (All Caps Allowed)
* an **HTML HEXADÉCIMAL COLOR WITHOUT THE # SIGN**

## Mixing & Conflicting Options

* It is possible to define a general color of the graph with the `color` option, and then overwrite some of the values with the other options (you choose)
* Colors defined with the options can always be overwritten as a **per Node basis**, or a **per Edge basis** directly inside of the graphviz/dot syntax
* `color` option takes precedence over `lightcolor` and `darkcolor` options, but not over other options

# Usage

To use it in your Markdown doc, 

with SVG output:

    ```dot
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
    ```

or

    ```graphviz dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
    ```

or with PNG:

    ```graphviz dot attack_plan.png
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
    ```

**Supported Graphviz commands: dot, neato, fdp, sfdp, twopi, circo.**

Other examples in these pages:

* Trees : https://eskool.gitlab.io/tnsi/donnees/arbres/quelconques/
* Graphs : https://eskool.gitlab.io/tnsi/donnees/graphes/definitions/

# CSS / JS Classes

* Each graph has both a `dot` and a `graphviz` class in the `<svg>` tag, wich can be used for further customization via CSS / JS.
* Note that Javascript rod2ik's cdn `mkdocs_graphvis.js` **MUST BE SET** in `mkdocs.yml` for `lightcolor` and `darkcolor` options to be functionnal. All the other functionnalities don't need this extra Javascript.

```yaml
extra_javascript:
  - https://cdn.jsdelivr.net/gh/rod2ik/cdn@main/mkdocs/javascripts/mkdocs_graphviz.js
```

# Credits

Initially Forked from [cesaremorel/markdown-inline-graphviz](https://github.com/cesaremorel/markdown-inline-graphviz)

Inspired by [jawher/markdown-dot](https://github.com/jawher/markdown-dot),
which renders the dot graph to a file instead of inline.

All Newer Credits : [rodrigo.schwencke/mkdocs-graphviz](https://gitlab.com/rodrigo.schwencke/mkdocs-graphviz)

# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
