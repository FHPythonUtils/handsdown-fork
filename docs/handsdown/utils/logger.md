# Logger

Utilities for stdout stream logger.

[Handsdown API Index](../../README.md#handsdown-api-index) / [Handsdown](../index.md#handsdown) / [Utils](./index.md#utils) / Logger

> Auto-generated documentation for [handsdown.utils.logger](../../../handsdown/utils/logger.py) module.

- [Logger](#logger)
  - [get_logger](#get_logger)

## get_logger

[Show source in logger.py:9](../../../handsdown/utils/logger.py#L9)

Get stdout stream logger.

#### Arguments

- `level` - Desired logging level.

#### Returns

A `logging.Logger` instance.

#### Signature

```python
def get_logger(level: int | None = None) -> logging.Logger: ...
```