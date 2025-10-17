from hqapi_client.example import ExampleClient

# Set your token, get yours at https://hqapi.com/
EXAMPLE_API_TOKEN="--put--your--token--here--"

client = ExampleClient(token=EXAMPLE_API_TOKEN)
value = client.ping('hello, world!')

print(value)
