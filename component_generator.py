
"""Component generator using DeepSeek API"""
import os
import json
import requests


def get_api_key():
    """Get DeepSeek API key from environment variable.
    """
    return os.getenv("DEEPSEEK_API_KEY")


def generate_html(prompt, api_key):
    """Generate HTML component from natural language prompt.

    Args:
        prompt (str): Natural language description
        api_key (str): DeepSeek API key
    """
    instructions = """
    Create HTML with Tailwind CSS for the described UI component.
    Use appropriate colors, center text, and ensure readability.
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            
            # Clean up markdown if present
            if "```" in content:
                code_part = content.split("```")[1]
                if code_part.startswith("html"):
                    code_part = code_part[4:]  # Remove 'html' prefix
                return code_part.strip()
            return content.strip()
        else:
            raise Exception(f"API error: {response.status_code}")
    except Exception as e:
        # Fallback to simple component if API fails
        print(f"Error: {e}")
        return f'<div class="bg-blue-100 p-4 rounded">{prompt}</div>'
