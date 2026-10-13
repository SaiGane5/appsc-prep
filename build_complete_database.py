import os
import json
import re

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
WEB_APP_DATA = os.path.join(BASE_DIR, "web-app/src/data")
os.makedirs(WEB_APP_DATA, exist_ok=True)

SUBJECT_FOLDERS = [
  ("01_History_and_Culture_India", "History and Culture of India", "Mains Paper-II (Section A) & Screening Paper-I (Section A)"),
  ("02_History_and_Culture_AP", "History and Culture of Andhra Pradesh", "Mains Paper-II (Section B) & Screening Paper-I (Section B)"),
  ("03_Geography_India_and_AP", "Geography - India & Andhra Pradesh", "Mains Paper-II (Section C) & Screening Paper-I (Section C)"),
  ("04_Polity_Constitution_Governance", "Polity, Constitution, Governance, Law & Ethics", "Mains Paper-III (Section A) & Screening Paper-I (Section D)"),
  ("05_Ethics_and_Law", "Ethics and Law", "Mains Paper-III (Section B) & Screening Paper-I (Section D)"),
  ("06_Economy_India_and_AP", "Economy - India & AP", "Mains Paper-IV & Screening Paper-II"),
  ("07_Science_Technology_Environment", "Science, Technology & Environment", "Mains Paper-V & Screening Paper-II"),
  ("08_General_Mental_and_Psychological_Abilities", "General Mental and Psychological Abilities", "Screening Paper-II (Section B)")
]

all_notes = []
manifest_subjects = []
mcq_bank = []
mains_bank = []

total_word_count = 0

for folder_name, default_title, default_paper in SUBJECT_FOLDERS:
  folder_path = os.path.join(BASE_DIR, folder_name)
  if not os.path.exists(folder_path):
    print(f"Warning: {folder_path} does not exist")
    continue

  json_files = sorted([f for f in os.listdir(folder_path) if f.endswith(".json")])
  print(f"Processing {folder_name}: {len(json_files)} topics")

  subject_topics = []
  
  for order_idx, jf in enumerate(json_files, 1):
    file_path = os.path.join(folder_path, jf)
    with open(file_path, "r", encoding="utf-8") as f:
      note = json.load(f)

    # Ensure required fields
    note["folder"] = folder_name
    note["file_name"] = jf
    if "subject_title" not in note or not note["subject_title"]:
      note["subject_title"] = default_title
    if "paper" not in note or not note["paper"]:
      note["paper"] = default_paper
      
    all_notes.append(note)
    total_word_count += note.get("word_count", 0)

    subject_topics.append({
      "order": order_idx,
      "topic_id": note.get("topic_id", f"TOPIC-{order_idx}"),
      "file": jf,
      "title": note.get("topic_title", jf.replace(".json", "").replace("_", " ").title()),
      "word_count": note.get("word_count", 0),
      "status": "completed"
    })

    # Extract MCQs & Mains questions
    content = note.get("content", [])
    in_mains_section = False
    in_prelims_section = False

    for block in content:
      b_type = block.get("type")
      b_text = block.get("text", "")

      if b_type == "heading":
        if "Part A: Mains" in b_text or "Part A: Analytical" in b_text or "Mains Analytical" in b_text:
          in_mains_section = True
          in_prelims_section = False
        elif "Part B: Screening" in b_text or "Part B: Prelims" in b_text or "Objective Questions" in b_text:
          in_prelims_section = True
          in_mains_section = False
        elif block.get("level", 2) <= 2:
          in_mains_section = False
          in_prelims_section = False

      elif b_type == "list":
        items = block.get("items", [])
        if in_mains_section:
          for it in items:
            mains_bank.append({
              "topic_id": note.get("topic_id", ""),
              "topic_title": note.get("topic_title", ""),
              "subject_title": note.get("subject_title", ""),
              "raw_text": it
            })
        elif in_prelims_section:
          for it in items:
            mcq_bank.append({
              "topic_id": note.get("topic_id", ""),
              "topic_title": note.get("topic_title", ""),
              "subject_title": note.get("subject_title", ""),
              "raw_text": it
            })
        else:
          # Fallback check if item has Q or Question format
          for it in items:
            str_it = str(it)
            if "**Q:" in str_it or str_it.startswith("Q1.") or str_it.startswith("Q2.") or str_it.startswith("Q3.") or str_it.startswith("Q4.") or str_it.startswith("Q5."):
              mcq_bank.append({
                "topic_id": note.get("topic_id", ""),
                "topic_title": note.get("topic_title", ""),
                "subject_title": note.get("subject_title", ""),
                "raw_text": it
              })

  manifest_subjects.append({
    "folder": folder_name,
    "title": default_title,
    "paper": default_paper,
    "topics_count": len(subject_topics),
    "topics": subject_topics
  })

manifest = {
  "exam": "APPSC Group-1 Services 2026-2027",
  "notification": "Notification No. 07/2026, Dated: 06/10/2026",
  "screening_date": "24/01/2027",
  "structure": {
    "total_subjects": len(manifest_subjects),
    "total_topics": len(all_notes),
    "completed_topics": len(all_notes),
    "progress_percentage": "100.0%",
    "total_word_count": total_word_count,
    "total_mcqs": len(mcq_bank),
    "total_mains_questions": len(mains_bank)
  },
  "subjects": manifest_subjects
}

# Write syllabus_manifest.json
manifest_path = os.path.join(BASE_DIR, "syllabus_manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
  json.dump(manifest, f, indent=2, ensure_ascii=False)
print(f"Saved {manifest_path} with {len(all_notes)} topics, {len(mcq_bank)} MCQs, {len(mains_bank)} Mains questions")

# Write web-app/src/data/notesDatabase.js
js_file_path = os.path.join(WEB_APP_DATA, "notesDatabase.js")
with open(js_file_path, "w", encoding="utf-8") as f:
  f.write("// Auto-generated APPSC Group-1 Master Notes Database\n")
  f.write(f"export const manifest = {json.dumps(manifest, indent=2, ensure_ascii=False)};\n\n")
  f.write(f"export const allNotes = {json.dumps(all_notes, indent=2, ensure_ascii=False)};\n\n")
  f.write(f"export const mcqBank = {json.dumps(mcq_bank, indent=2, ensure_ascii=False)};\n\n")
  f.write(f"export const mainsBank = {json.dumps(mains_bank, indent=2, ensure_ascii=False)};\n")

print(f"Successfully compiled {js_file_path}!")
print(f"Total notes: {len(all_notes)}")
print(f"Total MCQs: {len(mcq_bank)}")
print(f"Total Mains PYQs: {len(mains_bank)}")
