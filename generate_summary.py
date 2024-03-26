import os
import re
import configparser

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def generate_summary(directory, base_path="", ignore_dirs=[], level=0, use_natural_sort=False):
    summary_lines = []
    items = [item for item in os.listdir(directory) if item not in ignore_dirs]
    
    if use_natural_sort:
        items.sort(key=natural_sort_key)
    else:
        items.sort(key=lambda x: x.lower())
    
    indent = '    ' * level

    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            summary_lines.append(f"{indent}- [{item}]()")
            new_base = os.path.join(base_path, item)
            summary_lines.extend(generate_summary(path, new_base, ignore_dirs, level + 1, use_natural_sort))
        elif item.endswith(".md"):
            link = os.path.join(base_path, item).replace('\\', '/')
            name = os.path.splitext(item)[0]
            summary_lines.append(f"{indent}- [{name}]({link})")

    return summary_lines

def create_summary_file(src_directory, output_file="SUMMARY.md", ignore_dirs=[], use_natural_sort=False):
    summary_content = '\n'.join(generate_summary(src_directory, "", ignore_dirs, 0, use_natural_sort))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(summary_content)
    print(f"SUMMARY.md has been created at {output_file}")

def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    src_directory = config['src']['directory']
    output_file = config['src'].get('output_file', 'SUMMARY.md')
    ignore_dirs = config['src'].get('ignore_dirs', '').split(',')
    use_natural_sort = config['src'].getboolean('use_natural_sort', False)
    
    return src_directory, output_file, ignore_dirs, use_natural_sort

def main():
    src_directory, output_file, ignore_dirs, use_natural_sort = read_config('config.ini')
    create_summary_file(src_directory, output_file, ignore_dirs, use_natural_sort)

if __name__ == "__main__":
    main()
