# JinjaManager

Jinja2 `Environment` manager.

[Handsdown API Index](../README.md#handsdown-api-index) / [Handsdown](./index.md#handsdown) / JinjaManager

> Auto-generated documentation for [handsdown.jinja_manager](../../handsdown/jinja_manager.py) module.

- [JinjaManager](#jinjamanager)
  - [JinjaManager](#jinjamanager-1)
    - [JinjaManager().env](#jinjamanager()env)
    - [JinjaManager.escape_md](#jinjamanagerescape_md)
    - [JinjaManager().render](#jinjamanager()render)
    - [JinjaManager.trim_eof](#jinjamanagertrim_eof)
    - [JinjaManager.update_globals](#jinjamanagerupdate_globals)

## JinjaManager

[Show source in jinja_manager.py:11](../../handsdown/jinja_manager.py#L11)

Jinja2 `Environment` manager.

#### Signature

```python
class JinjaManager:
    def __init__(self) -> None: ...
```

### JinjaManager().env

[Show source in jinja_manager.py:40](../../handsdown/jinja_manager.py#L40)

Get `jinja2.Environment`.

#### Signature

```python
@property
def env(self) -> jinja2.Environment: ...
```

### JinjaManager.escape_md

[Show source in jinja_manager.py:35](../../handsdown/jinja_manager.py#L35)

Escape underscore characters.

#### Signature

```python
@staticmethod
def escape_md(value: str) -> str: ...
```

### JinjaManager().render

[Show source in jinja_manager.py:50](../../handsdown/jinja_manager.py#L50)

#### Signature

```python
def render(self, template_path: Path, **kwargs: Any) -> str: ...
```

### JinjaManager.trim_eof

[Show source in jinja_manager.py:45](../../handsdown/jinja_manager.py#L45)

Trim EOF newlines and add one newline.

#### Signature

```python
@staticmethod
def trim_eof(value: str) -> str: ...
```

### JinjaManager.update_globals

[Show source in jinja_manager.py:24](../../handsdown/jinja_manager.py#L24)

Update global variables in `jinja2.Environment`.

#### Arguments

- `kwargs` - Globals to set.

#### Signature

```python
@classmethod
def update_globals(cls, **kwargs: object) -> None: ...
```