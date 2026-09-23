
# Click Stack on Click

## Data Type

`ClickStackOnClickSearch | ClickStackOnClickDashboard | ClickStackOnClickExternal`

## Cases

| Type |
|  --- |
| [`ClickStackOnClickSearch`](../../../doc/models/click-stack-on-click-search.md) |
| [`ClickStackOnClickDashboard`](../../../doc/models/click-stack-on-click-dashboard.md) |
| [`ClickStackOnClickExternal`](../../../doc/models/click-stack-on-click-external.md) |

## ClickStackOnClickSearch

### Initialization Code

#### Example

```python
value = ClickStackOnClickSearch(
    target=ClickStackOnClickTargetIdVariant(
        id='65f5e4a3b9e77c001a567890'
    ),
    where_template='ServiceName = \'{{ServiceName}}\''
)
```

## ClickStackOnClickDashboard

### Initialization Code

#### Example

```python
value = ClickStackOnClickDashboard(
    target=ClickStackOnClickTargetIdVariant(
        id='65f5e4a3b9e77c001a567890'
    ),
    where_template='ServiceName = \'{{ServiceName}}\''
)
```

## ClickStackOnClickExternal

### Initialization Code

#### Example

```python
value = ClickStackOnClickExternal(
    url_template='https://example.com/d/abc?var-service={{ServiceName}}'
)
```

