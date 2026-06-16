# ClassRecord

Wrapper for an `ast.ClassDef` node.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Node Records](./index.md#node-records) / ClassRecord

> Auto-generated documentation for [handsdown.ast_parser.node_records.class_record](../../../../handsdown/ast_parser/node_records/class_record.py) module.

- [ClassRecord](#classrecord)
  - [ClassRecord](#classrecord-1)
    - [ClassRecord().find_record](#classrecord()find_record)
    - [ClassRecord().get_public_methods](#classrecord()get_public_methods)
    - [ClassRecord().init_method](#classrecord()init_method)
    - [ClassRecord().iter_records](#classrecord()iter_records)
    - [ClassRecord().related_names](#classrecord()related_names)

## ClassRecord

[Show source in class_record.py:20](../../../../handsdown/ast_parser/node_records/class_record.py#L20)

Wrapper for an `ast.ClassDef` node.

#### Arguments

- `node` - AST node.

#### Signature

```python
class ClassRecord(NodeRecord):
    def __init__(self, node: ast.ClassDef) -> None: ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ClassRecord().find_record

[Show source in class_record.py:39](../../../../handsdown/ast_parser/node_records/class_record.py#L39)

Find child method or attribute record.

#### Arguments

- `name` - Record name to lookup.

#### Returns

Itself or None.

#### Signature

```python
def find_record(self, name: str) -> NodeRecord | None: ...
```

### ClassRecord().get_public_methods

[Show source in class_record.py:90](../../../../handsdown/ast_parser/node_records/class_record.py#L90)

Get Class public methods.

Skips methods with names starting with `_` and magic methods  `__` if
they have no docstring. Method `__init__` is always skipped.

#### Returns

A list of child records.

#### Signature

```python
def get_public_methods(self) -> list[FunctionRecord]: ...
```

#### See also

- [FunctionRecord](./function_record.md#functionrecord)

### ClassRecord().init_method

[Show source in class_record.py:130](../../../../handsdown/ast_parser/node_records/class_record.py#L130)

Get the `__init__` method.

#### Signature

```python
@property
def init_method(self) -> FunctionRecord | None: ...
```

### ClassRecord().iter_records

[Show source in class_record.py:78](../../../../handsdown/ast_parser/node_records/class_record.py#L78)

Iterate over Class public methods.

#### Yields

A child record.

#### Signature

```python
def iter_records(self) -> Iterator[NodeRecord]: ...
```

#### See also

- [NodeRecord](./node_record.md#noderecord)

### ClassRecord().related_names

[Show source in class_record.py:63](../../../../handsdown/ast_parser/node_records/class_record.py#L63)

Set of related names.

#### Signature

```python
@property
def related_names(self) -> set[str]: ...
```