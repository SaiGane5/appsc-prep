import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "02_History_and_Culture_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-APHC-04",
    "filename": "04_kakatiyas_of_warangal_administration_tanks_and_temples",
    "title": "Kakatiyas of Warangal: Administration, Tank Irrigation & Temple Architecture",
    "mapping": "History and Culture of Andhra Pradesh: Medieval Andhra - Kakatiyas of Warangal (Prola II to Prataparudra), Rani Rudrama Devi, Administration (Nayankara System), Motupalli Charter, Chain Tank Irrigation and Architecture (Ramappa Temple, Warangal Fort).",
    "intro": "The Kakatiya dynasty (c. 1158–1323 CE) established a glorious unified Telugu state spanning Telangana and Coastal Andhra from their fortified capital Orugallu (Warangal). Renowned for the heroic reign of Rani Rudrama Devi, pioneering hydraulic chain-tank engineering (Pakhal, Ramappa, Laknavaram), commercial protection of foreign maritime traders via the Motupalli Charter, and floating-brick temple architecture at Ramappa (UNESCO World Heritage Site), the Kakatiyas forged a enduring regional identity.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Ramappa_Temple.jpg", "caption": "The Ramappa (Rudreshwara) Temple at Palampet (1213 CE), celebrated for floating-brick technology and bracket dancing maiden sculptures.", "alt": "Ramappa Temple at Palampet"},
    "table": {
      "caption": "Sovereigns & Structural Achievements of the Kakatiya Golden Era",
      "headers": ["Monarch & Reign", "Military & Political Milestones", "Agrarian & Commercial Reforms", "Architectural Legacies"],
      "rows": [
        ["Rudradeva / Prataparudra I (1158–1195 CE)", "Declared sovereign independence from Western Chalukyas; recorded feats in the Thousand Pillar Temple Inscription (Anumakonda).", "Patronized Shaivism; commenced construction of Orugallu stone fort.", "Built the Trikuta-style Thousand Pillar Temple at Anumakonda."],
        ["Ganapatideva (1199–1262 CE)", "Unified Andhra coast, Rayalaseema, and Telangana; long reign of 63 years.", "Issued the landmark Motupalli Abhaya Sasanam (1244 CE) granting protection and fixed customs duties to foreign merchant ships; built massive irrigation reservoirs.", "Completed outer stone ramparts and 4 magnificent Torana gateways of Warangal Fort; general Recharla Rudra constructed Ramappa Temple (1213 CE)."],
        ["Rani Rudrama Devi (1262–1289 CE)", "One of India's few reigning queens; ruled as 'Rudradeva Maharaja'; repelled Yadavas of Devagiri, Eastern Gangas, and Pandyas.", "Visited by Venetian traveler Marco Polo (1293) who praised her administrative justice and diamond mining at Golconda.", "Defended Warangal's double fortification; died fighting rebel Kayastha chieftain Ambadeva in Chandupatla (Nalgonda)."],
        ["Prataparudra II (1289–1323 CE)", "Subdued internal revolts; reformed Nayankara military recruitment.", "Encouraged expansion of agriculture in dry tracts; compiled Telugu legal codes.", "Heroically resisted five Delhi Sultanate invasions (Malik Kafur, Khusrau Khan, Ulugh Khan) until Warangal fell in 1323 CE."]
      ]
    },
    "bullets": [
      "Motupalli Abhaya Sasanam (1244 CE): Pillar charter at Motupalli port (Bapatla district) by Ganapatideva promising foreign traders that their ships would not be confiscated if shipwrecked; fixed customs duty (Krupa) on silk, camphor, pearls, and metals at modest 1/30th value.",
      "Hydraulic Chain-Tank Engineering: Interconnected irrigation tanks across undulating topography where overflow from upper tanks filled lower reservoirs; constructed massive earthen bunds: Pakhal Lake, Ramappa Lake, Laknavaram Lake, and Sanigaram Lake.",
      "Nayankara System Origins: Kakatiyas were the original architects of the Nayankara system; Prataparudra divided the realm into 77 Nayankaras assigned to Padmanayaka warrior chiefs, directly ancestral to the Vijayanagar system.",
      "Ramappa Temple Architecture: Built by sculptor Ramappa under general Recharla Rudra; constructed using lightweight floating porous bricks (sponge bricks) and carved black basalt bracket figures (Madanikas / Salabhanjikas)."
    ],
    "mains": [
      "Analyze the administrative, hydraulic, and commercial contributions of the Kakatiyas of Warangal. How did their chain-tank irrigation system revolutionize agriculture in the Deccan? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the socio-political context of Kakatiya state-building in the dry red-soil Deccan; explain the engineering brilliance of the chain-tank system (Pakhal, Ramappa, Laknavaram) connecting natural stream catchments via massive stone-faced earthen bunds, enabling wet paddy cultivation; analyze Ganapatideva's Motupalli Abhaya Sasanam promoting foreign maritime trade; examine the proto-feudal Nayankara military organization dividing the kingdom among 77 warrior chiefs; evaluate Ramappa Temple's floating-brick engineering."
    ],
    "mcqs": [
      "Q1. Which Kakatiya monarch issued the famous 'Motupalli Abhaya Sasanam' in 1244 CE, granting royal security and fixed customs tariffs to foreign sea merchants?\n(a) Rudradeva\n(b) Ganapatideva\n(c) Rani Rudrama Devi\n(d) Prataparudra II\nCorrect Answer: (b) Ganapatideva [Explanation: King Ganapatideva issued the Motupalli Pillar Charter in 1244 CE promising safety and fair duties to maritime traders from across the Indian Ocean.]",
      "Q2. The world-renowned Ramappa (Rudreshwara) Temple at Palampet, inscribed as a UNESCO World Heritage Site in 2021, was constructed in 1213 CE under the supervision of which general?\n(a) Recharla Rudra\n(b) Gona Ganna Reddy\n(c) Muppidi Nayaka\n(d) Prola Bhupati\nCorrect Answer: (a) Recharla Rudra [Explanation: General Recharla Rudra commissioned the temple in 1213 CE, uniquely named after its chief architect-sculptor Ramappa.]",
      "Q3. Venetian traveler Marco Polo visited the Andhra coast in the late 13th century at the port of Motupalli during the reign of which illustrious ruler?\n(a) Ganapatideva\n(b) Rani Rudrama Devi\n(c) Prataparudra II\n(d) Prola II\nCorrect Answer: (b) Rani Rudrama Devi [Explanation: Marco Polo visited coastal Andhra around 1293 CE, praising the administrative wisdom and diamond exports under Queen Rudrama Devi.]",
      "Q4. Which inscription discovered in Nalgonda district definitively established the martyrdom and death date (1289 CE) of Rani Rudrama Devi in battle against Kayastha Ambadeva?\n(a) Anumakonda Inscription\n(b) Chandupatla Inscription\n(c) Bayyaram Inscription\n(d) Malkapuram Inscription\nCorrect Answer: (b) Chandupatla Inscription [Explanation: The Chandupatla stone inscription (dated 27 November 1289) proved that Rani Rudrama Devi died fighting the rebellious Kayastha chieftain Ambadeva.]",
      "Q5. How many Nayankaras (feudal military commands) were established by Kakatiya King Prataparudra II to reorganize the defense of the kingdom?\n(a) 50\n(b) 72\n(c) 77\n(d) 108\nCorrect Answer: (c) 77 [Explanation: Prataparudra II divided the Kakatiya kingdom into 77 Nayankaras entrusted to loyal Padmanayaka warrior chiefs, laying the foundation for the Nayankara military system.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-05",
    "filename": "05_musunuri_nayakas_and_reddis_of_kondavidu",
    "title": "Musunuri Nayakas & Reddis of Kondavidu: Telugu Liberation & Golden Age of Poetry",
    "mapping": "History and Culture of Andhra Pradesh: Post-Kakatiya Andhra - Musunuri Nayakas (Prolaya Nayaka, Kapaya Nayaka, Vilasa Grant), Reddis of Kondavidu and Rajahmundry (Kumaragiri Reddi, Kataya Vema Reddi), Patronage of Kavisarvabhauma Srinatha.",
    "intro": "Following the fall of Warangal to the Delhi Sultanate in 1323 CE, coastal Andhra and Telangana witnessed a heroic nationalist liberation movement led by the Musunuri Nayakas, who expelled the Tughlaq garrison. Concurrently, the Reddi kingdoms of Kondavidu and Rajahmundry established an independent renaissance of Telugu culture, celebrated for agricultural tank construction, Vasantotsava spring festivals, and the immortal poetry of Kavisarvabhauma Srinatha.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Kondavidu_Fort.jpg", "caption": "The hill fortress of Kondavidu in Guntur district, capital of the Kondavidu Reddi dynasty.", "alt": "Kondavidu hill fort ramparts"},
    "table": {
      "caption": "Political & Literary Profile of Post-Kakatiya Telugu Dynasties",
      "headers": ["Dynasty & Eras", "Prominent Rulers & Capitals", "Political Liberation & Military Feats", "Literary & Cultural Legacies"],
      "rows": [
        ["Musunuri Nayakas (1325–1368 CE)", "Musunuri Prolaya Nayaka, Kapaya Nayaka; Rekapalli & Warangal.", "Vilasa copper plate grant describes Islamic devastation and liberation; unified 75 confederate Nayakas; liberated Warangal from Tughlaq governor Malik Maqbul in 1336 CE.", "Proclaimed 'Andhra Desadhiswara'; restored Vedic temples and agraharas; overthrown by the rival Recherla Velamas of Devarakonda."],
        ["Reddis of Kondavidu (1325–1424 CE)", "Prolaya Vema Reddi, Anavota Reddi, Kumaragiri Reddi; Addanki & Kondavidu.", "Fortified Kondavidu hill citadel; constructed stepways to Srisailam (Patala Ganga) and Ahobilam; repelled Sultanate invasions.", "Golden age of Telugu kavya; Kumaragiri Reddi authored dance treatise 'Vasantarajiya' and celebrated Spring Festivals (Karpura Vasantaraya); court poet Yerrapragada completed the Mahabharata translation."],
        ["Reddis of Rajahmundry (1395–1448 CE)", "Kataya Vema Reddi, Allada Reddi, Veerabhadra Reddi; Rajamahendravaram.", "Kataya Vema Reddi authored commentaries on Kalidasa's plays ('Kumaragirirajiyam'); protected Godavari delta.", "Patronized Kavisarvabhauma Srinatha (court poet); poet Potana composed 'Andhra Maha Bhagavatam' in nearby Bammera."]
      ]
    },
    "bullets": [
      "Vilasa Grant of Musunuri Prolaya Nayaka: Discovered in East Godavari; rare contemporary record lamenting the fall of Kakatiyas, the burning of villages and destruction of temples under Tughlaq armies, and celebrating Prolaya Nayaka as the savior who resurrected Dharma.",
      "Kavisarvabhauma Srinatha: Greatest Telugu poet of the medieval era; authored 'Haravilasa', 'Kasikhandam', 'Sringara Naishadham', 'Bhimakhandam', and the historical ballad 'Palnati Vira Charitra'; defeated Gauda Dindima Bhatta in the court of Devaraya II at Vijayanagara and was showered with molten gold (Kanakabhishekam).",
      "Yerrapragada (Errana): Court poet of Prolaya Vema Reddi; third of the Kavitrayam (Trinity of Telugu Poets); completed the unfinished Aranya Parva of Nannaya; authored 'Harivamsam' and 'Nrisimhapuranam'; honoured with titles 'Prabandha Parameshwara' and 'Sambhudasa'.",
      "Architectural Infrastructure: Built fortified hill strongholds at Kondavidu, Bellamkonda, Vinukonda, and Nagarjunakonda; constructed flight of stone steps (Sopanamarga) to the sacred hill shrines of Srisailam and Ahobilam."
    ],
    "mains": [
      "Discuss the socio-political significance of the Musunuri Nayakas in liberating Andhra from Delhi Sultanate rule, and evaluate the literary contributions of the Reddi Kings of Kondavidu. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the aftermath of the 1323 fall of Warangal and Tughlaq administrative oppression; analyze the Vilasa Grant of Prolaya Nayaka documenting the confederacy of 75 Nayakas that drove out the Sultanate governor from Warangal in 1336 CE; evaluate the Reddis of Kondavidu: economic reconstruction through tank building, royal patronage of Telugu poetry by Prolaya Vema Reddi and Kumaragiri Reddi; examine the literary zenith: completion of Mahabharata by Errana, and the peerless works of Srinatha ('Haravilasa', 'Sringara Naishadham'); conclude on this era as the renaissance of Telugu cultural self-assertion."
    ],
    "mcqs": [
      "Q1. Which famous copper plate grant of Musunuri Prolaya Nayaka provides an authentic historical narrative of the liberation of Andhra from Delhi Sultanate rule?\n(a) Motupalli Grant\n(b) Vilasa Grant\n(c) Kondavidu Grant\n(d) Draksharama Grant\nCorrect Answer: (b) Vilasa Grant [Explanation: The Vilasa copper plate grant of Prolaya Nayaka describes the devastation caused by the Tughlaqs and details the confederacy of Nayakas that liberated the Telugu country.]",
      "Q2. Which Reddi monarch of Kondavidu was celebrated with the title 'Karpura Vasantaraya' for his patronage of music, dance, and annual spring festivals?\n(a) Prolaya Vema Reddi\n(b) Anavota Reddi\n(c) Kumaragiri Reddi\n(d) Racha Vema Reddi\nCorrect Answer: (c) Kumaragiri Reddi [Explanation: Kumaragiri Reddi authored the Sanskrit drama treatise 'Vasantarajiya' and celebrated lavish Vasantotsavas, earning the title 'Karpura Vasantaraya'.]",
      "Q3. The great Telugu poet laureate Kavisarvabhauma Srinatha was bathed in gold (Kanakabhishekam) in the Pearl Hall (Muthyala Shala) of which emperor's court?\n(a) Krishnadevaraya\n(b) Devaraya II\n(c) Harihara II\n(d) Kumaragiri Reddi\nCorrect Answer: (b) Devaraya II [Explanation: Srinatha defeated royal court scholar Dindima Bhatta in debate and was honoured with Kanakabhishekam by Vijayanagar Emperor Devaraya II in Hampi.]",
      "Q4. Which poet among the 'Kavitrayam' (Trinity of Telugu Poets) was patronized by Prolaya Vema Reddi and completed the unfinished Aranya Parva of the Mahabharata?\n(a) Nannaya\n(b) Tikkana\n(c) Yerrapragada (Errana)\n(d) Srinatha\nCorrect Answer: (c) Yerrapragada (Errana) [Explanation: Errana (Yerrapragada), court poet of Prolaya Vema Reddi, completed the half-finished Aranya Parva left by Nannaya, earning the title 'Prabandha Parameshwara'.]",
      "Q5. Which historic hill fortress served as the impregnable capital of the Reddi kingdom in Guntur district before its capture by the Vijayanagar Empire?\n(a) Kondapalli Fort\n(b) Kondavidu Fort\n(c) Chandragiri Fort\n(d) Gandikota Fort\nCorrect Answer: (b) Kondavidu Fort [Explanation: Kondavidu Fort in Guntur was the formidable capital of the Reddi rulers, renowned for its triple ramparts, water reservoirs, and granaries.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-06",
    "filename": "06_vijayanagara_empire_in_andhra_and_lepakshi_art",
    "title": "Vijayanagara in Andhra: Rayalaseema Zenith, Lepakshi Art & Telugu Literature",
    "mapping": "History and Culture of Andhra Pradesh: Vijayanagar Era in Andhra - Rayalaseema Hinterland, Krishnadevaraya's Patronage of Ashtadiggajas, Lepakshi Veerabhadra Temple Architecture, Murals, Penukonda and Chandragiri Forts.",
    "intro": "The Vijayanagar Empire held a deeply intimate connection with the Andhra region, particularly the Rayalaseema hinterland. Under Emperor Sri Krishnadevaraya (1509–1529 CE), Telugu literature attained its classical 'Prabandha' zenith with the court circle of 'Ashtadiggajas'. Concurrently, Andhra architecture reached supreme expressive heights in the hanging pillars and vibrant fresco murals of the Lepakshi Veerabhadra Temple, while Penukonda and Chandragiri served as imperial redoubts following the Battle of Talikota.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Lepakshi_Nandi.jpg", "caption": "The colossal monolithic Nandi at Lepakshi, Anantapur district, carved out of a single granite boulder (16th century).", "alt": "Monolithic stone bull Nandi at Lepakshi"},
    "table": {
      "caption": "Cultural & Architectural Highlights of Vijayanagar Rule in Andhra",
      "headers": ["Monument / Cultural Domain", "Location & Royal Builders", "Key Features & Art Highlights", "Historical Significance"],
      "rows": [
        ["Lepakshi Veerabhadra Temple", "Lepakshi, Anantapur; built by brothers Virupanna and Veeranna (1530 CE) under Achyuta Deva Raya.", "World-famous 'Hanging Pillar' (floating column), colossal monolithic granite Nandi (largest in India), Natya Mandapa with 70 carved musical pillars.", "Contains India's finest 16th-century Vijayanagar fresco ceiling murals depicting Kiratarjuniya and mythological legends using vegetable dyes."],
        ["Prabandha Literary Golden Age", "Bhuvanavijayam royal assembly, Hampi & Rayalaseema; Sri Krishnadevaraya.", "Krishnadevaraya composed 'Amuktamalyada' in Telugu; patronized 'Ashtadiggajas' (Allasani Peddana, Tenali Ramakrishna, Nandi Timmana, Dhurjati, Madayyagari Mallana, Ayyalaraju Ramabhadrudu, Pingali Surana, Ramarajabhushana).", "Telugu elevated to the status of royal court language; declaration: 'Desa Bhashalandu Telugu Lessa' (Among the country's languages, Telugu is the finest)."],
        ["Penukonda & Chandragiri Forts", "Penukonda (Anantapur) & Chandragiri (Tirupati); Aravidu Dynasty.", "Hill citadels with Gagan Mahal palace architecture synthesizing Hindu and Islamic arch vaults; Chandragiri was the royal seat where Venkata II granted Madras to the English (1639).", "Served as the second and third capitals of the Vijayanagar Empire after the fall of Hampi in 1565 CE."],
        ["Religious Endowments in Rayalaseema", "Tirumala Venkateswara Temple, Srisailam, Srikalahasti, Ahobilam.", "Krishnadevaraya visited Tirumala 7 times with his queens Tirumala Devi and Chinna Devi, installing gold-plated vimana (Ananda Nilayam) and bronze statues; erected the 120-foot Rajagopuram at Srikalahasti."]
      ]
    },
    "bullets": [
      "Amuktamalyada: Masterpiece composed by Krishnadevaraya detailing the divine marriage of Lord Ranganatha with Tamil Alvar poetess Goda Devi (Andal); contains the famous fourth canto on political statecraft, diplomacy, and righteous governance (Rajaniti).",
      "Ashtadiggajas Masterpieces: Allasani Peddana ('Manucharitra'), Nandi Timmana ('Parijatapaharanam'), Tenali Ramakrishna ('Panduranga Mahatmyam'), Dhurjati ('Kalahastiswara Mahatmyam'), Pingali Surana ('Kalapurnodayam' - world's first novelistic prabandha).",
      "Lepakshi Hanging Pillar: Architectural marvel among 70 pillars in the Natya Mandapa that does not touch the stone floor, allowing thin cloth or paper to pass underneath.",
      "Tallapaka Annamacharya (1408–1503 CE): The 'Pada Kavita Pitamaha'; contemporary saint-composer who composed 32,000 sringara and sankirtana padas in Telugu dedicated to Lord Venkateswara of Tirupati, engraved on copper plates stored in the Sankeertana Bhandagaram."
    ],
    "mains": [
      "Critically evaluate the architectural and artistic features of the Lepakshi Veerabhadra Temple complex in Andhra Pradesh. What makes its mural paintings and stone sculptures unique in South Indian art? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Introduce Lepakshi as the supreme architectural jewel of 16th-century Vijayanagar art built by Virupanna and Veeranna; detail structural elements: the Natya Mandapa with 70 carved granite pillars, the legendary 'Hanging Pillar', and the colossal monolithic Nandi carved from a single boulder; analyze the mural frescoes: ceiling paintings depicting mythological narratives (Parvati Kalyanam, Kiratarjuniya) executed with mineral and vegetable dyes displaying dynamic line work, expressive profile faces, and intricate textile patterns; conclude on its status as the pinnacle of late medieval Andhra pictorial art."
    ],
    "mcqs": [
      "Q1. Which architectural marvel inside the Natya Mandapa of the Lepakshi Veerabhadra Temple is renowned for not resting entirely on the ground floor?\n(a) Monolithic Nandi\n(b) The Hanging Pillar\n(c) Nagalinga\n(d) Kalyana Mandapa\nCorrect Answer: (b) The Hanging Pillar [Explanation: The Hanging Pillar of Lepakshi is a famed stone column suspended slightly above the temple floor, demonstrating Vijayanagar engineering precision.]",
      "Q2. In his Telugu epic 'Amuktamalyada', Sri Krishnadevaraya famously declared which linguistic tribute to the Telugu language?\n(a) 'Telugu Talli Chirunavvu'\n(b) 'Desa Bhashalandu Telugu Lessa'\n(c) 'Andhra Bhasha Amrutham'\n(d) 'Vaganusasana Telugu'\nCorrect Answer: (b) 'Desa Bhashalandu Telugu Lessa' [Explanation: In the introduction to 'Amuktamalyada', Krishnadevaraya proclaimed 'Desa Bhashalandu Telugu Lessa' (Among the languages of the nation, Telugu is the best).]",
      "Q3. Who among the 'Ashtadiggajas' authored the celebrated poetic work 'Parijatapaharanam' to reconcile a domestic lovers' tiff between Krishnadevaraya and Queen Tirumala Devi?\n(a) Allasani Peddana\n(b) Nandi Timmana\n(c) Tenali Ramakrishna\n(d) Madayyagari Mallana\nCorrect Answer: (b) Nandi Timmana [Explanation: Mukku Timmana (Nandi Timmana) composed 'Parijatapaharanam' (The Theft of the Parijata Flower), presenting the charming mythological tale to pacify royal marital discord.]",
      "Q4. Which saint-composer, revered as 'Pada Kavita Pitamaha', composed 32,000 devotional sankirtanas in Telugu dedicated to Lord Venkateswara of Tirumala?\n(a) Tyagaraja\n(b) Tallapaka Annamacharya\n(c) Kancharla Gopanna (Ramadasu)\n(d) Kshetriyya\nCorrect Answer: (b) Tallapaka Annamacharya [Explanation: Tallapaka Annamacharya (1408–1503 CE) composed 32,000 padas inscribed on copper plates preserved in the Tirumala temple, pioneering the Telugu Sankirtana tradition.]",
      "Q5. Which historic fort in Andhra Pradesh served as the final imperial capital of the Vijayanagar Aravidu dynasty, where British envoy Francis Day secured the charter for Madras in 1639?\n(a) Gooty Fort\n(b) Chandragiri Fort\n(c) Penukonda Fort\n(d) Udayagiri Fort\nCorrect Answer: (b) Chandragiri Fort [Explanation: Chandragiri Fort near Tirupati served as the seat of Emperor Venkata II and Damarla Chennappa Nayaka, who leased Madraspatnam to the English EIC in 1639.]"
    ]
  }
]

for t in topics:
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "History and Culture of Andhra Pradesh",
    "paper": "Paper-II (Mains Section B) & Paper-I (Screening Section A)",
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

print("Part 2 of Subject 2 generated successfully")
