import os, json, glob

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "04_Polity_Constitution_Governance"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-POL-10",
    "filename": "10_statutory_and_regulatory_bodies_niti_aayog_nhrc_lokpal",
    "title": "Statutory & Regulatory Bodies: NITI Aayog, NHRC, Lokpal & CVC",
    "mapping": "Polity, Constitution & Governance: Quasi-Judicial, Statutory & Regulatory Bodies - NITI Aayog (Structure, Cooperative Federalism), National Human Rights Commission (NHRC), Lokpal and Lokayuktas Act 2013, Central Vigilance Commission (CVC), Central Information Commission (CIC).",
    "intro": "Modern democratic governance relies on independent statutory, regulatory, and ombudsman institutions to protect human rights, curb public corruption, ensure competitive market fairness, and guide national strategic development. These bodies—including NITI Aayog, the National Human Rights Commission (NHRC), the Lokpal, the Central Vigilance Commission (CVC), and the Central Information Commission (CIC)—operate outside direct ministerial hierarchy to enforce institutional checks and balances.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/NITI_Aayog_New_Delhi.jpg", "caption": "NITI Aayog headquarters in New Delhi, the policy think-tank fostering cooperative federalism.", "alt": "NITI Aayog building New Delhi"},
    "table": {
      "caption": "Charter of Premier Statutory, Regulatory & Ombudsman Institutions",
      "headers": ["Institution", "Statutory Act / Resolution", "Composition & Selection Committee", "Mandate & Operational Powers"],
      "rows": [
        ["NITI Aayog (National Institution for Transforming India)", "Cabinet Resolution (1 January 2015, replacing Planning Commission).", "Chairperson (PM), Vice-Chairperson, CEO, Ex-officio members, Governing Council (all CMs and Lt Governors).", "Think-tank fostering 'Cooperative and Competitive Federalism'; bottom-up approach; Sustainable Development Goals (SDG) India Index; Aspirational Districts Programme."],
        ["National Human Rights Commission (NHRC)", "Protection of Human Rights Act 1993 (amended 2019).", "Chairperson (retired CJI or SC judge) + 5 members; appointed by committee (PM, Home Minister, Speaker, Deputy Chairman RS, Leaders of Opposition in LS & RS).", "Inquires into human rights violations; visits jails; civil court powers; can recommend compensation and prosecution; non-binding advisory powers."],
        ["Lokpal of India (Anticorruption Ombudsman)", "Lokpal and Lokayuktas Act 2013.", "Chairperson + max 8 members (50% judicial, 50% SC/ST/OBC/Women/Minority); selection committee (PM, Speaker, LoP, CJI, eminent jurist).", "Inquires into corruption allegations against public functionaries including Prime Minister (with safeguards), Union Ministers, MPs, and Group A, B, C, D officers; has inquiry and prosecution wings."],
        ["Central Vigilance Commission (CVC)", "CVC Act 2003 (originally K. Santhanam Committee 1964).", "Central Vigilance Commissioner + max 2 Vigilance Commissioners; appointed by committee (PM, Home Minister, LoP in LS).", "Apex integrity watchdog; superintends CBI investigations under Prevention of Corruption Act; advises central ministries on vigilance matters."]
      ]
    },
    "bullets": [
      "NITI Aayog vs Planning Commission: Replaced top-down uniform planning with bottom-up tailored strategy; eliminated discretionary plan funds allocation (devolved to Finance Commission); emphasizes evidence-based ranking of states (SDG Index, Export Preparedness Index, Health Index).",
      "Central Information Commission (CIC): Established under the Right to Information Act 2005; hears second appeals against denial of public information; enforces proactive transparency.",
      "Regulatory Authorities: Competition Commission of India (CCI, Competition Act 2002 - prevents anti-competitive cartels and abuses of dominance); Telecom Regulatory Authority of India (TRAI Act 1997); Securities and Exchange Board of India (SEBI Act 1992 - capital market regulator); Insurance Regulatory and Development Authority of India (IRDAI Act 1999, headquartered in Hyderabad).",
      "Lokayukta in Andhra Pradesh: Statutory anti-corruption ombudsman established under the AP Lokayukta and Upa-Lokayukta Act 1983; investigates maladministration and corruption by public servants and ministers in AP."
    ],
    "mains": [
      "Critically evaluate the performance of NITI Aayog in promoting cooperative and competitive federalism in India since replacing the Planning Commission in 2015. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the institutional shift: replacing the centralized, top-down allocation model of the Planning Commission with NITI Aayog as a national knowledge and strategy think-tank; analyze mechanisms promoting Cooperative Federalism: the Governing Council bringing all Chief Ministers as equal partners in formulating national agendas; examine Competitive Federalism: indices ranking states on performance (SDG India Index, Multidimensional Poverty Index, Aspirational Districts Programme) stimulating peer competition; discuss structural limitations: lack of financial resource-allocation powers (leaving states reliant on Finance Commission and Union ministries), advisory recommendations without binding enforceability, and concerns from regional states on centralized conditionalities."
    ],
    "mcqs": [
      "Q1. Which body was replaced on 1 January 2015 by the Government of India through a Cabinet Resolution to establish NITI Aayog?\n(a) National Development Council\n(b) Planning Commission of India\n(c) Finance Commission\n(d) National Advisory Council\nCorrect Answer: (b) Planning Commission of India [Explanation: NITI Aayog was established on 1 January 2015 via an executive resolution, superseding the 65-year-old Planning Commission.]",
      "Q2. The Selection Committee that recommends the appointment of the Chairperson and Members of the National Human Rights Commission (NHRC) is headed by:\n(a) Chief Justice of India\n(b) President of India\n(c) Prime Minister of India\n(d) Union Home Minister\nCorrect Answer: (c) Prime Minister of India [Explanation: Under the Protection of Human Rights Act 1993, the selection committee is chaired by the Prime Minister and includes the Speaker, Home Minister, and Leaders of the Opposition.]",
      "Q3. Which landmark committee on the Prevention of Corruption appointed in 1962 recommended the establishment of the Central Vigilance Commission (CVC)?\n(a) K. Santhanam Committee\n(b) Sarkaria Commission\n(c) Gorwala Committee\n(d) Paul Appleby Committee\nCorrect Answer: (a) K. Santhanam Committee [Explanation: The Santhanam Committee on Prevention of Corruption (1962–1964) recommended creating the CVC to tackle corruption in central government administration.]",
      "Q4. Under the Lokpal and Lokayuktas Act 2013, what minimum proportion of the members of the Lokpal must be drawn from SCs, STs, OBCs, Minorities, and Women?\n(a) 25%\n(b) 33.33%\n(c) 50%\n(d) 60%\nCorrect Answer: (c) 50% [Explanation: Section 3(3) of the Lokpal Act mandates that not less than 50% of the members of the Lokpal shall be from SCs, STs, OBCs, Minorities, and Women.]",
      "Q5. The Insurance Regulatory and Development Authority of India (IRDAI), which oversees and regulates the insurance sector in India, is headquartered in which city?\n(a) Mumbai\n(b) New Delhi\n(c) Hyderabad\n(d) Bengaluru\nCorrect Answer: (c) Hyderabad [Explanation: IRDAI is a statutory regulatory body established in 1999 and headquartered in Hyderabad, Telangana (formerly undivided Andhra Pradesh).]"
    ]
  },
  {
    "id": "APPSC-G1-POL-11",
    "filename": "11_good_governance_citizens_charter_and_rti_act",
    "title": "Good Governance: Citizen's Charter, Sevottam Model & RTI Act 2005",
    "mapping": "Polity, Constitution & Governance: Administrative Transparency & Accountability - Good Governance (8 Characteristics), Citizen's Charters, Sevottam Model, Right to Information Act 2005 (Structure, Section 4 Proactive Disclosure, Section 8 Exemptions), Social Audit.",
    "intro": "Good Governance represents the paradigm shift from bureaucratic authority to citizen-centric public service delivery. Grounded in the United Nations' eight core attributes—participation, rule of law, transparency, responsiveness, consensus orientation, equity, efficiency, and accountability—it is operationalized in India through statutory instruments like the Right to Information Act 2005, the Sevottam Citizen's Charter framework, and grassroots Social Audits.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/RTI_Act_India.jpg", "caption": "The Right to Information Act 2005 symbol, representing democratic transparency and public accountability.", "alt": "RTI Act official logo"},
    "table": {
      "caption": "Instruments of Administrative Transparency & Citizen Centricity",
      "headers": ["Governance Instrument", "Legal Basis & Origin", "Core Operational Mechanisms", "Impact on Public Administration"],
      "rows": [
        ["Right to Information Act (RTI 2005)", "Enacted 15 June 2005; came into force 12 October 2005.", "Public Information Officers (PIOs) must provide information within 30 days (48 hours for life/liberty); Section 4(1)(b) proactive disclosure; Section 8 limited exemptions; Central & State Information Commissions.", "Empowered ordinary citizens to question executive corruption, audit muster rolls (MGNREGA), and enforce administrative accountability."],
        ["Citizen's Charter", "Originated in UK (1991, John Major); adopted in India (1997).", "Written declaration specifying standards, quality, time-frames of service delivery, grievance redress mechanisms, and citizen obligations.", "Transforms citizens from passive recipients to active consumers; non-justiciable per se unless backed by statutory service delivery acts."],
        ["Sevottam Model", "Developed by DARPG (Department of Administrative Reforms and Public Grievances).", "Three-pillar assessment framework: 1. Citizen's Charter implementation, 2. Public Grievance Redressal mechanism, 3. Service Delivery Capability.", "Benchmark quality management tool for certifying government departments (IS 15700:2005)."],
        ["Social Audit", "MGNREGA Act 2005 Section 17; pioneered by MKSS in Rajasthan.", "Independent audit of government welfare expenditure conducted jointly by beneficiaries and Gram Sabha using primary vouchers and muster rolls.", "Exposes ghost beneficiaries, prevents wage theft, and ensures grassroots participatory monitoring; AP Social Audit Society is national benchmark."]
      ]
    },
    "bullets": [
      "Section 4(1)(b) of RTI Act: Mandates all public authorities to proactively publish 17 categories of operational information (budgets, norms, directory of officers, subsidies) on websites to minimize public RTI applications.",
      "Section 8 Exemptions: Protects information affecting national sovereignty/security, contempt of court, commercial confidence/trade secrets, fiduciary relationships, and unwarranted invasion of individual privacy.",
      "Andhra Pradesh Right to Public Services Legislation: AP Guaranteed Delivery of Services Act ensures time-bound delivery of essential citizen certificates (caste, income, birth, land records) through village/ward secretariats with penalties on defaulting officers.",
      "Second ARC (Fourth Report - 'Ethics in Governance'): Recommended amending Official Secrets Act 1923, protecting whistleblowers, operationalizing Ombudsman in local bodies, and establishing clear Citizen's Charters with service compensation."
    ],
    "mains": [
      "Critically evaluate the performance of the Right to Information (RTI) Act 2005 as a tool for deepening participatory democracy and combating administrative corruption in India. Discuss current operational challenges. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define RTI as a sunshine law giving teeth to freedom of speech and expression (Article 19(1)(a)); analyze its transformative impact: exposing high-level corruption (Adarsh, Commonwealth Games), empowering marginalized beneficiaries to track ration cards and MGNREGA wages, and dismantling bureaucratic secrecy; evaluate operational and structural challenges: high pendency of appeals in Central and State Information Commissions, vacancies of Information Commissioners, attacks and killings of RTI whistleblowers, misuse of Section 8 privacy exemptions; assess the impact of the RTI Amendment Act 2019 centralizing terms and salaries of commissioners; suggest proactive digitization and whistleblower protections."
    ],
    "mcqs": [
      "Q1. Under Section 7(1) of the Right to Information Act 2005, what is the mandatory time limit for providing information if it concerns the life or liberty of a person?\n(a) 24 hours\n(b) 48 hours\n(c) 7 days\n(d) 30 days\nCorrect Answer: (b) 48 hours [Explanation: Section 7(1) of the RTI Act 2005 provides that where the information sought concerns the life or liberty of a person, it shall be provided within forty-eight hours of receipt.]",
      "Q2. The 'Sevottam Model', developed by the Department of Administrative Reforms and Public Grievances (DARPG), is an assessment framework for:\n(a) E-governance software architecture\n(b) Excellence in Public Service Delivery and Citizen's Charters\n(c) Environmental impact assessment\n(d) Direct benefit transfers\nCorrect Answer: (b) Excellence in Public Service Delivery and Citizen's Charters [Explanation: Sevottam (Service Excellence) is an assessment-improvement framework for public service delivery based on Citizen's Charters, grievance redress, and service capability.]",
      "Q3. Section 4(1)(b) of the Right to Information Act 2005 mandates which vital transparency obligation on all public authorities?\n(a) Annual confidential reports of civil servants\n(b) Proactive suo-motu disclosure of 17 categories of public information\n(c) Compulsory audio-recording of cabinet meetings\n(d) Disclosure of intelligence agency budgets\nCorrect Answer: (b) Proactive suo-motu disclosure of 17 categories of public information [Explanation: Section 4(1)(b) mandates every public authority to proactively publish details of its organization, functions, norms, budgets, and employee directories.]",
      "Q4. Which section of the Right to Information Act 2005 specifies exemptions from disclosure of information, including matters affecting national security and commercial confidence?\n(a) Section 4\n(b) Section 8\n(c) Section 12\n(d) Section 20\nCorrect Answer: (b) Section 8 [Explanation: Section 8 enumerates ten categories of information that are exempt from disclosure, including sovereignty of India, cabinet papers, and trade secrets.]",
      "Q5. Which civil society grassroots organization, founded by Aruna Roy in Rajasthan, pioneered the 'Jan Sunwai' (Public Hearing) and Social Audit movement leading to the RTI Act?\n(a) Mazdoor Kisan Shakti Sangathan (MKSS)\n(b) Chipko Movement\n(c) Narmada Bachao Andolan\n(d) Pratham Foundation\nCorrect Answer: (a) Mazdoor Kisan Shakti Sangathan (MKSS) [Explanation: The Mazdoor Kisan Shakti Sangathan (MKSS) spearheaded the right to information struggle in rural Rajasthan, demanding access to muster rolls and bills in village Jan Sunwais.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-12",
    "filename": "12_e_governance_initiatives_and_administrative_reforms",
    "title": "E-Governance Initiatives & Civil Service Reforms: 2nd ARC & Digital India",
    "mapping": "Polity, Constitution & Governance: Administrative Modernization - E-Governance (NeGP, Digital India, DBT, JAM Trinity), Public Grievance Redressal (CPGRAMS, Spandana in AP), Second Administrative Reforms Commission (2nd ARC) Recommendations, Civil Service Neutrality and Reforms.",
    "intro": "Administrative modernization in India is driven by the transformative convergence of Digital Governance and structural civil service reforms. Moving from traditional paper-driven bureaucracy to algorithm-enabled digital delivery platforms (Digital India, JAM Trinity, e-Office), the state enhances speed, eliminates leakage, and improves citizen access, guided by the foundational recommendations of the Second Administrative Reforms Commission (2nd ARC).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Digital_India_logo.png", "caption": "The Digital India mission logo, embodying paperless, faceless, and cashless governance.", "alt": "Digital India program logo"},
    "table": {
      "caption": "Digital Governance Architectures & Citizen Service Platforms",
      "headers": ["Digital Platform / Scheme", "Nodal Agency & Technology Core", "Operational Mechanism", "Governance Impact & Inclusion"],
      "rows": [
        ["Digital India Mission (2015)", "Ministry of Electronics & IT (MeitY).", "Nine pillars: broadband highways, universal mobile access, public internet, e-governance, e-kranti, information for all, electronics manufacturing, IT for jobs, early harvest.", "Created digital public infrastructure (DPI / India Stack: Aadhaar, UPI, DigiLocker, CoWIN)."],
        ["JAM Trinity & Direct Benefit Transfer (DBT)", "Ministry of Finance & NPCI.", "Jan Dhan accounts + Aadhaar biometric identification + Mobile connectivity; operates across 300+ welfare schemes.", "Eliminated middlemen and ghost beneficiaries; saved over Rs 2.7 lakh crore in cumulative public welfare leakages."],
        ["CPGRAMS & State Grievance Portals", "DARPG (Central Portal) & State Portals (Spandana in AP).", "Centralised Public Grievance Redress and Monitoring System; web-based single-window tracking with AI classification and appeal mechanism.", "Monitors redressal timelines; citizens receive SMS tracking; accountability fixed on designated officers."],
        ["Grama / Ward Sachivalayam (AP Model)", "Government of Andhra Pradesh.", "Over 15,000 decentralized village/ward secretariats staffed by 134,000 functional employees supported by 260,000 ward volunteers.", "Faceless, door-step delivery of 540+ citizen welfare services within fixed Citizen Charter timelines."]
      ]
    },
    "bullets": [
      "Second Administrative Reforms Commission (2nd ARC, 2005–2009): Chaired by Veerappa Moily; submitted 15 comprehensive reports covering 'Ethics in Governance', 'Unlocking Human Capital', 'Citizen Centric Administration', 'Local Governance', and 'Promoting e-Governance'.",
      "Key 2nd ARC Civil Service Recommendations: Introduce performance-related incentives, periodic mid-career reviews at 15 and 20 years with premature retirement for deadwood, lateral entry of domain specialists at Joint Secretary level, statutory Civil Services Code with code of ethics, and independent Civil Services Board.",
      "Mission Karmayogi (National Programme for Civil Services Capacity Building - NPCSCB): Digital competency-based training platform (iGOT Karmayogi) shifting civil servants from 'Rule-based' to 'Role-based' performance.",
      "National Data Sharing and Accessibility Policy (NDSAP) & DigiLocker: Promotes open government data (data.gov.in) and cloud-based verification of official documents without physical notarization."
    ],
    "mains": [
      "Examine the key recommendations of the Second Administrative Reforms Commission (2nd ARC) on civil service reforms in India. How has the Digital Public Infrastructure (DPI / India Stack) revolutionized welfare delivery and public accountability? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Analyze 2nd ARC core recommendations (Report 10 - 'Refurbishing Personnel Administration'): performance management systems, tenure security through statutory Civil Services Boards, lateral entry to infuse domain expertise, and rigorous integrity audits weeding out corrupt officers; explain the digital leap: India Stack architecture (Aadhaar identity layer, UPI payment layer, DigiLocker paperless layer); evaluate DBT impact: direct cash transfers under PM-KISAN and MGNREGA removing corrupt intermediaries and leakage; cite AP Grama Sachivalayam and Spandana as innovative decentralization models; address digital divides and privacy concerns."
    ],
    "mcqs": [
      "Q1. Who served as the Chairman of the Second Administrative Reforms Commission (2nd ARC) constituted by the Government of India in 2005?\n(a) K. Kasturirangan\n(b) M. Veerappa Moily\n(c) Bimal Jalan\n(d) Montek Singh Ahluwalia\nCorrect Answer: (b) M. Veerappa Moily [Explanation: The Second ARC was appointed in August 2005 under the chairmanship of M. Veerappa Moily (later succeeded by V. Ramachandran) and produced 15 landmark reports.]",
      "Q2. 'Mission Karmayogi', launched by the Union Cabinet in September 2020, is a comprehensive institutional mission designed for:\n(a) Rural electrification infrastructure\n(b) Civil Services Capacity Building and competency training\n(c) Tribal education scholarship disbursement\n(d) Micro-irrigation management in drylands\nCorrect Answer: (b) Civil Services Capacity Building and competency training [Explanation: Mission Karmayogi (NPCSCB) focuses on modernizing civil service competencies through the digital iGOT-Karmayogi platform, fostering role-based governance.]",
      "Q3. The centralized online grievance redressal platform operated by the Government of India to register citizen complaints across central ministries is known as:\n(a) PRAGATI\n(b) CPGRAMS\n(c) e-Taal\n(d) UMANG\nCorrect Answer: (b) CPGRAMS [Explanation: CPGRAMS (Centralised Public Grievance Redress and Monitoring System) is the 24x7 online single-window grievance portal managed by DARPG.]",
      "Q4. Which acronym is universally used to describe the digital financial inclusion architecture combining basic bank accounts, biometric identification, and mobile connectivity in India?\n(a) UPI Trinity\n(b) JAM Trinity (Jan Dhan-Aadhaar-Mobile)\n(c) DBT Matrix\n(d) NeGP Grid\nCorrect Answer: (b) JAM Trinity (Jan Dhan-Aadhaar-Mobile) [Explanation: The JAM Trinity (Pradhan Mantri Jan Dhan Yojana, Aadhaar, and Mobile connectivity) provides the technological bedrock for Direct Benefit Transfers.]",
      "Q5. Which innovative decentralized governance model was introduced in Andhra Pradesh to provide doorstep delivery of over 500 citizen services via 15,000 local secretariats?\n(a) MeeSeva Portal\n(b) Grama / Ward Sachivalayam System\n(c) e-Seva Kendra\n(d) Praja Vedika\nCorrect Answer: (b) Grama / Ward Sachivalayam System [Explanation: The Grama/Ward Sachivalayam system in Andhra Pradesh deployed over 15,000 secretariats staffed by local functionaries and volunteers to provide localized public service delivery.]"
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

# Delete old lumped files
old_prefixes = ['01_constitutional_framework', '02_federal_structure', '03_local_governance', '04_parliament_and', '05_judiciary_and', '06_public_administration', '07_civil_society', '08_good_governance']
for p in old_prefixes:
    for f in glob.glob(os.path.join(SUBJ_DIR, p + '*')):
        os.remove(f)

remaining = [f for f in os.listdir(SUBJ_DIR) if f.endswith('.json')]
print("Subject 4 total segregated JSON files:", len(remaining))
