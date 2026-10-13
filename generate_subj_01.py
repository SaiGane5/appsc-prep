import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

# List of all 30 segregated topics for Subject 1: History and Culture of India
topics = [
  {
    "id": "APPSC-G1-HIST-01",
    "filename": "01_indus_valley_civilization",
    "title": "Indus Valley Civilization: Urban Planning, Society, Trade & Religion",
    "mapping": "History and Culture of India: Indus Valley Civilization - Features, Major Sites, Urban Morphology, Society, Cultural History, Trade Networks, Art, Religion and Decline Theories.",
    "intro": "The Indus Valley Civilization (c. 2600–1900 BCE Mature Phase) represents South Asia's primary Bronze Age urban threshold. Spanning over 1.3 million sq km across the Indus-Ghaggar-Hakra river basins, it was distinguished by standardized baked brick architecture, municipal drainage systems, long-distance maritime commerce with Mesopotamia (Meluhha), and an undeciphered logo-syllabic script.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Great_bath_view_Mohenjodaro.JPG", "caption": "The Great Bath at Mohenjo-daro, demonstrating waterproof bitumen engineering and ritual cleansing architecture.", "alt": "Great Bath ruins at Mohenjo-daro"},
    "table": {
      "caption": "Archaeological Matrix of Key Harappan Sites & Findings",
      "headers": ["Site & Location", "Excavator & River", "Key Architectural Findings", "Economic / Cultural Significance"],
      "rows": [
        ["Harappa (Punjab, Pakistan)", "Daya Ram Sahni (1921), Ravi", "6 Granaries in two rows, red sandstone torso, workmen quarters.", "First site discovered; citadel and lower town gridiron planning."],
        ["Mohenjo-daro (Sindh, Pakistan)", "R.D. Banerjee (1922), Indus", "Great Bath, Great Granary, Bronze Dancing Girl, Priest-King steatite head.", "Metropolitan capital with multi-storeyed houses and individual soak pits."],
        ["Dholavira (Kutch, Gujarat)", "R.S. Bisht (1990), Luni basin", "Tripartite division (Citadel, Middle Town, Lower Town), 16 rock-cut reservoirs, 10-sign signboard.", "UNESCO World Heritage Site; world's earliest advanced water conservation system."],
        ["Lothal (Saurashtra, Gujarat)", "S.R. Rao (1954), Bhogava", "Tidal dockyard basin, double burial, Persian Gulf button seal, terracotta rice husks.", "Principal maritime port trading with Dilmun (Bahrain) and Makan (Oman)."],
        ["Kalibangan (Rajasthan)", "A. Ghosh / B.B. Lal, Ghaggar", "Ploughed field surface (furrow marks), fire altars, camel bones.", "Earliest evidence of ploughed agriculture and pre-Harappan transition."],
        ["Rakhigarhi (Haryana)", "Amarendra Nath / Vasant Shinde", "Largest Harappan site (550+ hectares), granary, gold foundry, ancient DNA burials.", "Confirms indigenous genetic continuity without Central Asian steppe admixture in Mature IVC."]
      ]
    },
    "bullets": [
      "Urban Planning & Municipal Sanitation: Strict gridiron plan (chess-board pattern) with streets intersecting at right angles; underground covered drains flanked by inspection traps and soak pits.",
      "Social Stratification & Crafts: Absence of royal palaces or military barracks; dominance of merchant-artisan guilds; lapidary bead-making at Chanhudaro; shell-working at Balakot.",
      "Religion & Ritual Practices: Iconography of Proto-Shiva (Pashupati seal flanked by elephant, tiger, rhino, buffalo, and deer beneath the seat), Mother Goddess terracotta figurines, phallic lingam stones, pipal tree veneration, and unicorn motifs.",
      "Decline Dynamics: Multi-causal transformation rather than abrupt Aryan massacre; drying of Saraswati/Ghaggar system, shifting monsoons, ecological degradation, tectonic river blockages, and collapse of Mesopotamian trade."
    ],
    "mains": [
      "Analyze the urban morphology and water management systems of the Indus Valley Civilization. How do archaeological discoveries at Dholavira and Lothal showcase Harappan hydraulic engineering? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail gridiron layout, division into citadel and lower town, burnt brick standardization (1:2:4 ratio); explain Dholavira's hydraulic cascade: 16 bunded check-dams and reservoirs carved into bedrock conserving seasonal storm runoffs; examine Lothal's trapezoidal dockyard connected via sluice gate to the tidal Bhogava river, enabling cargo navigation during high tides; conclude on sustainability lessons for 21st-century urban drainage."
    ],
    "mcqs": [
      "Q1. Which Indus Valley Civilization site features a unique tripartite urban classification consisting of a Citadel, a Middle Town, and a Lower Town?\n(a) Mohenjo-daro\n(b) Kalibangan\n(c) Dholavira\n(d) Banawali\nCorrect Answer: (c) Dholavira [Explanation: Unlike most Harappan settlements divided into two zones, Dholavira in Kutch is divided into three distinct fortified sectors: Citadel, Middle Town, and Lower Town, accompanied by an elaborate water-harvesting reservoir system.]",
      "Q2. The famous 'Pashupati Seal' discovered at Mohenjo-daro depicts a horned yogic figure surrounded by which group of four animals?\n(a) Elephant, Tiger, Rhinoceros, Buffalo\n(b) Lion, Tiger, Elephant, Bull\n(c) Horse, Elephant, Bull, Rhinoceros\n(d) Tiger, Lion, Horse, Deer\nCorrect Answer: (a) Elephant, Tiger, Rhinoceros, Buffalo [Explanation: The Pashupati (Proto-Shiva) seal shows a three-faced seated deity surrounded by an elephant, tiger, rhinoceros, and water buffalo, with two deer depicted below his stool.]",
      "Q3. The earliest archaeological evidence of an agricultural field ploughed with criss-cross furrows was discovered at which Harappan site?\n(a) Harappa\n(b) Kalibangan\n(c) Lothal\n(d) Chanhudaro\nCorrect Answer: (b) Kalibangan [Explanation: Excavations at Kalibangan in Rajasthan revealed a pre-Harappan ploughed agricultural field with grid furrow lines showing simultaneous dual-crop cultivation (mustard and gram).]",
      "Q4. In cuneiform inscriptions of the Akkadian Empire in ancient Mesopotamia, which geographical term was used to denote the Indus Valley region?\n(a) Magan\n(b) Dilmun\n(c) Meluhha\n(d) Punt\nCorrect Answer: (c) Meluhha [Explanation: Akkadian and Sumerian texts refer to maritime commerce with Meluhha (Indus region), Dilmun (Bahrain, trade intermediary), and Magan (Oman peninsula).]",
      "Q5. At which Harappan site was an exclusive craft workshop for bead manufacturing, devoid of any fortified citadel, excavated?\n(a) Chanhudaro\n(b) Surkotada\n(c) Kot Diji\n(d) Alamgirpur\nCorrect Answer: (a) Chanhudaro [Explanation: Chanhudaro in Sindh was a dedicated industrial and craft township without a protective citadel, specializing in steatite bead-making, seal carving, and shell ornaments.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-02",
    "filename": "02_vedic_age_and_culture",
    "title": "Vedic Age: Early & Later Vedic Polity, Economy, Society & Literature",
    "mapping": "History and Culture of India: Vedic Age - Rigvedic Society, Later Vedic Transformation, Epic Period, Caste Evolution, Religious Transitions and Vedic Literature.",
    "intro": "The Vedic Age (c. 1500–600 BCE) marked the pastoral-tribal settlement of Indo-Aryan communities in the Sapta Sindhu region and their subsequent eastward migration into the Ganga-Yamuna Doab. The advent of iron metallurgy ('Shyama Ayas') in the Later Vedic era catalyzed agrarian surpluses, territorial statehood (Janapadas), rigid four-fold Varna stratification, and complex sacrificial rituals.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Rigveda_MS2097.jpg", "caption": "A 19th-century Devanagari manuscript of the Rigveda, preserving hymns composed in the Sapta Sindhu river basin.", "alt": "Rigveda manuscript folio"},
    "table": {
      "caption": "Evolutionary Paradigm: Early Vedic (Rigvedic) vs Later Vedic Era",
      "headers": ["Parametric Theme", "Early Vedic Period (c. 1500–1000 BCE)", "Later Vedic Period (c. 1000–600 BCE)"],
      "rows": [
        ["Geographical Focus", "Sapta Sindhu (Indus, Saraswati, Ravi, Beas, Chenab, Jhelum, Sutlej).", "Aryavarta / Kuru-Panchala realm in the Ganga-Yamuna Doab."],
        ["Political Structure", "Tribal chiefdom (Rajan) checked by popular assemblies (Sabha, Samiti, Vidatha); voluntary tributes (Bali).", "Territorial monarchies (Janapadas); divine kingship; standing royal bureaucracy (Ratnins); compulsory taxation (Bali, Bhaga, Shulka)."],
        ["Socio-Economic Base", "Pastoral economy; cattle as primary wealth (Gavisti = search for cows); barter; copper/bronze (Ayas).", "Sedentary iron-axe agriculture (Shyama Ayas); Painted Grey Ware (PGW); emergence of trade guilds (Srenis)."],
        ["Social Stratification", "Flexible occupational classes; absence of hereditary caste; women enjoyed high status (Gargi, Maitreyi).", "Rigid hereditary four-fold Varna (Purusha Sukta); Gotra endogamy; exclusion of women from political assemblies and education."],
        ["Religious Pantheon", "Polytheistic nature deities (Indra/Purandara, Agni, Varuna); simple fire oblations without large-scale killings.", "Ascendancy of Trimurti/Prajapati, Rudra, and Vishnu; costly animal sacrifices (Ashvamedha, Rajasuya, Vajapeya); Upanishadic philosophical revolt."]
      ]
    },
    "bullets": [
      "Vedic Literary Corpus: Shruti (revealed: 4 Vedas, Brahmanas, Aranyakas, Upanishads) and Smriti (remembered: Vedangas, Upavedas, Dharmashastras, Epics).",
      "Four Vedas: Rigveda (1,028 suktas, Gayatri Mantra in Mandala 3); Samaveda (book of melodies, origins of Indian classical music); Yajurveda (prose ritual formulas: Shukla and Krishna); Atharvaveda (charms, spells, medicine, daily customs).",
      "Upanishadic Philosophy: 108 Upanishads (principal 10: Isha, Kena, Katha, Mundaka, Chandogya, Brihadaranyaka); central thesis of Moksha through realizing the identity of Atman (individual soul) and Brahman (universal consciousness).",
      "Six Vedangas: Shiksha (phonetics), Kalpa (ritual), Vyakarana (grammar), Nirukta (etymology), Chhanda (metrics), and Jyotisha (astronomy)."
    ],
    "mains": [
      "Trace the socio-economic and political shifts from the Early Vedic pastoral tribalism to the Later Vedic territorial statehood. How did iron technology facilitate this structural transition? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast the Sapta Sindhu pastoralism with Ganga-Yamuna agricultural settlements; explain the metallurgical revolution of iron ('Shyama Ayas') from 1000 BCE at Atranjikhera clearing dense monsoonal sal forests; examine the rise of surplus paddy cultivation yielding land revenue that financed royal armies and ritual legitimacy (Rajasuya, Vajapeya); evaluate the hardening of Varna hierarchies and social subjugation of Shudras and women."
    ],
    "mcqs": [
      "Q1. Which famous Vedic assembly was open to women and functioned as the earliest popular deliberative tribal council in the Early Vedic era?\n(a) Sabha\n(b) Samiti\n(c) Vidatha\n(d) Gana\nCorrect Answer: (c) Vidatha [Explanation: The Vidatha was the earliest Rigvedic folk assembly where women actively participated alongside men in tribal deliberations, religious rites, and war loot distribution.]",
      "Q2. The national motto of India, 'Satyameva Jayate' (Truth Alone Triumphs), is inscribed from which ancient Upanishad?\n(a) Chandogya Upanishad\n(b) Mundaka Upanishad\n(c) Katha Upanishad\n(d) Brihadaranyaka Upanishad\nCorrect Answer: (b) Mundaka Upanishad [Explanation: 'Satyameva Jayate' is an excerpt from the Mundaka Upanishad (3.1.6), adopted as the official national motto on 26 January 1950.]",
      "Q3. In the Later Vedic administrative apparatus, which royal functionary among the Ratnins was designated as the Chief Collector of Revenue?\n(a) Suta\n(b) Bhagadugha\n(c) Sangrahitri\n(d) Akshavapa\nCorrect Answer: (b) Bhagadugha [Explanation: In the Later Vedic state, the Bhagadugha collected the king's share of agrarian taxes (Bhaga), while the Sangrahitri functioned as the royal treasurer.]",
      "Q4. The philosophical dialogue between the young seeker Nachiketa and Yama (the God of Death) regarding the nature of the soul and life after death is preserved in:\n(a) Katha Upanishad\n(b) Kena Upanishad\n(c) Prashna Upanishad\n(d) Aitareya Upanishad\nCorrect Answer: (a) Katha Upanishad [Explanation: The famous discourse on self-realization, the immortality of Atman, and spiritual wisdom between Yama and Nachiketa is the central subject of the Katha Upanishad.]",
      "Q5. Which Mandala of the Rigveda contains the famous 'Purusha Sukta' hymn that provides the earliest textual reference to the four-fold Varna system?\n(a) Mandala 1\n(b) Mandala 3\n(c) Mandala 7\n(d) Mandala 10\nCorrect Answer: (d) Mandala 10 [Explanation: Mandala 10, Hymn 90 (Purusha Sukta) represents a late Rigvedic interpolation describing the cosmic sacrifice of Purusha from whose mouth, arms, thighs, and feet the Brahmin, Kshatriya, Vaishya, and Shudra arose.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-03",
    "filename": "03_mahajanapadas_and_heterodox_religions",
    "title": "Second Urbanization, 16 Mahajanapadas, Jainism & Buddhism",
    "mapping": "History and Culture of India: Second Urbanization in 6th Century BCE - 16 Mahajanapadas, Heterodox Revolutions: Jainism and Buddhism - Philosophies, Councils, Sects and Socio-Economic Impact.",
    "intro": "The 6th century BCE witnessed the 'Second Urbanization' in the middle Gangetic plains, driven by iron technology, coinage (punch-marked coins), and flourishing trade. This economic shift spawned 16 territorial states (Mahajanapadas) and sparked a profound intellectual revolution against Brahminical orthodoxy led by Gautama Buddha (Buddhism) and Vardhamana Mahavira (Jainism).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Mahabodhi_Temple_2012.jpg", "caption": "The Mahabodhi Temple at Bodh Gaya, Bihar, commemorating the site of Siddhartha Gautama's enlightenment.", "alt": "Mahabodhi Temple exterior tower"},
    "table": {
      "caption": "Comparative Analysis: Buddhist Dhamma vs Jaina Philosophy",
      "headers": ["Philosophical Dimension", "Buddhism (Gautama Buddha)", "Jainism (Vardhamana Mahavira)"],
      "rows": [
        ["Core Teaching & Path", "Madhyama Marga (Middle Path); avoided both extreme sensual indulgence and severe physical self-mortification.", "Extreme asceticism, severe penance, and total renunciation of possessions (Aparigraha) including clothing in Digambara."],
        ["Ahimsa (Non-Violence)", "Pragmatic Ahimsa; focused on ethical compassion; permitted monkhood without extreme physical restrictions.", "Absolute, unconditional Ahimsa towards all living beings, plants, insects, and elemental particles (Jiva)."],
        ["Metaphysical Doctrine", "Anatta (No permanent soul/self), Anicca (Impermanence), Pratityasamutpada (Dependent Origination).", "Anekantavada (Non-absolutism/pluralism), Syadvada (Theory of conditional prediction), eternity of individual souls (Jiva)."],
        ["Social Patronage", "Vaishya merchants, royal monarchs (Bimbisara, Ashoka, Kanishka), universal open Sangha for all castes.", "Supported heavily by mercantile and trading classes (due to farming requiring killing of insects); royal patronage by Bimbisara, Chandragupta Maurya, Kharavela."],
        ["Canonical Scriptures", "Tripitakas (Vinaya, Sutta, Abhidhamma) composed in popular Prakrit/Pali.", "12 Angas and 12 Upangas composed in Ardhamagadhi Prakrit."]
      ]
    },
    "bullets": [
      "16 Mahajanapadas: Recorded in Buddhist Anguttara Nikaya and Jain Bhagavati Sutra; divided into monarchies (Magadha, Kosala, Vatsa, Avanti) and republican oligarchies / Ganasanghas (Vajji confederacy, Malla).",
      "Four Buddhist Councils: 1st Council at Rajgir (483 BCE, Ajatashatru, Mahakassapa); 2nd at Vaishali (383 BCE, Kalasoka, Sabakami); 3rd at Pataliputra (250 BCE, Ashoka, Moggaliputta Tissa); 4th in Kashmir (72 CE, Kanishka, Vasumitra - split into Hinayana and Mahayana).",
      "Jain Councils: 1st Council at Pataliputra (c. 300 BCE, Sthulabhadra - compilation of 12 Angas, Digambara-Svetambara schism); 2nd Council at Vallabhi (512 CE, Devardhi Kshamasramana - final codification).",
      "Triratna & Five Vows: Jainism stresses Right Faith (Samyag Darshana), Right Knowledge (Samyag Jnana), Right Conduct (Samyag Charitra); 5 Vows: Ahimsa, Satya, Asteya (non-stealing), Aparigraha, Brahmacharya (added by Mahavira)."
    ],
    "mains": [
      "Examine the socio-economic conditions that fostered the rise of heterodox religious movements (Buddhism and Jainism) in the 6th century BCE Gangetic plains. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Connect the Second Urbanization, iron technology, and coinage (punch-marked silver karshapanas) to the emergence of affluent merchant classes (Sethis/Gahapatis); explain how Brahminical Vedic rituals and animal sacrifices depleted cattle wealth vital for plough agriculture; show how the rigid Varna system relegated wealthy Vaishyas below Kshatriyas and Brahmins; explain the democratic appeal of Buddha and Mahavira preaching in vernacular Pali and Ardhamagadhi."
    ],
    "mcqs": [
      "Q1. Which ancient oligarchic republican confederacy (Ganasangha) was composed of eight clans, with its capital situated at Vaishali?\n(a) Malla\n(b) Vajji\n(c) Kamboja\n(d) Chedi\nCorrect Answer: (b) Vajji [Explanation: The Vajji confederacy was a celebrated republican oligarchy comprising eight clans (most prominent being the Lichchhavis) headquartered at Vaishali.]",
      "Q2. The Buddhist doctrine of 'Pratityasamutpada' (Dependent Origination), which asserts that all phenomena arise in dependence upon causes, is articulated in which section of the Tripitaka?\n(a) Vinaya Pitaka\n(b) Sutta Pitaka\n(c) Abhidhamma Pitaka\n(d) Jatakas\nCorrect Answer: (b) Sutta Pitaka [Explanation: The core philosophical discourses of the Buddha, including Pratityasamutpada and the Four Noble Truths, are preserved in the Sutta Pitaka (notably the Samyutta Nikaya).]",
      "Q3. The historic split of Jainism into two primary traditions—Digambara and Svetambara—originated during a devastating famine in Magadha led by which respective teachers?\n(a) Bhadrabahu and Sthulabhadra\n(b) Mahavira and Parshvanatha\n(c) Hemachandra and Haribhadra\n(d) Vasumitra and Nagarjuna\nCorrect Answer: (a) Bhadrabahu and Sthulabhadra [Explanation: During the 12-year Magadhan famine under Chandragupta Maurya, Bhadrabahu led followers to Shravanabelagola maintaining strict nudity (Digambara), while Sthulabhadra stayed in the north adopting white robes (Svetambara).]",
      "Q4. Which royal patron hosted the Third Buddhist Council at Pataliputra, where the Abhidhamma Pitaka was completed and the 'Kathavatthu' incorporated?\n(a) Ajatashatru\n(b) Kalasoka\n(c) Ashoka Maurya\n(d) Kanishka\nCorrect Answer: (c) Ashoka Maurya [Explanation: Emperor Ashoka convened the Third Buddhist Council at Pataliputra around 250 BCE presided over by Moggaliputta Tissa to purge monastic corruption and finalize the Theravada canon.]",
      "Q5. The philosophical concept of 'Syadvada' (the theory of conditioned or qualified predication with seven-fold nuances) is a distinctive hallmark of:\n(a) Buddhism\n(b) Ajivika\n(c) Charvaka\n(d) Jainism\nCorrect Answer: (d) Jainism [Explanation: Syadvada (the logic of seven perspectives: Saptabhangi Naya) is a fundamental epistemological doctrine of Jainism asserting that truth is contextual and relative.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-04",
    "filename": "04_rise_of_magadha_and_pre_mauryan_dynasties",
    "title": "Imperial Ascendancy of Magadha: Haryankas, Shishunagas & Nandas",
    "mapping": "History and Culture of India: Rise of Magadha - Geographical and Material Factors, Dynastic Matrix (Haryanka, Shishunaga, Nanda), Persian and Macedonian Invasions.",
    "intro": "Between the 6th and 4th centuries BCE, the kingdom of Magadha outpaced rival Mahajanapadas (Kosala, Vatsa, Avanti) to emerge as India's first pan-regional imperial nucleus. Ruled successively by the Haryanka, Shishunaga, and Nanda dynasties, Magadha built a massive standing army, perfected riverine warfare, and laid the administrative groundwork for the Mauryan Empire.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/3/36/Rajgir_Cyclopean_Wall.jpg", "caption": "The ancient Cyclopean Wall of Rajgir (Rajagriha), the first fortified hill capital of Magadha.", "alt": "Cyclopean dry-stone wall in Rajgir"},
    "table": {
      "caption": "Chronological Trajectory of Magadhan Imperial Consolidation",
      "headers": ["Dynasty & Eras", "Prominent Monarchs", "Strategic Milestones & Innovations", "Capitals & Infrastructure"],
      "rows": [
        ["Haryanka Dynasty (c. 544–412 BCE)", "Bimbisara, Ajatashatru, Udayin", "Bimbisara expanded through matrimonial alliances (Kosala, Lichchhavi, Madra); Ajatashatru defeated Vajji using catapults (Mahashilakantaka) and armored chariots (Rathamusala).", "Rajagriha (protected by 5 hills); Udayin shifted capital to Pataliputra at the confluence of Ganga, Son, and Gandak."],
        ["Shishunaga Dynasty (c. 412–344 BCE)", "Shishunaga, Kalasoka (Kakavarna)", "Shishunaga permanently subdued the 100-year-old arch-rival kingdom of Avanti (Pradyota dynasty); Kalasoka convened the Second Buddhist Council at Vaishali (383 BCE).", "Alternated between Pataliputra and Vaishali."],
        ["Nanda Dynasty (c. 344–322 BCE)", "Mahapadma Nanda ('Ekarat', 'Sarvakshatrantaka'), Dhana Nanda", "First non-Kshatriya empire; dismantled all traditional Kshatriya lineages; accumulated enormous treasury; maintained vast standing army (200k infantry, 20k cavalry, 3k war elephants).", "Pataliputra; established a centralized revenue collection bureaucracy under Amatyas."],
        ["Foreign Invasions (6th–4th C BCE)", "Darius I (Persia), Alexander of Macedon", "Darius annexed Indus valley as 20th Satrapy (introduced Kharosthi script); Alexander defeated Porus at Hydaspes (326 BCE) but mutinying Greek troops refused to advance against the Nandas.", "Opened direct land and sea communication routes between India and the Greco-Persian world."]
      ]
    },
    "bullets": [
      "Geographical Determinants: Strategic natural defenses of Rajgir (ringed by five hills) and Pataliputra (Jaladurga / water fortress at river confluences); dense Gangetic alluvium yielding bumper paddy harvests.",
      "Mineral Wealth & Technology: Control over rich iron ore deposits of Chota Nagpur (near modern Jamshedpur) enabled manufacturing superior iron weapons and agricultural ploughshares.",
      "Military Factor - War Elephants: First Indian state to deploy large formations of trained war elephants sourced from nearby eastern forests, smashing wooden fortifications and cavalry charges.",
      "Impact of Alexander's Invasion: Shattered petty northwestern tribal republics, creating a political vacuum that enabled Chandragupta Maurya and Chanakya to liberate the Indus basin and overthrow Dhana Nanda."
    ],
    "mains": [
      "Evaluate the strategic, economic, and military factors that enabled Magadha to establish imperial hegemony over all other Mahajanapadas. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Analyze Magadha's geographical vantage (Rajgir's natural hill fortress and Pataliputra's river junction); explain material advantages: iron ore mines of southern Bihar enabling cutting-edge arms, dense forests providing war elephants, fertile Gangetic soil generating regular taxation; assess leadership of Bimbisara (diplomacy), Ajatashatru (military inventions like Rathamusala), and Mahapadma Nanda (unified pan-Indian sovereignty)."
    ],
    "mcqs": [
      "Q1. Who among the Magadhan rulers founded the new imperial capital city of Pataliputra at the strategic confluence of the Ganga and Son rivers?\n(a) Bimbisara\n(b) Ajatashatru\n(c) Udayin\n(d) Kalasoka\nCorrect Answer: (c) Udayin [Explanation: Udayin (son of Ajatashatru) established the city of Pataliputra (Patna) and shifted the Magadhan royal capital permanently from Rajagriha.]",
      "Q2. Which ancient Indian emperor assumed the imperial titles 'Sarvakshatrantaka' (Uprooter of all Kshatriyas) and 'Ekarat' (Sole Monarch)?\n(a) Bimbisara\n(b) Mahapadma Nanda\n(c) Chandragupta Maurya\n(d) Pushyamitra Sunga\nCorrect Answer: (b) Mahapadma Nanda [Explanation: Mahapadma Nanda, the founder of the Nanda dynasty, destroyed the ancient Kshatriya ruling houses and crowned himself 'Ekarat' as India's first empire-builder.]",
      "Q3. In his war against the republican Lichchhavis of Vaishali, Ajatashatru introduced which two formidable military technological innovations?\n(a) Matchlock rifles and Iron cannon\n(b) Rathamusala and Mahashilakantaka\n(c) Greek fire and War galleys\n(d) Crossbows and Ballistas\nCorrect Answer: (b) Rathamusala and Mahashilakantaka [Explanation: Ajatashatru deployed the Rathamusala (a scythed chariot with spinning blades) and the Mahashilakantaka (a siege catapult for slinging large stone boulders) to overcome Vaishali.]",
      "Q4. In 326 BCE, the army of Alexander the Great reached the banks of which river before his mutinous soldiers refused to march eastward against the mighty Nanda empire?\n(a) Jhelum (Hydaspes)\n(b) Chenab (Acesines)\n(c) Beas (Hyphasis)\n(d) Ravi (Hydraotes)\nCorrect Answer: (c) Beas (Hyphasis) [Explanation: At the river Beas (Hyphasis), exhausted Macedonian soldiers struck and refused to advance further eastward, forcing Alexander to turn back.]",
      "Q5. The earliest foreign political inscription in India that mentions Indian troops ('Hindush') serving in the Persian imperial army is found in the records of:\n(a) Cyrus the Great\n(b) Darius I\n(c) Xerxes\n(d) Alexander\nCorrect Answer: (b) Darius I [Explanation: Inscriptions at Behistun, Persepolis, and Naqsh-e-Rustam of Persian Achaemenid Emperor Darius I (522–486 BCE) attest that 'Gandhara' and 'Hindush' constituted the richest 20th satrapy of the empire.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-05",
    "filename": "05_mauryan_empire_administration_and_ashoka",
    "title": "Mauryan Empire: Centralized Administration, Arthashastra & Ashoka's Dhamma",
    "mapping": "History and Culture of India: The Mauryan Empire - Chandragupta Maurya, Kautilya's Arthashastra, Megasthenes' Indica, Imperial Administration, Ashoka's Dhamma, Art, Architecture and Edicts.",
    "intro": "Founded by Chandragupta Maurya in 322 BCE with the guidance of Chanakya (Kautilya), the Mauryan Empire established India's first subcontinental centralized administrative state. Reaching its zenith under Ashoka the Great (268–232 BCE), the empire combined rigorous bureaucratic control with an innovative paternalistic statecraft based on moral universalism ('Dhamma').",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Ashoka_Pillar_at_Vaishali.jpg", "caption": "Ashokan Pillar at Kolhua, Vaishali, demonstrating monolithic polished sandstone masonry and the royal lion capital.", "alt": "Monolithic sandstone Ashoka pillar with lion capital"},
    "table": {
      "caption": "Administrative Machinery of the Mauryas (Arthashastra & Indica)",
      "headers": ["Departmental Tier", "Key Institutional Functionaries", "Administrative Role & Legal Jurisdiction"],
      "rows": [
        ["Central Government", "King & Mantriparishad; Saptanga State Theory (Swami, Amatya, Janapada, Durga, Kosa, Danda, Mitra).", "Samaharta (Chief Tax Assessor & Collector), Sannidhata (Treasurer), Akshapataladhyaksha (Accountant General)."],
        ["Espionage Network", "Sanstha (Stationary spies) and Sanchara (Roving spies).", "Gudhapurushas, Vishakanyas, and secret agents reporting directly to the emperor on bureaucratic integrity and public sentiment."],
        ["Military Organization", "War Commission of 30 members divided into 6 boards of 5 members each.", "Infantry, Cavalry, War Elephants, Chariots, Navy, and Military Transport/Commissariat."],
        ["Municipal Governance", "City Commission of Pataliputra (30 members across 6 boards).", "Regulated artisans, recorded births and deaths, licensed merchants, inspected trade weights, and collected 10% sales tax."],
        ["Provincial & Local", "Kumara / Aryaputra (Royal Princes) governing provinces (Taxila, Ujjain, Suvarnagiri, Tosali).", "Rajjukas (district land measurement and civil justice), Gopa (accountant of 5–10 villages), Gramika (village headman)."]
      ]
    },
    "bullets": [
      "Ashoka's Policy of Dhamma: Rooted in moral universalism rather than sectarian Buddhism; aimed at civic harmony across diverse ethnic domains; denounced animal sacrifice, promoted filial piety, reverence for ascetics, kind treatment of servants, and inter-religious tolerance (Major Rock Edict XII).",
      "Kalinga War (261 BCE, Major Rock Edict XIII): Turning point that resulted in renouncing 'Bherighosha' (conquest by war) in favor of 'Dhammaghosha' (conquest by moral virtue).",
      "Ashokan Edicts Classification: 14 Major Rock Edicts, Minor Rock Edicts, 7 Pillar Edicts, and Cave Inscriptions; inscribed in Prakrit (Brahmi and Kharosthi scripts) as well as Greek and Aramaic (Kandahar bilingual edict).",
      "Mauryan Art & Architecture: Highly polished monolithic sandstone pillars (Chunar sandstone), Sarnath Lion Capital (National Emblem of India), rock-cut Barabar Caves (Sudama and Lomas Rishi caves gifted to Ajivikas), and Yaksha/Yakshini sculptures (Didarganj Yakshini)."
    ],
    "mains": [
      "Critically evaluate Ashoka's policy of Dhamma. Was it a state-promoted Buddhist religious propaganda or an enlightened socio-political instrument of imperial integration? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define Dhamma through Ashoka's Rock Edicts (II, VII, XI, XII) emphasizing universal humanitarian ethics rather than specific Buddhist rituals; argue against sectarian propaganda: lack of mention of Nirvana, Four Noble Truths, or Eightfold Path; explain socio-political utility: integrating a sprawling empire of Greeks, tribal forest-dwellers, Buddhists, Brahmins, and Jains; conclude that Dhamma was an ideological cement maintaining political cohesion without military repression."
    ],
    "mcqs": [
      "Q1. Which Major Rock Edict of Ashoka contains his famous call for religious tolerance and mutual respect among all sects ('Samavaya eva sadhuh')?\n(a) Major Rock Edict V\n(b) Major Rock Edict VIII\n(c) Major Rock Edict XII\n(d) Major Rock Edict XIII\nCorrect Answer: (c) Major Rock Edict XII [Explanation: Major Rock Edict XII is the landmark declaration of inter-faith tolerance, condemning self-praise of one's own sect and urging dialogue and mutual understanding across all religions.]",
      "Q2. In Kautilya's Arthashastra, which high-ranking official was designated as the Collector-General of Revenue responsible for fiscal planning and taxation?\n(a) Sannidhata\n(b) Samaharta\n(c) Vyavaharika\n(d) Pradeshta\nCorrect Answer: (b) Samaharta [Explanation: In the Mauryan administrative hierarchy, the Samaharta oversaw revenue assessment and tax collection, whereas the Sannidhata served as the custodian of the royal treasury.]",
      "Q3. The bilingual rock inscription of Ashoka written in both Greek and Aramaic scripts was discovered at which northwestern frontier site?\n(a) Shahbazgarhi\n(b) Mansehra\n(c) Kandahar\n(d) Taxila\nCorrect Answer: (c) Kandahar [Explanation: The Kandahar bilingual rock inscription in southern Afghanistan was carved in classical Greek and Aramaic to communicate Ashoka's Dhamma to local Hellenistic and Persian populations.]",
      "Q4. Megasthenes, the Seleucid ambassador to the court of Chandragupta Maurya, famously recorded in his 'Indica' that Indian society was divided into how many classes?\n(a) Four classes\n(b) Five classes\n(c) Seven classes\n(d) Nine classes\nCorrect Answer: (c) Seven classes [Explanation: Megasthenes classified Mauryan society into seven distinct functional groups: Philosophers, Farmers, Herdsmen/Hunters, Artisans/Traders, Soldiers, Overseers/Spies, and Councillors/Magistrates.]",
      "Q5. Which rock-cut caves, noted for their glass-like mirror polish on granite interiors, were gifted by Ashoka to the non-theistic Ajivika sect?\n(a) Kanheri Caves\n(b) Barabar Caves\n(c) Udayagiri Caves\n(d) Bagh Caves\nCorrect Answer: (b) Barabar Caves [Explanation: In the Barabar Hills near Gaya, Ashoka and his grandson Dasharatha dedicated granite rock-cut shrines (such as the Lomas Rishi and Sudama caves) to ascetics of the Ajivika order.]"
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
  
  # Calculate word count
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
  
  # Save JSON
  json_path = os.path.join(SUBJ_DIR, f"{t['filename']}.json")
  with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    
  # Save Markdown
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

print("Part 1 of Subject 1 generated successfully")
