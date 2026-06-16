# FunctionRecord

Wrapper for an `ast.FunctionDef` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / FunctionRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.function_record](../../../../handsdown/ast_parser/node_records/function_record.py) module.

- [FunctionRecord](#functionrecord)
  - [FunctionRecord](#functionrecord-1)
    - [FunctionRecord().is_init](#functionrecord()is_init)
    - [FunctionRecord().parse_type_comments](#functionrecord()parse_type_comments)
    - [FunctionRecord().related_names](#functionrecord()related_names)

## FunctionRecord

[Show source in function_record.py:17](../../../../handsdown/ast_parser/node_records/function_record.py#L17)

Wrapper for an `ast.FunctionDef` and `ast.AsyncFunctionDef` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class FunctionRecord(NodeRecord):
    def __init__(self, node: ASTFunctionDef, is_method: bool) -> None: ...
```

#### See also

- [ASTFunctionDef](../type_defs.md#astfunctiondef)
- [NodeRecord](./node_record.md#noderecord)

### FunctionRecord().is_init

[Show source in function_record.py:139](../../../../handsdown/ast_parser/node_records/function_record.py#L139)

Returns True if function is an __init__ method.

#### Signature

```python
def is_init(self) -> bool: ...
```

### FunctionRecord().parse_type_comments

[Show source in function_record.py:96](../../../../handsdown/ast_parser/node_records/function_record.py#L96)

Extract comment type annotations from a function definiition lines.

Sets `arguments_record` to a new `TextRecord` for each found type annotaiton.
Also sets `return_type_hint` to a `TextRecord` if function return type found.

#### Signature

```python
def parse_type_comments(self, lines: Iterable[str]) -> None: ...
```

### FunctionRecord().related_names

[Show source in function_record.py:42](../../../../handsdown/ast_parser/node_records/function_record.py#L42)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```