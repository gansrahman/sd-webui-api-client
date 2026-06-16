# SD WebUI API Client

Python client for AUTOMATIC1111 WebUI.

## Usage
```python
from sd_client import SDClient
client = SDClient('http://localhost:7860')
img = client.txt2img('a sunset', steps=30)
img.save('output.png')
```
