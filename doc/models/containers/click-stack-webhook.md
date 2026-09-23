
# Click Stack Webhook

## Data Type

`ClickStackSlackWebhook | ClickStackIncidentIoWebhook | ClickStackGenericWebhook | ClickStackSlackApiWebhook | ClickStackPagerDutyApiWebhook`

## Cases

| Type |
|  --- |
| [`ClickStackSlackWebhook`](../../../doc/models/click-stack-slack-webhook.md) |
| [`ClickStackIncidentIoWebhook`](../../../doc/models/click-stack-incident-io-webhook.md) |
| [`ClickStackGenericWebhook`](../../../doc/models/click-stack-generic-webhook.md) |
| [`ClickStackSlackApiWebhook`](../../../doc/models/click-stack-slack-api-webhook.md) |
| [`ClickStackPagerDutyApiWebhook`](../../../doc/models/click-stack-pager-duty-api-webhook.md) |

## ClickStackSlackWebhook

### Initialization Code

#### Example

```python
value = ClickStackSlackWebhook(
    id='507f1f77bcf86cd799439011',
    name='Production Alerts',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends critical alerts to the #incidents channel'
)
```

## ClickStackIncidentIoWebhook

### Initialization Code

#### Example

```python
value = ClickStackIncidentIoWebhook(
    id='507f1f77bcf86cd799439012',
    name='Incident Response',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://api.incident.io/v2/alert_events/http/abc123',
    description='Routes alerts to incident.io for on-call escalation'
)
```

## ClickStackGenericWebhook

### Initialization Code

#### Example

```python
value = ClickStackGenericWebhook(
    id='507f1f77bcf86cd799439013',
    name='PagerDuty Integration',
    updated_at=dateutil.parser.parse('2025-06-15T10:30:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://example.com/webhooks/alerts',
    description='Forwards alert payloads to an external monitoring service',
    body='{"alert": "{{title}}", "severity": "{{level}}"}'
)
```

## ClickStackSlackApiWebhook

### Initialization Code

#### Example

```python
value = ClickStackSlackApiWebhook(
    id='65f5e4a3b9e77c001a789012',
    name='Slack Alerts',
    updated_at=dateutil.parser.parse('2025-01-15T12:00:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://hooks.slack.com/services/EXAMPLE/WEBHOOK/URL',
    description='Sends alerts to #engineering channel'
)
```

## ClickStackPagerDutyApiWebhook

### Initialization Code

#### Example

```python
value = ClickStackPagerDutyApiWebhook(
    id='65f5e4a3b9e77c001a789013',
    name='PagerDuty Alerts',
    updated_at=dateutil.parser.parse('2025-01-15T12:00:00Z'),
    created_at=dateutil.parser.parse('2025-01-01T00:00:00Z'),
    url='https://events.pagerduty.com/v2/enqueue',
    description='Sends critical alerts to PagerDuty'
)
```

