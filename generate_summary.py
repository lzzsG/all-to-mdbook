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
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')  # 确保这个路径是正确的，或者根据需要进行调整
    repo_url = config['repository']['url']

    # 检查根目录下是否存在README.md，如果存在，则在最顶部添加它的引用
    readme_path = os.path.join(src_directory, "README.md")
    readme_link = ""
    if os.path.isfile(readme_path):
        readme_link = "[README](README.md)\n\n"
    
    # 生成目录内容
    summary_content = readme_link + '\n'.join(generate_summary(src_directory, "", ignore_dirs, 0, use_natural_sort))
    
    # 创建 about-this-mdbook.md 文件
    about_content = f"mdBook 内容来源：[{repo_url}]({repo_url})\n\nmdBook 自动生成：[https://github.com/lzzsG/test-all-to-mdbook](https://github.com/lzzsG/test-all-to-mdbook)"
    about_file_path = os.path.join(src_directory, "about-this-mdbook.md")
    with open(about_file_path, "w", encoding="utf-8") as about_file:
        about_file.write(about_content)
    
    # 在目录的最后添加 about-this-mdbook.md 的引用
    summary_content += "\n\n[About This MdBook](about-this-mdbook.md)"
    
    # 写入最终的 SUMMARY.md 文件
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