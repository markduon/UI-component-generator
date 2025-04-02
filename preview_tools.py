"""Tools for previewing HTML components"""

import html


def wrap_with_tailwind(component_html):
    """Wrap component HTML with Tailwind CSS for preview.

    Args:
        component_html (str): Component HTML code
    """
    html_template = f"""<!DOCTYPE html>
                        <html>
                        <head>
                            <script src="https://cdn.tailwindcss.com"></script>
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <style>
                                body {{
                                    display: flex;
                                    justify-content: center;
                                    align-items: center;
                                    min-height: 100vh;
                                    margin: 0;
                                }}
                                .container {{
                                    max-width: 400px;
                                    padding: 20px;
                                }}
                            </style>
                        </head>
                        <body>
                            <div class="container">
                                {component_html}
                            </div>
                        </body>
                        </html>"""
    return html_template


def create_preview_iframe(html_content, height=300):
    """Create iframe HTML for component preview.

    Args:
        html_content (str): Complete HTML to display
        height (int, optional): Frame height. Defaults to 300.
    """
    escaped = html.escape(html_content)
    return f'<iframe srcdoc="{escaped}" width="100%" height="{height}" frameborder="0"></iframe>'
