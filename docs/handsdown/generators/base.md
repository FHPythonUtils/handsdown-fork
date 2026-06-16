# Base

Main handsdown documentation generator.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Generators](./index.md#generators) / Base

> Auto-generated documentation for [handsdown.generators.base](../../../handsdown/generators/base.py) module.

- [Base](#base)
  - [BaseGenerator](#basegenerator)
    - [BaseGenerator()._write_changed](#basegenerator()_write_changed)
    - [BaseGenerator().cleanup_old_docs](#basegenerator()cleanup_old_docs)
    - [BaseGenerator().generate_doc](#basegenerator()generate_doc)
    - [BaseGenerator().generate_docs](#basegenerator()generate_docs)
    - [BaseGenerator().generate_external_configs](#basegenerator()generate_external_configs)
    - [BaseGenerator().generate_index](#basegenerator()generate_index)
    - [BaseGenerator().get_children_module_records](#basegenerator()get_children_module_records)
    - [BaseGenerator().get_external_configs_templates](#basegenerator()get_external_configs_templates)
    - [BaseGenerator().get_md_document](#basegenerator()get_md_document)
    - [BaseGenerator().get_see_also_links](#basegenerator()get_see_also_links)
    - [BaseGenerator().replace_links](#basegenerator()replace_links)

## BaseGenerator

[Show source in base.py:31](../../../handsdown/generators/base.py#L31)

#### Attributes

- `INDEX_NAME` - Index filename: 'README.md'

- `INDEX_TITLE` - Index title: 'Index'

- `insert_toc` - Whether to add ToC to generated module docs: False


Base documentation generator.

#### Arguments

- `project_name` - Name of the project.
- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise `LoaderError` instead of silencing in.
- `source_code_url` - URL to source files to use instead of relative paths,
    useful for [GitHub Pages](https://pages.github.com/).
- `source_code_path` - Path to local source code
- `toc_depth` - Maximum depth of child modules ToC
- `encoding` - File encoding

#### Signature

```python
class BaseGenerator:
    def __init__(
        self,
        input_path: Path,
        output_path: Path,
        source_paths: Iterable[Path],
        project_name: str | None = None,
        docstring_processor: BaseDocstringProcessor | None = None,
        loader: Loader | None = None,
        raise_errors: bool = False,
        source_code_url: str | None = None,
        source_code_path: Path | None = None,
        toc_depth: int = 1,
        encoding: str = ENCODING,
    ) -> None: ...
```

#### See also

- [ENCODING](../constants.md#encoding)

### BaseGenerator()._write_changed

[Show source in base.py:386](../../../handsdown/generators/base.py#L386)

Write content to file if it's changed.

#### Signature

```python
def _write_changed(self, path: Path, content: str) -> bool: ...
```

### BaseGenerator().cleanup_old_docs

[Show source in base.py:146](../../../handsdown/generators/base.py#L146)

Remove old docs generated for this module.

#### Signature

```python
def cleanup_old_docs(self) -> None: ...
```

### BaseGenerator().generate_doc

[Show source in base.py:174](../../../handsdown/generators/base.py#L174)

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- `GeneratorError` - If `source_path` not found in current repo.

#### Signature

```python
def generate_doc(self, source_path: Path) -> None: ...
```

### BaseGenerator().generate_docs

[Show source in base.py:244](../../../handsdown/generators/base.py#L244)

Generate all doc files at once.

#### Signature

```python
def generate_docs(self) -> None: ...
```

### BaseGenerator().generate_external_configs

[Show source in base.py:395](../../../handsdown/generators/base.py#L395)

#### Signature

```python
def generate_external_configs(self) -> None: ...
```

### BaseGenerator().generate_index

[Show source in base.py:253](../../../handsdown/generators/base.py#L253)

Generate `<output>/README.md` file.

Contains a Tree of all modules in the project.

#### Signature

```python
def generate_index(self) -> None: ...
```

### BaseGenerator().get_children_module_records

[Show source in base.py:407](../../../handsdown/generators/base.py#L407)

Get all module records that are children of this module.

#### Signature

```python
def get_children_module_records(self, parent: ModuleRecord) -> list[ModuleRecord]: ...
```

#### See also

- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)

### BaseGenerator().get_external_configs_templates

[Show source in base.py:362](../../../handsdown/generators/base.py#L362)

Get a tuple with pairs of template path to project path.

#### Signature

```python
def get_external_configs_templates(self) -> tuple[tuple[Path, Path], Ellipsis]: ...
```

### BaseGenerator().get_md_document

[Show source in base.py:204](../../../handsdown/generators/base.py#L204)

Get or create MDDocument for module record.

#### Signature

```python
def get_md_document(self, module_record: ModuleRecord) -> MDDocument: ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)

### BaseGenerator().get_see_also_links

[Show source in base.py:330](../../../handsdown/generators/base.py#L330)

Get links to other modules that are referenced in the docstring.

#### Signature

```python
def get_see_also_links(
    self, record: NodeRecord, module_record: ModuleRecord, md_document: MDDocument
) -> list[str]: ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)
- [NodeRecord](../ast_parser/node_records/node_record.md#noderecord)

### BaseGenerator().replace_links

[Show source in base.py:271](../../../handsdown/generators/base.py#L271)

#### Signature

```python
def replace_links(
    self,
    module_record: ModuleRecord,
    record: NodeRecord,
    md_document: MDDocument,
    docstring: str,
) -> str: ...
```

#### See also

- [MDDocument](../md_document.md#mddocument)
- [ModuleRecord](../ast_parser/node_records/module_record.md#modulerecord)
- [NodeRecord](../ast_parser/node_records/node_record.md#noderecord)