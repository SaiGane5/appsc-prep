import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "04_Polity_Constitution_Governance"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-POL-07",
    "filename": "07_federal_structure_and_centre_state_relations",
    "title": "Federal Structure of India: Centre-State Relations & Emergency Provisions",
    "mapping": "Polity, Constitution & Governance: Federalism - Legislative, Administrative and Financial Relations (Seventh Schedule Lists), Inter-State Council (Art 263), Water Disputes (Art 262), Emergency Provisions (Arts 352, 356, 360), GST Council.",
    "intro": "The Indian Constitution establishes a 'quasi-federal' union with a strong centralizing unitary tilt ('an indestructible Union of destructible States'). Part XI and Part XII govern the three-fold distribution of legislative, administrative, and financial relations between the Union and the States, fortified by statutory coordination bodies like the Inter-State Council, the GST Council, and the Finance Commission, alongside extraordinary Emergency Provisions under Part XVIII.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/GST_Council_Meeting.jpg", "caption": "The GST Council meeting, embodying cooperative federalism in indirect tax harmonization.", "alt": "GST Council meeting of Finance Ministers"},
    "table": {
      "caption": "Three-Fold Legislative & Financial Distribution under Seventh Schedule",
      "headers": ["Legislative List", "Original / Current Subjects", "Key Subject Domains", "Jurisdictional Rule & Conflicts"],
      "rows": [
        ["List I: Union List", "97 original / 100 current subjects.", "Defense, Foreign Affairs, Atomic Energy, Banking, Railways, Airways, Inter-State Trade.", "Parliament has exclusive lawmaking power; Residuary Powers vest in Parliament under Article 248."],
        ["List II: State List", "66 original / 61 current subjects (5 shifted by 42nd Amendment).", "Public Order, Police, Public Health, Agriculture, Land, Local Government, Tolls.", "State legislatures have exclusive normal jurisdiction, subject to Parliamentary override under Articles 249, 250, 252, and 253."],
        ["List III: Concurrent List", "47 original / 52 current subjects (Education, Forests, Weights/Measures, Birds/Animals, Administration of Justice added by 42nd Amendment).", "Criminal Law, Marriage, Civil Procedure, Trade Unions, Price Control, Electricity.", "Both Parliament and States can legislate; Doctrine of Repugnancy (Article 254): Union law prevails unless State law received Presidential Assent."],
        ["Financial Relations & GST", "Articles 268 to 293; GST Council under Article 279A.", "Direct taxes to Centre (Corporate, Income); State taxes (Stamp, Excise on alcohol, Land revenue); GST on goods and services.", "101st Amendment (2016) created dual GST; GST Council decisions require 75% weighted majority (Centre has 1/3rd, States have 2/3rd votes)."]
      ]
    },
    "bullets": [
      "Emergency Provisions (Part XVIII): National Emergency (Art 352 - war, external aggression, armed rebellion; 44th Amendment required written cabinet advice and special majority); President's Rule (Art 356 - failure of constitutional machinery in state; max 3 years with periodic approvals per Bommai standards); Financial Emergency (Art 360 - threat to financial stability; never invoked).",
      "Inter-State Council (Article 263): Constitutional body established by presidential order in 1990 following Sarkaria Commission recommendations; chaired by Prime Minister, comprises all Chief Ministers and 6 Union Cabinet Ministers.",
      "Inter-State River Water Disputes (Article 262): Parliament enacted Inter-State River Water Disputes Act 1956; empowers Union to set up ad-hoc tribunals; bars Supreme Court from exercising jurisdiction over river water sharing disputes (Krishna and Godavari Water Disputes Tribunals).",
      "Commissions on Federalism: Administrative Reforms Commission (1966), Rajamannar Committee (1969, Tamil Nadu), Sarkaria Commission (1983–1988), and M.M. Punchhi Commission (2007–2010)."
    ],
    "mains": [
      "Examine the evolving dynamics of Centre-State financial relations in India post-101st Constitutional Amendment (GST). Is cooperative federalism giving way to centralized fiscal dominance? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define cooperative federalism as embodied in the GST Council (Article 279A) pooling state and national indirect tax sovereignty; evaluate fiscal benefits: eliminating cascading taxes, unified common market; analyze structural friction points: states surrendering autonomous sales tax flexibility, end of the 5-year GST compensation cess window (June 2022) creating severe state revenue shortfalls, and proliferation of non-shareable cesses and surcharges by the Centre (over 12% of gross tax revenue bypassing Finance Commission devolution); analyze Mohit Minerals judgment (2022) holding that GST Council recommendations are not legally binding; conclude on reviving Inter-State Council and reforming tax devolution."
    ],
    "mcqs": [
      "Q1. Residuary powers of legislation—matters not enumerated in the Union, State, or Concurrent Lists—are vested in which authority under Article 248?\n(a) State Legislatures\n(b) Parliament of India\n(c) President of India\n(d) Supreme Court of India\nCorrect Answer: (b) Parliament of India [Explanation: Unlike the US Constitution where residuary powers vest in states, Article 248 of the Indian Constitution vests residuary legislative powers exclusively in Parliament.]",
      "Q2. Five key subjects—including Education, Forests, and Weights and Measures—were transferred from the State List to the Concurrent List by which Constitutional Amendment?\n(a) 24th Amendment Act 1971\n(b) 42nd Amendment Act 1976\n(c) 44th Amendment Act 1978\n(d) 73rd Amendment Act 1992\nCorrect Answer: (b) 42nd Amendment Act 1976 [Explanation: The 42nd Amendment Act of 1976 transferred Education, Forests, Weights & Measures, Protection of Wild Animals, and Administration of Justice from List II to List III.]",
      "Q3. Under Article 279A, what weighted voting share is held by the Central Government and the State Governments respectively in the GST Council?\n(a) Centre: 50%, States: 50%\n(b) Centre: 1/3rd (33.33%), States: 2/3rd (66.67%)\n(c) Centre: 25%, States: 75%\n(d) Equal vote for each member\nCorrect Answer: (b) Centre: 1/3rd (33.33%), States: 2/3rd (66.67%) [Explanation: Under Article 279A(9), the Central Government has a weight of one-third of total votes cast, while all State Governments combined have a weight of two-thirds, requiring 75% for decision-making.]",
      "Q4. Which permanent constitutional body to promote inter-governmental coordination was established under Article 263 by a Presidential Order in 1990?\n(a) NITI Aayog\n(b) Inter-State Council\n(c) National Development Council\n(d) Zonal Councils\nCorrect Answer: (b) Inter-State Council [Explanation: Following the Sarkaria Commission recommendations, the Inter-State Council was formally constituted under Article 263 in May 1990 to investigate and advise on inter-state policy issues.]",
      "Q5. Which ground for proclaiming a National Emergency under Article 352 was substituted with 'Armed Rebellion' by the 44th Constitutional Amendment Act 1978?\n(a) External aggression\n(b) Internal disturbance\n(c) War\n(d) Insurgency\nCorrect Answer: (b) Internal disturbance [Explanation: The 44th Amendment Act (1978) substituted 'armed rebellion' for the vague phrase 'internal disturbance' to prevent arbitrary invocation of emergency powers.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-08",
    "filename": "08_local_governance_73rd_and_74th_amendments_pesa",
    "title": "Local Self-Government: 73rd & 74th Amendments & PESA Act 1996",
    "mapping": "Polity, Constitution & Governance: Grassroots Decentralization - 73rd and 74th Constitutional Amendment Acts (1992), Three-Tier Panchayati Raj, Municipalities, Eleventh and Twelfth Schedules, State Finance Commission, PESA Act 1996 in Scheduled Areas.",
    "intro": "The 73rd and 74th Constitutional Amendment Acts of 1992 revolutionized Indian federalism by granting constitutional status to rural (Panchayati Raj) and urban (Municipalities) local self-governments, establishing a three-tier federal architecture. Augmented by the Panchayats (Extension to Scheduled Areas) Act (PESA) 1996 for tribal Fifth Schedule tracts, grassroots democracy empowers Gram Sabhas with participatory planning, social audits, and resource sovereignty.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Gram_Sabha_meeting.jpg", "caption": "A democratic Gram Sabha meeting deliberating on rural infrastructure and welfare entitlements.", "alt": "Gram Sabha village gathering"},
    "table": {
      "caption": "Constitutional Comparison: 73rd vs 74th Amendment Acts (1992)",
      "headers": ["Constitutional Dimension", "Panchayati Raj (73rd Amendment, Part IX)", "Urban Municipalities (74th Amendment, Part IX-A)"],
      "rows": [
        ["Constitutional Articles & Schedule", "Articles 243 to 243-O; Eleventh Schedule (29 functional subjects).", "Articles 243-P to 243-ZG; Twelfth Schedule (18 functional subjects)."],
        ["Structural Tiers", "Gram Panchayat (village), Panchayat Samiti (intermediate block), Zilla Parishad (district level).", "Nagar Panchayat (transitional area), Municipal Council (smaller urban area), Municipal Corporation (larger urban area)."],
        ["Direct Democracy Foundation", "Gram Sabha (Art 243A): all registered voters of village; supreme social audit organ.", "Ward Committees (Art 243S) in municipalities with population of 300,000 or more."],
        ["Mandatory Reservations", "Art 243D: SCs and STs in proportion to population; minimum 1/3rd seats for women (50% in AP, Bihar, etc.).", "Art 243T: SCs, STs, and minimum 1/3rd seats reserved for women across wards and mayoral posts."],
        ["Institutional Organs", "State Election Commission (Art 243K) for independent elections; State Finance Commission (Art 243I) for fiscal devolution every 5 years.", "State Election Commission (Art 243ZA) and State Finance Commission (Art 243Y); District Planning Committee (Art 243ZD)."]
      ]
    },
    "bullets": [
      "PESA Act 1996 (Bhuria Committee): Extends Part IX to Fifth Schedule tribal areas in 10 states (including AP); empowers Gram Sabha with absolute ownership of Minor Forest Produce (MFP), mandatory consultation prior to land acquisition or mining leases, control over local money lenders, and power to enforce prohibition.",
      "Evolutionary Committees: Balwant Rai Mehta (1957 - 3-tier Panchayati Raj and 'Democratic Decentralization'), Ashok Mehta (1977 - 2-tier model), G.V.K. Rao (1985 - 'grass without roots' warning), L.M. Singhvi (1986 - recommended constitutional recognition of PRIs).",
      "Andhra Pradesh Grama/Ward Sachivalayam System: Groundbreaking decentralization model establishing over 15,000 village/ward secretariats delivering 500+ government services directly at citizen doorsteps through volunteer networks.",
      "The 3 F's Dilemma: Panchayati Raj institutions across India continue to suffer from inadequate devolution of Funds, Functions, and Functionaries by state governments, undermining true local self-governance."
    ],
    "mains": [
      "Critically evaluate the performance of Panchayati Raj Institutions (PRIs) three decades after the 73rd Constitutional Amendment Act. Examine how the PESA Act of 1996 empowers tribal Gram Sabhas in the Fifth Schedule areas of Andhra Pradesh. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Evaluate 30 years of the 73rd Amendment: historic deepening of democracy, political empowerment of women (over 1.4 million elected women representatives), and institutionalized Gram Sabhas; examine structural bottlenecks: chronic shortfall of fiscal devolution (Funds), reluctance of line departments to surrender subjects (Functions), and lack of bureaucratic capacity (Functionaries); analyze PESA 1996 in AP tribal agency tracts: statutory recognition of customary laws, ownership of minor forest produce, mandatory Gram Sabha consent for bauxite/sand mining; discuss implementation gaps: bureaucratic bypassing of Gram Sabhas, diluted consultation, and conflicts over forest rights (FRA 2006)."
    ],
    "mcqs": [
      "Q1. Which landmark committee appointed in 1957 recommended the establishment of a three-tier system of Panchayati Raj based on 'Democratic Decentralization'?\n(a) Ashok Mehta Committee\n(b) Balwant Rai Mehta Committee\n(c) L.M. Singhvi Committee\n(d) G.V.K. Rao Committee\nCorrect Answer: (b) Balwant Rai Mehta Committee [Explanation: The Balwant Rai Mehta Committee (1957) submitted the foundational report recommending a 3-tier Panchayati Raj system (Gram, Block, and District) to implement the Community Development Programme.]",
      "Q2. The Eleventh Schedule of the Constitution, added by the 73rd Constitutional Amendment Act 1992, contains how many functional matters entrusted to Panchayats?\n(a) 18 functional items\n(b) 21 functional items\n(c) 29 functional items\n(d) 35 functional items\nCorrect Answer: (c) 29 functional items [Explanation: The Eleventh Schedule (Article 243G) specifies 29 functional items (including agriculture, water management, minor forest produce, rural housing) devolved to Panchayats.]",
      "Q3. The Panchayats (Extension to Scheduled Areas) Act (PESA), enacted in 1996 to extend grassroots self-governance to Fifth Schedule tribal tracts, was based on the recommendations of:\n(a) Bhuria Committee\n(b) Sarkaria Commission\n(c) Verma Committee\n(d) Kaka Kalelkar Commission\nCorrect Answer: (a) Bhuria Committee [Explanation: The Dileep Singh Bhuria Committee (1994–1995) formulated the framework that became the PESA Act 1996, vesting statutory power in tribal Gram Sabhas.]",
      "Q4. Under Article 243D of the Constitution, what is the minimum mandatory proportion of total seats reserved for women in Panchayati Raj institutions across India?\n(a) 25%\n(b) 33.33% (One-third)\n(c) 50%\n(d) 15%\nCorrect Answer: (b) 33.33% (One-third) [Explanation: Article 243D(3) mandates that not less than one-third of the total number of seats in every Panchayat must be reserved for women (several states like AP have enhanced this to 50%).]",
      "Q5. Which constitutional body is constituted every five years by the Governor of a State under Article 243-I to review the financial position of Panchayats and Municipalities?\n(a) State Election Commission\n(b) State Finance Commission\n(c) District Planning Committee\n(d) State Planning Board\nCorrect Answer: (b) State Finance Commission [Explanation: Article 243-I mandates the Governor to appoint a State Finance Commission every 5 years to recommend principles for tax devolution and grants-in-aid to PRIs and ULBs.]"
    ]
  },
  {
    "id": "APPSC-G1-POL-09",
    "filename": "09_constitutional_bodies_ec_upsc_cag_finance_commission",
    "title": "Constitutional Bodies: ECI, UPSC, CAG & Finance Commission",
    "mapping": "Polity, Constitution & Governance: Constitutional Bodies - Election Commission of India (Art 324), Union Public Service Commission (Art 315), Comptroller and Auditor General (Art 148), Finance Commission (Art 280), National Commissions for SCs, STs and BCs.",
    "intro": "Constitutional bodies derive their institutional existence, autonomy, and mandate directly from the text of the Constitution of India, safeguarding democratic integrity, administrative merit, and financial probity. Serving as neutral watchdogs of the republic, these institutions—the Election Commission of India (ECI), the Union Public Service Commission (UPSC), the Comptroller and Auditor General (CAG), and the Finance Commission—operate independently of executive interference.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Election_Commission_of_India.jpg", "caption": "Nirvachan Sadan, the headquarters of the Election Commission of India in New Delhi.", "alt": "Election Commission of India building Nirvachan Sadan"},
    "table": {
      "caption": "Charter of Premier Independent Constitutional Bodies in India",
      "headers": ["Constitutional Body", "Article Reference", "Composition & Appointment", "Core Mandate & Constitutional Safeguards"],
      "rows": [
        ["Election Commission of India (ECI)", "Article 324", "Chief Election Commissioner (CEC) and two ECs; appointed by President; 6 yrs or 65 age.", "Superintendence, direction, and control of elections to Parliament, State Legislatures, and offices of President/VP; CEC removed only like a Supreme Court judge."],
        ["Comptroller & Auditor General (CAG)", "Article 148 to 151", "Appointed by President; 6 yrs or 65 age; ineligible for further office.", "'Guardian of the Public Purse'; audits all expenditure from Consolidated Fund of India and States; submits 3 audit reports to President laid before PAC; removed only like SC judge."],
        ["Finance Commission of India", "Article 280", "Chairman and 4 members appointed by President every 5 years.", "Recommends horizontal and vertical devolution of central divisible tax pool between Union and States, and grants-in-aid under Article 275."],
        ["Union Public Service Commission (UPSC)", "Articles 315 to 323", "Chairman and members appointed by President; 6 yrs or 65 age; ineligible for further office.", "'Watchdog of merit system'; conducts civil service and defense exams; consulted on personnel management and disciplinary cases; reports laid before Parliament."]
      ]
    },
    "bullets": [
      "Anoop Baranwal Judgment (2023): Landmark constitution bench ruling establishing that the CEC and ECs should be appointed by the President on the advice of a selection committee comprising the Prime Minister, the Leader of the Opposition, and the Chief Justice of India; Parliament subsequently enacted the Chief Election Commissioner Act 2023 substituting CJI with a Union Cabinet Minister.",
      "CAG's Constitutional Role: Dr. Ambedkar declared the CAG as the 'most important officer under the Constitution of India'; audits compliance, propriety, and performance (CAG vs Government executive disputes in 2G, Coal block allocations).",
      "National Commissions for Marginalized Classes: National Commission for Scheduled Castes (NCSC, Art 338), National Commission for Scheduled Tribes (NCST, Art 338A, created by 89th Amendment 2003), and National Commission for Backward Classes (NCBC, Art 338B, granted constitutional status by 102nd Amendment 2018); possess civil court powers to investigate atrocities and monitor constitutional safeguards.",
      "15th & 16th Finance Commissions: 15th FC (chaired by N.K. Singh) recommended 41% vertical devolution to states, using 2011 population data alongside demographic performance, income distance, and forest cover criteria; 16th FC constituted under Dr. Arvind Panagariya."
    ],
    "mains": [
      "Dr. B.R. Ambedkar described the Comptroller and Auditor General (CAG) as the most important officer under the Constitution. Critically evaluate the role of the CAG in upholding financial accountability in Indian governance. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Cite Dr. Ambedkar's constituent assembly address on the four bulwarks of the Constitution (SC, ECI, UPSC, CAG); detail constitutional safeguards guaranteeing independence: removal only on grounds of proven misbehavior or incapacity like SC judge, salary charged on Consolidated Fund of India, disqualification from future government posts (Article 148); analyze the tripartite audit roles: compliance audit (lawful expenditure), financial audit (accounting precision), and propriety audit (checking wastefulness and executive wisdom); evaluate the CAG-PAC nexus where Public Accounts Committee investigates CAG audit findings; discuss modern frontiers: environmental auditing, audit of PPP projects, and performance evaluation of welfare schemes."
    ],
    "mcqs": [
      "Q1. Which Article of the Constitution of India provides for the office of the Comptroller and Auditor General (CAG) as the supreme audit authority of the republic?\n(a) Article 110\n(b) Article 148\n(c) Article 280\n(d) Article 324\nCorrect Answer: (b) Article 148 [Explanation: Article 148 establishes the office of the Comptroller and Auditor General of India, independent of executive interference.]",
      "Q2. Under Article 280 of the Constitution, who constitutes the Finance Commission of India at the expiration of every fifth year or earlier?\n(a) Prime Minister\n(b) President of India\n(c) Parliament of India\n(d) Governor of the Reserve Bank of India\nCorrect Answer: (b) President of India [Explanation: Article 280 provides that the President of India shall constitute a Finance Commission consisting of a Chairman and four other members every fifth year.]",
      "Q3. Constitutional status was granted to the National Commission for Backward Classes (NCBC) under Article 338B by which Constitutional Amendment Act?\n(a) 99th Amendment Act 2014\n(b) 101st Amendment Act 2016\n(c) 102nd Amendment Act 2018\n(d) 103rd Amendment Act 2019\nCorrect Answer: (c) 102nd Amendment Act 2018 [Explanation: The 102nd Constitutional Amendment Act of 2018 inserted Article 338B, conferring full constitutional status on the National Commission for Backward Classes.]",
      "Q4. A member of the Union Public Service Commission (UPSC) holds office for a term of six years or until attaining what maximum age?\n(a) 60 years\n(b) 62 years\n(c) 65 years\n(d) 70 years\nCorrect Answer: (c) 65 years [Explanation: Under Article 316(2), a member of the UPSC holds office for a term of six years or until the age of 65 years, whichever is earlier.]",
      "Q5. Which constitutional amendment bifucated the combined National Commission for SCs and STs into two independent bodies under Articles 338 and 338A?\n(a) 65th Amendment Act 1990\n(b) 86th Amendment Act 2002\n(c) 89th Amendment Act 2003\n(d) 93rd Amendment Act 2005\nCorrect Answer: (c) 89th Amendment Act 2003 [Explanation: The 89th Constitutional Amendment Act 2003 bifurcated the joint commission into the National Commission for SCs (Art 338) and the National Commission for STs (Art 338A).]"
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

print("Part 3 of Subject 4 generated successfully")
