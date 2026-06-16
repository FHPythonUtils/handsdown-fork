# Strings

Utils for strings.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Utils](./index.md#utils) / Strings

> Auto-generated documentation for [handsdown.utils.strings](../../../handsdown/utils/strings.py) module.

- [Strings](#strings)
  - [extract_md_title](#extract_md_title)
  - [make_title](#make_title)

## extract_md_title

[Show source in strings.py:46](../../../handsdown/utils/strings.py#L46)

Extract title from the first line of content.

If title is present - return a title and a remnaing content.
if not - return an empty title and untouched content.

#### Examples

```python
extract_md_title('# Title\ncontent')
('Title', 'content')

extract_md_title('no title\ncontent')
('', 'no title\ncontent')
```

#### Returns

A tuple fo title and remaining content.

#### Signature

```python
def extract_md_title(content: str) -> tuple[str, str]: ...
```



## make_title

[Show source in strings.py:4](../../../handsdown/utils/strings.py#L4)

Convert `pathlib.Path` part or any other string to a human-readable title.

Replace underscores with spaces and capitalize result.

#### Examples

```python
make_title(Path("my_module/my_path.py").stem)
"My Path"

make_title("my_title")
"My Title"

make_title("__init__.py")
"Init Py"

make_title(Path("my_module/__main__.py").stem)
"Module"
```

#### Arguments

- `file_stem` - Stem from path.

#### Returns

A human-readable title as a string.

#### Signature

```python
def make_title(file_stem: str) -> str: ...
```