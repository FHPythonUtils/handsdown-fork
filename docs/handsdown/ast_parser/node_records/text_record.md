# TextRecord

Wrapper for a text-only `ast.expr` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / TextRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.text_record](../../../../handsdown/ast_parser/node_records/text_record.py) module.

- [TextRecord](#textrecord)
  - [TextRecord](#textrecord-1)
    - [TextRecord().related_names](#textrecord()related_names)

## TextRecord

[Show source in text_record.py:9](../../../../handsdown/ast_parser/node_records/text_record.py#L9)

Wrapper for a text-only `ast.expr` node.

#### Arguments

- `node` - Related AST node.
- `text` - Text to represent it.

#### Signature

```python
class TextRecord(ExpressionRecord):
    def __init__(self, node: ast.AST, text: str) -> None: ...
```

#### See also

- [ExpressionRecord](./expression_record.md#expressionrecord)

### TextRecord().related_names

[Show source in text_record.py:26](../../../../handsdown/ast_parser/node_records/text_record.py#L26)

A list of fake `ast.Name.id` records inside the node.

#### Examples

```python
TextRecord(ast_node, 'Union[str, MyClass]').related_names
{'Union', 'str', 'MyClass'}
```

#### Returns

A set of related names.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```