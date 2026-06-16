# NodeRecord

Base class for all node records.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / NodeRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.node_record](../../../../handsdown/ast_parser/node_records/node_record.py) module.

- [NodeRecord](#noderecord)
  - [NodeRecord](#noderecord-1)
    - [NodeRecord().class_name](#noderecord()class_name)
    - [NodeRecord().get_documented_attribute_strings](#noderecord()get_documented_attribute_strings)
    - [NodeRecord().line_number](#noderecord()line_number)
    - [NodeRecord().line_number](#noderecord()line_number-1)
    - [NodeRecord().parse](#noderecord()parse)
    - [NodeRecord().related_names](#noderecord()related_names)
    - [NodeRecord().render](#noderecord()render)

## NodeRecord

[Show source in node_record.py:11](../../../../handsdown/ast_parser/node_records/node_record.py#L11)

Base class for all node records.

#### Signature

```python
class NodeRecord:
    def __init__(self, node: ast.AST) -> None: ...
```

### NodeRecord().class_name

[Show source in node_record.py:156](../../../../handsdown/ast_parser/node_records/node_record.py#L156)

Record class name.

#### Signature

```python
@property
def class_name(self) -> str: ...
```

### NodeRecord().get_documented_attribute_strings

[Show source in node_record.py:137](../../../../handsdown/ast_parser/node_records/node_record.py#L137)

Render each of `attribute_records` to a Markdown string.

Includes `name`, `docstring` and `value` of an `ArgumentRecord`.

#### Returns

A list of rendered strings.

#### Signature

```python
def get_documented_attribute_strings(self) -> list[str]: ...
```

### NodeRecord().line_number

[Show source in node_record.py:28](../../../../handsdown/ast_parser/node_records/node_record.py#L28)

Return node line number in source.

#### Returns

A line number startign with 1.

#### Signature

```python
@property
def line_number(self) -> int: ...
```

### NodeRecord().line_number

[Show source in node_record.py:44](../../../../handsdown/ast_parser/node_records/node_record.py#L44)

#### Signature

```python
@line_number.setter
def line_number(self, value: int) -> None: ...
```

### NodeRecord().parse

[Show source in node_record.py:82](../../../../handsdown/ast_parser/node_records/node_record.py#L82)

Get all information from a node.

Executes only once if called multiple times.

#### Signature

```python
def parse(self) -> None: ...
```

### NodeRecord().related_names

[Show source in node_record.py:65](../../../../handsdown/ast_parser/node_records/node_record.py#L65)

Get a set of referenced object names in `node`.

Returns an empty set, should be overriden by a child class.

#### Returns

A set of referenced object name.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```

### NodeRecord().render

[Show source in node_record.py:106](../../../../handsdown/ast_parser/node_records/node_record.py#L106)

Render node to a string.

#### Returns

A string representation of `node`.

#### Signature

```python
def render(self) -> str: ...
```