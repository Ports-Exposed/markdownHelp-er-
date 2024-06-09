#!/usr/bin/env python3
import subprocess
import sys
import re

def run_help_command(command):
    try:
        result = subprocess.run(command, text=True, capture_output=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

def format_flags(text):
    return re.sub(r'(\s|\[)(-{1,2}[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*)(?=\s|,|\]|$)', r'\1`\2`', text)

def parse_help(output):
    sections = {'Usage': '', 'Positional Arguments': '', 'Options': ''}
    lines = output.splitlines()
    current_section = None

    for line in lines:
        if 'usage:' in line:
            sections['Usage'] = line.replace('usage:', '').strip()
            current_section = None
        elif 'positional arguments:' in line:
            current_section = 'Positional Arguments'
            sections[current_section] = ''
        elif 'options:' in line:
            current_section = 'Options'
            sections[current_section] = ''
        elif current_section:
            sections[current_section] += format_flags(line.strip()) + '<br> '
        elif line.strip() and not current_section:
            sections['Usage'] += ' ' + format_flags(line.strip())

    return sections

def extract_operations(positional_arguments):
    operations = re.findall(r'{(.*?)}', positional_arguments)
    if operations:
        return [op.strip() for op in operations[0].split(',')]
    return []

def generate_markdown(help_data):
    markdown = ["<!--HELP GEN START-->"]
    markdown.append("## Help Documentation")
    markdown.append("| Operation | Usage | Positional Arguments | Options |")
    markdown.append("| --- | --- | --- | --- |")

    for op, data in help_data.items():
        usage = data['Usage']
        pos_args = data['Positional Arguments']
        options = data['Options']
        markdown.append(f"| **{op}** | {usage} | {pos_args} | {options} |")

    markdown.append("<!--HELP GEN END-->")
    return '\n'.join(markdown)

def main(script_name):
    help_data = {}
    main_help_output = run_help_command([script_name, '-h'])
    if not main_help_output:
        print("Failed to get help output for the main command.")
        return

    main_sections = parse_help(main_help_output)
    help_data['Main'] = main_sections
    operations = extract_operations(main_sections['Positional Arguments'])

    for operation in operations:
        op_help_output = run_help_command([script_name, operation, '-h'])
        if op_help_output:
            op_sections = parse_help(op_help_output)
            if any(help_data[op].get('Usage') == op_sections.get('Usage') for op in help_data):
                print(f"Skipping duplicate help output for alias: {operation}")
                continue
            help_data[operation] = op_sections
        else:
            print(f"Failed to get help output for operation: {operation}")

    markdown_content = generate_markdown(help_data)
    print(markdown_content)
    with open('help_output.md', 'w') as f:
        f.write(markdown_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markdownHelper.py <script_name>")
    else:
        main(sys.argv[1])