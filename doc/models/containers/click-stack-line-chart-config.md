
# Click Stack Line Chart Config

## Data Type

`ClickStackLineBuilderChartConfig | ClickStackLineRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackLineBuilderChartConfig`](../../../doc/models/click-stack-line-builder-chart-config.md) |
| [`ClickStackLineRawSqlChartConfig`](../../../doc/models/click-stack-line-raw-sql-chart-config.md) |

## ClickStackLineBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackLineBuilderChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.COUNT,
            value_expression='Duration',
            alias='Request Duration',
            where='service:api',
            metric_name='http.server.duration',
            period_agg_fn=PeriodAggFn.DELTA
        )
    ],
    group_by='host',
    series_limit=5
)
```

## ClickStackLineRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackLineRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

