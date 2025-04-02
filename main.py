"""DeepSeek UI Component Generator App"""

import streamlit as st
import os

from component_generator import get_api_key, generate_html
from preview_tools import wrap_with_tailwind, create_preview_iframe


def main():
    """Run the UI component generator app"""
    # Page configuration
    st.set_page_config(page_title="UI Generator", layout="wide")

    # Heading
    st.title("UI Component Generator")
    st.write("Create UI components from text descriptions using DeepSeek AI")

    # Get API key
    api_key = get_api_key()
    if not api_key:
        col1, col2 = st.columns([2, 1])
        with col1:
            api_key = st.text_input("DeepSeek API Key:", type="password")
        with col2:
            if st.button("Save Key"):
                if api_key:
                    os.environ["DEEPSEEK_API_KEY"] = api_key
                    st.success("API key saved!")
                    st.rerun()
        st.stop()

    # Input section
    st.subheader("Describe Your Component")

    description = st.text_area(
        "Component description:",
        value="A blue button with rounded corners that says 'Submit'",
        height=100,
    )

    # Generation
    if st.button("Generate Component", type="primary"):
        with st.spinner("Creating component..."):
            component_html = generate_html(description, api_key)

        # Results display
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Generated Code")
            st.code(component_html, language="html")

            # Copy button (uses JavaScript)
            st.markdown(
                f"""
                <button 
                    onclick="navigator.clipboard.writeText(`{component_html}`);this.textContent='Copied!'" 
                    style="background:#4CAF50;color:white;border:none;padding:8px 16px;border-radius:4px;cursor:pointer"
                >
                    Copy Code
                </button>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.subheader("Preview")
            full_html = wrap_with_tailwind(component_html)
            iframe = create_preview_iframe(full_html, 400)
            st.components.v1.html(iframe, height=420)

    # Examples section
    st.subheader("Try These Examples")
    examples = [
        "A navigation bar with logo and 3 menu items",
        "A contact form with name, email and message fields",
        "A pricing card with a monthly subscription plan",
        "A success notification with a checkmark icon",
    ]

    for example in examples:
        if st.button(example):
            # Set the textarea value using JavaScript
            st.write(
                f"<script>document.querySelector('textarea').value = '{example}';</script>",
                unsafe_allow_html=True,
            )
            # Force rerun to update the UI
            st.rerun()


if __name__ == "__main__":
    main()
