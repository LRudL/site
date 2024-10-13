import os
import re
from build import load_metas

def update_image_references(content: str, label: str) -> str:
    def replace_image(match):
        alt_text, old_path = match.groups()
        new_path = f"img/{label}/{os.path.basename(old_path)}"
        return f"![{alt_text}]({new_path})"

    image_pattern = r'!\[(.*?)\]\((.*?)\)'
    return re.sub(image_pattern, replace_image, content)

def process_markdown_files(src_dir: str = "src"):
    metas = load_metas()

    for meta in metas:
        md_file_path = os.path.join(src_dir, f"{meta.label}.md")
        
        if not os.path.exists(md_file_path):
            print(f"Warning: Markdown file for '{meta.label}' not found. Skipping.")
            continue

        with open(md_file_path, "r") as f:
            content = f.read()

        updated_content = update_image_references(content, meta.label)

        if content != updated_content:
            with open(md_file_path, "w") as f:
                f.write(updated_content)
            # print(f"Updated image references in {meta.label}.md")
        # else:
            # print(f"No changes needed for {meta.label}.md")

if __name__ == "__main__":
    process_markdown_files()
