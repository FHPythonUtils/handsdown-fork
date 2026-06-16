# ModuleRecordList

Aggregation of `ModuleRecord` objects.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [AST Parser.](./index.md#ast-parser) / ModuleRecordList

> Auto-generated documentation for [handsdown.ast_parser.module_record_list](../../../handsdown/ast_parser/module_record_list.py) module.

- [ModuleRecordList](#modulerecordlist)
  - [ModuleRecordList](#modulerecordlist-1)
    - [ModuleRecordList().__iter__](#modulerecordlist()__iter__)
    - [ModuleRecordList().add](#modulerecordlist()add)
    - [ModuleRecordList().find_module_record](#modulerecordlist()find_module_record)
    - [ModuleRecordList().get_package_names](#modulerecordlist()get_package_names)

## ModuleRecordList

[Show source in module_record_list.py:15](../../../handsdown/ast_parser/module_record_list.py#L15)

Aggregation of `ModuleRecord` objects.

#### Signature

```python
class ModuleRecordList:
    def __init__(self) -> None: ...
```

### ModuleRecordList().__iter__

[Show source in module_record_list.py:67](../../../handsdown/ast_parser/module_record_list.py#L67)

Iterate over all added `ModuleRecord` entries.

#### Yields

`ModuleRecord` entries.

#### Signature

```python
def __iter__(self) -> Iterator[ModuleRecord]: ...
```

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().add

[Show source in module_record_list.py:56](../../../handsdown/ast_parser/module_record_list.py#L56)

Add new `ModuleRecord`.

#### Arguments

- `module_record` - A new `ModuleRecord`

#### Signature

```python
def add(self, module_record: ModuleRecord) -> None: ...
```

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().find_module_record

[Show source in module_record_list.py:23](../../../handsdown/ast_parser/module_record_list.py#L23)

Find `ModuleRecord` by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found `NodeRecord` instance or None.

#### Signature

```python
def find_module_record(self, import_string: ImportString) -> ModuleRecord | None: ...
```

#### See also

- [ImportString](../utils/import_string.md#importstring)

### ModuleRecordList().get_package_names

[Show source in module_record_list.py:46](../../../handsdown/ast_parser/module_record_list.py#L46)

Get top level import strings.

#### Returns

A set of top level imports as strings.

#### Signature

```python
def get_package_names(self) -> set[str]: ...
```