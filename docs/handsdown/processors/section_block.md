# SectionBlock

`Section` block.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Processors](./index.md#processors) / SectionBlock

> Auto-generated documentation for [handsdown.processors.section_block](../../../handsdown/processors/section_block.py) module.

- [SectionBlock](#sectionblock)
  - [SectionBlock](#sectionblock-1)
    - [SectionBlock().render](#sectionblock()render)

## SectionBlock

[Show source in section_block.py:7](../../../handsdown/processors/section_block.py#L7)

`Section` block.

#### Arguments

- `lines` - List of lines.

#### Signature

```python
class SectionBlock:
    def __init__(self, lines: Iterable[str]) -> None: ...
```

### SectionBlock().render

[Show source in section_block.py:19](../../../handsdown/processors/section_block.py#L19)

Render trimmed block lines.

#### Returns

Block lines as a text.

#### Signature

```python
def render(self) -> str: ...
```