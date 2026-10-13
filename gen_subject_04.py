import os, json, glob

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "04_Polity_Constitution_Governance"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-POL-01",
    "filename": "01_constitutional_evolution_preamble_and_basic_features",
    "title": "Constitutional Evolution, Preamble & Basic Structure Doctrine",
    "mapping": "Polity, Constitution & Governance: Constitutional Framework - Historical Evolution (Acts of 1773 to 1947), Constituent Assembly, Preamble (Philosophy and Values), Salient Features and Basic Structure Doctrine (Kesavananda Bharati).",
    "intro": "The Constitution of India represents the world's most detailed written democratic social contract. Evolving through colonial administrative experiments (Regulating Act 1773 to Government of India Act 1935) and crafted by the Constituent Assembly under Dr. B.R. Ambedkar, the Constitution embodies a transformative philosophy in its Preamble and is anchored by the judicial Basic Structure Doctrine established in the historic Kesavananda Bharati case (1973).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Constitution_of_India_Preamble.jpg", "caption": "The original calligraphy of the Preamble to the Constitution of India, decorated by Beohar Rammanohar Sinha.", "alt": "Preamble to the Constitution of India original artwork"},
    "table": {
      "caption": "Evolutionary Milestones in the Making of the Indian Constitution",
      "headers": ["Constitutional Milestone", "Year & Statutory Instrument", "Core Provisions & Institutional Innovations", "Impact on Contemporary Constitution"],
      "rows": [
        ["Government of India Act 1935", "1935 (British Parliament)", "Federal Scheme, Provincial Autonomy, Bicameralism in 6 provinces, Federal Court, Three Legislative Lists.", "Over 60% of current administrative and structural provisions borrowed directly from this Act."],
        ["Constituent Assembly", "1946–1949 (Cabinet Mission Plan)", "389 initial members; Drafting Committee chaired by Dr. B.R. Ambedkar; completed in 2 yrs, 11 mos, 18 days.", "Framed 395 Articles and 8 Schedules adopted on 26 Nov 1949; came into force on 26 Jan 1950."],
        ["Preamble & 42nd Amendment", "Adopted 1949; Amended 1976", "Declared India a Sovereign, Socialist, Secular, Democratic Republic committed to Justice, Liberty, Equality, Fraternity.", "42nd Amendment 1976 added 'Socialist', 'Secular', and 'Integrity'; held as integral part of Constitution (LIC of India case)."],
        ["Basic Structure Doctrine", "1973 (Kesavananda Bharati Case)", "Supreme Court 13-judge constitutional bench ruled Parliament cannot alter the 'Basic Structure' under Article 368.", "Safeguards judicial review, federalism, secularism, democracy, and fundamental rights against majoritarian amendments."]
      ]
    },
    "bullets": [
      "Preamble as the Key to Constitution: Kesavananda Bharati (1973) overruled the earlier Berubari Union (1960) stance, affirming that the Preamble is an integral part of the Constitution and can be amended under Article 368 without altering the basic features.",
      "Salient Features: Blend of rigidity and flexibility, Parliamentary sovereignty balanced with Judicial supremacy, Single integrated judicial hierarchy, Universal adult suffrage without property qualifications, and Single citizenship.",
      "Constitutional Sources: Parliamentary system and Rule of Law (Britain), Fundamental Rights and Judicial Review (USA), DPSP (Ireland), Concurrent List and Joint Sitting (Australia), Federal system with strong Centre (Canada), Emergency provisions (Weimar Germany).",
      "Basic Structure Components: Supremacy of the Constitution, Republican and Democratic form of government, Secular character, Separation of Powers, Federalism, Judicial Review, and Free and fair elections."
    ],
    "mains": [
      "Critically evaluate the significance of the Preamble to the Constitution of India. Discuss how the Basic Structure Doctrine evolved as a constitutional safeguard against parliamentary overreach under Article 368. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the Preamble as the identity card and moral compass of the Constitution; explain its key ideals: Justice (Social, Economic, Political), Liberty, Equality, and Fraternity; trace the judicial evolution: Berubari (1960) denying Preamble as part of Constitution reversed by Kesavananda Bharati (1973) establishing it as integral; explain the emergence of the Basic Structure Doctrine in Kesavananda Bharati curtailing unlimited amending power under Art 368; discuss subsequent landmark confirmations: Minerva Mills (1980 - harmony between Parts III & IV), Indira Gandhi election case (1975), and S.R. Bommai (1994 - secularism and federalism as basic structure)."
    ],
    "mcqs": [
      "Q1. Which landmark 13-judge constitutional bench ruling of the Supreme Court of India in 1973 enunciated the 'Basic Structure Doctrine'?\n(a) Golaknath Case (1967)\n(b) Kesavananda Bharati Case (1973)\n(c) Minerva Mills Case (1980)\n(d) Maneka Gandhi Case (1978)\nCorrect Answer: (b) Kesavananda Bharati Case (1973) [Explanation: In Kesavananda Bharati v. State of Kerala (1973), a historic 13-judge bench held that Parliament's amending power under Article 368 does not extend to altering the Basic Structure of the Constitution.]",
      "Q2. The words 'Socialist', 'Secular', and 'Integrity' were inserted into the Preamble of the Constitution of India by which Constitutional Amendment Act?\n(a) 24th Amendment Act 1971\n(b) 42nd Amendment Act 1976\n(c) 44th Amendment Act 1978\n(d) 52nd Amendment Act 1985\nCorrect Answer: (b) 42nd Amendment Act 1976 [Explanation: The 42nd Constitutional Amendment Act of 1976 amended the Preamble for the only time in history, adding the words 'Socialist', 'Secular', and 'Integrity'.]",
      "Q3. The concept of 'Directive Principles of State Policy' (DPSP) embodied in Part IV of the Indian Constitution was borrowed from the constitution of which nation?\n(a) United States of America\n(b) Ireland (Irish Republic)\n(c) Australia\n(d) Canada\nCorrect Answer: (b) Ireland (Irish Republic) [Explanation: The framers of the Indian Constitution borrowed the Directive Principles of State Policy from the 1937 Constitution of Ireland, which had taken them from the Spanish Constitution.]",
      "Q4. In which case did the Supreme Court explicitly affirm that 'the Indian Constitution is founded on the bedrock of the balance between Fundamental Rights and Directive Principles'?\n(a) Shankari Prasad Case\n(b) Minerva Mills Case (1980)\n(c) Waman Rao Case\n(d) AK Gopalan Case\nCorrect Answer: (b) Minerva Mills Case (1980) [Explanation: In Minerva Mills Ltd. v. Union of India (1980), the Supreme Court ruled that the balance between Part III (Fundamental Rights) and Part IV (DPSP) is an essential basic feature.]",
      "Q5. Who described the Preamble of the Constitution of India as the 'Political Horoscope' of our sovereign democratic republic?\n(a) Dr. B.R. Ambedkar\n(b) K.M. Munshi\n(c) Pandit Thakur Das Bhargava\n(d) Sir Alladi Krishnaswamy Iyer\nCorrect Answer: (b) K.M. Munshi [Explanation: Dr. K.M. Munshi, a member of the Drafting Committee, famously characterized the Preamble as the 'Horoscope of our sovereign democratic republic'.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-02",
    "filename": "02_fundamental_rights_dpsp_and_fundamental_duties",
    "title": "Fundamental Rights, Directive Principles (DPSP) & Fundamental Duties",
    "mapping": "Polity, Constitution & Governance: Constitutional Rights & Directives - Part III Fundamental Rights (Articles 12 to 35, Article 21 Due Process, Article 32 Writs), Part IV Directive Principles of State Policy, Part IV-A Fundamental Duties.",
    "intro": "Parts III, IV, and IV-A of the Constitution constitute the moral and social conscience of the Indian democratic republic. Part III guarantees justiciable Fundamental Rights against state encroachment, revitalized by judicial expansion of Article 21 (Right to Life and Personal Liberty); Part IV articulates non-justiciable Directive Principles of State Policy guiding socio-economic welfare; and Part IV-A imposes civic Fundamental Duties upon citizens.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Supreme_Court_of_India.jpg", "caption": "The Supreme Court of India, the guarantor and defender of Fundamental Rights under Article 32.", "alt": "Supreme Court of India building facade"},
    "table": {
      "caption": "Constitutional Matrix: Fundamental Rights vs Directive Principles",
      "headers": ["Feature / Attribute", "Fundamental Rights (Part III, Arts 12–35)", "Directive Principles of State Policy (Part IV, Arts 36–51)"],
      "rows": [
        ["Nature & Enforcement", "Negative injunctions limiting state power; strictly justiciable under Articles 32 and 226.", "Positive commands urging state affirmative action; non-justiciable in courts (Article 37) but fundamental in governance."],
        ["Ideological Aim", "Establishes Political Democracy; protects individual civil liberties against executive tyranny.", "Establishes Social and Economic Democracy; establishes a Welfare State (Welfare State vs Police State)."],
        ["Scope of Suspension", "Can be suspended during National Emergency (Art 352) except Articles 20 and 21 (44th Amendment 1978).", "Cannot be suspended; operate continuously as legislative and administrative benchmarks."],
        ["Classification", "Six Categories: Equality (14–18), Freedom (19–22), Against Exploitation (23–24), Freedom of Religion (25–28), Cultural & Educational (29–30), Constitutional Remedies (32).", "Three Traditions: Socialistic (Arts 38, 39, 41, 42, 43), Gandhian (Arts 40, 43, 46, 47, 48), Liberal-Intellectual (Arts 44, 45, 48, 50, 51 - Uniform Civil Code, Separation of Judiciary)."]
      ]
    },
    "bullets": [
      "Article 21 & the Golden Triangle: Maneka Gandhi Case (1978) discarded the narrow 'Procedure Established by Law' (A.K. Gopalan 1950) in favor of American 'Due Process of Law'; established that law depriving liberty must be 'just, fair, and reasonable' under Articles 14, 19, and 21; expanded to include Right to Privacy (Puttaswamy 2017), Clean Environment, and Dignified Life.",
      "Primacy of Article 32: Dr. Ambedkar declared Article 32 as the 'Heart and Soul of the Constitution'; empowers the Supreme Court to issue five prerogative writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, and Quo-Warranto.",
      "Fundamental Duties (Part IV-A, Article 51A): Added by the 42nd Amendment 1976 on the recommendations of the Swaran Singh Committee (10 duties); 11th duty added by 86th Amendment 2002 (duty of parents to provide education to children aged 6–14); moral obligations non-enforceable directly by writs but judicially recognized as interpretative guides.",
      "Uniform Civil Code (Article 44): Directs the state to secure for citizens a uniform civil code throughout India; personal laws currently governed by diverse religious statutes."
    ],
    "mains": [
      "Examine how the judicial interpretation of Article 21 has evolved from 'Procedure Established by Law' in the A.K. Gopalan case to 'Due Process of Law' in the Maneka Gandhi case. Discuss its impact on expanding civil liberties. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast the literal, narrow interpretation in A.K. Gopalan (1950) where 'procedure established by law' was held to require only valid formal legislative enactment without examining substantive fairness; analyze the watershed Maneka Gandhi v. Union of India (1978) verdict: inter-linking Articles 14, 19, and 21 (Golden Triangle), establishing that procedure must be 'just, fair, and reasonable', effectively reading substantive Due Process into Article 21; detail the ensuing judicial revolution: expansion into Right to Privacy (K.S. Puttaswamy 2017), Right to Clean Environment, Right to Health, Right to Legal Aid, and Right to Die with Dignity (passive euthanasia); conclude on the transformation of the Supreme Court into the sentinel of human dignity."
    ],
    "mcqs": [
      "Q1. Which Article of the Indian Constitution was hailed by Dr. B.R. Ambedkar as the 'very soul of the Constitution and the very heart of it'?\n(a) Article 14\n(b) Article 19\n(c) Article 21\n(d) Article 32\nCorrect Answer: (d) Article 32 [Explanation: Dr. Ambedkar called Article 32 (Right to Constitutional Remedies) the heart and soul of the Constitution because it guarantees judicial enforcement of all other rights via writs.]",
      "Q2. In which landmark 2017 ruling did a nine-judge constitutional bench of the Supreme Court unanimously declare the Right to Privacy as a Fundamental Right under Article 21?\n(a) Shayara Bano Case\n(b) K.S. Puttaswamy v. Union of India\n(c) Navtej Singh Johar Case\n(d) Joseph Shine Case\nCorrect Answer: (b) K.S. Puttaswamy v. Union of India [Explanation: In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), the Supreme Court ruled that privacy is an intrinsic part of the Right to Life and Personal Liberty under Article 21.]",
      "Q3. The 11th Fundamental Duty (mandating parents to provide educational opportunities to children aged 6 to 14) was added to Article 51A by which Amendment?\n(a) 42nd Amendment Act 1976\n(b) 44th Amendment Act 1978\n(c) 86th Amendment Act 2002\n(d) 91st Amendment Act 2003\nCorrect Answer: (c) 86th Amendment Act 2002 [Explanation: The 86th Constitutional Amendment Act of 2002 introduced Article 21A (Right to Education) and added clause (k) to Article 51A as the 11th Fundamental Duty.]",
      "Q4. Which prerogative writ is issued by the higher judiciary to quash an order passed by an inferior court or tribunal that acted without or in excess of jurisdiction?\n(a) Habeas Corpus\n(b) Mandamus\n(c) Certiorari\n(d) Quo-Warranto\nCorrect Answer: (c) Certiorari [Explanation: The writ of Certiorari is a curative writ issued to quash an order of an inferior court or quasi-judicial body that exceeded its jurisdiction or violated principles of natural justice.]",
      "Q5. Which Directive Principle of State Policy in Part IV directs the state to secure for the citizens a Uniform Civil Code (UCC) throughout the territory of India?\n(a) Article 40\n(b) Article 44\n(c) Article 48\n(d) Article 50\nCorrect Answer: (b) Article 44 [Explanation: Article 44 of the Directive Principles of State Policy provides that 'the State shall endeavour to secure for the citizens a uniform civil code throughout the territory of India'.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-03",
    "filename": "03_union_executive_president_prime_minister_com",
    "title": "Union Executive: President, Prime Minister & Council of Ministers",
    "mapping": "Polity, Constitution & Governance: Union Executive - President (Election, Powers, Ordinance Art 123, Pardoning Art 72), Vice-President, Prime Minister, Council of Ministers (Collective Responsibility Art 75), Attorney General of India (Art 76).",
    "intro": "The Union Executive of India embodies the Westminster model of parliamentary democracy, establishing a constitutional dichotomy between the De Jure titular head of state (the President of India) and the De Facto real executive (the Prime Minister in Council of Ministers). Anchored in the principle of collective ministerial responsibility to the Lok Sabha, the executive exercises supreme governing authority over the Union.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Rashtrapati_Bhavan_New_Delhi.jpg", "caption": "Rashtrapati Bhavan, the official residence of the President of India in New Delhi.", "alt": "Rashtrapati Bhavan front facade"},
    "table": {
      "caption": "Constitutional Roles & Executive Powers in the Union Executive",
      "headers": ["Executive Functionary", "Constitutional Articles", "Method of Election / Appointment", "Core Executive & Discretionary Powers"],
      "rows": [
        ["President of India (Head of State)", "Articles 52 to 62, 72, 123, 352–360.", "Elected by Electoral College (Elected MPs of both Houses + Elected MLAs of all States/UTs) by single transferable vote.", "Supreme Commander of Armed Forces; summons/prorogues Parliament; Promulgates Ordinances (Art 123); Pardoning power (Art 72); Emergency powers; acts on aid and advice of CoM (Art 74)."],
        ["Vice-President of India", "Articles 63 to 71.", "Elected by Electoral College consisting of ALL MPs of both Houses of Parliament (elected and nominated).", "Ex-officio Chairman of Rajya Sabha (Art 64); acts as President during vacancy (up to 6 months)."],
        ["Prime Minister & Council of Ministers", "Articles 74, 75, 78.", "PM appointed by President; Ministers appointed on PM's recommendation; must be MP within 6 months.", "Real executive head; aids and advises President; allocates portfolios; determines policy; collectively responsible to Lok Sabha (Art 75(3)); individual responsibility to President."],
        ["Attorney General for India", "Article 76.", "Appointed by President; qualified to be appointed Supreme Court judge; holds office during President's pleasure.", "Chief legal advisor to Government of India; right of audience in all Indian courts; right to speak and take part in parliamentary proceedings without voting right."]
      ]
    },
    "bullets": [
      "Article 74(1) & 42nd/44th Amendments: 42nd Amendment (1976) made President bound by advice of Council of Ministers; 44th Amendment (1978) introduced proviso allowing President to return advice once for reconsideration, but bound if returned unchanged.",
      "Ordinance-Making Power (Article 123): Exercised only when Parliament is not in session and circumstances require immediate action; has same force as Act of Parliament; must be approved by Parliament within 6 weeks of reassembly; subject to judicial review (DC Wadhwa 1987).",
      "Pardoning Power of President (Article 72): Power to grant pardons, reprieves, respites, and remissions of punishment; extends to court-martial sentences and death penalties; exercised on advice of Union Home Ministry; subject to limited judicial review against arbitrariness (Kehar Singh 1989, Shatrughan Chauhan 2014).",
      "Prime Ministerial Discretionary Powers: Appointment of PM when no single party holds clear majority (Hung Parliament); dismissal of Council of Ministers that lost majority in Lok Sabha and refuses to resign."
    ],
    "mains": [
      "The President of India is a constitutional figurehead who reigns but does not rule. Critically evaluate the constitutional position of the President and discuss situations where the President exercises personal discretion. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the constitutional architecture: Article 53 vesting executive power in President, tempered by Article 74(1) mandating action on the 'aid and advice' of the Council of Ministers, reinforced by 42nd and 44th Amendments; demonstrate how this creates a titular head in a Westminster democracy; analyze real situational discretions: appointment of Prime Minister in a hung Parliament (choosing leader of single largest party or pre-poll alliance), dismissal of a ministry that has lost the confidence of the Lok Sabha, dissolution of Lok Sabha when no alternative government is viable, and pocket veto under Article 111 (Zail Singh's Indian Post Office Bill 1986); conclude that the President functions as a constitutional safety valve and moral guardian."
    ],
    "mcqs": [
      "Q1. Who constitutes the Electoral College for the election of the President of India under Article 54 of the Constitution?\n(a) All members of both Houses of Parliament\n(b) Elected members of both Houses of Parliament and elected members of State Legislative Assemblies (including Delhi and Puducherry)\n(c) Elected and nominated members of Parliament and State Assemblies\n(d) Only members of Lok Sabha and Rajya Sabha\nCorrect Answer: (b) Elected members of both Houses of Parliament and elected members of State Legislative Assemblies (including Delhi and Puducherry) [Explanation: Article 54 specifies that the presidential electoral college consists solely of elected MPs of Parliament and elected MLAs of state and UT legislative assemblies.]",
      "Q2. Under Article 123 of the Constitution, an Ordinance promulgated by the President during parliamentary recess ceases to operate within how many weeks of Parliament reassembling?\n(a) 2 weeks\n(b) 4 weeks\n(c) 6 weeks\n(d) 6 months\nCorrect Answer: (c) 6 weeks [Explanation: An Ordinance must be laid before both Houses of Parliament and expires six weeks from the date of reassembly unless approved earlier by both Houses.]",
      "Q3. Which Article of the Indian Constitution explicitly provides that the Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha)?\n(a) Article 74(1)\n(b) Article 75(3)\n(c) Article 77\n(d) Article 78\nCorrect Answer: (b) Article 75(3) [Explanation: Article 75(3) states that 'the Council of Ministers shall be collectively responsible to the House of the People', anchoring the core principle of parliamentary accountability.]",
      "Q4. The President's pardoning power under Article 72 differs fundamentally from the Governor's pardoning power under Article 161 in which key respect?\n(a) The President cannot pardon contempt of court\n(b) Only the President can pardon death sentences and sentences by Court Martial\n(c) The Governor can pardon military offenses\n(d) The Governor has wider pardon powers than the President\nCorrect Answer: (b) Only the President can pardon death sentences and sentences by Court Martial [Explanation: The President has exclusive authority to pardon sentences inflicted by a Court Martial and death sentences; Governors cannot pardon death sentences (they can only suspend/remit).]",
      "Q5. Which high constitutional officer has the unique right to speak and take part in the proceedings of either House of Parliament without the right to vote?\n(a) Comptroller and Auditor General\n(b) Attorney General for India\n(c) Chief Election Commissioner\n(d) Solicitor General\nCorrect Answer: (b) Attorney General for India [Explanation: Under Article 88, the Attorney General for India has the right to speak and participate in parliamentary proceedings and committees without voting rights.]"
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

print("Part 1 of Subject 4 generated successfully")
