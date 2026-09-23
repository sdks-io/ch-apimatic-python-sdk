
# Release Channel

Select fast if you want to get new ClickHouse releases as soon as they are available. You'll get new features faster, but with a higher risk of bugs. Select slow if you would like to defer releases to give yourself more time to test. This feature is only available for production services. default is the regular release channel.

## Enumeration

`ReleaseChannel`

## Fields

| Name |
|  --- |
| `SLOW` |
| `DEFAULT` |
| `FAST` |

## Example

```python
from openapispecforclickhousecloud.models.release_channel import ReleaseChannel

release_channel = ReleaseChannel.FAST
```

