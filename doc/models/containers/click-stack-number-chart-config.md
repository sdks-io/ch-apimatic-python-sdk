
# Click Stack Number Chart Config

## Data Type

`ClickStackNumberBuilderChartConfig | ClickStackNumberRawSqlChartConfig`

## Cases

| Type |
|  --- |
| [`ClickStackNumberBuilderChartConfig`](../../../doc/models/click-stack-number-builder-chart-config.md) |
| [`ClickStackNumberRawSqlChartConfig`](../../../doc/models/click-stack-number-raw-sql-chart-config.md) |

## ClickStackNumberBuilderChartConfig

### Initialization Code

#### Example

```python
value = ClickStackNumberBuilderChartConfig(
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
    ]
)
```

## ClickStackNumberRawSqlChartConfig

### Initialization Code

#### Example

```python
value = ClickStackNumberRawSqlChartConfig(
    connection_id='65f5e4a3b9e77c001a567890',
    sql_template='SELECT count() FROM otel_logs WHERE timestamp > now() - INTERVAL 1 HOUR',
    source_id='65f5e4a3b9e77c001a567890'
)
```

