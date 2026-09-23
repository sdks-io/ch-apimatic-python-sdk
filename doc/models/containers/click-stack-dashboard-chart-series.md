
# Click Stack Dashboard Chart Series

## Data Type

`ClickStackTimeChartSeries | ClickStackTableChartSeries | ClickStackNumberChartSeries | ClickStackSearchChartSeries | ClickStackMarkdownChartSeries`

## Cases

| Type |
|  --- |
| [`ClickStackTimeChartSeries`](../../../doc/models/click-stack-time-chart-series.md) |
| [`ClickStackTableChartSeries`](../../../doc/models/click-stack-table-chart-series.md) |
| [`ClickStackNumberChartSeries`](../../../doc/models/click-stack-number-chart-series.md) |
| [`ClickStackSearchChartSeries`](../../../doc/models/click-stack-search-chart-series.md) |
| [`ClickStackMarkdownChartSeries`](../../../doc/models/click-stack-markdown-chart-series.md) |

## ClickStackTimeChartSeries

### Initialization Code

#### Example

```python
value = ClickStackTimeChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    agg_fn=AggFn.COUNT,
    where='service:api',
    where_language=WhereLanguage.LUCENE,
    group_by=[
        'host'
    ],
    level=0.95,
    field='duration',
    alias='Request Duration',
    metric_data_type=MetricDataType.SUM,
    metric_name='http.server.duration',
    display_type=DisplayType.LINE
)
```

## ClickStackTableChartSeries

### Initialization Code

#### Example

```python
value = ClickStackTableChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    agg_fn=AggFn.COUNT,
    where='level:error',
    where_language=WhereLanguage.LUCENE,
    group_by=[
        'errorType'
    ],
    level=0.95,
    field='duration',
    alias='Total Count',
    sort_order=SortOrder.DESC,
    metric_data_type=MetricDataType.SUM,
    metric_name='http.server.duration'
)
```

## ClickStackNumberChartSeries

### Initialization Code

#### Example

```python
value = ClickStackNumberChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    agg_fn=AggFn.COUNT,
    where='service:api',
    where_language=WhereLanguage.LUCENE,
    level=0.95,
    field='duration',
    alias='Total Requests',
    metric_data_type=MetricDataType.SUM,
    metric_name='http.server.duration'
)
```

## ClickStackSearchChartSeries

### Initialization Code

#### Example

```python
value = ClickStackSearchChartSeries(
    source_id='65f5e4a3b9e77c001a567890',
    fields=[
        'timestamp',
        'level',
        'message'
    ],
    where='level:error',
    where_language=WhereLanguage.LUCENE
)
```

## ClickStackMarkdownChartSeries

### Initialization Code

#### Example

```python
value = ClickStackMarkdownChartSeries(
    content='# Dashboard Title\n\nThis is a markdown widget.'
)
```

