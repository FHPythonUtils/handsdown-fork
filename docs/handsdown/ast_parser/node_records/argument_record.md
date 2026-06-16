# ArgumentRecord

Wrapper for an `ast.arg` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / ArgumentRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.argument_record](../../../../handsdown/ast_parser/node_records/argument_record.py) module.

- [ArgumentRecord](#argumentrecord)
  - [ArgumentRecord](#argumentrecord-1)
    - [ArgumentRecord().default](#argumentrecord()default)
    - [ArgumentRecord().related_names](#argumentrecord()related_names)
    - [ArgumentRecord().required](#argumentrecord()required)
    - [ArgumentRecord().set_default](#argumentrecord()set_default)

## ArgumentRecord

[Show source in argument_record.py:15](../../../../handsdown/ast_parser/node_records/argument_record.py#L15)

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.
- `name` - Argument name.
- `type_hint` - Argument type hint.
- `prefix` - Prefix for arguemnt name, used for starargs.

#### Signature

```python
class ArgumentRecord(NodeRecord):
    def __init__(
        self,
        node: ast.arg,
        name: str,
        type_hint: ast.expr | None = None,
        prefix: str = "",
    ) -> None: ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ArgumentRecord().default

[Show source in argument_record.py:42](../../../../handsdown/ast_parser/node_records/argument_record.py#L42)

Default value of the argument.

#### Returns

Default exression or None.

#### Signature

```python
@property
def default(self) -> ExpressionRecord | None: ...
```

### ArgumentRecord().related_names

[Show source in argument_record.py:77](../../../../handsdown/ast_parser/node_records/argument_record.py#L77)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```

### ArgumentRecord().required

[Show source in argument_record.py:53](../../../../handsdown/ast_parser/node_records/argument_record.py#L53)

Whether the argument is required.

#### Returns

True if required, False otherwise.

#### Signature

```python
@property
def required(self) -> bool: ...
```

### ArgumentRecord().set_default

[Show source in argument_record.py:64](../../../../handsdown/ast_parser/node_records/argument_record.py#L64)

Set default expression from test or `ast.AST` node.

#### Arguments

- `node` - Text or AST node.

#### Signature

```python
def set_default(self, node: Node) -> None: ...
```

#### See also

- [Node](../type_defs.md#node)