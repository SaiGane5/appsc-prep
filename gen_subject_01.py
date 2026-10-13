import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
SUBJ_DIR = os.path.join(BASE_DIR, "01_History_and_Culture_India")

def save_note(data, filename_base):
    # Calculate word count
    text_content = ""
    for c in data["content"]:
        if "text" in c: text_content += c["text"] + " "
        if "items" in c: text_content += " ".join(c["items"]) + " "
        if "rows" in c:
            for r in c["rows"]: text_content += " ".join(r) + " "
    words = len(text_content.split())
    data["word_count"] = words
    data["estimated_read_time_mins"] = max(3, round(words / 170))
    data["file_name"] = f"{filename_base}.json"
    data["folder"] = "01_History_and_Culture_India"
    
    # Save JSON
    json_path = os.path.join(SUBJ_DIR, f"{filename_base}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    # Save Markdown
    md_lines = [
        f"# {data['topic_title']}\n",
        f"**Topic ID:** `{data['topic_id']}` | **Subject:** {data['subject_title']} | **Paper:** {data['paper']}\n",
        f"**Syllabus Mapping:** {data['syllabus_mapping']}\n",
        "---\n"
    ]
    for item in data["content"]:
        t = item.get("type")
        if t == "heading":
            md_lines.append(f"\n{'#' * item.get('level', 2)} {item.get('text')}\n")
        elif t == "paragraph":
            md_lines.append(f"\n{item.get('text')}\n")
        elif t == "image":
            md_lines.append(f"\n![{item.get('alt_text', 'Illustration')}]({item.get('url')})\n*Caption: {item.get('caption', '')}*\n")
        elif t == "table":
            if item.get("caption"):
                md_lines.append(f"\n### Table: {item.get('caption')}\n")
            headers = item.get("headers", [])
            rows = item.get("rows", [])
            if headers:
                md_lines.append("| " + " | ".join(headers) + " |")
                md_lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
                for r in rows:
                    md_lines.append("| " + " | ".join(r) + " |")
                md_lines.append("\n")
        elif t == "list":
            style = item.get("style", "bullet")
            items = item.get("items", [])
            for idx, it in enumerate(items, 1):
                if style == "numbered":
                    md_lines.append(f"{idx}. {it}\n")
                else:
                    md_lines.append(f"* {it}\n")
            md_lines.append("\n")
            
    md_path = os.path.join(SUBJ_DIR, f"{filename_base}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"Generated {filename_base} ({words} words)")

print("Script template ready")
