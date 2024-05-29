import os

def update_markdown_links(content_dir):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, content_dir)
                new_path_prefix = f"{{static}}/{relative_path}/images"
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = content.replace('](./images', f']({new_path_prefix}')
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Updated file: {file_path}")

content_directory = "content"
update_markdown_links(content_directory)
