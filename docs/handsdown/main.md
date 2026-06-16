# Main

Main CLI entrypoint for `handsdown`.

[Handsdown API Index](../README.md#handsdown-api-index) / [Handsdown](./index.md#handsdown) / Main

> Auto-generated documentation for [handsdown.main](../../handsdown/main.py) module.

- [Main](#main)
  - [api](#api)
  - [main](#main)
  - [select_generator_cls](#select_generator_cls)

## api

[Show source in main.py:22](../../handsdown/main.py#L22)

#### Signature

```python
def api(args: CLINamespace) -> None: ...
```

#### See also

- [CLINamespace](./cli_parser.md#clinamespace)



## main

[Show source in main.py:50](../../handsdown/main.py#L50)

Main entrypoint for CLI.

#### Signature

```python
def main() -> None: ...
```



## select_generator_cls

[Show source in main.py:14](../../handsdown/main.py#L14)

Select a generator based on the theme.

#### Signature

```python
def select_generator_cls(theme: Theme) -> type[BaseGenerator]: ...
```

#### See also

- [BaseGenerator](generators/base.md#basegenerator)
- [Theme](./constants.md#theme)