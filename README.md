# DeepSeek UI Component Generator

Create UI components from text descriptions using DeepSeek AI.

## Features

- Text-to-UI conversion with DeepSeek-V3
- Tailwind CSS integration for styling
- Live component preview
- Simple copy-paste functionality

## Files

- `main.py` - Streamlit application
- `component_generator.py` - DeepSeek API integration
- `preview_tools.py` - HTML preview utilities

## Setup

```bash
# Install dependencies
pip install streamlit requests

# Set API key (optional)
export DEEPSEEK_API_KEY="your-api-key"

# Run the app
streamlit run main.py
```

## Usage

1. Enter your DeepSeek API key if not set as environment variable
2. Describe the UI component you want to create
3. Click "Generate Component"
4. Copy the generated code to use in your project

## Example Descriptions

- "A blue button with rounded corners that says 'Submit'"
- "A navigation bar with logo and 3 menu items"
- "A contact form with name, email and message fields"
- "A success notification with a checkmark icon"