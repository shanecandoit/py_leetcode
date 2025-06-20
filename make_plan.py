import os
import requests
import json
from ollama import chat

# Ollama models
# deepseek-r1:latest
# gemma3:1b
# gemma3:4b
MODEL = "gemma3:4b"  # DO NOT CHANGE


def read_file_content(file_path):
    """Read and return the content of a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def generate_plan_with_ollama(code_content):
    """Send code content to Ollama and get a plan back."""
    # Adjust the URL if your Ollama instance is running elsewhere
    url = "http://localhost:11434/api/generate"

    prompt = f"""
    Please analyze the following Python code and create a detailed plan
    for how it works and how it could be improved or extended:

    ```python
    {code_content}
    ```
    Hints:
    - Use '-' for lists, not '*'
    - Do NOT use bold text

    Format your response as markdown with clear sections for:
    # Plan for <the name of the function, file, or class>
    1. Code Overview
    2. Main Components
    3. Workflow
    4. Potential Improvements
    5. Extension Ideas
    """

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,  
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        if 'response' in result:
            result = result['response']
        return result
    except Exception as e:
        print(f"Error communicating with Ollama: {e}")
        return None

def save_plan_to_file(plan_content, output_file):
    """Save the generated plan to a markdown file."""

    lines = plan_content.splitlines()

    # remove first line if it is "```markdown"
    if lines[0] and lines[0].startswith("```markdown"):
        lines[0] = ""

    # remove last line if it is "```"
    if lines[-1] and lines[-1].startswith("```"):
        lines[-1] = ""


    plan_content = "\n".join(lines).strip()

    # remove bold things
    # annoying
    plan_content = plan_content.replace(" **", "")
    plan_content = plan_content.replace("**  ", " ")
    plan_content = plan_content.replace("**", "")

    # remove extra spaces in lists
    plan_content = plan_content.replace("-     ", "- ")
    plan_content = plan_content.replace("-    ", "- ")
    plan_content = plan_content.replace("-   ", "- ")
    plan_content = plan_content.replace("-  ", "- ")
    plan_content = plan_content.replace(".  ", ". ")

    for line in plan_content.splitlines():
        chopped = line.strip()
        if chopped.startswith("* "):
            new_line = line.replace("* ", "- ")
            plan_content = plan_content.replace(line, new_line)

    # add a newline at the end of the file
    if not plan_content.endswith("\n"):
        plan_content += "\n"
            
    try:
        with open(output_file, 'w') as file:
            file.write(plan_content)
        print(f"Plan successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving plan to {output_file}: {e}")

def main():
    # Define file paths
    main_py_path = "main.py"
    plan_md_path = "plan.md"

    # Read the content from main.py
    code_content = read_file_content(main_py_path)
    if code_content is None:
        return

    print(f"Successfully read content from {main_py_path}")

    # Generate a plan using Ollama
    print("Requesting plan from Ollama...")
    plan = generate_plan_with_ollama(code_content)
    if plan is None:
        return

    # Save the plan to plan.md
    save_plan_to_file(plan, plan_md_path)

if __name__ == "__main__":
    main()
