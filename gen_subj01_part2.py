import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-HIST-06",
    "filename": "06_post_mauryan_foreign_invasions",
    "title": "Post-Mauryan Invasions: Indo-Greeks, Sakas & Parthians",
    "mapping": "History and Culture of India: Post-Mauryan Period - Foreign Invasions (Indo-Greeks, Scythians/Sakas, Parthians), Political Trajectory, Numismatics, Art and Cross-Cultural Synthesis.",
    "intro": "The disintegration of the Mauryan Empire around 185 BCE left northwestern India exposed to successive waves of foreign incursions from Central Asia and Bactria. Indo-Greeks, Scythians (Sakas), and Indo-Parthians introduced Hellenistic artistic idioms, standardized portrait gold and silver coinage, astronomy, and the Gandhara school of Buddhist iconography.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Menander_coin.jpg", "caption": "Silver drachm of Indo-Greek King Menander I (Milinda) featuring bilingual Greek and Kharosthi legends.", "alt": "Indo-Greek silver coin of Menander"},
    "table": {
      "caption": "Dynastic Profile of Post-Mauryan Invading Powers",
      "headers": ["Invading Dynasty", "Key Monarchs & Capitals", "Numismatic & Inscriptional Legacy", "Cultural & Religious Synthesis"],
      "rows": [
        ["Indo-Greeks (Bactrian Greeks)", "Demetrius I, Menander I (Milinda); Sakala (Sialkot).", "First rulers to issue die-struck gold coins with royal portraits and bilingual legends (Greek & Kharosthi).", "Menander embraced Buddhism after theological dialogue with monk Nagasena, immortalized in the Pali classic 'Milindapanha'."],
        ["Scythians / Sakas (Western Kshatrapas)", "Maues, Chashtana, Rudradaman I; Ujjain & Junagadh.", "Junagadh Rock Inscription (150 CE) in pure classical Sanskrit; issued dated silver coins.", "Rudradaman I repaired the Sudarshana lake dam without levying emergency taxes (Vishti); patronized Sanskrit kavya."],
        ["Indo-Parthians (Pahlavas)", "Gondophares (c. 19–46 CE); Taxila.", "Takht-i-Bahi inscription in Mardan; issued copper and billon coinage.", "Christian traditions record the arrival of Apostle St. Thomas in northwestern India during Gondophares' reign."]
      ]
    },
    "bullets": [
      "Indo-Greek Innovations: Introduced curtains into Indian theatre (named 'Yavanika' after Yavanas/Greeks); popularized planetary horoscopy and astronomy ('Gargi Samhita' states: 'The Greeks are barbarians, but the science of astronomy originated with them and for this they must be reverenced as gods').",
      "Western Kshatrapas (Kaharata & Kardamaka): Ruled Gujarat, Malwa, and northern Maharashtra; prolonged warfare with the Satavahanas for control of lucrative Konkan ports (Bharuch/Barygaza, Sopara).",
      "Sudarshana Lake Reservoir History: Originally excavated under Chandragupta Maurya (Pushyagupta), conduits added under Ashoka (Tushaspha), repaired by Saka king Rudradaman I (Suvisakha) in 150 CE, and repaired again by Gupta king Skandagupta (Chakrapalita) in 456 CE."
    ],
    "mains": [
      "Examine the cultural, numismatic, and scientific consequences of Indo-Greek and Saka rule in northwestern India. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight numismatic revolution: die-struck coins with royal portraits, titles, and bilingual scripts replacing crude punch-marked coins; trace birth of Gandhara art combining Greek realism with Buddhist spirituality; assess scientific transfer in astronomy (Paulisa and Romaka Siddhantas) and theatrical terminology (Yavanika); analyze Rudradaman's Junagadh inscription as milestone in classical Sanskrit epigraphy."
    ],
    "mcqs": [
      "Q1. The famous philosophical dialogue between Buddhist monk Nagasena and the Indo-Greek king Menander is preserved in which Pali text?\n(a) Mahavamsa\n(b) Dipavamsa\n(c) Milindapanha\n(d) Divyavadana\nCorrect Answer: (c) Milindapanha [Explanation: 'Milindapanha' (Questions of King Milinda) records the philosophical debate between Menander I and Nagasena, leading to Menander's conversion to Buddhism.]",
      "Q2. The earliest major royal inscription composed entirely in chaste, refined classical Sanskrit prose without Prakritisms is:\n(a) Hathigumpha Inscription of Kharavela\n(b) Junagadh Inscription of Rudradaman I\n(c) Allahabad Pillar Inscription of Samudragupta\n(d) Aihole Inscription of Pulakesin II\nCorrect Answer: (b) Junagadh Inscription of Rudradaman I [Explanation: Dated to c. 150 CE, the Junagadh rock inscription of Saka Mahakshatrapa Rudradaman I is the celebrated pioneer of classical Sanskrit epigraphic literature.]",
      "Q3. According to early Christian church traditions, which Apostle arrived in northwestern India during the reign of Indo-Parthian King Gondophares?\n(a) St. Peter\n(b) St. Thomas\n(c) St. Paul\n(d) St. Bartholomew\nCorrect Answer: (b) St. Thomas [Explanation: Apocryphal Acts of Thomas records that Apostle Thomas visited the court of Gondophares in Taxila around 40 CE before traveling to the Malabar coast.]",
      "Q4. Which term was adopted in ancient Indian Sanskrit drama for the stage curtain, reflecting Hellenistic theatrical influence?\n(a) Yavanika\n(b) Sutradhara\n(c) Nataka\n(d) Vidushaka\nCorrect Answer: (a) Yavanika [Explanation: The Sanskrit theatrical curtain was termed 'Yavanika' (derived from 'Yavana', meaning Ionian Greek), denoting Greek theatrical mechanical influence.]",
      "Q5. Which Saka ruler was decisively defeated and killed by Satavahana monarch Gautamiputra Satakarni, as recorded in the Nashik Cave Inscription?\n(a) Chashtana\n(b) Nahapana\n(c) Rudradaman I\n(d) Bhumaka\nCorrect Answer: (b) Nahapana [Explanation: Gautamiputra Satakarni exterminated the Kshaharata dynasty by killing Nahapana and counter-striking thousands of his silver coins, as discovered at the Jogalthambi hoard.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-07",
    "filename": "07_kushan_empire_and_kanishka",
    "title": "The Kushan Empire: Kanishka, Silk Route, Gandhara & Mathura Art",
    "mapping": "History and Culture of India: The Kushans - Kujula Kadphises, Kanishka I, Saka Era (78 CE), Fourth Buddhist Council, Trans-Eurasian Trade, Gandhara and Mathura Art.",
    "intro": "Originating from the Yuezhi nomadic confederation of Central Asia, the Kushans established a trans-continental empire straddling the Oxus and the Ganga (Uzbekistan, Afghanistan, Pakistan, and Northern India). Reaching its zenith under Kanishka I (78 CE), the empire linked the Silk Route trade networks of Rome and Han China, fostered Mahayana Buddhism, and patronized the twin sculptural traditions of Gandhara and Mathura.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Kanishka_coin.jpg", "caption": "Gold dinar of Emperor Kanishka I depicting the standing monarch on the obverse and Buddha ('BODDO') on the reverse.", "alt": "Kanishka gold coin with Buddha image"},
    "table": {
      "caption": "Artistic Dichotomy: Gandhara School vs Mathura School of Art",
      "headers": ["Artistic Attribute", "Gandhara School of Art", "Mathura School of Art"],
      "rows": [
        ["Geographical Centre", "Northwest frontier (Taxila, Peshawar, Swat, Hadda, Bamiyan).", "Yamuna valley (Mathura, Sonkh, Kankali Tila)."],
        ["Medium & Material", "Grey schist sandstone, stucco, clay, terracotta.", "Indigenous spotted red sandstone (Sikri sandstone)."],
        ["Stylistic Influences", "Greco-Roman / Hellenistic realism; wavy hair curls, Apollo-like facial anatomy, heavy drapery folds.", "Purely indigenous Indian aesthetic; fleshy smiling features, transparent thin drapery, spiritual prabhavali (halo)."],
        ["Religious Scope", "Exclusively Buddhist (Buddha, Bodhisattvas like Maitreya, Avalokiteshvara).", "Pluralistic: Buddhism, Jainism (Ayagapatas / votive tablets, Tirthankaras), and Brahmanical deities (Shiva Linga, Vishnu, Kartikeya)."],
        ["Royal Patronage", "Kushans, Saka-Parthians, post-Kushan local chieftains.", "Kushans and later Guptas; established the iconic canonical seated Buddha prototype."]
      ]
    },
    "bullets": [
      "Kanishka I (78 CE): Inaugurated the Saka Era (official civil calendar of modern India); established twin capitals at Purushapura (Peshawar) and Mathura; erected a 400-foot multi-tiered wooden stupa at Shah-ji-ki-Dheri.",
      "Fourth Buddhist Council (Kundalvana, Kashmir): Presided over by Vasumitra and Ashvaghosha; compiled the 'Mahavibhasha Sastra'; formalized the doctrinal schism between Theravada/Hinayana and Mahayana (worship of Buddha as a divine saviour through idol worship).",
      "Court Luminaries: Ashvaghosha (authored 'Buddhacharita' and 'Saundarananda'), Vasumitra, Charaka (court physician, 'Charaka Samhita'), and Nagarjuna (philosopher of Madhyamaka / Sunyavada).",
      "Silk Route Trade & Numismatics: Controlled northern trans-Asian overland arteries; issued the purest gold dinars and heavy copper coins matching Roman imperial standards; received Roman gold for Indian spices, silk, and gems."
    ],
    "mains": [
      "Analyze the role of the Kushan Empire in facilitating trans-Eurasian trade and catalyzing the spread of Mahayana Buddhism along the Silk Route. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Map Kushan strategic geography commanding the Khyber Pass and Silk Route junctions; evaluate gold coinage matching Roman standards that lubricated global trade; explain Kanishka's sponsorship of the Fourth Buddhist Council in Kashmir; demonstrate how Buddhist monasteries along caravan nodes (Taxila, Bamiyan, Dunhuang) operated as banking and cultural conduits diffusing Mahayana art and texts into Central Asia and China."
    ],
    "mcqs": [
      "Q1. The Indian National Calendar, adopted by the Government of India in 1957, is based on the historic Saka Era founded in which year?\n(a) 57 BCE\n(b) 78 CE\n(c) 319 CE\n(d) 248 CE\nCorrect Answer: (b) 78 CE [Explanation: The Saka Era, commencing in 78 CE with the accession of Kushan Emperor Kanishka I, forms the basis of the official National Civil Calendar of India.]",
      "Q2. Who served as the Vice-President of the Fourth Buddhist Council held in Kashmir and authored the celebrated classical Sanskrit epic 'Buddhacharita'?\n(a) Vasumitra\n(b) Ashvaghosha\n(c) Nagarjuna\n(d) Asanga\nCorrect Answer: (b) Ashvaghosha [Explanation: Ashvaghosha, court poet of Kanishka, was the vice-president of the council and authored 'Buddhacharita' (the earliest complete biography of the Buddha in Sanskrit) and 'Saundarananda'.]",
      "Q3. The medium predominantly used by sculptors of the Gandhara School of Art to carve realistic Buddhist sculptures was:\n(a) Spotted red sandstone\n(b) Grey schist and stucco\n(c) White marble\n(d) Monolithic granite\nCorrect Answer: (b) Grey schist and stucco [Explanation: The Gandhara artists utilized local grey/bluish schist stone and stucco (plaster) to render Buddha images imbued with Greco-Roman realistic drapery and Apollo-like countenances.]",
      "Q4. Which celebrated ancient physician, regarded as the founding father of Indian internal medicine (Kayachikitsa), served as the royal court physician of Kanishka?\n(a) Sushruta\n(b) Charaka\n(c) Vagbhata\n(d) Dhanvantari\nCorrect Answer: (b) Charaka [Explanation: Charaka, author of the foundational Ayurvedic compendium 'Charaka Samhita', flourished under Kushan patronage in Kanishka's court.]",
      "Q5. Which Buddhist philosopher pioneered the Madhyamaka (Middle Way) school and the doctrine of 'Sunyavada' (Emptiness) under Kushan patronage?\n(a) Dignaga\n(b) Dharmakirti\n(c) Nagarjuna\n(d) Vasubandhu\nCorrect Answer: (c) Nagarjuna [Explanation: Acharya Nagarjuna developed the Madhyamaka philosophy and Sunyata doctrine in his treatise 'Mulamadhyamakakarika', active during the late Kushan-Satavahana transition.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-08",
    "filename": "08_sungas_kanvas_and_chedis",
    "title": "Post-Mauryan Indigenous Dynasties: Sungas, Kanvas & Chedis",
    "mapping": "History and Culture of India: Post-Mauryan Indigenous Rulers - Sunga Dynasty (Pushyamitra Sunga), Kanva Dynasty, Chedis of Kalinga (Kharavela and Hathigumpha Inscription).",
    "intro": "Following the assassination of the last Mauryan ruler Brihadratha in 185 BCE by his commander-in-chief Pushyamitra Sunga, indigenous Brahminical dynasties reasserted authority in northern and central India. The Sungas and Kanvas revived Vedic sacrificial rites while generously patronizing Buddhist art at Bharhut and Sanchi, while the Chedi dynasty of Kalinga reached imperial zenith under Emperor Kharavela.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/5/53/Bharhut_Stupa_railings.jpg", "caption": "Sculpted stone railing from the Bharhut Stupa (Sunga period), currently preserved at the Indian Museum, Kolkata.", "alt": "Bharhut Stupa carved stone railing panels"},
    "table": {
      "caption": "Comparative Framework of Indigenous Post-Mauryan Dynasties",
      "headers": ["Dynastic House", "Founders & Prominent Rulers", "Political & Military Feats", "Artistic, Religious & Epigraphic Legacy"],
      "rows": [
        ["Sunga Dynasty (c. 185–73 BCE)", "Pushyamitra Sunga, Agnimitra, Bhagabhadra; Pataliputra & Vidisha.", "Repelled Indo-Greek invasions led by Demetrius/Menander; performed two Ashvamedha sacrifices; revived Vedic rituals.", "Patanjali authored 'Mahabhasya'; Agnimitra celebrated in Kalidasa's 'Malavikagnimitram'; Heliodorus Garuda Pillar at Vidisha; embellished Bharhut Stupa."],
        ["Kanva Dynasty (c. 73–28 BCE)", "Vasudeva Kanva, Susarman; Pataliputra.", "Overthrew the decadent Sunga ruler Devabhuti; brief 45-year rule over Magadha.", "Maintained orthodox Brahminical administrative court until overthrown by the Deccan Satavahanas (Andhrabhrityas)."],
        ["Chedi Dynasty of Kalinga (c. 1st Century BCE)", "Mahameghavahana, Kharavela; Kalinganagara.", "Conquered Magadha (retrieved Jina image stolen by Nandas), subdued Satavahana king Satakarni, routed Tamil confederacy.", "Hathigumpha 17-line biographical inscription in Udayagiri; excavated rock-cut Jain caves at Udayagiri and Khandagiri (Rani Gumpha, Hathi Gumpha)."]
      ]
    },
    "bullets": [
      "Pushyamitra Sunga & Buddhist Historiography: Early Buddhist texts (Divyavadana) portray Pushyamitra as a persecutor of monks, but archaeological evidence at Bharhut and Sanchi proves substantial royal and merchant patronage of stupa railings and gateways during the Sunga era.",
      "Besnagar Heliodorus Pillar: Greek ambassador Heliodorus (sent by Indo-Greek king Antialcidas to Sunga king Bhagabhadra) erected a monolithic stone Garuda pillar at Vidisha, identifying himself as a 'Bhagavata' (devotee of Vasudeva-Krishna).",
      "Hathigumpha Inscription: 17-line Prakrit Brahmi inscription of Kharavela recording his year-by-year military campaigns, irrigation repairs of canal dug by King Nanda 300 years prior, musical expertise, and building of Jain residential caves for monks."
    ],
    "mains": [
      "Critically evaluate the political achievements, religious leanings, and historical significance of Emperor Kharavela as documented in the Hathigumpha Inscription. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Introduce Kharavela as the third ruler of the Mahameghavahana Chedi dynasty of Kalinga; summarize his chronological feats from Hathigumpha: military expeditions reaching Magadha (defeating Bahasatimita), retrieval of the Kalinga Jina, repairs of ancient irrigation canals, and routing of southern kingdoms; evaluate his devout patronage of Jainism alongside claims of universal religious tolerance ('Sarva Pasanda Pujaka'); emphasize the inscription's value as a rare biographical epigraphic timeline."
    ],
    "mcqs": [
      "Q1. Which Sunga commander-in-chief assassinated the last Mauryan ruler Brihadratha during an army parade in 185 BCE to establish the Sunga dynasty?\n(a) Agnimitra\n(b) Pushyamitra Sunga\n(c) Vasumitra\n(d) Bhagabhadra\nCorrect Answer: (b) Pushyamitra Sunga [Explanation: Pushyamitra Sunga, the Senapati (commander) of Brihadratha, executed a coup d'état during a military review in 185 BCE, founding the Sunga dynasty.]",
      "Q2. The famous monolithic stone pillar at Besnagar (Vidisha) with a Garuda capital was dedicated to Lord Vasudeva by which Greek ambassador?\n(a) Megasthenes\n(b) Deimachus\n(c) Heliodorus\n(d) Dionysius\nCorrect Answer: (c) Heliodorus [Explanation: Heliodorus, an envoy from Taxila sent by Indo-Greek King Antialcidas to Sunga King Bhagabhadra, erected the Besnagar pillar and declared himself a 'Bhagavata' (Vaishnavite).]",
      "Q3. The 17-line biographical Hathigumpha Inscription of King Kharavela is incised on the southern face of which hill near Bhubaneswar?\n(a) Dhauli Hills\n(b) Udayagiri Hills\n(c) Khandagiri Hills\n(d) Barabar Hills\nCorrect Answer: (b) Udayagiri Hills [Explanation: The Hathigumpha (Elephant Cave) inscription is located in the Udayagiri Hills near Bhubaneswar, Odisha, carved in the Brahmi script.]",
      "Q4. Which famous Sanskrit grammatical treatise was composed by sage Patanjali during the reign of Pushyamitra Sunga?\n(a) Ashtadhyayi\n(b) Mahabhasya\n(c) Siddhanta Kaumudi\n(d) Nirukta\nCorrect Answer: (b) Mahabhasya [Explanation: Patanjali composed the 'Mahabhasya' (a comprehensive commentary on Panini's Ashtadhyayi) during Pushyamitra Sunga's reign and participated in his Ashvamedha sacrifices.]",
      "Q5. Which play composed by celebrated dramatist Kalidasa is based on the romantic court intrigue between Sunga prince Agnimitra and Malavika?\n(a) Abhijnanasakuntalam\n(b) Vikramorvasiyam\n(c) Malavikagnimitram\n(d) Mudrarakshasa\nCorrect Answer: (c) Malavikagnimitram [Explanation: 'Malavikagnimitram' by Kalidasa dramatizes the love story of Sunga king Agnimitra and Malavika, offering historical glimpses of Sunga-Yavana conflicts.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-09",
    "filename": "09_satavahana_empire",
    "title": "The Satavahana Empire: Polity, Society, Trade & Amaravati Art",
    "mapping": "History and Culture of India: The Satavahanas (Andhrabhrityas) - Political History, Gautamiputra Satakarni, Administration, Royal Land Grants, Amaravati School of Art, Society and Maritime Commerce.",
    "intro": "The Satavahanas (known as Andhras in the Puranas) held sway over the Deccan plateau (Maharashtra, Andhra Pradesh, and northern Karnataka) for over four centuries (c. 1st Century BCE to 3rd Century CE). Founded by Simuka with capitals at Pratishthana (Paithan) and Dhanyakataka (Amaravati), the Satavahanas pioneered royal land grants (Agraharas), built rock-cut Buddhist chaityas across the Western Ghats, and fostered Indian Ocean maritime commerce.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Amaravati_Stupa_Relief.jpg", "caption": "Marble relief medallion from the Amaravati Maha Stupa depicting the Buddha's miraculous parinirvana.", "alt": "Carved white marble panel from Amaravati Stupa"},
    "table": {
      "caption": "Imperial Milestones of Eminent Satavahana Sovereigns",
      "headers": ["Monarch", "Dynastic Standing & Reign", "Key Inscriptions & Numismatics", "Historical Accomplishments"],
      "rows": [
        ["Simuka", "Founder (c. 1st Century BCE)", "Coins excavated at Kotilingala (Telangana).", "Overthrew the declining Kanva and Sunga remnants in Central India."],
        ["Satakarni I", "3rd King, Great Conqueror", "Nanaghat Inscription of Queen Nayanika.", "Assumed titles 'Dakshinapathapati' and 'Apratihatachakra'; performed two Ashvamedhas and one Rajasuya; earliest record of tax-free land gifts to priests."],
        ["Hala", "17th King, Literary Patron", "Prakrit anthology 'Gathasaptasati' (Gaha Sattasai).", "Golden era of vernacular Maharashtri Prakrit literature; composed 700 rural, erotic, and lyrical poems."],
        ["Gautamiputra Satakarni", "23rd King (c. 106–130 CE), Greatest Monarch", "Nashik Prashasti of Queen Mother Gautami Balasri.", "Defeated Saka king Nahapana (Jogalthambi coin hoard); assumed titles 'Ekabrahmana' and 'Trisamudratoyapitavahana' (one whose horses drank waters of three seas)."],
        ["Yajna Sri Satakarni", "Last Great Monarch (c. 165–194 CE)", "Ship-motif lead and potin coins excavated along coastal Andhra and Coromandel.", "Revived maritime supremacy in the Bay of Bengal; extensive Indian Ocean trade with the Roman Empire."]
      ]
    },
    "bullets": [
      "Royal Land Grants (Agrahara System): Satavahanas were the first dynasty in Indian history to issue epigraphically recorded tax-free land grants with administrative immunities (Pariharas) to Buddhist monks and Brahmins, sowing seeds of feudalism.",
      "Amaravati School of Art: Flourished in lower Krishna-Godavari valley (Amaravati, Nagarjunakonda, Bhattiprolu); characterized by use of white Palnadu limestone (marble), dynamic narrative relief panels, and depicting human emotions in assemblies.",
      "Administration & Social Life: Provinces called Aharas governed by Amatyas; military governors called Gaulmikas; matrilineal metronymics (naming after mothers: Gautamiputra, Vashishtiputra) combined with strictly patrilineal throne succession.",
      "Rock-Cut Architecture in Western Deccan: Excavated magnificent chaitya-grihas and viharas at Karle (largest rock-cut chaitya), Bhaja, Bedsa, Kanheri, and Nashik."
    ],
    "mains": [
      "Analyze the administrative structure, agrarian innovations, and maritime commercial expansion of the Satavahana Empire in peninsular India. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the administrative division into Aharas, Gramas, and rural Gaulmika garrisons; explain the historic introduction of tax-free royal land grants (Agraharas) to Brahmins and Buddhist monasteries creating autonomous agrarian pockets; evaluate maritime commerce via ports like Barygaza, Kalyan, Sopara, and Motupalli supported by Yajna Sri Satakarni's ship-motif coins; discuss exports of Muslin, spices, and beads against Roman gold dinars."
    ],
    "mcqs": [
      "Q1. Which famous Satavahana queen mother issued the Nashik Prashasti inscription eulogizing the military victories and virtues of her son Gautamiputra Satakarni?\n(a) Nayanika\n(b) Gautami Balasri\n(c) Rudradharani\n(d) Samgharakkhita\nCorrect Answer: (b) Gautami Balasri [Explanation: Gautami Balasri recorded the celebrated Nashik Cave Prashasti in the 19th regnal year of her grandson Pulumavi II, commemorating Gautamiputra Satakarni as 'Ekabrahmana'.]",
      "Q2. The earliest epigraphic evidence in Indian history recording the grant of tax-free land to religious beneficiaries is found in which inscription?\n(a) Hathigumpha Inscription\n(b) Nanaghat Inscription of Queen Nayanika\n(c) Junagadh Inscription\n(d) Eran Inscription\nCorrect Answer: (b) Nanaghat Inscription of Queen Nayanika [Explanation: The Nanaghat cave inscription of Queen Nayanika (wife of Satakarni I) contains the earliest epigraphically documented grant of land and villages to Vedic priests.]",
      "Q3. The famous Prakrit romantic poetic anthology 'Gathasaptasati' (700 stanzas) was compiled by which Satavahana monarch?\n(a) Simuka\n(b) Hala\n(c) Pulumavi I\n(d) Satakarni II\nCorrect Answer: (b) Hala [Explanation: King Hala (the 17th Satavahana ruler) composed the 'Gathasaptasati' (Gaha Sattasai) in Maharashtri Prakrit, providing rich insights into ancient Deccan rural society.]",
      "Q4. Which distinctive stone was predominantly utilized by sculptors of the ancient Amaravati School of Art in Andhra Pradesh?\n(a) Grey schist\n(b) White marble-like limestone\n(c) Red sandstone\n(d) Black basalt\nCorrect Answer: (b) White marble-like limestone [Explanation: The Amaravati School of Art made exclusive use of white/greenish Palnadu limestone (often called Amaravati marble) to carve intricate Buddhist narrative reliefs.]",
      "Q5. Which Satavahana monarch issued unique copper and lead coins stamped with the symbol of a two-masted ship, reflecting trans-oceanic maritime trade?\n(a) Gautamiputra Satakarni\n(b) Vashishtiputra Pulumavi\n(c) Yajna Sri Satakarni\n(d) Kuntala Satakarni\nCorrect Answer: (c) Yajna Sri Satakarni [Explanation: Yajna Sri Satakarni issued coins bearing two-masted seafaring ship designs, demonstrating Satavahana naval power and flourishing Bay of Bengal maritime commerce.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-10",
    "filename": "10_sangam_age_in_south_india",
    "title": "The Sangam Age: Polity, Society, Trade & Classical Tamil Literature",
    "mapping": "History and Culture of India: Sangam Age in South India - Sangam Assemblies, Classical Literature (Ettuthokai, Pattupattu, Tolkappiyam, Epics), Muvendar Kingdoms, Social Ecology (Five Thinais) and Roman Trade.",
    "intro": "The Sangam Age (c. 3rd Century BCE to 3rd Century CE) represents the classical literary and state-formation epoch of ancient Tamilakam (modern Tamil Nadu and Kerala). Named after the literary academies ('Sangams') held under the royal patronage of the Pandyas at Madurai, the era was characterized by the 'Muvendar' (Cheras, Cholas, Pandyas), an ecological taxonomy of five landscapes (Aintinai), and intense maritime commerce with the Roman Empire.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Kallanai_Dam_Grand_Anicut.jpg", "caption": "The Kallanai (Grand Anicut) on the Kaveri River, built by Chola King Karikala in the 2nd century CE.", "alt": "Ancient stone barrage of Kallanai Dam"},
    "table": {
      "caption": "The Five Ecological Landscapes (Aintinai) of Tamilakam",
      "headers": ["Thinai (Landscape)", "Geographical Ecology", "Primary Deity", "Economic Occupation", "Inhabitants / Tribe"],
      "rows": [
        ["Kurinji", "Hilly / Mountainous forests", "Murugan (Seyon)", "Hunting and honey collection", "Kanavar, Kuravar"],
        ["Mullai", "Pastoral scrublands & grasslands", "Mayon (Vishnu / Krishna)", "Cattle-rearing and dairy farming", "Ayars, Idaiyars"],
        ["Marudham", "Fertile river valleys & plains", "Vendan (Indra)", "Paddy agriculture and irrigation", "Ulavar, Vellalar"],
        ["Neydhal", "Coastal seashore & lagoons", "Varunan (Kadal-on)", "Fishing and salt manufacturing", "Paratavar, Meenavar"],
        ["Palai", "Arid / Parched wasteland", "Korravai (Goddess of War)", "Highway robbery and cattle raiding", "Maravar, Eyinar"]
      ]
    },
    "bullets": [
      "The Three Royal Houses (Muvendar): Cheras (emblem: Bow; port: Muziris; capital: Vanji; ruler: Senguttuvan who introduced Pattini/Kannagi cult); Cholas (emblem: Tiger; port: Puhar/Kaveripattinam; capital: Uraiyur; ruler: Karikala who built Kallanai dam); Pandyas (emblem: Fish; port: Korkai; capital: Madurai; famous for pearl fisheries and patronizing the Sangams).",
      "Sangam Literary Corpus: Tolkappiyam (author: Tolkappiyar, earliest grammar and poetics); Pathinenmelkanakku: Ettuthokai (8 anthologies including Agananuru and Purananuru) and Pattupattu (10 idylls); Pathinenkilkanakku (18 ethical works including Tiruvalluvar's Tirukkural).",
      "Twin Tamil Epics: Silappadikaram ('The Tale of an Anklet' by Ilango Adigal, story of Kovalan, Kannagi, and Madhavi) and Manimekalai (by Sattanar, Buddhist sequel detailing the life of Kovalan's daughter).",
      "Maritime Commerce with Rome: Periplus of the Erythraean Sea and Pliny's Natural History document trade through Muziris and Arikamedu; exports: black pepper ('Yavanapriya'), beryl, pearls, ivory, fine cotton; imports: Roman gold/silver denarii, Arretine pottery, amphorae wine."
    ],
    "mains": [
      "Elucidate the socio-economic structure and maritime trade of ancient Tamilakam as illuminated by Sangam literature and Greco-Roman classical accounts. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Describe the five-fold ecological classification (Thinai) connecting geography to occupation and deity; explain the Muvendar administrative chieftains and agrarian wealth (Kaveri delta under Karikala); detail overseas trade through ports like Muziris, Arikamedu, and Korkai exporting black pepper ('Yavanapriya') and pearls; cite Roman historian Pliny lamenting the massive gold drain of 50 million sesterces annually to India; discuss archaeological findings of Roman amphorae and coin hoards across peninsular India."
    ],
    "mcqs": [
      "Q1. Which ancient Tamil treatise is the earliest surviving work on Tamil grammar, rhetoric, and social conventions of the Sangam Age?\n(a) Tirukkural\n(b) Tolkappiyam\n(c) Silappadikaram\n(d) Manimekalai\nCorrect Answer: (b) Tolkappiyam [Explanation: Authored by Tolkappiyar, the 'Tolkappiyam' is the foundational work of classical Tamil literature, covering phonology, syntax, and poetic conventions.]",
      "Q2. The Chera monarch Cheran Senguttuvan is celebrated in the epic 'Silappadikaram' for introducing which religious cult in Tamil society?\n(a) Murugan Cult\n(b) Pattini (Kannagi) Cult\n(c) Bhagavata Cult\n(d) Korravai Cult\nCorrect Answer: (b) Pattini (Kannagi) Cult [Explanation: Senguttuvan founded the Pattini cult (veneration of Kannagi as the ideal chaste woman), bringing a stone from the Himalayas to carve her idol.]",
      "Q3. In Sangam poetry, what was the term used by merchants and writers to describe black pepper due to its intense demand among Roman and Greek traders?\n(a) Karpu\n(b) Yavanapriya\n(c) Yavanasura\n(d) Marakkar\nCorrect Answer: (b) Yavanapriya [Explanation: Black pepper from Kerala was known as 'Yavanapriya' (beloved of the Yavanas/Greeks/Romans) and fetched its weight in silver in Roman markets.]",
      "Q4. Which ancient coastal port site in Tamil Nadu was excavated by Sir Mortimer Wheeler, revealing an Indo-Roman commercial trading station with Roman amphorae and Arretine pottery?\n(a) Muziris\n(b) Korkai\n(c) Arikamedu\n(d) Puhar\nCorrect Answer: (c) Arikamedu [Explanation: Arikamedu (near Puducherry) was an Indo-Roman maritime trade emporium where excavations yielded Roman clay wine amphorae, terra sigillata ware, and glass beads.]",
      "Q5. Who was the author of the celebrated classical Tamil Buddhist epic 'Manimekalai', written as a sequel to 'Silappadikaram'?\n(a) Ilango Adigal\n(b) Chithalai Chathanar\n(c) Tiruvalluvar\n(d) Kapilar\nCorrect Answer: (b) Chithalai Chathanar [Explanation: Sittalai Sattanar (Chithalai Chathanar), a grain merchant of Madurai, composed the epic 'Manimekalai' recounting the spiritual conversion of Kovalan's daughter to Buddhism.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-11",
    "filename": "11_gupta_empire_golden_age_and_culture",
    "title": "The Gupta Empire: Classical Age, Administration, Art & Science",
    "mapping": "History and Culture of India: The Gupta Empire - Political History, Samudragupta, Chandragupta II, Classical Renaissance, Sanskrit Literature, Science and Mathematics, Architecture and Epigraphic Evidence.",
    "intro": "The Gupta Empire (c. 319–550 CE), established by Sri Gupta and consolidated by Chandragupta I, is traditionally celebrated as the 'Golden Age' or 'Classical Period' of ancient India. The era was distinguished by political unification across Aryavarta, decentralized provincial governance, the flowering of Sanskrit literature (Kalidasa), revolutionary breakthroughs in mathematics and astronomy (Aryabhata), and the transition from rock-cut shrines to free-standing stone temple architecture.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/3/30/Iron_Pillar_Delhi.jpg", "caption": "The Mehrauli Iron Pillar at Delhi, carrying an inscription of King Chandra (Chandragupta II), showcasing rust-resistant metallurgy.", "alt": "Mehrauli Iron Pillar in Delhi Qutb complex"},
    "table": {
      "caption": "Pillars of Scientific, Literary, and Architectural Genius of the Guptas",
      "headers": ["Field", "Pioneering Figures / Monuments", "Key Contributions & Historical Significance"],
      "rows": [
        ["Literature & Drama", "Kalidasa, Visakhadatta, Sudraka, Bhasa", "Kalidasa: 'Abhijnanasakuntalam', 'Meghaduta', 'Raghuvamsha'; Visakhadatta: 'Mudrarakshasa', 'Devichandraguptam'; Sudraka: 'Mrichchhakatika'."],
        ["Mathematics & Astronomy", "Aryabhata (476–550 CE), Varahamihira", "Aryabhata: 'Aryabhatiya' (discovered 0, place-value decimal system, Pi = 3.1416, earth's rotation on its axis); Varahamihira: 'Brihat Samhita', 'Panchasiddhantika'."],
        ["Medicine & Metallurgy", "Sushruta tradition, Mehrauli Iron Pillar", "Refinements in surgery; Mehrauli forge-welded high-phosphorus iron pillar standing uncorroded for over 1,600 years."],
        ["Structural Temple Architecture", "Deogarh Dashavatara Temple (UP), Bhitargaon Brick Temple", "Earliest free-standing stone temples featuring a shikhara, Garbhagriha, and sculpted Ramayana/Vishnu narrative reliefs."],
        ["Cave Paintings & Sculpture", "Ajanta Caves (XVI, XVII, XIX), Sultanganj Bronze Buddha", "Fresco murals depicting Jataka tales; Sarnath seated Buddha preaching the first sermon in Dharmachakra Pravartana Mudra."]
      ]
    },
    "bullets": [
      "Samudragupta (c. 335–375 CE, 'Indian Napoleon'): Allahabad Pillar Inscription (Prayag Prashasti) composed by court poet Harisena in champu style; military strategy: Digvijaya and Prasabhoddharana (violent extermination of 9 North Indian rulers) vs Grahana-Mokshanugraha (capture and release of 12 South Indian kings upon tribute).",
      "Chandragupta II Vikramaditya (c. 375–415 CE): Defeated the Western Kshatrapas, annexing Malwa and Gujarat; established second capital at Ujjain; court graced by 'Navaratnas' (Nine Gems: Kalidasa, Amarasimha, Varahamihira, Dhanvantari, etc.); Chinese pilgrim Fa-Hien recorded peaceful governance without capital punishment.",
      "Administration & Feudal Transition: Decentralized empire divided into Bhuktis (provinces under Uparikas) and Vishayas (districts under Vishayapatis); proliferation of religious and secular land grants; decline in urban monetary trade, and emergence of earliest epigraphically recorded Sati at Eran (510 CE, Bhanugupta's reign).",
      "Nalanda Mahavihara: Founded by Kumaragupta I (Mahendraditya) in the 5th century CE; grew into Asia's premier international Buddhist university."
    ],
    "mains": [
      "Why is the Gupta period characterized as the 'Golden Age' of ancient India? Critically examine whether this cultural efflorescence masked an underlying socio-economic decline and feudalization. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight cultural peaks: classical Sanskrit (Kalidasa), mathematical-astronomical genius (Aryabhata), iron metallurgy (Mehrauli pillar), and structural temples (Deogarh); counterbalance with critical Marxist historiography (R.S. Sharma): proliferation of untouchability (Fa-Hien notes Chandalas striking wood when entering cities), subjection of women (earliest epigraphic Sati record at Eran in 510 CE), ruralization of economy, decline in trade and coinage post-Skandagupta, and fragmentation of state authority through tax-free agraharas."
    ],
    "mcqs": [
      "Q1. The Prayag Prashasti (Allahabad Pillar Inscription), detailing the military conquests of Samudragupta, was composed in classical Sanskrit by his court poet:\n(a) Kalidasa\n(b) Harisena\n(c) Ravikirti\n(d) Banabhatta\nCorrect Answer: (b) Harisena [Explanation: Harisena, court poet and minister of Samudragupta, composed the 33-line Prayag Prashasti in chaste Sanskrit champu kavya style on the Ashokan pillar at Allahabad.]",
      "Q2. In his monumental astronomical treatise 'Aryabhatiya' (499 CE), Aryabhata proposed which revolutionary scientific concept centuries before European astronomers?\n(a) Elliptical planetary orbits\n(b) Earth rotates daily on its own axis\n(c) Gravitational attraction of water\n(d) Speed of light\nCorrect Answer: (b) Earth rotates daily on its own axis [Explanation: Aryabhata stated that the starry sphere is stationary and the earth rotates daily on its axis ('prana'), causing the illusion of rising and setting celestial bodies.]",
      "Q3. The earliest inscriptional reference to the self-immolation of a widow (Sati) in Indian history, dated to 510 CE, was discovered at which site in Madhya Pradesh?\n(a) Deogarh\n(b) Eran\n(c) Bhitargaon\n(d) Mandasor\nCorrect Answer: (b) Eran [Explanation: The Eran stone pillar inscription of King Bhanugupta (510 CE) records that Goparaja, a royal general, died in battle and his devoted wife cremated herself on his funeral pyre.]",
      "Q4. Which Gupta emperor established the world-renowned Buddhist monastic university at Nalanda in modern Bihar?\n(a) Chandragupta II\n(b) Kumaragupta I\n(c) Skandagupta\n(d) Purugupta\nCorrect Answer: (b) Kumaragupta I [Explanation: Kumaragupta I (bearing the title Mahendraditya) founded the celebrated Nalanda Mahavihara, which later flourished under Harsha and the Pala kings.]",
      "Q5. Which Chinese Buddhist pilgrim traveled throughout northern India during the reign of Chandragupta II Vikramaditya and documented the peaceful social conditions?\n(a) Xuanzang (Hiuen Tsang)\n(b) Faxian (Fa-Hien)\n(c) Yijing (I-Tsing)\n(d) Song Yun\nCorrect Answer: (b) Faxian (Fa-Hien) [Explanation: Faxian (Fa-Hien) visited India between 399 and 412 CE during Chandragupta II's reign, noting that people were prosperous, vegetarian, and governed without torture or capital punishment.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-12",
    "filename": "12_harsha_vardhana_and_post_gupta_dynasties",
    "title": "Harsha Vardhana, Kanauj Assembly & Post-Gupta Formations",
    "mapping": "History and Culture of India: Post-Gupta Era - Harsha Vardhana (Pushyabhuti Dynasty), Administration, Assembly of Kanauj, Prayag Quinquennial Assembly, Xuanzang's Account and the Vakatakas.",
    "intro": "Following the collapse of the Gupta Empire under Huna invasions, political unity fragmented into regional successor kingdoms: the Pushyabhutis of Thanesar, the Maukharies of Kanauj, the Maitrakas of Vallabhi, and the Gaudas of Bengal. Harsha Vardhana (606–647 CE) reunited northern India, shifted his imperial capital to Kanauj, patronized Mahayana Buddhism, and hosted Chinese pilgrim Xuanzang (Hiuen Tsang).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Xuanzang_travels.jpg", "caption": "Xuanzang on his pilgrimage across India, carrying sacred Sanskrit Buddhist manuscripts back to Chang'an, China.", "alt": "Xuanzang carrying Buddhist scriptures"},
    "table": {
      "caption": "Post-Gupta Political Matrix & Harsha's Imperial Horizon",
      "headers": ["Dynasty & Region", "Prominent Monarchs", "Strategic Significance & Conflict", "Literary & Cultural Legacies"],
      "rows": [
        ["Pushyabhuti / Vardhana (Thanesar & Kanauj)", "Prabhakaravardhana, Rajyavardhana, Harsha Vardhana (606–647 CE).", "Harsha unified northern India; defeated Shashanka of Gauda; established Kanauj as the premier metropolis of North India.", "Harsha authored 3 Sanskrit plays: 'Ratnavali', 'Priyadarshika', 'Nagananda'; court poet Banabhatta authored 'Harshacharita' and 'Kadambari'."],
        ["Maukharies of Kanauj (UP & Bihar)", "Ishnavarman, Grahavarman.", "Grahavarman married Harsha's sister Rajyashri; allied with Thanesar against the Malwa-Gauda alliance.", "Fortified Kanauj (Mahodaya Nagar) as an imperial administrative centre."],
        ["Maitrakas of Vallabhi (Gujarat)", "Bhatarka, Dhruvasena II.", "Controlled Arabian Sea ports; Dhruvasena II married Harsha's daughter.", "Vallabhi hosted the Second Jain Council (512 CE) and emerged as a renowned Buddhist university town visited by Xuanzang."],
        ["Vakatakas of Deccan (Maharashtra)", "Vindhyashakti, Pravarasena I, Prabhavatigupta (regent).", "Matrimonial alliance with Guptas (Chandragupta II married daughter Prabhavatigupta to Rudrasena II).", "Patronized Ajanta Caves (rock-cut paintings in Caves XVI and XVII); developed the Vaidarbhi style of Sanskrit kavya."]
      ]
    },
    "bullets": [
      "The Battle of Narmada (c. 618 CE): Harsha attempted to conquer the Deccan but was decisively defeated on the banks of the Narmada River by Western Chalukya King Pulakesin II of Badami, as recorded in the Aihole Inscription ('Harsha, whose joy melted away in fear').",
      "Kanauj Religious Assembly (643 CE): Grand ecumenical debate hosted by Harsha to publicize Mahayana Buddhism, presided over by Xuanzang; attended by 20 tributary kings, 4,000 monks, and 3,000 Brahmins and Jains.",
      "Prayag Mahamoksha Parishad: Quinquennial assembly held every five years at the confluence of Ganga and Yamuna, where Harsha emptied his treasury by giving away all accumulated royal wealth in charity to ascetics, orphans, and the poor.",
      "Xuanzang's Travelogue ('Si-Yu-Ki'): Documented caste rigidity, untouchability, trial by ordeal, widespread robbery (he was robbed twice), Nalanda's scholarly rigour under chancellor Silabhadra, and Harsha's division of royal revenue into four equal shares."
    ],
    "mains": [
      "Assess the political achievements, administrative system, and religious patronage of Harsha Vardhana based on Banabhatta's 'Harshacharita' and Xuanzang's 'Si-Yu-Ki'. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Trace Harsha's rise from Thanesar to sovereign of Kanauj; examine administrative centralization vs feudal devolution (payment of officers through land assignments, rising feudatories / Samantas); analyze religious eclecticism: initially Shaivite, later patron of Mahayana Buddhism under Xuanzang's influence; describe the Kanauj assembly and Prayag charity congregations; detail his literary legacy ('Ratnavali', 'Priyadarshika', 'Nagananda')."
    ],
    "mcqs": [
      "Q1. Which Chalukyan monarch halted the southern imperial expansion of Harsha Vardhana at the Narmada River, as recorded in the Aihole Inscription?\n(a) Pulakesin I\n(b) Pulakesin II\n(c) Vikramaditya I\n(d) Kirtivarman I\nCorrect Answer: (b) Pulakesin II [Explanation: The Aihole Prashasti, composed by court poet Ravikirti, records that Western Chalukya King Pulakesin II defeated Harsha on the banks of the Narmada around 618 CE.]",
      "Q2. Who was the chancellor (head) of the international Nalanda University when Chinese pilgrim Xuanzang (Hiuen Tsang) studied Buddhist philosophy there?\n(a) Dharmapala\n(b) Silabhadra\n(c) Chandragomin\n(d) Vasubandhu\nCorrect Answer: (b) Silabhadra [Explanation: The venerable Buddhist scholar Acharya Silabhadra was the supreme head (Kulapati) of Nalanda Mahavihara who taught Yogacara philosophy to Xuanzang.]",
      "Q3. Which three celebrated Sanskrit dramas were authored by Emperor Harsha Vardhana himself?\n(a) Malavikagnimitram, Vikramorvasiyam, Sakuntalam\n(b) Ratnavali, Priyadarshika, Nagananda\n(c) Mudrarakshasa, Devichandraguptam, Mricchakatika\n(d) Mahaviracharita, Malatimadhava, Uttararamacharita\nCorrect Answer: (b) Ratnavali, Priyadarshika, Nagananda [Explanation: Harsha authored three classical Sanskrit plays: 'Ratnavali' and 'Priyadarshika' (romantic court comedies) and 'Nagananda' (Buddhist drama based on the self-sacrifice of Jimutavahana).]",
      "Q4. Court poet Banabhatta, who adorned the royal court of Harsha, authored which foundational Sanskrit biographical work?\n(a) Rajatarangini\n(b) Harshacharita\n(c) Kumarapalacharita\n(d) Vikramankadevacharita\nCorrect Answer: (b) Harshacharita [Explanation: Banabhatta composed the 'Harshacharita' (the first formal historical biography in classical Sanskrit) and the celebrated romantic prose romance 'Kadambari'.]",
      "Q5. According to Xuanzang's accounts, into how many equal shares did Emperor Harsha divide the royal revenues of the state?\n(a) Two parts\n(b) Three parts\n(c) Four parts\n(d) Six parts\nCorrect Answer: (c) Four parts [Explanation: Xuanzang recorded that Harsha divided state revenues into four quarters: one for state administration, one for salaries of public servants, one for rewarding intellectual talent, and one for charity to religious orders.]"
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

print("Part 2 of Subject 1 generated successfully")
