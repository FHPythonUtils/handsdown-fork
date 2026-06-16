# Section

Section in a `SectionMap`.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / Section

> Auto-generated documentation for [handsdown.processors.section](../../../handsdown/processors/section.py) module.

- [Section](#section)
  - [Section](#section-1)
    - [Section().iterate_blocks](#section()iterate_blocks)
    - [Section().render](#section()render)

## Section

[Show source in section.py:7](../../../handsdown/processors/section.py#L7)

Section in a `SectionMap`.

#### Arguments

- `title` - Section title.
- `blocks` - List of line blocks.

#### Signature

```python
class Section:
    def __init__(self, title: str, blocks: Iterable[SectionBlock]) -> None: ...
```

#### See also

- [SectionBlock](./section_block.md#sectionblock)

### Section().iterate_blocks

[Show source in section.py:33](../../../handsdown/processors/section.py#L33)

Iterate over all non-empty Section block lines.

#### Returns

Section block lines.

#### Signature

```python
def iterate_blocks(self) -> Iterable[SectionBlock]: ...
```

#### See also

- [SectionBlock](./section_block.md#sectionblock)

### Section().render

[Show source in section.py:21](../../../handsdown/processors/section.py#L21)

Render all Section block lines.

#### Returns

Section lines as a text.

#### Signature

```python
def render(self) -> str: ...
```