
# Click Stack Saved Filter Value

## Data Type

`ClickStackSqlSavedFilterValue | ClickStackVariableSavedFilterValue`

## Cases

| Type |
|  --- |
| [`ClickStackSqlSavedFilterValue`](../../../doc/models/click-stack-sql-saved-filter-value.md) |
| [`ClickStackVariableSavedFilterValue`](../../../doc/models/click-stack-variable-saved-filter-value.md) |

## ClickStackSqlSavedFilterValue

### Initialization Code

#### Example

```python
value = ClickStackSqlSavedFilterValue(
    condition='ServiceName IN (\'hdx-oss-dev-api\')',
    mtype=Type18.SQL
)
```

## ClickStackVariableSavedFilterValue

### Initialization Code

#### Example

```python
value = ClickStackVariableSavedFilterValue(
    name='service',
    values=[
        'hdx-oss-dev-api'
    ]
)
```

