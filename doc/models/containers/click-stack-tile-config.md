
# Click Stack Tile Config

## Data Type

`ClickStackLineBuilderChartConfig | ClickStackLineRawSqlChartConfig | ClickStackBarBuilderChartConfig | ClickStackBarRawSqlChartConfig | ClickStackTableBuilderChartConfig | ClickStackTableRawSqlChartConfig | ClickStackNumberBuilderChartConfig | ClickStackNumberRawSqlChartConfig | ClickStackPieBuilderChartConfig | ClickStackPieRawSqlChartConfig | ClickStackCategoricalBarBuilderChartConfig | ClickStackCategoricalBarRawSqlChartConfig | ClickStackHeatmapChartConfig | ClickStackSearchChartConfig | ClickStackEventPatternsChartConfig | ClickStackMarkdownChartConfig`

## Cases

| Type |
|  --- |
| [`Any`](../../../doc/models/containers/click-stack-line-chart-config.md) |
| [`Any`](../../../doc/models/containers/click-stack-bar-chart-config.md) |
| [`Any`](../../../doc/models/containers/click-stack-table-chart-config.md) |
| [`Any`](../../../doc/models/containers/click-stack-number-chart-config.md) |
| [`Any`](../../../doc/models/containers/click-stack-pie-chart-config.md) |
| [`Any`](../../../doc/models/containers/click-stack-categorical-bar-chart-config.md) |
| [`ClickStackHeatmapChartConfig`](../../../doc/models/click-stack-heatmap-chart-config.md) |
| [`ClickStackSearchChartConfig`](../../../doc/models/click-stack-search-chart-config.md) |
| [`ClickStackEventPatternsChartConfig`](../../../doc/models/click-stack-event-patterns-chart-config.md) |
| [`ClickStackMarkdownChartConfig`](../../../doc/models/click-stack-markdown-chart-config.md) |

## Any

### Initialization Code

#### Example

```python
value = ClickStackLineBuilderChartConfig(
    source_id='sourceId0',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## Any

### Initialization Code

#### Example

```python
value = ClickStackBarBuilderChartConfig(
    source_id='sourceId0',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        ),
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## Any

### Initialization Code

#### Example

```python
value = ClickStackTableBuilderChartConfig(
    source_id='sourceId6',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        ),
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## Any

### Initialization Code

#### Example

```python
value = ClickStackNumberBuilderChartConfig(
    source_id='sourceId6',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        ),
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## Any

### Initialization Code

#### Example

```python
value = ClickStackPieBuilderChartConfig(
    source_id='sourceId8',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        ),
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        ),
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## Any

### Initialization Code

#### Example

```python
value = ClickStackCategoricalBarBuilderChartConfig(
    source_id='sourceId4',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.MAX
        )
    ]
)
```

## ClickStackHeatmapChartConfig

### Initialization Code

#### Example

```python
value = ClickStackHeatmapChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select=[
        ClickStackHeatmapSelectItem(
            value_expression='Duration',
            count_expression='count()',
            heatmap_scale_type=HeatmapScaleType.LOG
        )
    ],
    where='ServiceName = \'api\''
)
```

## ClickStackSearchChartConfig

### Initialization Code

#### Example

```python
value = ClickStackSearchChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select='timestamp, level, message',
    where_language=WhereLanguage4.SQL,
    where='level:error'
)
```

## ClickStackEventPatternsChartConfig

### Initialization Code

#### Example

```python
value = ClickStackEventPatternsChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select='Body',
    where='level:error'
)
```

## ClickStackMarkdownChartConfig

### Initialization Code

#### Example

```python
value = ClickStackMarkdownChartConfig(
    markdown='# Dashboard Title\n\nThis is a markdown widget.'
)
```

