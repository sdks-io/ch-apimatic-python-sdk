
# Click Stack Categorical Bar Chart Config

## Data Type

`ClickStackCategoricalBarBuilderChartConfig | ClickStackCategoricalBarRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackCategoricalBarBuilderChartConfig`](../../../doc/models/click-stack-categorical-bar-builder-chart-config.md) |
| [`ClickStackCategoricalBarRawSqlChartConfig`](../../../doc/models/click-stack-categorical-bar-raw-sql-chart-config.md) |

## ClickStackCategoricalBarBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackCategoricalBarBuilderChartConfig(
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

## ClickStackCategoricalBarRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackCategoricalBarRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

