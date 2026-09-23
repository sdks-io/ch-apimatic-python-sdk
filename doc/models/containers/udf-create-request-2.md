
# Udf Create Request 2

## Data Type

`UdfCreateRequest | UdfCreateRequest1`

## Cases

| Type |
|  --- |
| [`UdfCreateRequest`](../../../doc/models/udf-create-request.md) |
| [`UdfCreateRequest1`](../../../doc/models/udf-create-request-1.md) |

## UdfCreateRequest

### Initialization Code

#### Example

```python
value = UdfCreateRequest(
    upload_id='000017c4-0000-0000-0000-000000000000',
    runtime=Runtime.ENUM_PYTHON311,
    arguments=[
        UdfArgument(
            name='name8',
            mtype='type2'
        )
    ],
    return_type='returnType2',
    function_name='functionName2',
    command_read_timeout=10000,
    command_write_timeout=10000,
    send_chunk_header=False,
    deterministic=False,
    format='TabSeparated',
    sandbox_type=SandboxType.BASIC,
    sandbox_version=SandboxVersion.V2
)
```

## UdfCreateRequest1

### Initialization Code

#### Example

```python
value = UdfCreateRequest1(
    upload_id='00000046-0000-0000-0000-000000000000',
    runtime=Runtime.ENUM_PYTHON311,
    arguments=[
        UdfArgument(
            name='name8',
            mtype='type2'
        )
    ],
    return_type='returnType2',
    function_name='functionName2',
    command_read_timeout=10000,
    command_write_timeout=10000,
    send_chunk_header=False,
    deterministic=False,
    format='TabSeparated',
    sandbox_type=SandboxType.BASIC,
    sandbox_version=SandboxVersion.V2,
    pool_size=3,
    max_command_execution_time=10
)
```

