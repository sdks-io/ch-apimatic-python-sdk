
# Click Stack Alert Channel

## Data Type

`ClickStackAlertChannelEmail | ClickStackAlertChannelWebhook`

## Cases

| Type |
|  --- |
| [`ClickStackAlertChannelEmail`](../../../doc/models/click-stack-alert-channel-email.md) |
| [`ClickStackAlertChannelWebhook`](../../../doc/models/click-stack-alert-channel-webhook.md) |

## ClickStackAlertChannelEmail

### Initialization Code

#### Example

```python
value = ClickStackAlertChannelEmail(
    mtype=Type16.WEBHOOK,
    email_recipients=[
        'emailRecipients1',
        'emailRecipients2',
        'emailRecipients3'
    ]
)
```

## ClickStackAlertChannelWebhook

### Initialization Code

#### Example

```python
value = ClickStackAlertChannelWebhook(
    mtype=Type17.WEBHOOK,
    webhook_id='65f5e4a3b9e77c001a789012',
    webhook_service='slack_api',
    slack_channel_id='C01ABCDEF23'
)
```

