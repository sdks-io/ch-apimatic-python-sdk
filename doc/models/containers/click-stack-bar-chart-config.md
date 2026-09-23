
# Click Stack Bar Chart Config

## Data Type

`ClickStackBarBuilderChartConfig | ClickStackBarRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackBarBuilderChartConfig`](../../../doc/models/click-stack-bar-builder-chart-config.md) |
| [`ClickStackBarRawSqlChartConfig`](../../../doc/models/click-stack-bar-raw-sql-chart-config.md) |

## ClickStackBarBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackBarBuilderChartConfig(
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
    group_by='service',
    series_limit=5
)
```

## ClickStackBarRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackBarRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

