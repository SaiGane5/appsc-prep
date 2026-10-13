import os
import json
import re

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
WEB_APP_DATA_DIR = os.path.join(BASE_DIR, "web-app/src/data")

def json_to_markdown(note):
    md = []
    md.append(f"# {note['topic_title']}\n")
    md.append(f"**Topic ID:** `{note['topic_id']}` | **Subject:** {note['subject_title']} | **Paper:** {note['paper']}\n")
    md.append(f"**Syllabus Mapping:** {note['syllabus_mapping']}\n")
    md.append("---\n")
    
    for item in note['content']:
        itype = item.get('type')
        if itype == 'heading':
            lvl = '#' * (item.get('level', 2))
            md.append(f"\n{lvl} {item.get('text')}\n")
        elif itype == 'paragraph':
            md.append(f"\n{item.get('text')}\n")
        elif itype == 'image':
            md.append(f"\n![{item.get('alt_text', 'Illustration')}]({item.get('url')})\n*Caption: {item.get('caption', '')}*\n")
        elif itype == 'table':
            caption = item.get('caption')
            if caption:
                md.append(f"\n### Table: {caption}\n")
            headers = item.get('headers', [])
            rows = item.get('rows', [])
            if headers:
                md.append("| " + " | ".join(headers) + " |")
                md.append("| " + " | ".join(["---"] * len(headers)) + " |")
                for r in rows:
                    md.append("| " + " | ".join(r) + " |")
                md.append("\n")
        elif itype == 'list':
            style = item.get('style', 'bullet')
            items = item.get('items', [])
            for idx, it in enumerate(items, 1):
                if style == 'numbered':
                    md.append(f"{idx}. {it}\n")
                else:
                    md.append(f"* {it}\n")
            md.append("\n")
    return "\n".join(md)

print("Helper defined successfully")
