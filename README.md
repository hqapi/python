# HQAPI Python Client

A lightweight and easy-to-use Python client for interacting with the
**HQAPI** web services.

This client provides convenient access to HQAPI endpoints for tasks such as
authentication, data retrieval, and account management — without manually
handling HTTP requests.

---

## 🚀 Features

- Simple, intuitive interface for all HQAPI endpoints  
- Automatic authentication (API key or token)  
- Built-in error handling and response parsing  
- Synchronous and asynchronous support  
- 100% typed and PEP8-compliant  

---

## 📦 Installation

Install via pip:

```bash
pip install hqapi-client
```

## License

Distributed under the MIT License.

## Examples
### Screenshot Create method

```python
from hqapi_client.screenshot import ScreenshotClient

# Set your token, get yours at https://hqapi.com/
SCREENSHOT_API_TOKEN="--put--your--token--here--"

client = ScreenshotClient(token=SCREENSHOT_API_TOKEN)
image_data = client.create(url="https://hqapi.com/")

# Save to disk
with open("screenshot.png", "wb") as f:
    f.write(image_data)
```

