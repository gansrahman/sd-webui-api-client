# SD WebUI API Client
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/) [![PyTorch](https://img.shields.io/badge/pytorch-2.0+-ee4c2c.svg)](https://pytorch.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Python client for AUTOMATIC1111 WebUI.

## Usage
```python
from sd_client import SDClient
client = SDClient('http://localhost:7860')
img = client.txt2img('a sunset', steps=30)
img.save('output.png')
```
