# ExpressionRecord

Wrapper for an `ast.expr` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / ExpressionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.expression_record](../../../../handsdown/ast_parser/node_records/expression_record.py) module.

- [ExpressionRecord](#expressionrecord)
  - [ExpressionRecord](#expressionrecord-1)
    - [ExpressionRecord().related_names](#expressionrecord()related_names)
    - [ExpressionRecord().render_str](#expressionrecord()render_str)

## ExpressionRecord

[Show source in expression_record.py:10](../../../../handsdown/ast_parser/node_records/expression_record.py#L10)

Wrapper for an `ast.expr` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class ExpressionRecord(NodeRecord):
    def __init__(self, node: ast.AST) -> None: ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ExpressionRecord().related_names

[Show source in expression_record.py:26](../../../../handsdown/ast_parser/node_records/expression_record.py#L26)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```

### ExpressionRecord().render_str

[Show source in expression_record.py:50](../../../../handsdown/ast_parser/node_records/expression_record.py#L50)

Render expression to a string.

#### Signature

```python
def render_str(self) -> str: ...
```