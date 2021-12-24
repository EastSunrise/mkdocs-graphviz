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

    $ pip install mkdocs-graphviz

# Configuration

## Activation

Activate the `mkdocs_graphviz` extension. For example, with **Mkdocs**, you add a
stanza to `mkdocs.yml`:

```yaml
markdown_extensions:
    - mkdocs_graphviz
```

## Options

**Optionnally**, use any (or a combination) of the following options with all colors being written as **HTML COLORS WITHOUT THE # SIGN** (the default values are written hereafter):

```yaml
markdown_extensions:
    - mkdocs_graphviz:
        color: 999999            # or any other HTML color WITHOUT the '#' sign
        bgcolor: none            # or any other HTML color WITHOUT the '#' sign
        graph_color: 999999      # or any other HTML color WITHOUT the '#' sign
        graph_fontcolor: 999999  # or any other HTML color WITHOUT the '#' sign
        node_color: 999999       # or any other HTML color WITHOUT the '#' sign
        node_fontcolor: 999999   # or any other HTML color WITHOUT the '#' sign
        edge_color: 999999       # or any other HTML color WITHOUT the '#' sign
        edge_fontcolor: 999999   # or any other HTML color WITHOUT the '#' sign

```

Where:

* `color` (default `999999` to be an *average* for dark and light modes in mkdocs) will modify **ALL** the following colors in just one parameter:
    * All Nodes
    * All Texts inside Nodes
    * All Edges
    * All Labels aside Edges
    FORMAT
* `bgcolor` (default `none`) sets :
    * the background color of the graph (HTML FORMAT WITHOUT THE '#' SIGN)
    * sets the graph to be transparent (`bgcolor: none`)
* `graph_color` (default `999999`) sets the color of all Subgraphs/Clusters Roundings (HTML FORMAT WITHOUT THE '#' SIGN)
* `graph_fontcolor` (default `999999`) sets the color of all Subgraphs/Clusters Titles (HTML FORMAT WITHOUT THE '#' SIGN)
* `node_color` (default `999999`) sets the color of all Nodes (HTML FORMAT WITHOUT THE '#' SIGN)
* `node_fontcolor` (default `999999`) sets the color of all Texts inside Nodes (HTML FORMAT WITHOUT THE '#' SIGN)
* `edge_color` (default `999999`) sets the color of all Edges (HTML FORMAT WITHOUT THE '#' SIGN)
* `edge_fontcolor` (default `999999`) sets the color of all Labels aside Edges (HTML FORMAT WITHOUT THE '#' SIGN)

## Mixing Options

* It is possible to define a general color of the graph with the `color` option, and then overwrite some of the values with the other options (you choose)
* Colors defined with the options can always be overwritten as a **per Node basis**, or a **per Edge basis** directly inside of the graphviz/dot syntax

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

# CSS / JS Classes

Each graph has both a `dot` and a `graphviz` class, wich can be customized after rendering (as an image) via CSS / JS.

# Credits

Initially Forked from [cesaremorel/markdown-inline-graphviz](https://github.com/cesaremorel/markdown-inline-graphviz)

Inspired by [jawher/markdown-dot](https://github.com/jawher/markdown-dot),
which renders the dot graph to a file instead of inline.

All Newer Credits : [rodrigo.schwencke/mkdocs-graphviz](https://gitlab.com/rodrigo.schwencke/mkdocs-graphviz)

# License

[MIT License](http://www.opensource.org/licenses/mit-license.php)
