import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "04_Polity_Constitution_Governance"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-POL-04",
    "filename": "04_parliament_of_india_structure_lawmaking_committees",
    "title": "Parliament of India: Legislative Procedures, Privileges & Committees",
    "mapping": "Polity, Constitution & Governance: Union Legislature - Parliament of India (Rajya Sabha, Lok Sabha), Lawmaking Process, Money Bill vs Financial Bill, Parliamentary Privileges, Committee System (PAC, Estimates), Anti-Defection Law (10th Schedule).",
    "intro": "The Parliament of India (comprising the President, Council of States / Rajya Sabha, and House of the People / Lok Sabha) serves as the supreme representative, legislative, and deliberative organ of the Union. Through financial control over the executive via Money Bills, scrutiny through Department-Related Standing Committees, and deterrence against political defection under the Tenth Schedule, Parliament upholds executive accountability to the electorate.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/New_Parliament_House_New_Delhi.jpg", "caption": "The new Parliament House (Sansad Bhavan) in New Delhi, the supreme legislative seat of India.", "alt": "New Parliament House building exterior"},
    "table": {
      "caption": "Procedural Comparison: Lok Sabha vs Rajya Sabha & Legislative Instruments",
      "headers": ["Legislative Dimension", "Lok Sabha (House of the People)", "Rajya Sabha (Council of States)"],
      "rows": [
        ["Composition & Tenure", "Maximum 550 members directly elected by universal adult suffrage; 5-year tenure subject to dissolution.", "Maximum 250 members (238 elected by state MLAs, 12 nominated by President); permanent House; 1/3rd retire every 2 years."],
        ["Special / Exclusive Powers", "Money Bills (Art 110) introduced solely in Lok Sabha; Council of Ministers collectively responsible only to Lok Sabha; voting on Demands for Grants.", "Article 249 (authorizing Parliament to legislate on State List); Article 312 (creating new All-India Services); approval of Emergency if Lok Sabha dissolved."],
        ["Financial Legislation", "Speaker certifies Money Bills; Lok Sabha can accept or reject all Rajya Sabha recommendations.", "Can only withhold Money Bill for 14 days without amendment power; cannot vote on Demands for Grants."],
        ["Parliamentary Committees", "Public Accounts Committee (22 members: 15 LS + 7 RS; chaired by Opposition MP); Estimates Committee (30 members, ALL from Lok Sabha); Committee on Public Undertakings (22 members).", "Represented on all joint committees except Estimates Committee; Departmentally-Related Standing Committees (DRSCs) scrutinize budgetary demands."]
      ]
    },
    "bullets": [
      "Lawmaking Stages: First Reading (introduction and gazette publication), Second Reading (general discussion, clause-by-clause scrutiny, committee stage), Third Reading (voting on the bill as a whole), transmission to second House, and Presidential Assent (Article 111).",
      "Joint Sitting of Parliament (Article 108): Summoned by President to resolve legislative deadlock on Ordinary Bills and Financial Bills; presided over by Speaker of Lok Sabha; decided by simple majority; NOT applicable to Money Bills (Art 110) or Constitutional Amendment Bills (Art 368).",
      "Parliamentary Privileges (Article 105): Collective (right to publish debates, exclude strangers, punish for contempt of House) and Individual (freedom of speech in Parliament, immunity from court arrest in civil cases 40 days before and after sessions).",
      "Anti-Defection Law (10th Schedule, 52nd Amendment 1985 & 91st Amendment 2003): Disqualifies MPs/MLAs for voluntarily giving up party membership or voting against party whip; decided by Presiding Officer; subject to judicial review per Kihoto Hollohan (1992)."
    ],
    "mains": [
      "Critically evaluate the role of Parliamentary Committees, especially the Public Accounts Committee (PAC) and Departmentally-Related Standing Committees (DRSCs), in ensuring executive accountability to Parliament. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the parliamentary committee system as 'mini-legislatures' overcoming the limitation of parliamentary time and large assembly size; analyze the Public Accounts Committee (PAC): examining CAG audit reports, detecting financial irregularities, traditionally chaired by senior Opposition leader to ensure bipartisan scrutiny; analyze DRSCs: in-depth scrutiny of ministerial Demands for Grants, evaluating legislative bills and policy implementation beyond party lines; discuss contemporary challenges: declining referral of bills to standing committees, absence of legislative impact assessments, and non-binding nature of committee recommendations; suggest statutory institutional strengthening."
    ],
    "mcqs": [
      "Q1. Which Parliamentary Committee is composed exclusively of 30 members drawn entirely from the Lok Sabha, without any representation from the Rajya Sabha?\n(a) Public Accounts Committee (PAC)\n(b) Estimates Committee\n(c) Committee on Public Undertakings (COPU)\n(d) Committee on Subordinate Legislation\nCorrect Answer: (b) Estimates Committee [Explanation: The Estimates Committee consists of 30 members elected annually solely from the Lok Sabha to scrutinize government expenditure estimates and suggest administrative economies.]",
      "Q2. Under Article 108 of the Constitution, a Joint Sitting of both Houses of Parliament to resolve a legislative deadlock is presided over by the:\n(a) President of India\n(b) Vice-President of India (Rajya Sabha Chairman)\n(c) Speaker of the Lok Sabha\n(d) Union Minister for Parliamentary Affairs\nCorrect Answer: (c) Speaker of the Lok Sabha [Explanation: Under Article 118(4), the Speaker of the Lok Sabha (or in their absence, the Deputy Speaker) presides over joint sittings of Parliament summoned under Article 108.]",
      "Q3. In which landmark 1992 judgment did the Supreme Court hold that the decision of the Speaker/Chairman under the Tenth Schedule (Anti-Defection Law) is subject to judicial review?\n(a) Kesavananda Bharati Case\n(b) Kihoto Hollohan v. Zachillhu\n(c) S.R. Bommai Case\n(d) Indira Nehru Gandhi Case\nCorrect Answer: (b) Kihoto Hollohan v. Zachillhu [Explanation: In Kihoto Hollohan (1992), a constitution bench ruled that the Speaker acts as a tribunal when deciding anti-defection disqualifications and is subject to High Court/Supreme Court judicial review.]",
      "Q4. If a Money Bill transmitted by the Lok Sabha to the Rajya Sabha is not returned within how many days, it is deemed to have been passed by both Houses in its original form?\n(a) 14 days\n(b) 21 days\n(c) 30 days\n(d) 6 weeks\nCorrect Answer: (a) 14 days [Explanation: Under Article 109(5), the Rajya Sabha must return a Money Bill with or without recommendations within 14 days, failing which the bill automatically stands passed.]",
      "Q5. Which Article of the Indian Constitution empowers the Rajya Sabha to pass a special resolution with a two-thirds majority authorizing Parliament to legislate on a matter in the State List?\n(a) Article 249\n(b) Article 252\n(c) Article 312\n(d) Article 356\nCorrect Answer: (a) Article 249 [Explanation: Article 249 grants the Rajya Sabha exclusive power to declare by two-thirds majority that it is necessary in the national interest for Parliament to make laws on a State List subject for one year.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-05",
    "filename": "05_state_executive_and_state_legislature",
    "title": "State Executive & State Legislature: Governor, CM & Legislative Council",
    "mapping": "Polity, Constitution & Governance: State Government - Governor (Appointment, Powers, Constitutional Discretion Art 163, Sarkaria and Punchhi Recommendations), Chief Minister, State Council of Ministers, Legislative Assembly and Legislative Council (Art 169).",
    "intro": "The constitutional machinery at the state level mirrors the parliamentary structure of the Union. Headed by the Governor as the representative of the Union and constitutional executive, real authority resides in the Chief Minister and Council of Ministers responsible to the Legislative Assembly (Vidhan Sabha). The office of the Governor remains a sensitive focal point of Indian federalism, particularly regarding discretionary powers and recommendations under Article 356.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Andhra_Pradesh_Legislative_Assembly.jpg", "caption": "The Andhra Pradesh Legislative Assembly building at Velagapudi, Amaravati.", "alt": "Andhra Pradesh Legislative Assembly complex"},
    "table": {
      "caption": "Executive & Legislative Balance in State Governance",
      "headers": ["State Constitutional Organ", "Constitutional Articles", "Powers, Appointment & Composition", "Federal Challenges & Legal Standards"],
      "rows": [
        ["Governor of the State", "Articles 153 to 162, 163, 164, 200, 213, 356.", "Appointed by President; holds office during presidential pleasure; executive head of state.", "Discretionary powers under Art 163; reservation of bills for President (Art 200/201); appointment of CM in hung assemblies; reports on breakdown of constitutional machinery (Art 356 - S.R. Bommai guidelines)."],
        ["Chief Minister & State Council of Ministers", "Articles 163, 164, 167.", "CM appointed by Governor; ministers on CM's advice; collective responsibility to Legislative Assembly.", "Formulates state policy; real executive; communicates administrative decisions to Governor (Art 167)."],
        ["State Legislative Assembly (Vidhan Sabha)", "Article 170.", "Directly elected by adult suffrage (max 500, min 60 members; 175 members in Andhra Pradesh).", "Supreme legislative authority in state; exclusive power over Money Bills and state budget."],
        ["State Legislative Council (Vidhan Parishad)", "Articles 169, 171.", "Created or abolished by Parliament on special resolution by Assembly (Art 169); bicameral in 6 states (AP, Bihar, Karnataka, Maharashtra, Telangana, UP).", "Revisory second chamber (1/3rd elected by MLAs, 1/3rd by local bodies, 1/12th by graduates, 1/12th by teachers, 1/6th nominated by Governor); can delay ordinary bills by max 4 months."]
      ]
    },
    "bullets": [
      "Article 200 Options for Governor on Passed Bills: Give assent, withhold assent, return bill for reconsideration (if not Money Bill), or reserve bill for the consideration of the President (mandatory if bill endangers High Court powers).",
      "S.R. Bommai Guidelines on Article 356 (1994): Majority of ministry must be tested solely on the floor of the Assembly, not in Raj Bhavan; presidential proclamation subject to judicial review; dissolution of assembly permissible only after Parliament approves proclamation.",
      "Sarkaria Commission Recommendations on Governor: Eminent person from outside the state, detached from local active politics, appointed in consultation with Chief Minister, guaranteed fixed 5-year tenure save rare exceptions.",
      "Punchhi Commission (2010): Recommended localizing emergency under Art 355, adopting clear guidelines for government formation (leader of pre-poll alliance first), and amending Art 163 to curtail unfettered discretionary delays on bills."
    ],
    "mains": [
      "Critically examine the constitutional discretionary powers of the Governor under Article 163. How have judicial rulings in S.R. Bommai (1994) and Nabam Rebia (2016) circumscribed gubernatorial discretion in state politics? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Differentiate between constitutional discretion (expressly granted: reserving bills under Art 200, recommending President's Rule under Art 356) and situational discretion (appointing CM in hung house, dismissing ministry); evaluate federal frictions: Governor acting as partisan central agent to destabilize state ministries; analyze S.R. Bommai (1994) establishing that floor test is the sole acid test of majority and making Art 356 judicially reviewable; analyze Nabam Rebia (2016) ruling that Governor cannot summon or advance assembly sessions without the aid and advice of the Chief Minister; conclude on implementing Sarkaria and Punchhi commission recommendations to depoliticize the gubernatorial office."
    ],
    "mcqs": [
      "Q1. Under Article 169 of the Constitution of India, which body holds the constitutional power to create or abolish a State Legislative Council (Vidhan Parishad)?\n(a) State Legislative Assembly\n(b) Parliament of India\n(c) President of India\n(d) Governor of the State\nCorrect Answer: (b) Parliament of India [Explanation: Under Article 169, Parliament can by law create or abolish a Legislative Council if the State Legislative Assembly passes a resolution by special majority.]",
      "Q2. In which landmark 1994 verdict did the nine-judge bench of the Supreme Court rule that the floor of the Legislative Assembly is the sole constitutional forum to test a Chief Minister's majority?\n(a) Rameshwar Prasad Case\n(b) S.R. Bommai v. Union of India\n(c) Nabam Rebia Case\n(d) Kesavananda Bharati Case\nCorrect Answer: (b) S.R. Bommai v. Union of India [Explanation: The S.R. Bommai judgment (1994) curtailed misuse of Article 356, establishing that a ministry's majority can only be verified through a floor test in the Assembly.]",
      "Q3. How many members of a State Legislative Council are nominated by the Governor from among persons having special knowledge in literature, science, art, cooperative movement, and social service?\n(a) 1/3rd of total members\n(b) 1/6th of total members\n(c) 1/12th of total members\n(d) 1/10th of total members\nCorrect Answer: (b) 1/6th of total members [Explanation: Under Article 171(3)(e), 1/6th of the total members of the Legislative Council are nominated by the Governor from literature, science, art, cooperative movement, and social service.]",
      "Q4. Which Commission on Centre-State Relations (appointed in 1983) recommended that the Governor should be an eminent person from outside the state and not intimately connected with local politics?\n(a) Punchhi Commission\n(b) Sarkaria Commission\n(c) Rajamannar Committee\n(d) Venkatachaliah Commission\nCorrect Answer: (b) Sarkaria Commission [Explanation: Justice R.S. Sarkaria Commission (1983–1988) recommended that Governors should be distinguished persons from outside the state, appointed in consultation with the Chief Minister.]",
      "Q5. Under Article 213 of the Constitution, what is the maximum life of an Ordinance promulgated by a Governor during the recess of the State Legislature without legislative approval?\n(a) 6 months\n(b) 6 weeks from the reassembly of the legislature\n(c) 14 days\n(d) 3 months\nCorrect Answer: (b) 6 weeks from the reassembly of the legislature [Explanation: An Ordinance issued by the Governor under Article 213 ceases to operate six weeks after the reassembly of the State Legislature unless approved earlier.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-06",
    "filename": "06_indian_judiciary_supreme_court_high_courts_pil",
    "title": "Indian Judiciary: Supreme Court, High Courts, Collegium & PIL",
    "mapping": "Polity, Constitution & Governance: The Judiciary - Supreme Court of India (Jurisdictions: Original Art 131, Appellate, Advisory Art 143, Review), High Courts and Subordinate Courts, Collegium System, Judicial Review, Judicial Activism and Public Interest Litigation (PIL).",
    "intro": "The Indian Constitution establishes an integrated, single judicial pyramid with the Supreme Court at the apex, exercising supreme appellate authority, constitutional interpretation, and the defense of fundamental rights. Characterized by judicial independence guaranteed through tenure security and the judge-led Collegium appointment system, the Indian judiciary has pioneered proactive constitutional tools like Judicial Review, Judicial Activism, and Public Interest Litigation (PIL).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/High_Court_Andhra_Pradesh.jpg", "caption": "The High Court of Andhra Pradesh at Nelapadu, Amaravati, exercising constitutional jurisdiction under Article 226.", "alt": "Andhra Pradesh High Court building Amaravati"},
    "table": {
      "caption": "Jurisdictional Spectrum of the Supreme Court of India",
      "headers": ["Constitutional Jurisdiction", "Article Reference", "Legal Scope & Subject Matter", "Key Precedents & Principles"],
      "rows": [
        ["Original Jurisdiction", "Article 131", "Exclusive disputes between Government of India and one or more States, or between two or more States.", "Federal interstate legal disputes (State of Karnataka v. Union of India); excludes pre-constitution treaties."],
        ["Writ Jurisdiction", "Article 32 (SC) & Article 226 (HC)", "Enforcement of Fundamental Rights; power to issue 5 writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo-Warranto).", "Art 32 is itself a Fundamental Right; Art 226 of High Courts is broader, extending to 'any other legal right'."],
        ["Appellate Jurisdiction", "Articles 132, 133, 134, 136 (Special Leave Petition - SLP).", "Appeals from High Courts in constitutional, civil, and criminal matters; Article 136 grants discretionary residual power to hear appeals against any court/tribunal.", "Article 136 is an exceptional plenary jurisdiction to correct gross miscarriages of justice."],
        ["Advisory Jurisdiction", "Article 143", "President may refer questions of law or public importance to Supreme Court for opinion.", "SC opinion is advisory and not binding on President; e.g., Berubari Union (1960), Special Courts Bill (1978), 2G Spectrum (2012)."],
        ["Court of Record & Review", "Articles 129 & 137", "Judgments have evidentiary value and cannot be questioned in lower courts; power to punish for contempt of itself; power to review its own judgments.", "Enables self-correction of past constitutional doctrines."]
      ]
    },
    "bullets": [
      "The Collegium System: Developed through the 'Three Judges Cases' (SP Gupta 1981, Advocates-on-Record 1993, Special Reference 1998); Chief Justice of India and 4 senior-most Supreme Court judges recommend appointments to SC and High Courts; Supreme Court struck down the National Judicial Appointments Commission (NJAC, 99th Amendment 2014) in the Fourth Judges Case (2015) to preserve judicial independence.",
      "Public Interest Litigation (PIL): Relaxed traditional 'Locus Standi' rule; pioneered in late 1970s by Justices P.N. Bhagwati and V.R. Krishna Iyer; permits any public-spirited citizen or NGO to file writ petitions on behalf of disadvantaged citizens unable to access justice (Hussainara Khatoon 1979 - rights of undertrials; Bandhua Mukti Morcha 1984 - bonded labour).",
      "Judicial Review: Inherent in Articles 13, 32, 136, 142, and 226; power to declare legislative enactments and executive orders null and void if they violate constitutional provisions.",
      "Article 142 (Complete Justice): Unique constitutional power authorizing the Supreme Court to pass any decree or order necessary for doing 'complete justice' in any cause or matter before it (used in Union Carbide, Ayodhya title suit, ban on liquor shops on highways)."
    ],
    "mains": [
      "Critically evaluate the functioning of the Collegium system for judicial appointments in India. Examine the constitutional tension between Judicial Independence and Executive accountability highlighted by the NJAC judgment (2015). (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Trace the evolution of the Collegium through the Three Judges Cases, creating an unprecedented system where judges appoint judges; analyze the NJAC (99th Amendment Act 2014) proposing a 6-member commission including the Law Minister and eminent persons; explain why the Supreme Court struck down the NJAC in the Fourth Judges Case (2015): holding that executive presence in judicial appointments infringes Judicial Independence, which is a Basic Structure feature; evaluate criticisms of the Collegium: lack of transparency, nepotism, absence of public scrutiny, and delays in filling vacancies; suggest balanced reforms through a revised Memorandum of Procedure (MoP) incorporating objective eligibility criteria and search committees."
    ],
    "mcqs": [
      "Q1. Which Article of the Constitution of India empowers the Supreme Court to pass any decree or order necessary for doing 'complete justice' in any cause or matter?\n(a) Article 136\n(b) Article 141\n(c) Article 142\n(d) Article 143\nCorrect Answer: (c) Article 142 [Explanation: Article 142 provides the Supreme Court with extraordinary equitable power to issue orders necessary for doing 'complete justice' between the parties.]",
      "Q2. The concept of 'Public Interest Litigation' (PIL), which liberalized the traditional rule of locus standi, was pioneered in India primarily by which Supreme Court jurist?\n(a) Justice H.R. Khanna\n(b) Justice P.N. Bhagwati\n(c) Justice M.N. Venkatachaliah\n(d) Justice Y.V. Chandrachud\nCorrect Answer: (b) Justice P.N. Bhagwati [Explanation: Justice P.N. Bhagwati (alongside Justice V.R. Krishna Iyer) institutionalized Public Interest Litigation in India in cases like Hussainara Khatoon and SP Gupta.]",
      "Q3. In which landmark verdict in October 2015 did a five-judge constitutional bench of the Supreme Court strike down the National Judicial Appointments Commission (NJAC)?\n(a) First Judges Case (1981)\n(b) Second Judges Case (1993)\n(c) Third Judges Case (1998)\n(d) Fourth Judges Case (2015)\nCorrect Answer: (d) Fourth Judges Case (2015) [Explanation: In the Fourth Judges Case (Supreme Court Advocates-on-Record Association v. Union of India, 2015), the court struck down the 99th Amendment Act and the NJAC as unconstitutional.]",
      "Q4. Under Article 143 of the Constitution, who possesses the exclusive authority to refer a question of law or fact of public importance to the Supreme Court for its advisory opinion?\n(a) Prime Minister of India\n(b) President of India\n(c) Speaker of the Lok Sabha\n(d) Attorney General for India\nCorrect Answer: (b) President of India [Explanation: Article 143 empowers the President of India to consult the Supreme Court on questions of law or fact of public importance.]",
      "Q5. How does the writ jurisdiction of a High Court under Article 226 differ fundamentally from that of the Supreme Court under Article 32?\n(a) High Court cannot issue Habeas Corpus\n(b) High Court can issue writs only for fundamental rights\n(c) High Court's writ jurisdiction extends to fundamental rights as well as ordinary legal rights\n(d) Supreme Court has wider writ jurisdiction than High Courts\nCorrect Answer: (c) High Court's writ jurisdiction extends to fundamental rights as well as ordinary legal rights [Explanation: Under Article 226, High Courts can issue writs for fundamental rights and 'for any other purpose' (ordinary legal rights), making its scope wider than Article 32.]"
    ]
  }
]

for t in topics:
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "Polity, Constitution & Governance",
    "paper": "Mains Paper-III (Section A) & Screening Paper-I (Section C)",
    "topic_title": t["title"],
    "syllabus_mapping": t["mapping"],
    "last_updated": "2026-10",
    "content": [
      {"type": "heading", "level": 1, "text": t["title"]},
      {"type": "paragraph", "text": t["intro"]},
      {"type": "image", "url": t["img"]["url"], "caption": t["img"]["caption"], "alt_text": t["img"]["alt"]},
      {"type": "heading", "level": 2, "text": "1. Institutional & Structural Framework"},
      {"type": "table", "caption": t["table"]["caption"], "headers": t["table"]["headers"], "rows": t["table"]["rows"]},
      {"type": "heading", "level": 2, "text": "2. Salient Dimensions & Critical Analysis"},
      {"type": "list", "style": "bullet", "items": t["bullets"]},
      {"type": "heading", "level": 2, "text": "Previous Years Questions (PYQs) - APPSC Group-1"},
      {"type": "heading", "level": 3, "text": "Part A: Mains Analytical & Descriptive Questions"},
      {"type": "list", "style": "numbered", "items": t["mains"]},
      {"type": "heading", "level": 3, "text": "Part B: Screening / Prelims Objective Questions"},
      {"type": "list", "style": "bullet", "items": t["mcqs"]}
    ]
  }
  
  text_content = ""
  for c in data["content"]:
    if "text" in c: text_content += c["text"] + " "
    if "items" in c: text_content += " ".join(c["items"]) + " "
    if "rows" in c:
      for r in c["rows"]: text_content += " ".join(r) + " "
  words = len(text_content.split())
  data["word_count"] = words
  data["estimated_read_time_mins"] = max(3, round(words / 170))
  data["file_name"] = f"{t['filename']}.json"
  data["folder"] = FOLDER
  
  json_path = os.path.join(SUBJ_DIR, f"{t['filename']}.json")
  with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
  md_lines = [
    f"# {data['topic_title']}\n",
    f"**Topic ID:** `{data['topic_id']}` | **Subject:** {data['subject_title']} | **Paper:** {data['paper']}\n",
    f"**Syllabus Mapping:** {data['syllabus_mapping']}\n",
    "---\n"
  ]
  for item in data["content"]:
    t_type = item.get("type")
    if t_type == "heading":
      md_lines.append(f"\n{'#' * item.get('level', 2)} {item.get('text')}\n")
    elif t_type == "paragraph":
      md_lines.append(f"\n{item.get('text')}\n")
    elif t_type == "image":
      md_lines.append(f"\n![{item.get('alt_text', 'Illustration')}]({item.get('url')})\n*Caption: {item.get('caption', '')}*\n")
    elif t_type == "table":
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
    elif t_type == "list":
      style = item.get("style", "bullet")
      items = item.get("items", [])
      for idx, it in enumerate(items, 1):
        if style == "numbered":
          md_lines.append(f"{idx}. {it}\n")
        else:
          md_lines.append(f"* {it}\n")
      md_lines.append("\n")
      
  md_path = os.path.join(SUBJ_DIR, f"{t['filename']}.md")
  with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))
  print(f"Generated {t['filename']} ({words} words)")

print("Part 2 of Subject 4 generated successfully")
