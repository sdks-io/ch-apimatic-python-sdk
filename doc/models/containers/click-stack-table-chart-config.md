
# Click Stack Table Chart Config

## Data Type

`ClickStackTableBuilderChartConfig | ClickStackTableRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackTableBuilderChartConfig`](../../../doc/models/click-stack-table-builder-chart-config.md) |
| [`ClickStackTableRawSqlChartConfig`](../../../doc/models/click-stack-table-raw-sql-chart-config.md) |

## ClickStackTableBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackTableBuilderChartConfig(
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
    having='count > 100',
    order_by='count DESC',
    as_ratio=False,
    group_by_columns_on_left=False
)
```

## ClickStackTableRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackTableRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

