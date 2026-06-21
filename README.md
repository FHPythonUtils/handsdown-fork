# 🙌 Handsdown-fork

[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](https://pypistats.org/packages/handsdown-fork)
[![PyPI Total Downloads](https://img.shields.io/pepy/dt/handsdown-fork?style=for-the-badge&label=Total%20Downloads&cacheSeconds=28800)](https://pepy.tech/project/handsdown-fork)
[![PyPI Version](https://img.shields.io/pypi/v/handsdown-fork.svg?style=for-the-badge&cacheSeconds=28800)](https://pypi.org/project/handsdown-fork)

A fork of handsdown, the python docstring-based documentation generator for lazy perfectionists.

Huge thanks to <https://github.com/vemel/handsdown> for all of the groundwork!

- [🙌 Handsdown-fork](#-handsdown-fork)
  - [Features](#features)
  - [Do you need handsdown-fork?](#do-you-need-handsdown-fork)
  - [Examples](#examples)
  - [Usage](#usage)
    - [💻 From command line](#-from-command-line)
    - [🚀 Use a new Material design](#-use-a-new-material-design)
    - [📝 As a GitHub Pages manager](#-as-a-github-pages-manager)
    - [🐏 Deploy on Read the Docs](#-deploy-on-read-the-docs)
    - [📋 Build static HTML](#-build-static-html)
    - [🧩 As a module](#-as-a-module)
    - [⌨️ CLI arguments](#️-cli-arguments)
  - [Project Documentation](#project-documentation)
  - [Installation](#installation)
  - [Language information](#language-information)
  - [Working with the repo](#working-with-the-repo)
  - [Community Files](#community-files)
    - [Licence](#licence)
    - [Code of Conduct](#code-of-conduct)
    - [Contributing](#contributing)
    - [Security](#security)
    - [Support](#support)

## Features

- [Material design](#-use-a-new-material-design) support!
- [PEP 257](https://www.python.org/dev/peps/pep-0257/),
  [Google](http://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings),
  [Sphinx](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html)
  and [reStructuredText](https://www.python.org/dev/peps/pep-0287/)
  docstrings support. All of them are converted to a valid Markdown.
- Works with [Django](https://www.djangoproject.com/) and [Flask](https://palletsprojects.com/p/flask/) apps
- Can be used locally, or
  [right on GitHub](https://github.com/FHPythonUtils/handsdown-fork/blob/docs/README.md) or even deployed on
  [GitHub Pages](https://vemel.github.io/handsdown/) and [Read the Docs](https://handsdown.readthedocs.io/)!
- Signatures for every class, function, property and method.
- Support for type annotations. Even for the ones from the `__future__`!
- Nice list of all modules in [Index](https://github.com/FHPythonUtils/handsdown-fork/blob/docs/README.md)
- Gather all scattered `README.md` in submodules to one place
- Find related source code from every doc section.
- Make links by just adding `module.import.String` to docs.
- Do you use type annotations? Well, you get auto-discovery of related modules for free!

## Do you need handsdown-fork?

You definitely *do* if you:

- prefer to automate documentation builds
- work with a team and plan to simplify knowledge sharing
- want to show your project without navigating through a source code
- build `Django` or `Flask` applications
- are proud of your project and not afraid to show it
- love Open Source

## Examples

- [All documentation](https://vemel.github.io/handsdown/) in this project
- [Main](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/main_example.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/main_example.md)
- [RST docstrings](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/rst_docstrings.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/rst_docstrings.md)
- [Google docstrings](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/google_docstrings.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/google_docstrings.md)
- [PEP 257 docstrings](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/pep257_docstrings.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/pep257_docstrings.md)
- [Sphinx docstrings](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/sphinx_docstrings.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/sphinx_docstrings.md)
- [Type annotations](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/typed.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/typed.md)
- [Comment-style type annotations](https://github.com/FHPythonUtils/handsdown-fork/blob/main/examples/comment_typed.py) with [generated output](https://github.com/FHPythonUtils/handsdown-fork/tree/docs/examples/comment_typed.md)

## Usage

### 💻 From command line

Just go to your favorite project that has lots of docstrings but missing
auto-generated docs and let `handsdown` do the thing.

```bash
cd ~/my/project

# build documentation *.md* files in docs/* directory
handsdown

# or provide custom output directory: output_dir/*
handsdown -o output_dir

# generate docs only for my_module, but exclude migrations
handsdown my_module --exclude my_module/migrations

# generate documentation for deployment
handsdown --external `git config --get remote.origin.url` -n ProjectName --branch main --create-configs
```

Navigate to `docs/README.md` to check your new documentation!

### 🚀 Use a new Material design

- Add `mkdocs` and `mkdocs-material` to your dev dependencies or just install them

```bash
# generate MarkDown documentation in docsmd folder
handsdown --external `git config --get remote.origin.url` -o docsmd -n <project_name> --theme=material --create-configs

# generate html files to docs folder
python -m mkdocs build
```
<!-- 
### 📦 As a Docker image

Work in progress  -->

### 📝 As a GitHub Pages manager

With `--external` CLI flag, `handsdown` generates all required configuration
for [GitHub Pages](https://pages.github.com/), so you just need to setup your
GitHub repository.

```bash
# Generate documentation that points to main branch
# do not use custom output location, as `GitHub Pages`
# works only with `docs` directory
handsdown --external `git config --get remote.origin.url` --create-configs

# or specify GitHub url directly
handsdown --external https://github.com/<user>/<project> --create-configs
```

- Generate documentation with `--external` flag as shown above, do not use `--output`
  flag, only `docs` folder is supported by `GitHub Pages`
- Commit and push all changes a to `main` branch.
- Set your GitHub project `Settings` > `GitHub Pages` > `Source` to `main branch /docs folder`

All set! You can change `docs/_config.yml` to add your own touch.

With `--external` flag links to your source are absolute and point to your GitHub repo. If you
still want to have relative links to source, e.g. for using docs locally,
generate docs to another folder

```bash
# `docs_local` folder will be created in your project root
# you probably want to add it to .gitignore
handsdown -o docs_local
```

### 🐏 Deploy on Read the Docs

With `--external` CLI flag, `handsdown` generates all required configuration
for [Read the Docs](https://readthedocs.org/), so you just need to to add your
GitHub repository to `Read the Docs`.

```bash
# Generate documentation that points to main branch
# do not use custom output location, as `GitHub Pages`
# works only with `docs` directory
handsdown --external `git config --get remote.origin.url` --create-configs

# or specify GitHub url directly
handsdown --external https://github.com/<user>/<project>/ --create-configs
```

- Generate documentation with `--external` flag as shown above, do not use `--output`
  flag, only `docs` folder is supported by `Read the Docs`
- Commit and push all changes a to `main` branch.
- Add your repository on [Read the Docs](https://readthedocs.org/)

All set! You can change `.readthedocs.yml` and `mkdocs.yml` to add your own touch.

### 📋 Build static HTML

```bash
# Generate documentation that points to main branch
# with source links pointing to your repository
# this command also creates `mkdocs.yml`
handsdown --external `git config --get remote.origin.url` --create-configs

# Run mkdocs to build HTML
python -m mkdocs build
```

### 🧩 As a module

```python
from handsdown.generator import Generator
from handsdown.utils.path_finder import PathFinder

# this is our project root directory
repo_path = Path.cwd()

# this little tool works like `pathlib.Path.glob` with some extra magic
# but in this case `repo_path.glob("**/*.py")` would do as well
path_finder = PathFinder(repo_path, "**/*.py")

# no docs for tests and build
path_finder.exclude("tests/*", "build/*")

# initialize generator
handsdown = Generator(
    input_path=repo_path,
    output_path=repo_path / 'output',
    source_paths=path_finder.glob("**/*.py")
)

# generate all docs at once
handsdown.generate_docs()

# or generate just for one doc
handsdown.generate_doc(repo_path / 'my_module' / 'source.py')

# generate index.md file
handsdown.generate_index()

# and generate GitHub Pages and Read the Docs config files
handsdown.generate_configs()

# navigate to `output` dir and check results
```

### ⌨️ CLI arguments

```bash
handsdown [-h] [--exclude [EXCLUDE ...]] [-i INPUT_PATH] [-f [FILES ...]]
  [-o OUTPUT_PATH] [--external REPO_URL] [--source-code-path REPO_PATH]
  [--branch BRANCH] [--toc-depth TOC_DEPTH] [--cleanup] [-n PROJECT_NAME]
  [-e ENCODING] [--panic] [-d] [-q] [-V]
  [include ...]
```

| Argument | Description | Default |
|-|-|-|
| `include` | Path expressions to include source files | |
| `--exclude` | Path expressions to exclude source files | `'build/*' 'tests/*' 'test/*' '*/__pycache__/*' '.*/*'` |
| `-i` / `--input-path` | Path to project root folder | `<cwd>` |
| `-f` / `--files` | List of source files to use for generation. If empty - all are used. | |
| `-o` / `--output-path` | Path to output folder | `<cwd>/docs` |
| `--external` | Build docs and config for external hosting, GitHub Pages or Read the Docs. Provide the project GitHub .../blob/main/ URL here. | |
| `--source-code-path` | Path to source code in the project. Overrides `--branch` CLI argument | |
| `--branch` | Main branch name | `main` |
| `--toc-depth` | Maximum depth of child modules ToC | `3` |
| `--cleanup` | Remove orphaned auto-generated docs | |
| `-n` / `--name` | Project name | `<cwd>.name` |
| `-e` / `--encoding` | Input and output file encoding | `utf-8` |
| `--panic` | Panic and die on import error | |
| `--debug` | Show debug messages| |
| `--quiet` | Hide log output | |
| `--create-configs` | Create config files for deployment to RtD and GitHub Pages | |
| `-t` / `--theme` | Output mkdocs theme: `readthedocs` or `material` | `readthedocs` |
| `-h` | Show help | |

## Project Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

<!--
- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
-->
- The [Technical Reference](/docs) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software. Note this is generated
  with handsdown-fork
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Installation

Install using `pip` from PyPI

```bash
pip install handsdown-fork
```

or directly from GitHub if you cannot wait to test new features

```bash
pip install git+https://github.com/FHPythonUtils/handsdown-fork.git
```

## Language information

Using python 3.9, to 3.14

## Working with the repo

Clone, the repo with

```bash
git clone https://github.com/FHPythonUtils/handsdown-fork
```

Format

```sh
uv run ruff format
```

Linting

```sh
uv run ruff check
uv run python3 -m basedpyright -p .
```

Testing

```sh
uv run python3 -m pytest
```

Alternatively use `tox` to run tests over a range of python versions

```sh
uvx tox
```

Documentation

```sh
uv run handsdown
```

## Community Files

### Licence

MIT License
Copyright (c) FredHappyface
Copyright (c) 2019 Vlad Emelianov
(See the [LICENSE](/LICENSE) for more information.)

<!-- ### Changelog

See the [Changelog](/CHANGELOG.md) for more information. -->

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.
