# Markdown

Utils for markdown rendering.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Utils](./index.md#utils) / Markdown

> Auto-generated documentation for [handsdown.utils.markdown](../../../handsdown/utils/markdown.py) module.

- [Markdown](#markdown)
  - [Header](#header)
    - [Header().render](#header()render)
  - [TableOfContents](#tableofcontents)
    - [TableOfContents.parse](#tableofcontentsparse)
    - [TableOfContents().render](#tableofcontents()render)
  - [insert_md_toc](#insert_md_toc)

## Header

[Show source in markdown.py:8](../../../handsdown/utils/markdown.py#L8)

Markdown header.

#### Arguments

- `title` - Header title
- `level` - Header level, 1-6
- `anchor` - Anchor link

#### Signature

```python
class Header:
    def __init__(self, title: str, level: int, anchor: str) -> None: ...
```

### Header().render

[Show source in markdown.py:24](../../../handsdown/utils/markdown.py#L24)

Render menu item to string.

#### Signature

```python
def render(self) -> str: ...
```



## TableOfContents

[Show source in markdown.py:30](../../../handsdown/utils/markdown.py#L30)

MarkDown Table of Contents.

#### Arguments

- `headers` - List of headers

#### Signature

```python
class TableOfContents:
    def __init__(self, headers: Iterable[Header]) -> None: ...
```

#### See also

- [Header](#header)

### TableOfContents.parse

[Show source in markdown.py:42](../../../handsdown/utils/markdown.py#L42)

Parse table of Contents for MarkDown text.

#### Arguments

- `text` - MarkDown text.

#### Signature

```python
@classmethod
def parse(cls: type[_R], text: str) -> _R: ...
```

### TableOfContents().render

[Show source in markdown.py:71](../../../handsdown/utils/markdown.py#L71)

Render ToC to string.

#### Signature

```python
def render(self, max_level: int = 3) -> str: ...
```



## insert_md_toc

[Show source in markdown.py:85](../../../handsdown/utils/markdown.py#L85)

Insert Table of Contents before the first second-level header.

#### Signature

```python
def insert_md_toc(text: str, depth: int = 3) -> str: ...
```