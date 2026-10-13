import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-HIST-17",
    "filename": "17_mughal_empire_administration_and_art",
    "title": "Mughal Empire: Administration, Mansabdari System, Art & Architecture",
    "mapping": "History and Culture of India: Mughal Empire (1526–1707 CE) - Babur, Humayun, Akbar (Mansabdari, Zabti/Dahsala, Sulh-i-Kul), Jahangir, Shah Jahan, Aurangzeb, Painting and Architecture.",
    "intro": "Founded in 1526 CE by Zahir-ud-din Babur following his victory at the First Battle of Panipat, the Mughal Empire forged a centralized pan-Indian state that dominated South Asia for over two centuries. Under Akbar the Great (1556–1605 CE), the empire institutionalized the Mansabdari administrative-military hierarchy, Todar Mal's Dahsala land revenue assessment, and a composite cultural ethos based on Sulh-i-Kul (universal peace), culminating in the architectural zenith under Shah Jahan.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/d/da/Taj_Mahal_in_March_2004.jpg", "caption": "The Taj Mahal at Agra, commissioned by Shah Jahan in 1632 CE as the crowning jewel of Mughal white marble architecture.", "alt": "Taj Mahal exterior white marble view"},
    "table": {
      "caption": "Pillars of Mughal Imperial Administration & Culture",
      "headers": ["Administrative / Cultural Tier", "Institutional Mechanism & Functionaries", "Operational Function & Historical Legacy"],
      "rows": [
        ["Mansabdari System", "Dual ranks: Zat (personal rank and salary) and Sawar (number of cavalrymen required to maintain).", "Graded hierarchy of 66 ranks (from 10 to 10,000); non-hereditary military bureaucracy; paid in cash (Naqd) or through revenue assignments (Jagirs)."],
        ["Agrarian & Revenue System (Zabt / Dahsala)", "Raja Todar Mal (Finance Minister); Ain-i-Dahsala (1580 CE).", "Assessed average produce and prices over the preceding 10 years; state demand fixed at 1/3rd in cash; land classified into Polaj (annually cultivated), Parauti (fallow 1–2 years), Chachar (fallow 3–4 years), and Banjar (uncultivated 5+ years)."],
        ["Religious Policy & Diplomacy", "Sulh-i-Kul (Universal Peace), Ibadat Khana (Fatehpur Sikri 1575), Mahzarnama / Infallibility Decree (1579), Din-i-Ilahi (1582).", "Abolished Jizya (1564) and pilgrim taxes; forged strategic matrimonial alliances with Rajput clans (Amber, Bikaner); promoted merit-based governance across faiths."],
        ["Architecture & Miniature Painting", "Humayun's Tomb (first double-dome garden tomb), Fatehpur Sikri (Buland Darwaza), Taj Mahal, Red Fort.", "Synthesis of Persian, Central Asian, and Indian architectural idioms; Pietra dura inlay work; Jahangir patronized realistic miniature portraiture and naturalistic flora/fauna art (Ustad Mansur)."]
      ]
    },
    "bullets": [
      "Provincial Administration (Subah): Empire divided into 15 Subahs (provinces) under Subahdar / Sipahsalar; Subahs subdivided into Sarkars (under Faujdar), Parganas (under Shiqdar), and Gramas (Muqaddams and Patwaris).",
      "Decline Dynamics: Aurangzeb's prolonged Deccan campaigns (1681–1707, 'the Deccan ulcer ruined Aurangzeb as the Spanish ulcer ruined Napoleon'); re-imposition of Jizya (1679); alienation of Rajputs, Marathas, and Sikhs; agrarian uprisings of Jats and Satnamis; and the Jagirdari crisis.",
      "Mughal Literary Achievements: Abul Fazl authored 'Akbarnama' and 'Ain-i-Akbari'; Babur composed memoirs 'Baburnama' (Tuzuk-i-Baburi in Chaghatai Turkic); Gulbadan Begum wrote 'Humayun-nama'; Dara Shikoh translated 50 Upanishads into Persian as 'Sirr-i-Akbar'."
    ],
    "mains": [
      "Critically evaluate Akbar's Mansabdari and Dahsala revenue systems as the foundational administrative pillars of the Mughal Empire. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the dual-rank Mansabdari system (Zat fixing social precedence and salary, Sawar determining military quota); analyze how it integrated diverse ethnic elites (Turani, Irani, Rajput, Deccani) into a centralized imperial service without hereditary entrenchment; examine Todar Mal's Dahsala revenue settlement measuring land with bamboos linked by iron rings (Tanab) and calculating 10-year rolling averages to provide revenue predictability; assess how the later inflation of mansab ranks and shortage of fertile jagirs (be-jagiri) triggered imperial systemic collapse."
    ],
    "mcqs": [
      "Q1. In the Mughal administrative apparatus, what did the dual ranking terms 'Zat' and 'Sawar' specifically signify in the Mansabdari system?\n(a) Land revenue share and royal tax quota\n(b) Personal status/salary rank and cavalry contingent quota\n(c) Civil administrative rank and judicial authority\n(d) Infantry strength and artillery division size\nCorrect Answer: (b) Personal status/salary rank and cavalry contingent quota [Explanation: In Akbar's Mansabdari system, 'Zat' determined the officer's personal status and salary, while 'Sawar' specified the exact number of cavalry troopers he was required to maintain.]",
      "Q2. The landmark 10-year rolling land revenue assessment system, 'Ain-i-Dahsala' (introduced in 1580 CE), was devised by which Mughal finance minister?\n(a) Abul Fazl\n(b) Raja Todar Mal\n(c) Raja Man Singh\n(d) Bairam Khan\nCorrect Answer: (b) Raja Todar Mal [Explanation: Raja Todar Mal designed the Dahsala system, which computed the average yield and prices over the preceding ten years to fix equitable state revenue demand.]",
      "Q3. In which year did Emperor Akbar abolish the discriminatory religious poll-tax 'Jizya' levied on non-Muslim subjects?\n(a) 1556 CE\n(b) 1564 CE\n(c) 1575 CE\n(d) 1582 CE\nCorrect Answer: (b) 1564 CE [Explanation: As part of his policy of Sulh-i-Kul and religious tolerance, Akbar abolished the pilgrim tax in 1563 and the Jizya in 1564, though Aurangzeb reimposed it in 1679.]",
      "Q4. Which Mughal prince translated 50 sacred Upanishads from Sanskrit into Persian under the title 'Sirr-i-Akbar' (The Great Secret)?\n(a) Prince Khusrau\n(b) Dara Shikoh\n(c) Shah Shuja\n(d) Murad Bakhsh\nCorrect Answer: (b) Dara Shikoh [Explanation: Eldest son of Shah Jahan, Dara Shikoh was a philosopher-prince who translated the Upanishads into Persian as 'Sirr-i-Akbar' and authored 'Majma-ul-Bahrain' (Mingling of the Two Oceans).]",
      "Q5. The magnificent architectural monument 'Buland Darwaza' at Fatehpur Sikri was constructed by Akbar to commemorate his victorious military conquest of:\n(a) Bengal\n(b) Malwa\n(c) Gujarat\n(d) Kashmir\nCorrect Answer: (c) Gujarat [Explanation: Akbar erected the massive 54-meter Buland Darwaza (Gate of Magnificence) at Fatehpur Sikri in 1573 to celebrate his conquest of the rich maritime province of Gujarat.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-18",
    "filename": "18_bhakti_and_sufi_movements",
    "title": "Bhakti & Sufi Movements: Philosophies, Saints & Cultural Synthesis",
    "mapping": "History and Culture of India: Bhakti and Sufi Movements - Origins, Philosophical Schools (Advaita, Vishishtadvaita, Dvaita), Nirguna and Saguna Bhakti Saints, Major Sufi Silsilas (Chishti, Suhrawardi) and Syncretic Culture.",
    "intro": "The medieval period witnessed a transformative spiritual renaissance driven by the parallel streams of the Bhakti Movement and Sufism. Rejecting ritualistic orthodoxy, rigid caste barriers, and priestly mediation, these movements advocated passionate personal devotion (Bhakti/Ishq) to God, fostered regional vernacular literature, and created a lasting syncretic Indo-Islamic composite culture.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/a/ad/Sant_Kabir.jpg", "caption": "A traditional portrait of Saint Kabir, the foremost pioneer of Nirguna Bhakti and social equality.", "alt": "Sant Kabir weaving cloth portrait"},
    "table": {
      "caption": "Philosophical Matrix of Major Medieval Bhakti Thinkers",
      "headers": ["Philosopher & Era", "Doctrinal School (Darshana)", "Core Metaphysical Philosophy", "Literary & Cultural Impact"],
      "rows": [
        ["Adi Shankara (8th C CE)", "Advaita Vedanta (Non-Dualism)", "Brahman is the sole absolute reality; phenomenal world is Maya (illusion); identity of Atman and Brahman.", "Established 4 Mathas at Sringeri, Puri, Dwaraka, and Badrinath; synthesized Vedic philosophy."],
        ["Ramanuja (11th C CE)", "Vishishtadvaita (Qualified Non-Dualism)", "Brahman is personal (Vishnu); world and souls are real attributes (Prakaras) of Brahman; devotion (Bhakti) is the path to grace (Prapatti).", "Promoted temple entry for outcastes (Thirukulattar); expounded 'Sri Bhasya'."],
        ["Madhvacharya (13th C CE)", "Dvaita (Strict Dualism)", "Absolute eternal distinction between God (Paramatman) and individual souls (Jivatman); world is not an illusion.", "Founded the Krishna temple at Udupi; authored commentaries on Brahma Sutras."],
        ["Kabir (15th C CE)", "Nirguna Bhakti (Formless Divine)", "Universal formless God; denounced caste, untouchability, idol worship, and rituals of both Hindus and Muslims.", "Composed pithy vernacular couplets (Dohas) in Sadhukkadi; collected in the 'Bijak' and included in the Guru Granth Sahib."],
        ["Guru Nanak (1469–1539 CE)", "Nirguna Bhakti / Sikhism", "Ek Onkar (One God); equality of all humans; community kitchen (Langar) and congregation (Sangat); rejected ascetic renunciation.", "Founded Sikhism; hymns compiled in Adi Granth; emphasized Naam Japna, Kirat Karo, and Vand Chhako."]
      ]
    },
    "bullets": [
      "Saguna vs Nirguna Traditions: Saguna worships God with anthropomorphic form and attributes (Chaitanya Mahaprabhu in Bengal, Mirabai in Rajasthan, Tulsidas who composed 'Ramcharitmanas', Surdas who wrote 'Sur Sagar'); Nirguna worships the formless, unmanifest Divine without physical idols (Kabir, Nanak, Dadu Dayal).",
      "Maharashtra Dharma (Varkari Panth): Centered on Lord Vithoba of Pandharpur; spearheaded by Jnaneshwar (authored 'Jnaneshwari'), Namdev, Eknath, and Tukaram (devotional Abhangas).",
      "Major Sufi Silsilas (Orders): Chishti Order (founded in India by Khwaja Muinuddin Chishti of Ajmer; Bakhtiyar Kaki, Baba Farid whose verses are in Guru Granth Sahib, Nizamuddin Auliya; stressed poverty, vegetarian hospitality, and musical assemblies / Sama); Suhrawardi Order (founded by Bahauddin Zakariya of Multan; accepted state patronage); Naqshbandi Order (orthodox revivalist led by Sheikh Ahmad Sirhindi).",
      "Syncretic Impact: Fostered vernacular languages (Awadhi, Braj, Bengali, Marathi, Punjabi, Hindavi/Urdu), democratized spirituality across caste divides, and inspired eclectic royal policies like Akbar's Sulh-i-Kul."
    ],
    "mains": [
      "Discuss the socio-religious significance of the Bhakti and Sufi movements in medieval India. How did they bridge communal divisions and democratize religious expression? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the socio-cultural backdrop: rigidity of Brahminical ritualism, caste untouchability, and mutual estrangement between Hindu and Muslim orthodox elites; analyze the Bhakti response: Nirguna saints (Kabir, Nanak) rejecting temple-mosque dichotomy and preaching universal brotherhood in vernacular idioms; analyze Sufi Chishti practices: open hospices (Khanqahs), communal langar, and musical gatherings (Sama/Qawwali) embracing common folk regardless of creed; evaluate the lasting legacy: blossoming of vernacular literature, foundation of Sikhism, and cultural synthesis in music, architecture, and daily language."
    ],
    "mcqs": [
      "Q1. Which Bhakti saint-philosopher expounded the doctrine of 'Vishishtadvaita' (Qualified Non-Dualism) and advocated devotion to Lord Vishnu as the path to salvation?\n(a) Adi Shankaracharya\n(b) Ramanujacharya\n(c) Madhvacharya\n(d) Nimbarkacharya\nCorrect Answer: (b) Ramanujacharya [Explanation: Ramanuja founded the Vishishtadvaita school of Vedanta, asserting that individual souls and matter constitute the real body of the Supreme Personal God (Vishnu).]",
      "Q2. The holy verses and poetic compositions of which pioneer of the Chishti Sufi order were integrated into the sacred scripture of Sikhism, the Guru Granth Sahib?\n(a) Khwaja Muinuddin Chishti\n(b) Baba Fariduddin Ganj-i-Shakar\n(c) Nizamuddin Auliya\n(d) Amir Khusrau\nCorrect Answer: (b) Baba Fariduddin Ganj-i-Shakar [Explanation: 134 hymns of Punjabi Sufi saint Baba Farid (Fariduddin Ganj-i-Shakar) were incorporated by Guru Arjan Dev into the Adi Granth (Guru Granth Sahib).]",
      "Q3. The poetic compositions and philosophical dialogues of Saint Kabir are predominantly compiled in which sacred collection?\n(a) Ramcharitmanas\n(b) Bijak\n(c) Sursagar\n(d) Padavali\nCorrect Answer: (b) Bijak [Explanation: The 'Bijak' (compiled by his disciple Bhagodas) is the foundational scripture containing Kabir's Dohas, Sakhis, and Shabads criticizing external religious dogmas.]",
      "Q4. Who established the egalitarian community kitchen institution of 'Langar' to dismantle caste hierarchies through shared communal dining?\n(a) Ramananda\n(b) Guru Nanak\n(c) Chaitanya Mahaprabhu\n(d) Vallabhacharya\nCorrect Answer: (b) Guru Nanak [Explanation: Guru Nanak institutionalized 'Langar' (free community kitchen) where all individuals, regardless of caste, creed, or gender, sat together as equals in Pangat to dine.]",
      "Q5. Which medieval woman mystic and Bhakti saint from Rajasthan composed impassioned devotional bhajans expressing unconditional love for Lord Krishna as 'Giridhar Gopal'?\n(a) Andal\n(b) Akka Mahadevi\n(c) Mirabai\n(d) Lalleshwari\nCorrect Answer: (c) Mirabai [Explanation: Mirabai, a Rajput princess of Mewar, abandoned aristocratic royal luxuries to compose celebrated devotional poetry dedicated to Lord Krishna (Giridhar).]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-19",
    "filename": "19_european_trading_companies_and_rivalries",
    "title": "European Advent: Commercial Rivalries, Carnatic Wars & Plassey",
    "mapping": "History and Culture of India: Advent of European Powers - Portuguese, Dutch, English, French; Carnatic Wars; British Conquest of Bengal: Battle of Plassey (1757) and Battle of Buxar (1764), Treaty of Allahabad.",
    "intro": "The arrival of Vasco da Gama at Calicut in 1498 inaugurated European mercantile expansion in India. Over the next two centuries, the Portuguese, Dutch, French, and English East India Companies contested for maritime dominance over the spice and textile trade. Through the Anglo-French Carnatic Wars and the fateful conquest of Bengal at Plassey (1757) and Buxar (1764), the English East India Company transformed from a merchant corporation into a sovereign colonial empire.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Clive_at_Plassey.jpg", "caption": "Robert Clive meeting Mir Jafar following the Battle of Plassey (1757), sealing the British political subjugation of Bengal.", "alt": "Clive and Mir Jafar after Plassey painting"},
    "table": {
      "caption": "Timeline of European Chartered Trading Companies in India",
      "headers": ["European Power & Charter", "Key Pioneers & Settlements", "Commercial Monopoly & Trade Focus", "Downfall / Subjugation Factors"],
      "rows": [
        ["Portuguese (Estado da Índia, 1498)", "Vasco da Gama, Francisco de Almeida (Blue Water Policy), Afonso de Albuquerque (captured Goa 1510).", "Spices, black pepper, horse trade; instituted the Cartaz (naval permit) system on Indian Ocean shipping.", "Religious intolerance/Inquisition, loss of naval supremacy to English and Dutch, diversion of resources to Brazil."],
        ["Dutch (Vereenigde Oostindische Compagnie - VOC, 1602)", "Factories at Pulicat (Fort Geldria), Surat, Chinsurah, Nagapattinam.", "Spices, silk, fine cotton textiles; minted gold pagodas at Pulicat.", "Decisively defeated by English at Battle of Bedara/Chinsurah (1759) and by Marthanda Varma at Battle of Colachel (1741); shifted focus to Indonesia."],
        ["English East India Company (EIC, 1600)", "Royal Charter by Elizabeth I; Captain Hawkins (Jahangir's court 1608), Sir Thomas Roe (1615); Factories at Surat (1612), Madras (Fort St. George 1639), Bombay (1668), Calcutta (Fort William 1696).", "Calico, muslin, silk, saltpetre, indigo, tea; secured Golden Farman from Golconda (1632) and Farrukhsiyar's Royal Farman ('Magna Carta of EIC', 1717) granting duty-free trade (Dastaks) in Bengal.", "Emerged supreme imperial power through military discipline, naval superiority, industrial capitalist finance, and political machinations."],
        ["French East India Company (Compagnie des Indes, 1664)", "Colbert (under Louis XIV); Francois Caron (Surat 1668), Francois Martin (Pondicherry 1674), Dupleix.", "Textiles and spices; Pondicherry, Chandernagore, Mahe, Karaikal.", "Direct state control and financial bankruptcy; completely defeated by British in the Three Carnatic Wars (Battle of Wandiwash 1760)."]
      ]
    },
    "bullets": [
      "The Three Carnatic Wars (1746–1763): Anglo-French proxy wars in coastal Coromandel; First Carnatic War (Battle of St. Thome 1746 - small disciplined European force routed large Nawab army; Treaty of Aix-la-Chapelle 1748); Second Carnatic War (Robert Clive captured Arcot 1751); Third Carnatic War (Sir Eyre Coote defeated French General Lally at Battle of Wandiwash 1760; Treaty of Paris 1763 reduced French to unarmed trading posts).",
      "Battle of Plassey (23 June 1757): Nawab Siraj-ud-Daulah clashed with Robert Clive over misuse of trade passes (Dastaks) and fortification of Calcutta; Clive conspired with Nawab's treacherous commander Mir Jafar, financier Jagat Seth, and Rai Durlabh; battle won with minimal fighting; marked the foundation of British colonial rule in India.",
      "Battle of Buxar (22 October 1764): Decisive pitched battle where Major Hector Munro routed the combined confederacy of Mir Qasim (former Nawab of Bengal), Shuja-ud-Daula (Nawab of Awadh), and Mughal Emperor Shah Alam II.",
      "Treaty of Allahabad (1765): Robert Clive secured the 'Diwani' (civil administration and revenue collection rights) of Bengal, Bihar, and Orissa for the EIC from Shah Alam II in return for an annual tribute of 26 lakh rupees, institutionalizing the corrupt 'Dual Government' (1765–1772)."
    ],
    "mains": [
      "Why is the Battle of Buxar (1764) considered far more decisive and politically consequential than the Battle of Plassey (1757) in establishing British hegemony in India? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast the nature of the two battles: Plassey was a skirmish won through treason and palace conspiracy against an isolated young Nawab (Siraj-ud-Daulah), leaving the British as puppet-masters; Buxar was a genuine military contest where Company troops routed the combined forces of the Mughal Emperor (Shah Alam II), the Nawab of Awadh, and Mir Qasim; detail the political aftermath: Treaty of Allahabad (1765) granting sovereign Diwani rights over Bengal, Bihar, and Orissa; establish how Buxar made the Company the de jure rulers of India's richest agrarian region, funding future subcontinental conquests."
    ],
    "mcqs": [
      "Q1. Which Portuguese Viceroy instituted the 'Blue Water Policy' (Cartaz system), prioritizing naval supremacy over territorial land expansion in the Indian Ocean?\n(a) Francisco de Almeida\n(b) Afonso de Albuquerque\n(c) Nino da Cunha\n(d) Duarte Barbosa\nCorrect Answer: (a) Francisco de Almeida [Explanation: Francisco de Almeida (first Portuguese Viceroy, 1505–1509) initiated the Blue Water Policy to control Indian Ocean trade chokepoints through fortified naval supremacy.]",
      "Q2. The Mughal Emperor Farrukhsiyar issued his famous imperial Farman of 1717, granting the English East India Company duty-free trading privileges (Dastaks) in Bengal, which is often termed:\n(a) Charter of Commerce\n(b) Magna Carta of the Company\n(c) Golden Farman\n(d) Treaty of Murshidabad\nCorrect Answer: (b) Magna Carta of the Company [Explanation: Farrukhsiyar's 1717 Farman granted the Company duty-free trade in Bengal for an annual nominal payment of Rs. 3,000, famously hailed as the 'Magna Carta' of the EIC.]",
      "Q3. In which decisive battle of the Third Carnatic War in 1760 did British forces under Sir Eyre Coote crush the French army under Count de Lally, permanently ending French imperial ambitions in India?\n(a) Battle of St. Thome\n(b) Battle of Ambur\n(c) Battle of Wandiwash\n(d) Battle of Bedara\nCorrect Answer: (c) Battle of Wandiwash [Explanation: The Battle of Wandiwash (22 January 1760) in Tamil Nadu was a crushing British victory over the French, reducing French presence in India to unfortified enclaves.]",
      "Q4. Through which historic treaty concluded in 1765 did Mughal Emperor Shah Alam II grant the Diwani (revenue collection rights) of Bengal, Bihar, and Orissa to the British East India Company?\n(a) Treaty of Alinagar\n(b) Treaty of Allahabad\n(c) Treaty of Purandar\n(d) Treaty of Mangalore\nCorrect Answer: (b) Treaty of Allahabad [Explanation: Signed by Robert Clive and Shah Alam II in August 1765, the Treaty of Allahabad granted the Company sovereign Diwani revenue rights, inaugurating the Dual System of government in Bengal.]",
      "Q5. Which Travancore ruler decisively defeated the Dutch East India Company at the Battle of Colachel in 1741, marking the first major victory of an Indian monarch over a European naval power?\n(a) Swathi Thirunal\n(b) Marthanda Varma\n(c) Dharma Raja\n(d) Pazhassi Raja\nCorrect Answer: (b) Marthanda Varma [Explanation: King Marthanda Varma of Travancore routed the Dutch fleet at the Battle of Colachel on 10 August 1741, completely terminating Dutch political influence in Malabar.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-20",
    "filename": "20_british_expansion_and_paramountcy_policies",
    "title": "British Imperial Expansion: Marathas, Mysore, Sikhs & Paramountcy Policies",
    "mapping": "History and Culture of India: British Expansion - Anglo-Mysore Wars (Haidar Ali, Tipu Sultan), Anglo-Maratha Wars, Anglo-Sikh Wars, Imperialist Policies: Subsidiary Alliance (Wellesley) and Doctrine of Lapse (Dalhousie).",
    "intro": "Between 1767 and 1849, the British East India Company dismantled the premier military powers of the subcontinent—Mysore, the Maratha Confederacy, and the Sikh Empire—through a combination of military campaigns and diplomatic instruments of paramountcy. Guided by Lord Wellesley's Subsidiary Alliance and Lord Dalhousie's Doctrine of Lapse, the Company subjugated princely states, erasing Indian sovereignty across South Asia.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Tipu_Sultan_sword.jpg", "caption": "The personal flintlock and steel sword of Tipu Sultan ('Tiger of Mysore'), who resisted British paramountcy until the Fall of Seringapatam (1799).", "alt": "Sword and weapons of Tipu Sultan"},
    "table": {
      "caption": "Military Conquests of Regional Indian Powers by the East India Company",
      "headers": ["Regional Power & Adversaries", "Major Wars & Battles", "Decisive Treaties & Annexations", "Historical Impact & Imperial Mechanics"],
      "rows": [
        ["Kingdom of Mysore (Haidar Ali & Tipu Sultan)", "Four Anglo-Mysore Wars (1767–69, 1780–84, 1790–92, 1799).", "Treaty of Madras (1769), Treaty of Mangalore (1784), Treaty of Seringapatam (1792 - Tipu ceded half his kingdom), Fall of Seringapatam (4 May 1799 - Tipu died fighting).", "Mysore restored to minor Wodeyar heir under strict Subsidiary Alliance; Tipu pioneered military rocketry (Mysorean rockets) and planted the Jacobin Tree of Liberty."],
        ["Maratha Confederacy (Peshwa, Scindia, Holkar, Gaekwad, Bhonsle)", "Three Anglo-Maratha Wars (1775–82, 1803–05, 1817–18).", "Treaty of Salbai (1782, 20 years peace), Treaty of Bassein (1802, Peshwa Baji Rao II accepted Subsidiary Alliance), Third War (1818 - Peshwaship abolished).", "Peshwa exiled to Bithoor with a pension; Shivaji's descendant installed as puppet raja of Satara; Maratha territories annexed into Bombay Presidency."],
        ["Sikh Empire of Punjab (Maharaja Ranjit Singh)", "Two Anglo-Sikh Wars (1845–46, 1848–49).", "Treaty of Lahore (1846 - Jalandhar Doab annexed, Kashmir sold to Gulab Singh), Battle of Gujrat ('Battle of Guns', 1849).", "Lord Dalhousie annexed Punjab in March 1849; minor Maharaja Duleep Singh pensioned off to England; Koh-i-Noor diamond confiscated for Queen Victoria."]
      ]
    },
    "bullets": [
      "Subsidiary Alliance System (Lord Wellesley, 1798–1805): Princely state surrendered foreign relations to Company; stationed British subsidiary force at its own expense or ceded territory; accepted a British Resident in court; barred employing other Europeans. First state to sign: Nizam of Hyderabad (1798), followed by Mysore (1799), Tanjore (1799), Awadh (1801), and Peshwa (1802).",
      "Doctrine of Lapse (Lord Dalhousie, 1848–1856): If an Indian ruler of a protected state died without a natural male heir, the state 'lapsed' to the British Crown, nullifying traditional Hindu adoption rights. Annexed states: Satara (1848), Jaitpur and Sambalpur (1849), Baghat (1850), Udaipur (1852), Jhansi (1853), and Nagpur (1854).",
      "Annexation of Awadh (1856): Dalhousie deposed Nawab Wajid Ali Shah on the pretext of 'misgovernance' (based on James Outram's report), alienating thousands of Awadh sepoys who constituted the backbone of the Bengal Army."
    ],
    "mains": [
      "Examine the strategic features and imperialist objectives of Lord Wellesley's Subsidiary Alliance system and Lord Dalhousie's Doctrine of Lapse. How did these policies set the stage for the Revolt of 1857? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define Subsidiary Alliance: turning Indian rulers into emasculated protectorates bearing the financial cost of British standing armies, destroying indigenous military readiness; define Doctrine of Lapse: arbitrary annexation denying sovereign adoption rights, expropriating royal titles and pensions (Nana Saheb); discuss Dalhousie's annexation of Awadh on charges of misgovernance; demonstrate direct causality with 1857: dispossessed royal families (Rani Lakshmibai, Begum Hazrat Mahal), disbanded soldiers, and sepoy unrest (Awadh sepoys watching their homeland annexed) uniting in rebellion."
    ],
    "mcqs": [
      "Q1. Which Indian princely ruler was the very first to accept Lord Wellesley's Subsidiary Alliance system in 1798?\n(a) Nawab of Awadh\n(b) Nizam of Hyderabad\n(c) Peshwa Baji Rao II\n(d) Raja of Travancore\nCorrect Answer: (b) Nizam of Hyderabad [Explanation: The Nizam of Hyderabad (Nizam Ali Khan) signed the first Subsidiary Alliance treaty with Governor-General Lord Wellesley in September 1798.]",
      "Q2. In which historic battle during the Fourth Anglo-Mysore War did Tipu Sultan, the 'Tiger of Mysore', die heroically defending his capital?\n(a) Battle of Pollilur\n(b) Battle of Porto Novo\n(c) Fall of Seringapatam (1799)\n(d) Battle of Sholinghur\nCorrect Answer: (c) Fall of Seringapatam (1799) [Explanation: On 4 May 1799, Tipu Sultan was killed defending the breaches of his capital fort at Seringapatam against British forces led by General George Harris and Arthur Wellesley.]",
      "Q3. Under Lord Dalhousie's aggressive 'Doctrine of Lapse', which was the very first princely state annexed by the British in 1848?\n(a) Jhansi\n(b) Nagpur\n(c) Satara\n(d) Sambalpur\nCorrect Answer: (c) Satara [Explanation: Satara in Maharashtra was the first state annexed under the Doctrine of Lapse in 1848 when Raja Appa Sahib died without a biological male heir.]",
      "Q4. On what specific administrative grounds did Lord Dalhousie annex the wealthy kingdom of Awadh in February 1856?\n(a) Failure to pay subsidiary army arrears\n(b) Chronic internal misgovernance\n(c) Lack of a biological male heir\n(d) Treasonous alliance with Russia\nCorrect Answer: (b) Chronic internal misgovernance [Explanation: Dalhousie annexed Awadh in 1856 citing persistent 'misgovernance' under Nawab Wajid Ali Shah, acting on the controversial report of Resident James Outram.]",
      "Q5. By which treaty was the Second Anglo-Maratha War precipitated when Peshwa Baji Rao II fled to the British and signed a Subsidiary Alliance in 1802?\n(a) Treaty of Salbai\n(b) Treaty of Bassein\n(c) Treaty of Purandar\n(d) Treaty of Deogaon\nCorrect Answer: (b) Treaty of Bassein [Explanation: Under the Treaty of Bassein (1802), Peshwa Baji Rao II surrendered Maratha independence to the British in exchange for military restoration against Holkar.]"
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

print("Part 4 of Subject 1 generated successfully")
