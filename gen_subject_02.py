import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "02_History_and_Culture_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-APHC-01",
    "filename": "01_satavahanas_in_andhra_and_amaravati_art",
    "title": "Satavahanas in Andhra: Administration, Society, Economy & Amaravati Stupa",
    "mapping": "History and Culture of Andhra Pradesh: Ancient Andhra - Satavahana Dynasty, Capital Transitions (Kotilingala, Dhanyakataka), Administration, Social Structure, Maritime Trade and the Amaravati School of Art.",
    "intro": "The Satavahana dynasty (c. 1st Century BCE to 3rd Century CE) represents the foundational imperial epoch of Andhra history. Transitioning from Kotilingala to Dhanyakataka (Dharanikota/Amaravati) on the banks of the Krishna River, the Satavahanas integrated the Deccan plateau, patronized Mahayana Buddhism under Acharya Nagarjuna, developed the magnificent white marble-carved Amaravati Maha Stupa, and conducted lucrative Indo-Roman maritime commerce.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Amaravati_Stupa_Relief.jpg", "caption": "The Amaravati Maha Stupa limestone relief medallion depicting the universal adoration of the Buddha.", "alt": "Amaravati stupa relief carving"},
    "table": {
      "caption": "Socio-Cultural & Economic Matrix of Satavahanas in Andhra",
      "headers": ["Dimension", "Institutional Details & Key Historical Figures", "Economic / Architectural Outcomes"],
      "rows": [
        ["Political Centers", "Kotilingala (Karimnagar), Dhanyakataka / Dharanikota (Guntur), Paithan (Maharashtra).", "Dhanyakataka emerged as the supreme political and maritime emporium of eastern Deccan."],
        ["Maritime Trade & Ports", "Motupalli, Ghantasala, Machilipatnam (Maisolos), Kottapatnam; ship-motif coins of Yajna Sri Satakarni.", "Exported fine muslin, cotton textiles, and spices to the Roman Empire; imported Roman gold and silver denarii."],
        ["Buddhist Patronage", "Amaravati (Deepaladinne), Nagarjunakonda, Bhattiprolu, Guntupalli, Salihundam.", "Bhattiprolu relic casket inscription (earliest southern Brahmi script - precursor to Telugu script); Acharya Nagarjuna founded Madhyamaka philosophy at Sriparvata."],
        ["Art & Architecture", "Amaravati School of Art; soft green/white Palnadu limestone.", "Dynamic narrative relief panels depicting Jataka tales, life of Buddha, natural human movements and crowded scenes with profound emotional depth."]
      ]
    },
    "bullets": [
      "Bhattiprolu Inscription: Discovered in Guntur district; contains crystal reliquaries with Buddha relics; script showcases the 'Bhattiprolu script' (system of vowel markers), recognized by epigraphists as the direct ancestor of modern Telugu-Kannada alphabets.",
      "Acharya Nagarjuna: Patriarch of Mahayana Buddhism; stayed at Sriparvata (Nagarjunakonda) under the patronage of Satavahana king Yajna Sri Satakarni; composed 'Suhrallekha' (Friendly Epistle to King Gautamiputra) and 'Mulamadhyamakakarika'.",
      "Social Stratification: Four-class functional hierarchy (Maharathis/Mahabhojas, Amatyas/Sarthavahas, Halikas/cultivators, and Kammaras/artisans); flourishing trade guilds (Srenis: Kolika for weavers, Tilapishaka for oil-pressers) functioning as banks.",
      "Decline: After Yajna Sri Satakarni, the empire fragmented into feudatory successor lines: Ikshvakus in Coastal Andhra, Abhiras in Maharashtra, and Pallavas in the south."
    ],
    "mains": [
      "Critically evaluate the significance of the Satavahana era in the history and culture of Andhra Pradesh with special focus on the Amaravati School of Art and maritime trade. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight Satavahanas as the first unified state in Telugu territory; examine Dhanyakataka as the political-maritime nexus; assess maritime trade through Periplus accounts (Maisolos) and ship-motif coins excavated along the Coromandel; analyze the Amaravati School of Art: use of Palnadu limestone, narrative relief technique, vibrant human secularism combined with Buddhist spirituality; conclude on the linguistic legacy of the Bhattiprolu script in shaping early Telugu phonetics."
    ],
    "mcqs": [
      "Q1. Which ancient Buddhist stupa in Andhra Pradesh yielded the famous crystal reliquary with an inscription representing the earliest precursor to the Telugu script?\n(a) Amaravati Stupa\n(b) Bhattiprolu Stupa\n(c) Ghantasala Stupa\n(d) Salihundam Stupa\nCorrect Answer: (b) Bhattiprolu Stupa [Explanation: The Bhattiprolu Stupa in Guntur district contained caskets with the 'Bhattiprolu script' (c. 3rd Century BCE), featuring the earliest developmental vowel signs ancestral to Telugu.]",
      "Q2. The ancient Roman geographer Ptolemy and the author of 'Periplus of the Erythraean Sea' refer to the ancient port of Machilipatnam on the Andhra coast as:\n(a) Maisolos\n(b) Barygaza\n(c) Muziris\n(d) Poduke\nCorrect Answer: (a) Maisolos [Explanation: Greco-Roman trade texts designate coastal Machilipatnam and the Krishna delta as 'Maisolos', celebrated for manufacturing super-fine translucent cotton muslin.]",
      "Q3. The great Mahayana Buddhist philosopher Acharya Nagarjuna resided and taught at Sriparvata (Nagarjunakonda) under the royal patronage of which Satavahana monarch?\n(a) Simuka\n(b) Gautamiputra Satakarni\n(c) Yajna Sri Satakarni\n(d) Hala\nCorrect Answer: (c) Yajna Sri Satakarni [Explanation: Acharya Nagarjuna was patronized by King Yajna Sri Satakarni, who built a magnificent multi-storeyed monastery for him at Sriparvata (Nagarjunakonda).]",
      "Q4. Which Satavahana site in Telangana yielded the earliest dynastic coins bearing the legends of King Simuka, proving eastern Deccan origins?\n(a) Dhanyakataka\n(b) Kotilingala\n(c) Paithan\n(d) Kondapur\nCorrect Answer: (b) Kotilingala [Explanation: Excavations at Kotilingala in Karimnagar (Jagtial) district yielded punch-marked and cast coins of King Simuka, Satakarni I, and Satavahana, confirming early Deccan presence.]",
      "Q5. In the Satavahana socio-economic structure in Andhra, trade and craft guilds that functioned as financial institutions and received fixed deposits were termed:\n(a) Aharas\n(b) Srenis\n(c) Nigamas\n(d) Ganas\nCorrect Answer: (b) Srenis [Explanation: Srenis were autonomous merchant and artisan corporations (weavers, potters, oil-pressers) that regulated manufacturing standards and acted as public deposit banks.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-02",
    "filename": "02_ikshvakus_vishnukundins_and_salankayanas",
    "title": "Post-Satavahana Andhra: Ikshvakus of Vijayapuri & Vishnukundins",
    "mapping": "History and Culture of Andhra Pradesh: Post-Satavahana Era - Ikshvakus of Nagarjunakonda (Vijayapuri, Female Patronage), Brihatpalayanas, Salankayanas, Vishnukundins (Rock-Cut Caves, Undavalli, Mogalarajapuram).",
    "intro": "Following the collapse of the Satavahanas in the early 3rd century CE, coastal Andhra witnessed state-building under the Ikshvakus of Vijayapuri (Nagarjunakonda), followed by the Brihatpalayanas, Salankayanas of Vengi, and the powerful Vishnukundins. The period was marked by unique royal dual-patronage (kings performing Vedic sacrifices while queens lavishly financed Buddhist Mahachaityas), the flourishing of international monastic education, and the excavation of multi-storeyed rock-cut cave temples at Undavalli and Mogalarajapuram.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Undavalli_Caves.jpg", "caption": "The four-storeyed rock-cut cave temple at Undavalli near Vijayawada, excavated under the Vishnukundin dynasty.", "alt": "Undavalli four-storey rock-cut cave temple"},
    "table": {
      "caption": "Dynastic Profile of Post-Satavahana Andhra Kingdoms",
      "headers": ["Dynasty & Eras", "Capitals & Prominent Monarchs", "Religious Duality & Inscriptions", "Architectural & Cultural Legacies"],
      "rows": [
        ["Ikshvakus of Vijayapuri (c. 225–300 CE)", "Vijayapuri (Nagarjunakonda); Vasishthiputra Chamtamula, Virapurushadatta, Ehuvula Chamtamula.", "Kings performed Vedic Ashvamedha and Agnishtoma sacrifices; royal women (Chamtisri, Adavi Chamtisri) built Mahachaityas, viharas, and stupas for Aparamahavinaseliya Buddhist sect.", "Nagarjunakonda emerged as Asia's premier Buddhist university; amphitheatre; earliest structural Hindu temples (Sarvadeva temple, Pushpabhadrasvami temple in Sanskrit inscriptions)."],
        ["Salankayanas of Vengi (c. 300–440 CE)", "Vengipura (Pedavegi near Eluru); Hastivarman, Nandivarman.", "Devotees of Chitrarathasvami (Sun God); Samudragupta's Allahabad inscription mentions defeating Hastivarman of Vengi.", "Established Brahminical settlements in Vengi; early copper plate charters in Prakrit and Sanskrit."],
        ["Vishnukundins (c. 440–616 CE)", "Indrapalanagara, Vinukonda, Denduluru; Govindavarma, Madhavavarma II ('Janasraya').", "Devotees of Sriparvata Swami (Mallikarjuna of Srisailam); Madhavavarma II performed 11 Ashvamedha sacrifices and 1,000 Kratus.", "Excavated monumental 4-storeyed rock-cut caves at Undavalli (colossal reclining Vishnu/Anantasayana) and Mogalarajapuram; Govindavarma authored Sanskrit treatise 'Janasraya Chhandovichiti'."]
      ]
    },
    "bullets": [
      "Royal Female Benefactors at Nagarjunakonda: Princess Chamtisri (sister of Chamtamula I) erected the grand Mahachaitya housing the corporeal relics of the Buddha; Bodhisri, an upasika, financed monasteries for pilgrims from Ceylon (Sinhala Vihara), Kashmir, and China.",
      "Nagarjunakonda Amphitheatre: Roman-style open-air acoustic stone amphitheatre excavated in the valley, demonstrating intense Greco-Roman cultural interactions alongside Roman gold coin hoards.",
      "Vishnukundin Coinage: Unique iron and copper-alloy coins featuring a lion with upraised paw on obverse and a vase (Purna Kumbha) flanked by lamps on reverse.",
      "End of Vishnukundin Rule: Defeated in 624 CE by Western Chalukya monarch Pulakesin II at the Battle of Kunala (Kolleru lake), leading to the installation of Kubja Vishnuvardhana and the founding of the Eastern Chalukyas of Vengi."
    ],
    "mains": [
      "Discuss the unique socio-religious phenomenon of dual patronage under the Ikshvakus of Vijayapuri and examine the architectural legacy of the Vishnukundins in Andhra Pradesh. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the socio-religious duality: Ikshvaku kings (Chamtamula I) reviving orthodox Vedic sacrifices (Ashvamedha) to assert royal legitimacy, while their royal consorts, sisters, and daughters (Chamtisri) made monumental endowments to Buddhist monasteries, proving societal religious syncretism; highlight excavations at Nagarjunakonda: Sinhala Vihara, acoustic amphitheatre, and earliest Sanskrit Hindu structural shrines; evaluate Vishnukundin rock-cut architecture: transition from Buddhist caves to Brahmanical cave shrines at Undavalli (four storeys, colossal Anantasayana Vishnu) and Mogalarajapuram; conclude on their role in shaping early Andhra classical culture."
    ],
    "mcqs": [
      "Q1. Which royal Ikshvaku princess made the historic endowments recorded in inscriptions for the construction of the Great Mahachaitya at Nagarjunakonda?\n(a) Bodhisri\n(b) Chamtisri\n(c) Bappisri\n(d) Rudradharabhattarika\nCorrect Answer: (b) Chamtisri [Explanation: Princess Chamtisri, sister of King Chamtamula I and chief female patron, built the magnificent Mahachaitya at Vijayapuri (Nagarjunakonda) for the Aparamahavinaseliya Buddhist sect.]",
      "Q2. The Allahabad Pillar Inscription of Samudragupta records that during his southern campaign (Dakshinapatha), he defeated King Hastivarman of which ancient Andhra dynasty?\n(a) Ikshvakus\n(b) Salankayanas of Vengi\n(c) Vishnukundins\n(d) Anandagotras\nCorrect Answer: (b) Salankayanas of Vengi [Explanation: Harisena's Prayag Prashasti notes that Samudragupta defeated Hastivarman, the Salankayana king of Vengi, before restoring him as a tributary monarch.]",
      "Q3. The monumental four-storeyed rock-cut cave temple at Undavalli near Guntur, famous for its colossal reclining sculpture of Lord Anantasayana Vishnu, was excavated by:\n(a) Satavahanas\n(b) Ikshvakus\n(c) Vishnukundins\n(d) Eastern Chalukyas\nCorrect Answer: (c) Vishnukundins [Explanation: The rock-cut cave temples of Undavalli and Mogalarajapuram were excavated under the royal patronage of the Vishnukundin monarchs in the 5th and 6th centuries CE.]",
      "Q4. Which powerful Vishnukundin monarch assumed the title 'Janasraya' and performed eleven Ashvamedha sacrifices and thousands of Vedic Kratus?\n(a) Govindavarma\n(b) Madhavavarma II\n(c) Indrabhattaraka\n(d) Vikramendravarma\nCorrect Answer: (b) Madhavavarma II [Explanation: King Madhavavarma II (440–495 CE) was the greatest Vishnukundin sovereign, celebrated for performing 11 Ashvamedha and 1,000 Agnishtoma sacrifices.]",
      "Q5. Which sacred family deity (Kula Devata) was revered by the Vishnukundin rulers in their royal copper plate grants?\n(a) Lord Venkateswara\n(b) Sriparvata Swami (Mallikarjuna of Srisailam)\n(c) Amaralingeswara\n(d) Narasimha of Simhachalam\nCorrect Answer: (b) Sriparvata Swami (Mallikarjuna of Srisailam) [Explanation: The Vishnukundin charters invoke 'Sriparvata Swami Padanudhyata' (devotees at the feet of Sriparvata Swami, identified with Mallikarjuna of Srisailam).]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-03",
    "filename": "03_eastern_chalukyas_of_vengi_and_telugu_language_evolution",
    "title": "Eastern Chalukyas of Vengi: Telugu Language Evolution & Temple Architecture",
    "mapping": "History and Culture of India & AP: Eastern Chalukyas of Vengi (624–1075 CE) - Kubja Vishnuvardhana, Gunaga Vijayaditya, Renati Cholas & Erragudipadu Inscription, Nannaya Bhatta, Telugu Language Renaissance, Draksharama and Biccavolu Temples.",
    "intro": "The Eastern Chalukyas of Vengi (624–1075 CE) ruled coastal Andhra for over five centuries, providing the political and cultural foundation for modern Telugu identity. Founded by Kubja Vishnuvardhana, the dynasty nurtured the emergence of Telugu as a classical literary language, witnessed the pioneering Mahabharata translation by Adikavi Nannaya Bhatta, and erected magnificent Vesara-Dravidian temples at Draksharama, Biccavolu, and Chebrolu.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Draksharama_Temple.jpg", "caption": "The Bhimeswara Swamy Temple at Draksharama, East Godavari, built by Eastern Chalukya King Chalukya Bhima I.", "alt": "Draksharama Temple exterior tower"},
    "table": {
      "caption": "Milestones of Eastern Chalukyan Governance & Cultural Renaissance",
      "headers": ["Monarch & Reign", "Capitals & Political Achievements", "Telugu Literary & Epigraphic Evolution", "Temple Architecture"],
      "rows": [
        ["Kubja Vishnuvardhana (624–641 CE)", "Vengi (Pedavegi); younger brother of Pulakesin II.", "Assumed title 'Vishamasiddhi'; established autonomous sovereignty over coastal Andhra.", "Initiated transition from rock-cut to structural temples."],
        ["Gunaga Vijayaditya (848–892 CE)", "Vengi; Greatest military monarch; defeated Rashtrakuta Krishna II and Chedis of Dahala.", "Court general Panduranga set up the Addanki Inscription (848 CE) containing the earliest known Telugu verse (Taruvoja metre).", "Constructed numerous Shiva shrines across coastal Andhra."],
        ["Chalukya Bhima I (892–921 CE)", "Vengi; repelled Rashtrakuta invasions after fighting 360 battles.", "Patronized Telugu scholars and poets; issued Dharmavaram inscription (first Telugu Sisa metre verse).", "Constructed the colossal twin Bhimeswara temples at Draksharama (Draksharama Bhimeswara) and Chalukya Bhimavaram (Samarlakota)."],
        ["Rajaraja Narendra (1022–1061 CE)", "Rajahmundry (Rajamahendravaram) on Godavari river; married Chola princess Ammanga Devi.", "Court was the cradle of classical Telugu literature; patronized Adikavi Nannaya Bhatta who commenced the Telugu Mahabharata translation (Andhra Mahabharatamu).", "Embellished Rajahmundry as the cultural capital of Andhra; unified Chalukya-Chola lineages under son Kulottunga I."]
      ]
    },
    "bullets": [
      "Evolution of Telugu Inscriptions: Erragudipadu Inscription (575 CE) of Renati Chola king Dhananjaya is the earliest epigraph written entirely in the Telugu prose language (Kamalanadu, Kadapa district); followed by Eastern Chalukyan verse inscriptions at Addanki (Taruvoja metre), Kandukur (first Madhyakkara metre), and Bezwada (Yuddhamalla's inscription).",
      "Nannaya Bhatta (Adikavi): Translated the first two and a half Parvas (Adi, Sabha, and part of Aranya Parva) of the Mahabharata from Sanskrit into chaste Telugu; authored 'Andhra Sabda Chintamani' (first Telugu grammatical work written in Sanskrit); hailed as 'Vaganusasana' (Lawgiver of Language).",
      "Biccavolu Temple Complex: Located in East Godavari; cluster of 9th-century granite temples (Goluthesvara, Rajaraja, Chandrasekhara) showcasing mature Eastern Chalukyan sculpture and elegant vimana superstructures.",
      "Chalukya-Chola Union: In 1070 CE, Rajendra Chalukya (son of Rajaraja Narendra) ascended the Chola throne in Thanjavur as Kulottunga Chola I, merging the Eastern Chalukya and Imperial Chola crowns."
    ],
    "mains": [
      "Trace the evolution of the Telugu language and literature under the patronage of the Eastern Chalukyas of Vengi. Evaluate the seminal contribution of Nannaya Bhatta in founding classical Telugu literature. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Trace linguistic epigraphy from pre-Chalukyan times (Bhattiprolu Brahmi, Amaravati Prakrit) to the Erragudipadu inscription (575 CE); highlight Eastern Chalukyan epigraphic verses (Addanki, Dharmavaram, Bezwada) showcasing poetic metres (Taruvoja, Sisa); analyze the historic context of Rajahmundry under Rajaraja Narendra; explain Adikavi Nannaya Bhatta's translation of the Mahabharata (Andhra Mahabharatamu): establishing Sanskrit-Telugu (Tatsama) linguistic synthesis, metric elegance (Champukavya style), and cultural legitimation; discuss his Sanskrit grammar of Telugu ('Andhra Sabda Chintamani'); conclude on how this established the foundation of Telugu classical identity."
    ],
    "mcqs": [
      "Q1. Which inscription from Kadapa district, issued by Renati Chola king Dhananjaya in 575 CE, is recognized as the earliest epigraph in the Telugu language?\n(a) Addanki Inscription\n(b) Erragudipadu Inscription\n(c) Kalamalla Inscription\n(d) Bezwada Inscription\nCorrect Answer: (c) Kalamalla Inscription [Explanation: The Kalamalla inscription (575 CE) of Erikal Mutthuraju Dhananjaya is the earliest epigraphical record written entirely in archaic Telugu prose, closely followed by Erragudipadu.]",
      "Q2. The Addanki Inscription (848 CE), issued during the reign of Eastern Chalukya King Gunaga Vijayaditya, is renowned in Telugu literature for containing the earliest example of:\n(a) Sisa metre\n(b) Taruvoja metre\n(c) Kanda metre\n(d) Champu style\nCorrect Answer: (b) Taruvoja metre [Explanation: The Addanki stone inscription of general Panduranga contains the earliest known Telugu poetic verse composed in the 'Taruvoja' classical metre.]",
      "Q3. Adikavi Nannaya Bhatta commenced the translation of the Sanskrit Mahabharata into Telugu ('Andhra Mahabharatamu') under the royal patronage of which Eastern Chalukya king?\n(a) Gunaga Vijayaditya\n(b) Chalukya Bhima I\n(c) Rajaraja Narendra\n(d) Kubja Vishnuvardhana\nCorrect Answer: (c) Rajaraja Narendra [Explanation: Nannaya Bhatta, the poet laureate of Rajamahendravaram, translated the Adi, Sabha, and Aranya parvas under the patronage of King Rajaraja Narendra (1022–1061 CE).]",
      "Q4. The magnificent Draksharama Bhimeswara Swamy Temple in East Godavari was constructed by which illustrious Eastern Chalukya monarch?\n(a) Kubja Vishnuvardhana\n(b) Chalukya Bhima I\n(c) Jayasimha I\n(d) Gunaga Vijayaditya\nCorrect Answer: (b) Chalukya Bhima I [Explanation: Chalukya Bhima I (892–921 CE) built the colossal two-storeyed Bhimeswara Swamy temples at Draksharama and Samarlakota to commemorate his battlefield victories.]",
      "Q5. Which Eastern Chalukya prince married the Chola princess Ammanga Devi and unified the Eastern Chalukya and Imperial Chola thrones in 1070 CE as Kulottunga Chola I?\n(a) Vimaladitya\n(b) Rajaraja Narendra\n(c) Rajendra Chalukya (Kulottunga I)\n(d) Danarnava\nCorrect Answer: (c) Rajendra Chalukya (Kulottunga I) [Explanation: Son of Rajaraja Narendra and Chola princess Ammanga Devi, Rajendra Chalukya ascended the imperial throne at Gangaikondacholapuram as Kulottunga I in 1070 CE.]"
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

print("Part 1 of Subject 2 generated successfully")
