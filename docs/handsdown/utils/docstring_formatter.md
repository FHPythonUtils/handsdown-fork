# DocstringFormatter

Translator of docstrings to Markdown format.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Utils](./index.md#utils) / DocstringFormatter

> Auto-generated documentation for [handsdown.utils.docstring_formatter](../../../handsdown/utils/docstring_formatter.py) module.

- [DocstringFormatter](#docstringformatter)
  - [DocstringFormatter](#docstringformatter-1)
    - [DocstringFormatter._cleanup](#docstringformatter_cleanup)
    - [DocstringFormatter().render](#docstringformatter()render)

## DocstringFormatter

[Show source in docstring_formatter.py:7](../../../handsdown/utils/docstring_formatter.py#L7)

Translator of docstrings to Markdown format.

#### Arguments

- `docstring` - Raw docstring.

#### Signature

```python
class DocstringFormatter:
    def __init__(self, docstring: str) -> None: ...
```

### DocstringFormatter._cleanup

[Show source in docstring_formatter.py:23](../../../handsdown/utils/docstring_formatter.py#L23)

Fix multiline docstrings starting with no newline after quotes.

#### Arguments

- `docstring` - Raw docstring.

#### Returns

Aligned docstring.

#### Signature

```python
@staticmethod
def _cleanup(docstring: str) -> str: ...
```

### DocstringFormatter().render

[Show source in docstring_formatter.py:57](../../../handsdown/utils/docstring_formatter.py#L57)

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.

#### Signature

```python
def render(self) -> str: ...
```