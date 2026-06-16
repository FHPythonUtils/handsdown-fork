# ModuleAnalyzer

AST analyzer for `ast.Module` records.

[Handsdown API Index](../../../README.md#handsdown-api-index) / [Handsdown](../../index.md#handsdown) / [AST Parser.](../index.md#ast-parser) / [Analyzers](./index.md#analyzers) / ModuleAnalyzer

> Auto-generated documentation for [handsdown.ast_parser.analyzers.module_analyzer](../../../../handsdown/ast_parser/analyzers/module_analyzer.py) module.

- [ModuleAnalyzer](#moduleanalyzer)
  - [ModuleAnalyzer](#moduleanalyzer-1)
    - [ModuleAnalyzer().visit_AnnAssign](#moduleanalyzer()visit_annassign)
    - [ModuleAnalyzer().visit_Assign](#moduleanalyzer()visit_assign)
    - [ModuleAnalyzer().visit_AsyncFunctionDef](#moduleanalyzer()visit_asyncfunctiondef)
    - [ModuleAnalyzer().visit_ClassDef](#moduleanalyzer()visit_classdef)
    - [ModuleAnalyzer().visit_FunctionDef](#moduleanalyzer()visit_functiondef)
    - [ModuleAnalyzer().visit_Import](#moduleanalyzer()visit_import)
    - [ModuleAnalyzer().visit_ImportFrom](#moduleanalyzer()visit_importfrom)

## ModuleAnalyzer

[Show source in module_analyzer.py:10](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L10)

AST analyzer for `ast.Module` records.

#### Signature

```python
class ModuleAnalyzer(BaseAnalyzer):
    def __init__(self) -> None: ...
```

#### See also

- [BaseAnalyzer](./base_analyzer.md#baseanalyzer)

### ModuleAnalyzer().visit_AnnAssign

[Show source in module_analyzer.py:183](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L183)

Parse info about module attribute statements.

Adds new `ast.AnnAssign` entry to `attribute_nodes`.
Skips assignments with names starting with `_`.

#### Examples

```python
MY_MODULE_INT: int
MY_MODULE_ATTR: str = 'value'
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_AnnAssign(self, node: ast.AnnAssign) -> None: ...
```

### ModuleAnalyzer().visit_Assign

[Show source in module_analyzer.py:132](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L132)

Parse info about module attribute statements.

Adds new `ast.Assign` entry to `attribute_nodes`.
Skips assignments to anything other than a new variable.
Skips multiple assignments.
Skips assignments with names starting with `_`.
Parses `__all__` and add all values to `all_names`

#### Examples

```python
MY_MODULE_ATTR = 'value'
    my_attr = "value"
__all__ = ['MyClass', 'my_func']

# these entries are skipped
_MY_MODULE_ATTR = "value"
multi_attr_1, multi_attr_2 = [1, 2]
my_object.name = "value"
__all__ = all_list
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Assign(self, node: ast.Assign) -> None: ...
```

### ModuleAnalyzer().visit_AsyncFunctionDef

[Show source in module_analyzer.py:113](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L113)

Parse info about module `def ...` statements.

Adds `node` entry to `function_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
async def my_func(arg1):
    return await arg1
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None: ...
```

### ModuleAnalyzer().visit_ClassDef

[Show source in module_analyzer.py:57](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L57)

Parse info about module `class ...` statements.

Adds `node` entry to `class_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
class MyClass():
    pass
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ClassDef(self, node: ast.ClassDef) -> None: ...
```

### ModuleAnalyzer().visit_FunctionDef

[Show source in module_analyzer.py:94](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L94)

Parse info about module `def ...` statements.

Adds `node` entry to `function_nodes`.
Skips nodes with names starting with `_`.

#### Examples

```python
def my_func(arg1):
    return arg1
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_FunctionDef(self, node: ast.FunctionDef) -> None: ...
```

### ModuleAnalyzer().visit_Import

[Show source in module_analyzer.py:21](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L21)

Parse info about module `import ...` statements.

Adds `node` to `import_nodes`.

#### Examples

```python
import my_module
import my_module as my
import my_module.my_class
import my_module.my_class as my_class
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_Import(self, node: ast.Import) -> None: ...
```

### ModuleAnalyzer().visit_ImportFrom

[Show source in module_analyzer.py:40](../../../../handsdown/ast_parser/analyzers/module_analyzer.py#L40)

Parse info about module `import ... from ...` statements.

Adds `node` to `import_nodes`.

#### Examples

```python
from my_module import my_class
from my_module import my_class as new_class
```

#### Arguments

- `node` - AST node.

#### Signature

```python
def visit_ImportFrom(self, node: ast.ImportFrom) -> None: ...
```