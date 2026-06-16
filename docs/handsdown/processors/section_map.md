# SectionMap

Module for splitting docstring into `Section` groups.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / SectionMap

> Auto-generated documentation for [handsdown.processors.section_map](../../../handsdown/processors/section_map.py) module.

- [SectionMap](#sectionmap)
  - [SectionMap](#sectionmap-1)
    - [SectionMap().__iter__](#sectionmap()__iter__)
    - [SectionMap().add_block](#sectionmap()add_block)
    - [SectionMap().add_line](#sectionmap()add_line)
    - [SectionMap().add_line_indent](#sectionmap()add_line_indent)
    - [SectionMap().trim_block](#sectionmap()trim_block)

## SectionMap

[Show source in section_map.py:9](../../../handsdown/processors/section_map.py#L9)

Dict-based storage for parsed `Section` list.

Used for [BaseDocstringProcessor](./base.md#basedocstringprocessor).

Key is a `Section` title.
Value is a related `Section` instance.

#### Signature

```python
class SectionMap:
    def __init__(self) -> None: ...
```

### SectionMap().__iter__

[Show source in section_map.py:97](../../../handsdown/processors/section_map.py#L97)

Iterate over existing `Section` objects.

#### Yields

`Section` objects in order of appearance.

#### Signature

```python
def __iter__(self) -> Iterator[Section]: ...
```

#### See also

- [Section](./section.md#section)

### SectionMap().add_block

[Show source in section_map.py:65](../../../handsdown/processors/section_map.py#L65)

Add new `SectionBlock` to section `section_name`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title

#### Signature

```python
def add_block(self, section_name: str) -> None: ...
```

### SectionMap().add_line

[Show source in section_map.py:41](../../../handsdown/processors/section_map.py#L41)

Add new `line` to the last `SectionBlock` of section `section_name`.

If line and section are empty - section is not created.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

#### Signature

```python
def add_line(self, section_name: str, line: str) -> None: ...
```

### SectionMap().add_line_indent

[Show source in section_map.py:24](../../../handsdown/processors/section_map.py#L24)

Add line respecting indent of the current section block.

#### Arguments

- `section_name` - Target section title
- `line` - Line to add

#### Signature

```python
def add_line_indent(self, section_name: str, line: str) -> None: ...
```

### SectionMap().trim_block

[Show source in section_map.py:80](../../../handsdown/processors/section_map.py#L80)

Delete last empty lines from the last `SectionBlock`.

If `Section` does not exist - it is not created.

#### Arguments

- `section_name` - Target section title.

#### Signature

```python
def trim_block(self, section_name: str) -> None: ...
```