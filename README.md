# Hello World OpenAI

A simple Python project that demonstrates how to interact with OpenAI's API using the official Python client library.

## Overview

This project sends a prompt to OpenAI's GPT-4o model and displays the response. It serves as a beginner-friendly example of integrating OpenAI's API into a Python application.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (get one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ismaelpolancop/Hello_World_OpenAI.git
cd Hello_World_OpenAI
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to set up your OpenAI API key:

1. Open `Hello_World_OpenAI.py`
2. Replace `"API KEY"` with your actual OpenAI API key

**Security Note:** For production use, store your API key in an environment variable instead:
```python
import os
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
```


## Usage

Run the script:
```bash
python Hello_World_OpenAI.py
```

The script will send a prompt to OpenAI's GPT-4o model and print the response.

## Project Structure

```
Hello_World_OpenAI/
├── README.md                    # This file
├── Hello_World_OpenAI.py        # Main script
└── requirements.txt             # Python dependencies
```

## Dependencies

- **openai** - Official OpenAI Python client library

## Features

- Simple API integration with OpenAI
- Error handling for missing API keys
- Exception handling for API calls

## Troubleshooting

- **API Key Error**: Make sure your API key is correctly set in the script
- **Module Not Found**: Run `pip install -r requirements.txt` to install dependencies
- **API Errors**: Check that your API key is valid and has sufficient credits

## License

This project is open source and available under the MIT License.

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [OpenAI Python Client Library](https://github.com/openai/openai-python)

## Author

[ismaelpolancop](https://github.com/ismaelpolancop)
