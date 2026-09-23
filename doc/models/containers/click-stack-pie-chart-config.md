
# Click Stack Pie Chart Config

## Data Type

`ClickStackPieBuilderChartConfig | ClickStackPieRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackPieBuilderChartConfig`](../../../doc/models/click-stack-pie-builder-chart-config.md) |
| [`ClickStackPieRawSqlChartConfig`](../../../doc/models/click-stack-pie-raw-sql-chart-config.md) |

## ClickStackPieBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackPieBuilderChartConfig(
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
    order_by='"Count" DESC',
    limit=10
)
```

## ClickStackPieRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackPieRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

