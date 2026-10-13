import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-HIST-13",
    "filename": "13_early_medieval_south_india_chalukyas_and_rashtrakutas",
    "title": "Early Medieval South India: Badami Chalukyas, Eastern Chalukyas & Rashtrakutas",
    "mapping": "History and Culture of India: Early Medieval South India - Badami Chalukyas (Pulakesin II, Aihole Inscription), Eastern Chalukyas of Vengi, Rashtrakutas (Amoghavarsha, Ellora Kailasa Temple), Tripartite Struggle.",
    "intro": "Between the 6th and 10th centuries CE, the Deccan was dominated by powerful imperial dynasties that bridged North and South Indian cultural traditions. The Badami Chalukyas pioneered Vesara temple architecture in Karnataka; the Eastern Chalukyas anchored Telugu linguistic statehood in coastal Andhra; and the Rashtrakutas emerged as a paramount pan-Indian empire that contested the Tripartite Struggle for Kanauj and excavated the monolithic Kailasanatha rock-cut temple at Ellora.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Kailash_temple_at_ellora.jpg", "caption": "The rock-cut monolithic Kailasanatha Temple (Cave 16) at Ellora, excavated under Rashtrakuta King Krishna I.", "alt": "Kailash Temple at Ellora"},
    "table": {
      "caption": "Dynastic Matrix of Medieval Deccan Hegemons",
      "headers": ["Dynasty & Eras", "Prominent Monarchs & Capital", "Military Feats & Political Reach", "Architecture, Literature & Cultural Legacy"],
      "rows": [
        ["Badami Chalukyas (c. 543–753 CE)", "Pulakesin I, Pulakesin II, Vikramaditya I; Vatapi (Badami).", "Pulakesin II defeated Harsha at Narmada and Kadambas; diplomatic ties with Sasanian Persia.", "Vesara architectural idiom at Badami, Aihole ('Cradle of Indian Temple Architecture' - Lad Khan, Durga Temple), and Pattadakal (Virupaksha Temple - UNESCO site)."],
        ["Eastern Chalukyas (c. 624–1075 CE)", "Kubja Vishnuvardhana, Gunaga Vijayaditya; Vengi & Rajahmundry.", "Defended coastal Andhra against Rashtrakutas; marital alliances with the Cholas leading to the Chalukya-Chola union under Kulottunga I.", "Patronized earliest Telugu literary evolution; Nannaya Bhatta commenced translation of Mahabharata into Telugu at Rajahmundry; constructed Draksharama temple."],
        ["Rashtrakutas (c. 753–982 CE)", "Dantidurga, Krishna I, Amoghavarsha I, Krishna III; Manyakheta (Malkhed).", "Dantidurga performed Hiranyagarbha ritual; fought Tripartite Struggle against Palas and Gurjara-Pratiharas; captured Kanauj.", "Krishna I carved monolithic Kailasa Temple (Cave 16) at Ellora; Amoghavarsha I authored 'Kavirajamarga' (earliest Kannada poetic treatise) and 'Prashnottara Ratnamalika'; Arab traveler Al-Masudi called Rashtrakuta king 'Balhara' (one of the 4 greatest sovereigns of the world)."]
      ]
    },
    "bullets": [
      "Aihole Prashasti: Composed in 634 CE by court poet Ravikirti on the Meguti Jain temple at Aihole; provides authentic poetic account of Pulakesin II's conquests from the eastern coast to the western sea.",
      "Tripartite Struggle for Kanauj: Century-long conflict among the Rashtrakutas of the Deccan, Palas of Bengal (Dharmapala), and Gurjara-Pratiharas of Malwa (Nagabhata II, Mihira Bhoja) to control the agrarian riches and imperial symbol of Kanauj.",
      "Amoghavarsha I (814–878 CE, 'Ashoka of the South'): Devout Jain patron under preceptor Jinasena; ruled for 64 years; built capital Manyakheta; celebrated for his peaceful, non-aggressive reign and philosophical scholarship."
    ],
    "mains": [
      "Analyze the political and cultural contributions of the Rashtrakutas of Manyakheta with special reference to the Tripartite Struggle and the architecture of Ellora. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight Rashtrakuta pan-Indian military expeditions under Dhruva, Govinda III, and Krishna III dominating the Tripartite Struggle; explain Arab accounts (Sulaiman, Al-Masudi) documenting Rashtrakuta military might ('Balhara'); describe the engineering marvel of Kailasanatha temple (Cave 16) at Ellora carved top-down from a single basalt hill cliff; examine Amoghavarsha's patronization of Kannada literature ('Kavirajamarga') and Jain scholarship (Jinasena, Mahaviracharya)."
    ],
    "mcqs": [
      "Q1. The celebrated rock-cut monolithic Kailasanatha Temple (Cave 16) at Ellora was excavated under the royal patronage of which Rashtrakuta monarch?\n(a) Dantidurga\n(b) Krishna I\n(c) Amoghavarsha I\n(d) Govinda III\nCorrect Answer: (b) Krishna I [Explanation: King Krishna I (756–774 CE) commissioned the monolithic rock-cut Kailasanatha temple at Ellora, carved top-down out of a single basalt cliff.]",
      "Q2. The earliest surviving poetic work in the Kannada language, 'Kavirajamarga', is attributed to which illustrious Deccan ruler?\n(a) Pulakesin II\n(b) Amoghavarsha I\n(c) Vishnuvardhana\n(d) Tailapa II\nCorrect Answer: (b) Amoghavarsha I [Explanation: Rashtrakuta Emperor Amoghavarsha I Nrupatunga authored the celebrated 'Kavirajamarga' (c. 850 CE), the foundational treatise on Kannada grammar and poetics.]",
      "Q3. The Aihole Inscription of 634 CE, composed in Sanskrit by court poet Ravikirti, is inscribed on which temple structure at Aihole?\n(a) Lad Khan Temple\n(b) Meguti Jain Temple\n(c) Durga Temple\n(d) Huchimalli Temple\nCorrect Answer: (b) Meguti Jain Temple [Explanation: Ravikirti incised the Aihole Prashasti on the eastern wall of the Meguti Jain temple at Aihole during the reign of Western Chalukya King Pulakesin II.]",
      "Q4. Which 10th-century Arab traveler described the Rashtrakuta king ('Balhara') as one of the four great monarchs of the world alongside the emperors of Rome, China, and Baghdad?\n(a) Al-Masudi\n(b) Al-Biruni\n(c) Ibn Battuta\n(d) Abdur Razzaq\nCorrect Answer: (a) Al-Masudi [Explanation: Arab geographer Al-Masudi visited the Rashtrakuta capital Manyakheta in 915 CE and acclaimed the 'Balhara' (Vallabharaja) as one of the world's four greatest monarchs.]",
      "Q5. Who was the founder of the Eastern Chalukya dynasty of Vengi in coastal Andhra, appointed as viceroy by his elder brother Pulakesin II?\n(a) Vishnuvardhana (Kubja Vishnuvardhana)\n(b) Gunaga Vijayaditya\n(c) Rajaraja Narendra\n(d) Jayasimha I\nCorrect Answer: (a) Vishnuvardhana (Kubja Vishnuvardhana) [Explanation: Kubja Vishnuvardhana was installed as ruler of Vengi around 624 CE by Pulakesin II, founding the Eastern Chalukya dynasty that ruled coastal Andhra for five centuries.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-14",
    "filename": "14_imperial_cholas_administration_and_navy",
    "title": "Imperial Cholas: Administration, Uttaramerur Inscription & Maritime Navy",
    "mapping": "History and Culture of India: Imperial Cholas - Vijayalaya, Rajaraja I, Rajendra I, Local Self-Government (Uttaramerur Inscription), Chola Navy and Maritime Empire, Dravidian Architecture (Brihadisvara Temple) and Chola Bronzes.",
    "intro": "The Imperial Chola dynasty (c. 850–1279 CE), founded by Vijayalaya, established the most sophisticated administrative state and maritime empire in pre-colonial South Asia. Under Rajaraja I and Rajendra I, Chola naval fleets dominated the Indian Ocean, conquered Sri Lanka, and raided the Srivijaya maritime empire in Southeast Asia, while pioneering a democratic village autonomy system documented in the Uttaramerur Inscriptions.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Brihadisvara_Temple_Thanjavur.jpg", "caption": "The Brihadisvara Temple at Thanjavur, built by Rajaraja I in 1010 CE, displaying colossal Dravidian vimana architecture.", "alt": "Brihadisvara Temple vimana tower in Thanjavur"},
    "table": {
      "caption": "Structural Pillars of Chola Imperial Statecraft",
      "headers": ["Governance Dimension", "Institutional Mechanism", "Operational Functions & Historical Features"],
      "rows": [
        ["Central Administration", "King guided by royal decrees (Tirumukham); Perundanam (higher officials) & Sirudanam (lower officials).", "Conducted extensive cadastral land revenue surveys (under Rajaraja I in 1001 CE); revenue collected as Kadamai (1/3rd gross produce)."],
        ["Local Village Autonomy", "Three village assemblies: Ur (general village), Sabha/Mahasabha (Brahmin agrahara villages), Nagaram (merchants).", "Uttaramerur Inscriptions (Parantaka I, 919 & 921 CE) outline Kudavolai (pot-ticket lottery) election system, strict eligibility criteria, and disqualification for financial corruption."],
        ["Village Committees (Variyams)", "Executive committees operating under the Sabha: Samvatsara-variyam (annual council), Eri-variyam (tank committee), Thotta-variyam (garden committee).", "Managed irrigation tanks, collected village taxes, maintained local justice and land dispute resolutions independently."],
        ["Naval Supremacy & Overseas Trade", "Imperial Chola Navy ('Bay of Bengal as a Chola Lake'); merchant guilds (Manigramam, Ayyavole 500, Nanadesi).", "Conquered Anuradhapura (Sri Lanka), Maldives; Rajendra I sent naval expeditions across the Malacca Straits conquering Kedah and Srivijaya (Sumatra/Malaya) in 1025 CE."],
        ["Dravidian Architecture & Bronze Casting", "Brihadisvara Temple (Thanjavur), Gangaikondacholapuram, Airavatesvara Temple (Darasuram).", "Grand Dravidian vimana towers; lost-wax (cire perdue) casting of Nataraja (cosmic dancing Shiva) bronzes recognized as world art masterpieces."]
      ]
    },
    "bullets": [
      "Uttaramerur Inscriptions (919 and 921 CE, Parantaka I): Inscribed on the Vaikuntha Perumal temple; details democratic ward elections across 30 kudumbus (wards); candidates had to own land, possess Vedic learning, be between 35 and 70 years old, and have not served on a committee in the preceding 3 years.",
      "Rajaraja I (985–1014 CE): Built the 216-foot Brihadisvara (Rajarajesvaram) Temple at Thanjavur, crowned with an 80-ton monolithic granite cupola; compiled the Shaivite hymns into 'Tirumurai' through Nambi Andar Nambi.",
      "Rajendra I (1014–1044 CE): Marched armies to the Ganga, assumed title 'Gangaikondachola' and built new capital Gangaikondacholapuram; excavated the vast irrigation reservoir Cholagangam (16 miles long); launched historic trans-oceanic naval war against the Srivijaya Empire.",
      "Chola Bronze Sculptures: Cosmic Nataraja balance of creation (damaru drum), destruction (agni flame), protection (abhaya mudra), and illusion (crushing demon Apasmara Purusha)."
    ],
    "mains": [
      "Critically evaluate the system of local self-government and village autonomy under the Imperial Cholas as illuminated by the Uttaramerur Inscriptions. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the village assemblies (Ur, Sabha, Nagaram); analyze the Uttaramerur epigraphs of Parantaka I: selection of Variyam committee members via the Kudavolai (lottery ticket) method from 30 village wards; assess qualifications: property ownership (at least 1/4th veli of taxable land), educational standards (Vedic learning), age limits, and accountability provisions (mandatory audit of accounts and bar on corrupt relatives); explain functions of specialized committees (Eri-variyam for irrigation tanks); conclude on its status as an ancient precedent for democratic grassroots decentralization."
    ],
    "mcqs": [
      "Q1. The famous Uttaramerur Inscriptions, which provide a detailed constitutional blueprint of village assemblies and committee elections, belong to the reign of:\n(a) Vijayalaya\n(b) Parantaka I\n(c) Rajaraja I\n(d) Rajendra I\nCorrect Answer: (b) Parantaka I [Explanation: The two landmark inscriptions at Uttaramerur in Kanchipuram district were issued in the 12th and 14th regnal years of Chola King Parantaka I (919 and 921 CE).]",
      "Q2. Which Chola monarch assumed the proud title 'Gangaikondachola' (Conqueror of the Ganga) and founded a new imperial capital to commemorate his northern campaign?\n(a) Rajaraja I\n(b) Rajendra I\n(c) Kulottunga I\n(d) Rajadhiraja I\nCorrect Answer: (b) Rajendra I [Explanation: After his victorious military expedition to the banks of the River Ganga defeating Mahipala of Bengal, Rajendra I assumed the title 'Gangaikondachola' and founded Gangaikondacholapuram.]",
      "Q3. In the Chola village administrative machinery, which specialized committee ('Variyam') was specifically entrusted with the maintenance and desiltation of irrigation tanks?\n(a) Samvatsara-variyam\n(b) Eri-variyam\n(c) Thotta-variyam\n(d) Pon-variyam\nCorrect Answer: (b) Eri-variyam [Explanation: The Eri-variyam was the village tank committee responsible for maintaining irrigation reservoirs, water distribution, desilting canals, and repairing bund breaches.]",
      "Q4. The colossal Brihadisvara Temple at Thanjavur, completed in 1010 CE and celebrated for its towering 216-foot Dravidian Vimana, was dedicated to Lord Shiva by:\n(a) Aditya I\n(b) Rajaraja I\n(c) Rajendra Chola I\n(d) Sundara Chola\nCorrect Answer: (b) Rajaraja I [Explanation: Great Chola monarch Rajaraja I commissioned the magnificent Brihadisvara Temple (Peruvudaiyar Kovil) at Thanjavur, a UNESCO World Heritage Great Living Chola Temple.]",
      "Q5. Which famous merchant guild operated as an autonomous trans-oceanic corporate trading network across South India and Southeast Asia during the Chola era?\n(a) Sreni\n(b) Manigramam and Ayyavole 500\n(c) Mahajan\n(d) Gopa\nCorrect Answer: (b) Manigramam and Ayyavole 500 [Explanation: The Manigramam, Ayyavole 500 (Ainurruvar), and Nanadesi merchant corporations commanded extensive maritime networks trading spices, camphor, textiles, and gems across Southeast Asia.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-15",
    "filename": "15_delhi_sultanate_administration_and_reforms",
    "title": "Delhi Sultanate: Administration, Agrarian & Market Reforms",
    "mapping": "History and Culture of India: Delhi Sultanate (1206–1526 CE) - Dynastic Matrix (Mamluk, Khalji, Tughlaq, Sayyid, Lodi), Central Administration, Iqta System, Alauddin Khalji's Market Reforms, Muhammad bin Tughlaq's Experiments.",
    "intro": "The establishment of the Delhi Sultanate in 1206 CE following the victories of Muhammad Ghori inaugurated over three centuries of Turkish-Afghan rule across five successive dynasties: Mamluk/Slave, Khalji, Tughlaq, Sayyid, and Lodi. The Sultanate synthesized Perso-Islamic bureaucratic centralization with indigenous agrarian structures, introduced the Iqta land assignment system, and deployed radical economic controls under Alauddin Khalji.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Qutub_Minar_Delhi.jpg", "caption": "The Qutb Minar complex at Delhi, founded by Qutb-ud-din Aibak and completed by Iltutmish.", "alt": "Qutb Minar minaret in Delhi"},
    "table": {
      "caption": "Evolutionary Innovations Across Major Delhi Sultanate Dynasties",
      "headers": ["Dynasty & Rulers", "Administrative Institutions", "Economic, Agrarian & Market Reforms", "Architectural & Cultural Milestones"],
      "rows": [
        ["Mamluk / Slave (1206–1290 CE)", "Qutb-ud-din Aibak, Iltutmish, Balban; Delhi.", "Iltutmish institutionalized the Iqta system (transferable revenue assignments) and Corp of Forty (Chahalgani); introduced silver Tanka and copper Jital coinage.", "Balban introduced Persian court etiquette: Sijda (prostration), Paibos (kissing monarch's feet), Nauroz festival; doctrine of Divine Kingship (Niyabat-i-Khudai); Qutb Minar foundation."],
        ["Khalji Dynasty (1290–1320 CE)", "Jalaluddin Khalji, Alauddin Khalji; Siri.", "Alauddin Khalji: Military reforms (Dagh / horse-branding, Chehra / descriptive muster rolls, direct cash salary to soldiers).", "Market Regulations: Fixed ceiling prices for food grains, textiles, horses; established 4 regulated markets under Shahna-i-Mandi; Diwan-i-Mustakhraj (arrears revenue department); Alai Darwaza."],
        ["Tughlaq Dynasty (1320–1414 CE)", "Ghiyasuddin, Muhammad bin Tughlaq, Firuz Shah Tughlaq; Tughlaqabad.", "Muhammad bin Tughlaq: 5 radical administrative experiments (Taxation in Doab, Transfer of capital to Daulatabad 1327, Token copper/brass currency 1330, Khurasan expedition, Qarachil expedition); established Diwan-i-Kohi (agriculture ministry).", "Firuz Shah Tughlaq built network of irrigation canals (Yamuna-Sutlej), founded cities (Hissar, Firozabad, Jaunpur); established Diwan-i-Khairat (charity) and Diwan-i-Bandagan (slaves)."],
        ["Sayyid & Lodi (1414–1526 CE)", "Khizr Khan, Bahlul Lodi, Sikandar Lodi, Ibrahim Lodi; Delhi & Agra.", "Sikandar Lodi introduced 'Gaz-i-Sikandari' (32-digit measuring rod for land revenue assessment); founded Agra in 1504.", "Afghan tribal confederacy concept of kingship (Primus inter pares / first among equals); overthrown by Babur at First Battle of Panipat (1526)."]
      ]
    },
    "bullets": [
      "The Iqta System: Sultanate divided empire into Iqtas assigned to military commanders (Iqtadars / Muqtis); responsible for maintaining law and order, raising troops, and remitting surplus revenue (Fawazil) to the central treasury.",
      "Central Administrative Departments: Diwan-i-Wizarat (Finance under Wazir), Diwan-i-Arz (Military under Ariz-i-Mamalik), Diwan-i-Insha (Royal Correspondence under Dabir-i-Khas), Diwan-i-Rasalat (Religious endowments and foreign affairs under Sadr-us-Sudur).",
      "Alauddin Khalji's Agrarian Reforms: First sultan to order measurement of cultivable land (Maha) as basis for tax assessment; fixed state demand at 50% of gross produce (Kharaj); eliminated traditional intermediaries (Khuts, Muqaddams, Chaudharis) from extracting illegal cesses.",
      "Amir Khusrau (1253–1325 CE, 'Tuti-e-Hind'): Court poet of 7 sultans; pioneer of Hindavi, Qawwali, and ghazal forms; invented the Sitar and Tabla; authored 'Khazain-ul-Futuh' and 'Tughlaqnama'."
    ],
    "mains": [
      "Critically evaluate the market control regulations and price-fixation system implemented by Alauddin Khalji. What were the administrative objectives and economic outcomes of these measures? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain military motivation: sustaining a massive standing army on modest salaries to repel Mongol invasions and conquer the Deccan without depleting state reserves; detail mechanisms: price ceilings on grains, cloth, slaves, and livestock; establishment of distinct supervised markets under Shahna-i-Mandi, Diwan-i-Riyasat, and spies (Munhiyans); procurement through government granaries in Doab; evaluate economic impact: effective price stability during wartime but severe hardships for rural peasantry, suppression of merchant profits, and rapid collapse after Alauddin's death."
    ],
    "mcqs": [
      "Q1. Which Delhi Sultan introduced the rigorous military verification practices of 'Dagh' (branding of war horses) and 'Chehra' (descriptive roll of soldiers)?\n(a) Balban\n(b) Alauddin Khalji\n(c) Muhammad bin Tughlaq\n(d) Sikandar Lodi\nCorrect Answer: (b) Alauddin Khalji [Explanation: Alauddin Khalji instituted the Dagh and Chehra systems to eliminate military corruption, ghost soldiers, and substitution of inferior horses in royal muster rolls.]",
      "Q2. The department of agriculture, 'Diwan-i-Amir-Kohi', was established to extend cultivable land through state agricultural loans (Sondhar/Takkavi) by:\n(a) Iltutmish\n(b) Alauddin Khalji\n(c) Muhammad bin Tughlaq\n(d) Firuz Shah Tughlaq\nCorrect Answer: (c) Muhammad bin Tughlaq [Explanation: Muhammad bin Tughlaq founded the Diwan-i-Kohi to promote state-assisted agriculture, crop rotation, and extending land under the plough via agricultural loans.]",
      "Q3. The famous silver coin 'Tanka' and copper coin 'Jital' were standardized and introduced into the currency system of the Delhi Sultanate by:\n(a) Qutb-ud-din Aibak\n(b) Iltutmish\n(c) Balban\n(d) Sher Shah Suri\nCorrect Answer: (b) Iltutmish [Explanation: Shamsuddin Iltutmish introduced pure Arabic coinage into India, standardizing the silver Tanka (175 grains) and copper Jital.]",
      "Q4. Which Sultan of Delhi shifted his imperial capital from Delhi to Devagiri (renamed Daulatabad) in the Deccan in 1327 CE?\n(a) Alauddin Khalji\n(b) Ghiyasuddin Tughlaq\n(c) Muhammad bin Tughlaq\n(d) Bahlul Lodi\nCorrect Answer: (c) Muhammad bin Tughlaq [Explanation: Muhammad bin Tughlaq ordered the capital transfer to Daulatabad to exercise tighter strategic control over the Deccan and South India, causing severe hardship before reversing it.]",
      "Q5. Court poet and musicologist Amir Khusrau, known as the 'Parrot of India' (Tuti-e-Hind), was a devoted spiritual disciple of which renowned Sufi saint?\n(a) Khwaja Muinuddin Chishti\n(b) Hazrat Nizamuddin Auliya\n(c) Bakhtiyar Kaki\n(d) Sheikh Salim Chishti\nCorrect Answer: (b) Hazrat Nizamuddin Auliya [Explanation: Amir Khusrau was the beloved disciple of Chishti master Hazrat Nizamuddin Auliya in Delhi; he died of grief within months of his master's demise in 1325 CE.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-16",
    "filename": "16_vijayanagar_and_bahmani_kingdoms",
    "title": "Vijayanagar Empire: Administration, Nayankara System & Architecture",
    "mapping": "History and Culture of India: Vijayanagar Empire (1336–1646 CE) - Harihara & Bukka, Four Dynasties, Krishnadevaraya, Nayankara and Ayagar Systems, Foreign Travelers, Architecture (Hampi), Battle of Talikota (1565).",
    "intro": "Founded in 1336 CE on the southern banks of the Tungabhadra River by Harihara and Bukka of the Sangama dynasty under the spiritual guidance of sage Vidyaranya, the Vijayanagar Empire stood as the supreme guardian of South Indian culture and autonomy. Reaching its zenith under Krishnadevaraya (1509–1529 CE), it combined military-feudal Nayankara governance with grand temple architectural complexes at Hampi (UNESCO site).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/d/df/Stone_Chariot_Hampi.jpg", "caption": "The iconic Stone Chariot inside the Vittala Temple complex at Hampi, Karnataka.", "alt": "Stone Chariot at Hampi Vittala Temple"},
    "table": {
      "caption": "Dynastic Trajectory & Institutional Matrix of the Vijayanagar State",
      "headers": ["Dynasty & Eras", "Key Monarchs & Capitals", "Political & Military Feats", "Administrative, Literary & Architectural Legacies"],
      "rows": [
        ["Sangama Dynasty (1336–1485 CE)", "Harihara I, Bukka I, Devaraya II; Vijayanagara (Hampi).", "Subdued the Sultanate of Madurai (celebrated in Gangadevi's Sanskrit epic 'Madhuravijayam'); Devaraya II enlisted Turkish archers.", "Visited by Italian traveler Nicolo de' Conti (1420) and Persian envoy Abdur Razzaq (1443); constructed Hazara Rama Temple."],
        ["Saluva Dynasty (1485–1505 CE)", "Saluva Narasimha, Immadi Narasimha.", "Saluva usurpation prevented dynastic collapse; strengthened royal control over western horse-import ports.", "Paved way for the ascension of commander Narasa Nayaka's Tuluva dynasty."],
        ["Tuluva Dynasty (1505–1570 CE)", "Vira Narasimha, Sri Krishnadevaraya (1509–1529 CE), Achyuta Deva Raya, Rama Raya.", "Krishnadevaraya crushed Bahmani sultan, captured Raichur Doab (1520), defeated Gajapatis of Odisha (erected victory pillar at Simhachalam); allied with Portuguese governor Albuquerque for Arabian war horses.", "Golden age of Telugu literature: Krishnadevaraya authored 'Amuktamalyada' and patronized the 'Ashtadiggajas' (Allasani Peddana, Tenali Ramakrishna); built Vittala Temple (musical pillars, Stone Chariot); visited by Duarte Barbosa and Domingo Paes."],
        ["Aravidu Dynasty (1570–1646 CE)", "Tirumala Raya, Venkata II; Penukonda & Chandragiri.", "Founded after catastrophic defeat at the Battle of Talikota (Rakshasi-Tangadi, 1565) against the combined Deccani Sultanates.", "Patronized Carnatic music and Telugu scholarship; granted land at Madraspatnam to the English East India Company in 1639."]
      ]
    },
    "bullets": [
      "Nayankara System: Military-feudal administrative mechanism where military chieftains (Nayakas / Amaranayakas) received territorial estates (Amaram) in exchange for maintaining troops, war horses, and paying annual tribute to the Rayas.",
      "Ayagar System: Traditional village autonomous administration governed by a council of 12 hereditary functionaries (Karnam, Talayari, blacksmith, potter, etc.) remunerated through tax-free village land grants (Manyams).",
      "Vijayanagar Temple Architecture: Grand pillared Mandapas, towering entrance gateways (Raya Gopurams), sculpted monolithic pillars depicting mythical rearing Yali beasts, and dedicated marriage halls (Kalyana Mandapa).",
      "Battle of Talikota (Rakshasi-Tangadi, 23 Jan 1565): Allied Deccani Sultanates (Bijapur, Golconda, Ahmadnagar, Bidar) routed the Vijayanagar army under regent Aliya Rama Raya, leading to the sacking and abandonment of Hampi."
    ],
    "mains": [
      "Critically evaluate the political, economic, and military functioning of the Nayankara system in the Vijayanagar Empire. How did it compare with the contemporary Sultanate Iqta system? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the Nayankara system as recorded by Portuguese chroniclers Domingo Paes and Fernao Nuniz; explain the rights and obligations of Amaranayakas: maintaining specified quotas of cavalry, infantry, and war elephants, remitting 1/3rd revenue to royal treasury, and executing public works; contrast with the Sultanate Iqta: Amaram territories were military tenures with deep local roots and hereditary tendencies that weakened central control, whereas Iqtas were frequently transferred non-hereditary revenue assignments; assess how the growing autonomy of Nayakas eventually fragmented the empire post-Talikota."
    ],
    "mcqs": [
      "Q1. Which Vijayanagar emperor authored the celebrated Telugu epic poem 'Amuktamalyada' (detailing the life of Tamil Alvar saint Andal) and the Sanskrit play 'Jambavati Kalyanam'?\n(a) Devaraya II\n(b) Sri Krishnadevaraya\n(c) Bukka I\n(d) Rama Raya\nCorrect Answer: (b) Sri Krishnadevaraya [Explanation: Sri Krishnadevaraya was a versatile scholar-monarch who composed 'Amuktamalyada' (one of the 5 great Telugu mahakavyas) and 'Jambavati Kalyanam' in Sanskrit.]",
      "Q2. The catastrophic Battle of Talikota (Rakshasi-Tangadi), which resulted in the destruction and sacking of Vijayanagara, took place in which year?\n(a) 1526 CE\n(b) 1556 CE\n(c) 1565 CE\n(d) 1576 CE\nCorrect Answer: (c) 1565 CE [Explanation: On 23 January 1565, the combined armies of the Deccani Sultanates defeated Vijayanagar under regent Aliya Rama Raya at the Battle of Talikota (Rakshasi-Tangadi).]",
      "Q3. Who among the 'Ashtadiggajas' (eight literary gems in Krishnadevaraya's court) was honoured with the title 'Andhra Kavita Pitamaha' for his masterpiece 'Manucharitra'?\n(a) Allasani Peddana\n(b) Nandi Timmana\n(c) Tenali Ramakrishna\n(d) Dhurjati\nCorrect Answer: (a) Allasani Peddana [Explanation: Allasani Peddana, poet laureate of Krishnadevaraya's court, composed 'Svarochisha Manu Sambhavamu' (Manucharitra) and was acclaimed as 'Andhra Kavita Pitamaha'.]",
      "Q4. Persian ambassador Abdur Razzaq, who left an awe-inspired eyewitness account stating 'the eye has not seen, nor ear heard of any place to equal Vijayanagara', visited the court of which king in 1443 CE?\n(a) Harihara II\n(b) Devaraya II\n(c) Krishnadevaraya\n(d) Saluva Narasimha\nCorrect Answer: (b) Devaraya II [Explanation: Abdur Razzaq, envoy of Shah Rukh of Persia, visited Vijayanagara in 1443 CE during the reign of Sangama monarch Devaraya II (Gajabetekara).]",
      "Q5. In the Vijayanagar village administration, what was the hereditary system of twelve village functionaries remunerated through tax-free service land called?\n(a) Nayankara System\n(b) Ayagar System\n(c) Poligar System\n(d) Watandar System\nCorrect Answer: (b) Ayagar System [Explanation: The Ayagar system was the traditional village council of 12 hereditary officials (including headman, accountant, watchman) who administered rural justice and collected local dues.]"
    ]
  }
]

for t in topics:
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "History and Culture of India",
    "paper": "Paper-II (Mains Section A) & Paper-I (Screening Section A)",
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

print("Part 3 of Subject 1 generated successfully")
