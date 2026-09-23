
# Click Pipe Patch Kafka Source Credentials

## Data Type

`Plain | MskIamUser | AzureEventHub | MutualTls`

## Cases

| Type |
|  --- |
| [`Plain`](../../../doc/models/plain.md) |
| [`MskIamUser`](../../../doc/models/msk-iam-user.md) |
| [`AzureEventHub`](../../../doc/models/azure-event-hub.md) |
| [`MutualTls`](../../../doc/models/mutual-tls.md) |

## Plain

### Initialization Code

#### Example

```python
value = Plain(
    username='postgres_user',
    password='your_secure_password'
)
```

## MskIamUser

### Initialization Code

#### Example

```python
value = MskIamUser()
```

## AzureEventHub

### Initialization Code

#### Example

```python
value = AzureEventHub()
```

## MutualTls

### Initialization Code

#### Example

```python
value = MutualTls()
```

