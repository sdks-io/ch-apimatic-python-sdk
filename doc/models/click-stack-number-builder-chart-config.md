
# Click Stack Number Builder Chart Config

*This model accepts additional fields of type Any.*

## Structure

`ClickStackNumberBuilderChartConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display_type` | `str` | Required, Constant | Display type discriminator. Must be "number" for single big-number charts.<br><br>**Value**: `"number"` |
| `source_id` | `str` | Required | ID of the data source to query. |
| `select` | [`List[ClickStackSelectItem]`](../../doc/models/click-stack-select-item.md) | Required | Exactly one aggregated value to display as a single number — unless "formulas" is set, in which case the select items are the formula's operands and the (single) formula value is displayed instead. |
| `formulas` | [`List[ClickStackFormula]`](../../doc/models/click-stack-formula.md) | Optional | A single derived value computed from the select items via letter-ref arithmetic ("A" = select[0], "B" = select[1], ...). Metric, log, and trace sources only. Number tiles display the formula value and always hide the operand series. |
| `number_format` | [`ClickStackNumberFormat`](../../doc/models/click-stack-number-format.md) | Optional | - |
| `color` | [`Color4`](../../doc/models/color-4.md) | Optional | Optional static color applied to the displayed number. |
| `color_rules` | List[[ClickStackNumericColorCondition](../../doc/models/click-stack-numeric-color-condition.md) \| [ClickStackBetweenColorCondition](../../doc/models/click-stack-between-color-condition.md) \| [ClickStackEqualityColorCondition](../../doc/models/click-stack-equality-color-condition.md)] \| None | Optional | Ordered conditional color rules evaluated against the displayed value (last match wins). Falls back to color, then the default text color when no rule matches. |
| `background_chart` | [`ClickStackBackgroundChart`](../../doc/models/click-stack-background-chart.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from openapispecforclickhousecloud.models.agg_fn_3 import AggFn3
from openapispecforclickhousecloud.models.click_stack_background_chart import ClickStackBackgroundChart
from openapispecforclickhousecloud.models.click_stack_formula import ClickStackFormula
from openapispecforclickhousecloud.models.click_stack_number_builder_chart_config import ClickStackNumberBuilderChartConfig
from openapispecforclickhousecloud.models.click_stack_number_format import ClickStackNumberFormat
from openapispecforclickhousecloud.models.click_stack_numeric_color_condition import ClickStackNumericColorCondition
from openapispecforclickhousecloud.models.click_stack_select_item import ClickStackSelectItem
from openapispecforclickhousecloud.models.color import Color
from openapispecforclickhousecloud.models.color_1 import Color1
from openapispecforclickhousecloud.models.color_4 import Color4
from openapispecforclickhousecloud.models.level import Level
from openapispecforclickhousecloud.models.operator import Operator
from openapispecforclickhousecloud.models.output import Output
from openapispecforclickhousecloud.models.period_agg_fn import PeriodAggFn
from openapispecforclickhousecloud.models.type_19 import Type19
from openapispecforclickhousecloud.models.where_language_4 import WhereLanguage4

click_stack_number_builder_chart_config = ClickStackNumberBuilderChartConfig(
    source_id='65f5e4a3b9e77c001a111111',
    select=[
        ClickStackSelectItem(
            agg_fn=AggFn3.COUNT,
            value_expression='Duration',
            alias='Request Duration',
            level=Level.P50,
            where='service:api',
            where_language=WhereLanguage4.SQL,
            metric_name='http.server.duration',
            period_agg_fn=PeriodAggFn.DELTA,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    formulas=[
        ClickStackFormula(
            expression='expression2',
            alias='alias2',
            number_format=ClickStackNumberFormat(
                output=Output.CURRENCY,
                mantissa=170,
                thousand_separated=False,
                average=False,
                decimal_bytes=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackFormula(
            expression='expression2',
            alias='alias2',
            number_format=ClickStackNumberFormat(
                output=Output.CURRENCY,
                mantissa=170,
                thousand_separated=False,
                average=False,
                decimal_bytes=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    number_format=ClickStackNumberFormat(
        output=Output.CURRENCY,
        mantissa=170,
        thousand_separated=False,
        average=False,
        decimal_bytes=False,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    color=Color4.CHARTCYAN,
    color_rules=[
        ClickStackNumericColorCondition(
            operator=Operator.GT,
            value=38.3,
            color=Color1.CHARTGREEN,
            label='label8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        ClickStackNumericColorCondition(
            operator=Operator.GT,
            value=38.3,
            color=Color1.CHARTGREEN,
            label='label8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    background_chart=ClickStackBackgroundChart(
        mtype=Type19.LINE,
        color=Color.CHARTERROR,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

