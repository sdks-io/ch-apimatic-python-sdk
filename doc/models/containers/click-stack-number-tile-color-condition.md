
# Click Stack Number Tile Color Condition

## Data Type

`ClickStackNumericColorCondition | ClickStackBetweenColorCondition | ClickStackEqualityColorCondition`

## Cases

| Type |
|  --- |
| [`ClickStackNumericColorCondition`](../../../doc/models/click-stack-numeric-color-condition.md) |
| [`ClickStackBetweenColorCondition`](../../../doc/models/click-stack-between-color-condition.md) |
| [`ClickStackEqualityColorCondition`](../../../doc/models/click-stack-equality-color-condition.md) |

## ClickStackNumericColorCondition

### Initialization Code

#### Example

```python
value = ClickStackNumericColorCondition(
    operator=Operator.GT,
    value=100,
    color=Color1.CHARTGREEN,
    label='High'
)
```

## ClickStackBetweenColorCondition

### Initialization Code

#### Example

```python
value = ClickStackBetweenColorCondition(
    value=[
        100,
        500
    ],
    color=Color1.CHARTCYAN,
    label='Warning'
)
```

## ClickStackEqualityColorCondition

### Initialization Code

#### Example

```python
value = ClickStackEqualityColorCondition(
    operator=Operator1.EQ,
    value=58.94,
    color=Color1.CHARTWARNING,
    label='Healthy'
)
```

