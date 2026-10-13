import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "03_Geography_India_and_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-GEOG-06",
    "filename": "06_mineral_and_energy_resources_india_and_ap",
    "title": "Mineral & Energy Resources of India & AP: Barytes, Bauxite, Uranium & KG Basin",
    "mapping": "Geography of India & Andhra Pradesh: Economic Geography - Mineral Resources (Barytes at Mangampeta, Bauxite, Limestone, Heavy Mineral Beach Sands, Tummalapalle Uranium), Energy Resources (Krishna-Godavari Basin Gas, Thermal, Solar).",
    "intro": "Andhra Pradesh is recognized as the 'Mineral Storehouse of South India', possessing vast non-metallic and strategic mineral reserves. The state holds 97% of India's barytes (Mangampeta in Kadapa), world-class bauxite deposits in the Eastern Ghats, extensive cement-grade limestone across the Palnadu and Kurnool formations, the Tummalapalle uranium reserves, and the deepwater offshore hydrocarbon fields of the Krishna-Godavari (KG) Basin.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Baryte_mineral.jpg", "caption": "High-grade bedded barytes crystal from the Mangampeta mines in YSR Kadapa district.", "alt": "Barytes mineral rock specimen"},
    "table": {
      "caption": "Key Mineral & Energy Reserves in Andhra Pradesh",
      "headers": ["Mineral / Resource", "Key Geological Locations in AP", "Reserve Status & National Share", "Industrial & Strategic Applications"],
      "rows": [
        ["Barytes (Barium Sulphate)", "Mangampeta, YSR Kadapa district (Cuddapah Basin).", "Contains 97% of India's and 28% of the world's bedded barytes reserves.", "Crucial weighting agent in deep oil and gas drilling muds; barium chemical industries."],
        ["Bauxite (Aluminium Ore)", "Eastern Ghats belt: Araku, Chintapalli, Ananthagiri (ASR & Visakhapatnam districts).", "Second largest bauxite reserves in India (over 600 million tonnes of gibbsitic ore).", "Raw material for alumina refineries and aluminium smelting."],
        ["Limestone (Cement Grade)", "Palnadu (Guntur), Kurnool, YSR Kadapa, Anantapur.", "One of India's leading producers; vast Narji limestone beds.", "Major cement production hub of South India (cement capital at Macherla/Tadipatri)."],
        ["Uranium (Nuclear Fuel)", "Tummalapalle, Vemula mandal, YSR Kadapa district.", "One of the largest uranium reserves in the world (estimated 150,000+ tonnes of U3O8).", "Domestic fuel feed for India's nuclear power reactors (NPCIL)."],
        ["Heavy Mineral Beach Sands", "Bhavanapadu (Srikakulam), Bheemunipatnam (Vizag), Nizampatnam.", "Rich in Monazite (thorium source), Ilmenite, Rutile, Zircon, Garnet.", "Atomic minerals, titanium pigment, aerospace alloys, coastal sand mining."],
        ["Natural Gas & Crude Oil", "Krishna-Godavari (KG) Offshore Basin (KG-D6, Ravva field).", "Deepwater offshore sedimentary basin; major discoveries by ONGC and Reliance.", "Power generation, fertilizer production, City Gas Distribution, and national energy security."]
      ]
    },
    "bullets": [
      "Mangampeta Barytes Deposit: Unique volcanogenic bedded deposit discovered by Geological Survey of India; mined by Andhra Pradesh Mineral Development Corporation (APMDC); exported globally to Gulf oil fields.",
      "Tummalapalle Uranium Mine: Operated by Uranium Corporation of India Limited (UCIL); hosted in dolostone rocks of the Vempalle formation; low to medium-grade ore accessible through underground decline mining.",
      "Renewable Energy Leadership: Kurnool Ultra Mega Solar Park (1,000 MW, one of the world's pioneering single-location solar parks); Ananthapuramu Solar Park (1,500 MW); pumped storage hydro projects (Pinnapuram Integrated Renewable Energy Project).",
      "Thermal Power Hubs: Dr. Narla Tata Rao Thermal Power Station (VTPS, Ibrahimpatnam), Sri Damodaram Sanjeevaiah Thermal Power Station (Krishnapatnam), NTPC Simhadri (Visakhapatnam)."
    ],
    "mains": [
      "Analyze the spatial distribution of major mineral resources in Andhra Pradesh. Examine the strategic and industrial significance of the Mangampeta barytes and Tummalapalle uranium deposits. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Map out AP's mineral wealth across the Cuddapah Basin and Eastern Ghats; detail Mangampeta: world's premier bedded barytes reserve mined by APMDC, indispensable for global petroleum drilling muds generating substantial export revenue; analyze Tummalapalle: massive uranium ore discovery in Kadapa reducing India's dependence on imported yellowcake for civil nuclear reactors; evaluate KG Basin natural gas infrastructure; discuss environmental safeguards against illegal sand and bauxite mining in tribal agency tracts."
    ],
    "mcqs": [
      "Q1. The world's largest single deposit of bedded barytes, accounting for over 97% of India's total reserves, is located at which site in Andhra Pradesh?\n(a) Tummalapalle\n(b) Mangampeta\n(c) Bheemunipatnam\n(d) Macherla\nCorrect Answer: (b) Mangampeta [Explanation: Mangampeta in YSR Kadapa district possesses the world's largest known bedded barytes deposit, mined open-cast by the APMDC.]",
      "Q2. The massive domestic uranium deposit discovered by the Atomic Minerals Directorate and mined by UCIL is situated at Tummalapalle in which district of AP?\n(a) Kurnool\n(b) YSR Kadapa\n(c) Anantapur\n(d) Chittoor\nCorrect Answer: (b) YSR Kadapa [Explanation: Tummalapalle in YSR Kadapa district holds one of the largest uranium reserves in the world, with confirmed deposits exceeding 150,000 tonnes.]",
      "Q3. Which major deepwater offshore sedimentary basin in coastal Andhra Pradesh holds vast natural gas reserves, including the historic KG-D6 gas field?\n(a) Cauvery Basin\n(b) Krishna-Godavari (KG) Basin\n(c) Mahanadi Basin\n(d) Cambay Basin\nCorrect Answer: (b) Krishna-Godavari (KG) Basin [Explanation: The Krishna-Godavari (KG) offshore basin holds India's premier deepwater natural gas and crude reserves, operated by ONGC and Reliance.]",
      "Q4. Heavy mineral beach sands along the coastal belt of Srikakulam and Visakhapatnam contain rich concentrations of 'Monazite', which is the primary source of:\n(a) Uranium\n(b) Thorium\n(c) Titanium\n(d) Beryllium\nCorrect Answer: (b) Thorium [Explanation: Monazite beach sand contains rich concentrations of Thorium and rare earth elements, vital for the third stage of India's nuclear power programme.]",
      "Q5. The 1,000 MW Kurnool Ultra Mega Solar Park, one of the earliest mega single-location solar power installations in India, is situated in which mandal?\n(a) Orvakal\n(b) Bethamcherla\n(c) Banaganapalle\n(d) Dhone\nCorrect Answer: (a) Orvakal [Explanation: The 1,000 MW Kurnool Solar Park is situated across Orvakal mandal in Kurnool district, commissioned over 5,900 acres.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-07",
    "filename": "07_industrial_regions_and_infrastructure_corridors",
    "title": "Industrial Regions & Corridors of AP: VCIC, CBIC & Major Ports",
    "mapping": "Geography of India & Andhra Pradesh: Economic Infrastructure - Industrial Corridors (Visakhapatnam-Chennai Industrial Corridor - VCIC, Chennai-Bengaluru Industrial Corridor - CBIC), Major Ports (Visakhapatnam, Krishnapatnam, Gangavaram), Special Economic Zones and Logistics.",
    "intro": "Andhra Pradesh occupies a prime geostrategic gateway position on India's eastern seaboard, serving as the multimodal logistics hub connecting the hinterland to Southeast Asia. Driven by two national industrial economic corridors—the Visakhapatnam-Chennai Industrial Corridor (VCIC) and the Chennai-Bengaluru Industrial Corridor (CBIC)—and a network of deep-water ports (Visakhapatnam, Krishnapatnam, Gangavaram, Ramayapatnam), the state is accelerating port-led industrialization.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Visakhapatnam_Port.jpg", "caption": "The deepwater Outer Harbour of Visakhapatnam Port, India's premier public maritime gateway on the east coast.", "alt": "Visakhapatnam Port container cargo terminal"},
    "table": {
      "caption": "Industrial Nodes & Corridors in Andhra Pradesh",
      "headers": ["Industrial Corridor / Node", "Geographical Coverage & Anchor Nodes", "Key Priority Sectors", "Multimodal Connectivity & Financing"],
      "rows": [
        ["Visakhapatnam-Chennai Industrial Corridor (VCIC)", "Spans 800 km along coastal AP (part of East Coast Economic Corridor - ECEC). Nodes: Visakhapatnam, Kakinada, Machilipatnam, Srikalahasti-Yerpedu.", "Heavy engineering, petrochemicals, pharmaceuticals, textiles, automobiles, electronics.", "Financed by Asian Development Bank (ADB); National Highway 16 and dedicated freight lines."],
        ["Chennai-Bengaluru Industrial Corridor (CBIC)", "Southern Rayalaseema; Anchor node: Krishnapatnam Industrial Node (Orvakal in Kurnool).", "Automobiles, aerospace, defense manufacturing, electronics, heavy engineering.", "Supported by Japan International Cooperation Agency (JICA); linked to Krishnapatnam Port."],
        ["Major & Non-Major Maritime Ports", "Major: Visakhapatnam Port (natural harbour). Non-Major: Krishnapatnam, Gangavaram, Kakinada Deepwater; Greenfield: Ramayapatnam, Bhavanapadu (Mulapeta), Machilipatnam.", "Dry bulk (coal, iron ore), liquid cargo (crude oil, petroleum), containerized cargo, marine products.", "Coastal shipping under Sagarmala Project; deep drafts (18m+) handling Capesize vessels."],
        ["Petroleum, Chemicals & Petrochemicals (PCPIR)", "Visakhapatnam-Kakinada coastal belt (covers 603 sq km).", "Petroleum refining, polymers, specialty chemicals, fertilizers.", "Anchored by HPCL refinery and Kakinada SEZ."]
      ]
    },
    "bullets": [
      "Jawaharlal Nehru Pharma City (JNPC, Parawada): India's premier bulk drug and pharmaceutical manufacturing park in Visakhapatnam, housing global giants like Pfizer, Mylan, and Reddy's.",
      "Sri City Special Economic Zone: Located on the AP-Tamil Nadu border in Tirupati district; integrated multi-product industrial hub housing 200+ global manufacturing MNCs (Alstom metro coaches, Isuzu, Foxconn, Daikin, Mondelez).",
      "Visakhapatnam Steel Plant (Rashtriya Ispat Nigam Limited - RINL): India's first shore-based integrated steel plant; operates 7.3 MTPA liquid steel capacity.",
      "Automobile Clusters: Anantapur automotive manufacturing cluster anchored by Kia Motors India (Erandahalli plant producing Seltos and Sonet)."
    ],
    "mains": [
      "Evaluate the strategic importance of the Visakhapatnam-Chennai Industrial Corridor (VCIC) and port-led development in transforming Andhra Pradesh into a manufacturing and logistics powerhouse. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Position AP along the Bay of Bengal as the gateway to ASEAN under India's Act East Policy; detail the VCIC framework (ADB funded) with four priority industrial nodes (Visakhapatnam, Chittoor/Yerpedu, Donakonda, Machilipatnam); analyze port infrastructure: synergy of major (Vizag) and non-major private ports (Krishnapatnam, Gangavaram) providing deep drafts and container handling; examine anchor clusters: pharmaceutical hub at Parawada, electronic and auto hubs at Sri City and Anantapur (Kia); discuss challenges: land acquisition, water supply, and environmental coastal zone compliance."
    ],
    "mcqs": [
      "Q1. Which multilateral financial development institution is the primary funding partner for the Visakhapatnam-Chennai Industrial Corridor (VCIC)?\n(a) World Bank\n(b) Asian Development Bank (ADB)\n(c) New Development Bank (NDB)\n(d) Asian Infrastructure Investment Bank (AIIB)\nCorrect Answer: (b) Asian Development Bank (ADB) [Explanation: The Asian Development Bank (ADB) is the lead partner financing the VCIC, which is the first phase of the East Coast Economic Corridor (ECEC).]",
      "Q2. The world-class integrated multi-product industrial city and Special Economic Zone 'Sri City' is strategically located in which district of Andhra Pradesh?\n(a) Visakhapatnam\n(b) Tirupati (Sathyavedu)\n(c) Guntur\n(d) Kurnool\nCorrect Answer: (b) Tirupati (Sathyavedu) [Explanation: Sri City is situated in Sathyavedu constituency of Tirupati district on NH-16, adjoining the Tamil Nadu border, housing global manufacturing enterprises.]",
      "Q3. India's first shore-based integrated steel manufacturing plant, Rashtriya Ispat Nigam Limited (RINL), is situated at:\n(a) Machilipatnam\n(b) Visakhapatnam\n(c) Kakinada\n(d) Krishnapatnam\nCorrect Answer: (b) Visakhapatnam [Explanation: Visakhapatnam Steel Plant (Vizag Steel / RINL) was commissioned in 1990 as India's first coastal shore-based integrated steel plant.]",
      "Q4. Which private deepwater port in Andhra Pradesh, developed on the coast of SPSR Nellore district, is among the fastest-growing modern container and bulk cargo ports?\n(a) Kakinada Port\n(b) Krishnapatnam Port\n(c) Bhavanapadu Port\n(d) Nizampatnam Port\nCorrect Answer: (b) Krishnapatnam Port [Explanation: Krishnapatnam Port (operated by Adani Ports) in Nellore is a major deepwater, all-weather automated commercial port on the east coast.]",
      "Q5. The multinational automobile manufacturing facility of Kia Motors India is established at Erandahalli in which district of Andhra Pradesh?\n(a) Chittoor\n(b) Anantapur (Sri Sathya Sai)\n(c) YSR Kadapa\n(d) Kurnool\nCorrect Answer: (b) Anantapur (Sri Sathya Sai) [Explanation: Kia Motors set up its $1.1 billion integrated car manufacturing facility at Penukonda/Erandahalli in Sri Sathya Sai (Anantapur) district in 2017.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-08",
    "filename": "08_population_demographics_and_urbanization_ap",
    "title": "Demographic Profile & Tribal Communities of Andhra Pradesh",
    "mapping": "Geography of India & Andhra Pradesh: Social Demography - Census Trends (Population, Density, Sex Ratio, Literacy), Scheduled Tribes of AP (Particularly Vulnerable Tribal Groups - PVTGs: Chenchus, Kondareddis, Kolams), Urbanization Patterns.",
    "intro": "The demographic profile of Andhra Pradesh reflects advanced stages of the demographic transition, characterized by a declining total fertility rate (TFR below replacement level at 1.5), an aging population structure, and expanding urbanization. The state also harbors rich indigenous anthropological heritage, being home to 33 Scheduled Tribe communities including seven Particularly Vulnerable Tribal Groups (PVTGs) inhabiting the Eastern Ghats and Nallamala forests.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Chenchu_tribe.jpg", "caption": "Members of the indigenous Chenchu tribe, a Particularly Vulnerable Tribal Group (PVTG) inhabiting the Nallamala forest ranges.", "alt": "Chenchu tribal family portrait"},
    "table": {
      "caption": "Demographic Indicators of Andhra Pradesh (Census 2011 & NFHS Data)",
      "headers": ["Indicator", "Andhra Pradesh Statistic", "All-India Average", "Comparative Demographic Significance"],
      "rows": [
        ["Total Population (2011)", "49.57 Million (Post-bifurcation residual AP).", "1.21 Billion", "Ranks 10th among Indian states by population."],
        ["Decadal Growth Rate (2001–11)", "9.21%", "17.70%", "Significantly lower than national average; rapid fertility transition."],
        ["Population Density", "304 persons per sq km.", "382 persons per sq km.", "Highest in Krishna (518) and West Godavari; lowest in Kadapa and Anantapur."],
        ["Sex Ratio", "997 females per 1,000 males.", "943 females per 1,000 males.", "Superior to national average; rural sex ratio exceeds 1,000 in several coastal districts."],
        ["Literacy Rate", "67.02% (Male: 74.8%, Female: 59.1%).", "73.00%", "Lower than national average; significant rural-urban and tribal literacy gap."],
        ["Urbanization Level", "29.47% urban population.", "31.16%", "Accelerating urbanization in Visakhapatnam, Vijayawada-Guntur, and Tirupati regions."]
      ]
    },
    "bullets": [
      "Particularly Vulnerable Tribal Groups (PVTGs) in AP: 7 designated PVTGs: Chenchus (Nallamalas), Konda Reddis (Godavari gorge/Papikondas), Kolams, Porjas, Khonds, Gadabas, and Savaras (Srikakulam); characterized by pre-agricultural technology, stagnant population, and low literacy.",
      "The Chenchu Community: Hunter-gatherer semi-nomadic tribe dwelling in the Nallamala forest tiger reserve (Nagarjunasagar-Srisailam); traditional gatherers of wild honey, gum, and medicinal herbs; speak Chenchu (Dravidian tongue).",
      "Yanadi Tribe: Inhabiting the coastal plains of Nellore, Bapatla, and Chittoor; traditional expertise in rodent catch, snake tracking, and fishing; historically linked to the Sriharikota missile launch station (SHAR) rehabilitation.",
      "Integrated Tribal Development Agencies (ITDAs): Functioning in Paderu (ASR district), Rampachodavaram, Seethampeta, K.R. Puram, and Srisailam (Chenchu ITDA) to safeguard tribal land rights under the 1/70 Land Transfer Regulation and PESA Act."
    ],
    "mains": [
      "Analyze the demographic trends of Andhra Pradesh based on Census data. Discuss the socio-economic vulnerabilities and constitutional safeguards for the Particularly Vulnerable Tribal Groups (PVTGs) in the state. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight AP's demographic milestones: sub-replacement fertility rate (TFR 1.5), decelerating decadal growth (9.2%), favorable sex ratio (997), and literacy challenges (67%); profile the PVTGs of AP (Chenchus, Konda Reddis, Gadabas, Savaras): geographic isolation in the Eastern Ghats, malnutrition, sickle cell anemia, and loss of ancestral forest rights; evaluate constitutional and legal protections: Fifth Schedule administration, Agency Land Transfer Regulation 1 of 1970 prohibiting alienation of tribal land to non-tribals, Forest Rights Act 2006 (FRA), and targeted ITDA livelihoods missions."
    ],
    "mcqs": [
      "Q1. According to the 2011 Census, what is the overall sex ratio (females per 1,000 males) for the state of Andhra Pradesh?\n(a) 943\n(b) 974\n(c) 997\n(d) 1004\nCorrect Answer: (c) 997 [Explanation: Andhra Pradesh recorded a healthy sex ratio of 997 females per 1,000 males in Census 2011, notably above the national average of 943.]",
      "Q2. Which indigenous Scheduled Tribe of Andhra Pradesh, classified as a PVTG, is traditionally forest-dwelling in the Nallamala hills and practices honey collection?\n(a) Lambada\n(b) Chenchu\n(c) Yerukula\n(d) Valmiki\nCorrect Answer: (b) Chenchu [Explanation: The Chenchus are an ancient hunter-gatherer Particularly Vulnerable Tribal Group inhabiting the Nallamala forests across Kurnool, Nalgonda, and Prakasam.]",
      "Q3. How many tribal communities in Andhra Pradesh are officially designated by the Government of India as Particularly Vulnerable Tribal Groups (PVTGs)?\n(a) 4\n(b) 7\n(c) 12\n(d) 15\nCorrect Answer: (b) 7 [Explanation: Andhra Pradesh has 7 designated PVTGs: Chenchus, Konda Reddis, Kolams, Khonds, Porjas, Savaras, and Gadabas.]",
      "Q4. Which landmark state regulation strictly prohibits the transfer of any land in Scheduled Agency tracts of Andhra Pradesh to non-tribal individuals?\n(a) Land Ceiling Act 1973\n(b) AP Agency Land Transfer Regulation 1 of 1970 (LTR 1/70)\n(c) PESA Act 1996\n(d) Forest Conservation Act\nCorrect Answer: (b) AP Agency Land Transfer Regulation 1 of 1970 (LTR 1/70) [Explanation: Regulation 1 of 1970 (amending 1959 regulations) created an absolute statutory presumption that all land in Agency tracts belongs to tribals, barring transfer to non-tribals.]",
      "Q5. Which district in residual Andhra Pradesh holds the highest population density per square kilometer according to the 2011 Census?\n(a) Visakhapatnam\n(b) Krishna\n(c) Guntur\n(d) East Godavari\nCorrect Answer: (b) Krishna [Explanation: In the 2011 Census, Krishna district recorded the highest population density in the state at 518 persons per sq km, driven by fertile deltaic agriculture and urban centers.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-09",
    "filename": "09_biodiversity_forests_and_protected_areas_ap",
    "title": "Biodiversity, Forests & Protected Areas of AP: Wetlands & Biosphere Reserves",
    "mapping": "Geography of India & Andhra Pradesh: Ecology & Biodiversity - National Parks and Sanctuaries (Nagarjunasagar-Srisailam Tiger Reserve, Papikonda, Sri Venkateswara), Seshachalam Biosphere Reserve, Wetlands (Kolleru, Pulicat).",
    "intro": "Andhra Pradesh encompasses critical ecological habitats within the Eastern Ghats and the Coromandel coast. The state is home to India's largest tiger reserve (Nagarjunasagar-Srisailam), the Seshachalam Biosphere Reserve, national parks at Papikonda and Sri Venkateswara, the coastal wetland of Kolleru Lake (Ramsar Site), and the Pulicat brackish lagoon, which host rare endemic wildlife such as the golden gecko, slender loris, and Jerdon's courser.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Tiger_Nagarjunasagar.jpg", "caption": "Royal Bengal Tiger in the Nagarjunasagar-Srisailam Tiger Reserve, the largest Project Tiger conservation tract in India.", "alt": "Royal Bengal Tiger in Nallamala forest"},
    "table": {
      "caption": "Protected Areas & Ecological Reserves of Andhra Pradesh",
      "headers": ["Protected Area / Sanctuary", "Location & Habitat Type", "Flagship / Endemic Wildlife Species", "Conservation Status & Global Significance"],
      "rows": [
        ["Nagarjunasagar-Srisailam Tiger Reserve (NSTR)", "Nallamala Hills (Palnadu, Prakasam, Nandyal); dry deciduous forest.", "Royal Bengal Tiger, Leopard, Dhole, Pangolin, Chenchu tribal habitat.", "Largest Tiger Reserve in India (3,728 sq km); Project Tiger anchor."],
        ["Seshachalam Biosphere Reserve", "Tirupati & YSR Kadapa districts; rocky sandstone gorges.", "Red Sanders (Pterocarpus santalinus), Slender Loris, Golden Gecko.", "Designated National Biosphere Reserve (2010); high plant endemism."],
        ["Papikonda National Park", "Godavari gorge, Alluri Sitharama Raju & Eluru districts; moist deciduous.", "Tiger, Leopard, Indian Gaur, Sambar, endemic butterflies.", "Submergence concerns under Polavaram dam backwaters."],
        ["Kolleru Lake Bird Sanctuary", "Between Godavari and Krishna deltas, Eluru district; freshwater wetland.", "Spot-billed Pelican, Painted Stork, Grey Heron, migratory waterfowl.", "Designated Ramsar Wetland of International Importance; 'Operation Kolleru' evicted illegal fish tanks."],
        ["Pulicat Lake Bird Sanctuary", "Nellore district (shared with Tamil Nadu); shallow brackish lagoon.", "Greater Flamingo, Black-tailed Godwit, Sea turtles, estuarine fishes.", "Second largest brackish water lagoon in India; hosts annual Flamingo Festival at Sullurpeta."]
      ]
    },
    "bullets": [
      "Jerdon's Courser (Rhinoptilus bitorquatus): Nocturnal cursorial bird thought extinct until rediscovered in 1986 in the Sri Lankamalleswara Wildlife Sanctuary (Kadapa district); critically endangered on the IUCN Red List.",
      "Golden Gecko (Calodactylodes aureus): Rare rock-dwelling endemic lizard found exclusively in the deep rocky ravines of the Seshachalam and Tirumala hills.",
      "Operation Kolleru (2006): Massive environmental restoration drive executed by the Supreme Court of India and AP Forest Department, demolishing illegal commercial aquaculture bunds across 15,000 acres to restore the natural hydrological flow of the Ramsar wetland.",
      "Mangrove Ecosystem at Coringa: Ramsar site candidate; supports 35 mangrove plant species (Avicennia, Rhizophora) and a thriving population of the rare fishing cat (Prionailurus viverrinus)."
    ],
    "mains": [
      "Examine the biodiversity hotspots and wetland ecosystems of Andhra Pradesh. Discuss the ecological degradation and restoration challenges of Kolleru Lake and Pulicat Lagoon. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Map out key ecological zones: Seshachalam Biosphere Reserve (Red Sanders, Golden Gecko), Nagarjunasagar-Srisailam Tiger Reserve (largest tiger habitat in India), and Papikonda National Park; analyze Kolleru Lake: freshwater wetland threatened by illegal encroachment of commercial fish ponds (aquaculture), fertilizer pesticide runoffs, and weed choking (Eichhornia); evaluate 'Operation Kolleru' in demolishing fish bunds and ongoing challenges of livelihood rehabilitation; examine Pulicat Lagoon: threats from port expansion, siltation, and shrinkage impacting migratory flamingo breeding; conclude on wetland conservation policies."
    ],
    "mcqs": [
      "Q1. Which is the largest Tiger Reserve in India by total surface area, spanning the Nallamala hill forests across Andhra Pradesh?\n(a) Jim Corbett Tiger Reserve\n(b) Nagarjunasagar-Srisailam Tiger Reserve (NSTR)\n(c) Bandipur Tiger Reserve\n(d) Simlipal Tiger Reserve\nCorrect Answer: (b) Nagarjunasagar-Srisailam Tiger Reserve (NSTR) [Explanation: The Nagarjunasagar-Srisailam Tiger Reserve, covering over 3,700 sq km in the Nallamala range, is the largest tiger reserve in India.]",
      "Q2. The critically endangered nocturnal bird 'Jerdon's Courser' was dramatically rediscovered in 1986 in which wildlife sanctuary of Andhra Pradesh?\n(a) Coringa Wildlife Sanctuary\n(b) Sri Lankamalleswara Wildlife Sanctuary\n(c) Rollapadu Bird Sanctuary\n(d) Kaundinya Sanctuary\nCorrect Answer: (b) Sri Lankamalleswara Wildlife Sanctuary [Explanation: Believed extinct for over 80 years, Jerdon's Courser was rediscovered in 1986 in Sri Lankamalleswara Wildlife Sanctuary in Kadapa.]",
      "Q3. Which freshwater lake in Andhra Pradesh was designated as a Ramsar Wetland of International Importance in 2002?\n(a) Pulicat Lake\n(b) Kolleru Lake\n(c) Kondakarla Ava\n(d) Kanwar Lake\nCorrect Answer: (b) Kolleru Lake [Explanation: Kolleru Lake was declared a Ramsar wetland in November 2002, functioning as a major breeding habitat for the Spot-billed Pelican and Painted Stork.]",
      "Q4. Sullurpeta in Tirupati (Nellore) district is famous for hosting which annual eco-tourism festival celebrating the arrival of thousands of migratory birds at Pulicat Lake?\n(a) Pelican Festival\n(b) Flamingo Festival\n(c) Hornbill Festival\n(d) Olive Ridley Festival\nCorrect Answer: (b) Flamingo Festival [Explanation: The annual Flamingo Festival is held at Sullurpeta and Nelapattu to celebrate the massive migration of Greater Flamingos to Pulicat Lagoon.]",
      "Q5. Rollapadu Wildlife Sanctuary in Nandyal/Kurnool district is dedicated primarily to the conservation of which critically endangered grassland bird?\n(a) Great Indian Bustard\n(b) Jerdon's Courser\n(c) Bengal Florican\n(d) Lesser Florican\nCorrect Answer: (a) Great Indian Bustard [Explanation: Rollapadu Wildlife Sanctuary in the semi-arid grasslands of Kurnool was established to protect the critically endangered Great Indian Bustard (Ardeotis nigriceps).]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-10",
    "filename": "10_natural_hazards_disaster_management_and_cyclones_ap",
    "title": "Natural Hazards & Disaster Management in AP: Cyclones & Coastal Resilience",
    "mapping": "Geography of India & Andhra Pradesh: Disaster Management - Natural Hazards in AP (Tropical Cyclones, Storm Surges, Floods, Droughts), Coastal Zone Vulnerability (CRZ), Early Warning Systems and APSDMA Institutional Framework.",
    "intro": "Due to its long coastline, low-lying river deltas, and peninsular proximity to the cyclonically active Bay of Bengal, Andhra Pradesh is among India's most hazard-prone states. The state confronts a dual hazard spectrum: recurrent destructive tropical cyclones, storm surges, and riverine floods in coastal districts, alongside persistent chronic droughts in interior Rayalaseema. In response, the Andhra Pradesh State Disaster Management Authority (APSDMA) has pioneered coastal shelters, real-time Doppler radar early warning, and disaster mitigation models.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cyclone_shelter_Andhra.jpg", "caption": "A multi-purpose cyclone shelter along coastal Andhra Pradesh, providing community refuge against storm surges.", "alt": "Multi-purpose cyclone shelter building"},
    "table": {
      "caption": "Disaster Profile & Institutional Response Matrix of Andhra Pradesh",
      "headers": ["Hazard Category", "High-Risk Districts in AP", "Key Causative Factors & Impacts", "Mitigation Measures & Institutional Strategy"],
      "rows": [
        ["Tropical Cyclones & Storm Surges", "Srikakulam, Vizianagaram, Visakhapatnam, East/West Godavari, Krishna, Bapatla, Prakasam, Nellore.", "Bay of Bengal depression systems; destructive winds (>150 km/h), torrential rains, and sea surges (3–6m) inundating coastal villages.", "Construction of 1,000+ Multipurpose Cyclone Shelters (NCRMP); shelterbelt mangrove plantations; real-time alert sirens."],
        ["Riverine & Urban Floods", "Godavari and Krishna deltas, Vijayawada, Rajahmundry.", "Monsoonal dam releases from upstream states (Srisailam, Dowleswaram); breaching of river embankments.", "Automated River Basin Inflow Forecasting; flood bund strengthening; desiltation of drains."],
        ["Chronic Droughts", "Rayalaseema (Anantapur, Kurnool, Kadapa, Chittoor) and Prakasam.", "Rain-shadow location; low erratic monsoons (<550 mm); high temperature and evapotranspiration; groundwater depletion.", "Handri-Neeva & Galeru-Nagari canal diversions; check dams; farm ponds (Panta Sanjeevani); drip/sprinkler micro-irrigation."],
        ["Coastal Erosion & Sea Ingress", "Visakhapatnam (RK Beach), Uppada (Kakinada), Nizampatnam.", "High-energy wave action, sea-level rise, destruction of natural sand dunes and mangrove buffers.", "Geotube seawall protection at Uppada; strict enforcement of Coastal Regulation Zone (CRZ) norms; mangrove reforestation."]
      ]
    },
    "bullets": [
      "APSDMA Institutional Framework: Headed by the Chief Minister; operates the State Emergency Operation Centre (SEOC) in Kunchanapalli, Guntur; collaborates with Indian Meteorological Department (IMD) Doppler Weather Radars (Visakhapatnam and Machilipatnam).",
      "National Cyclone Risk Mitigation Project (NCRMP): World Bank-assisted project implementing underground electrical cabling in coastal cities, multi-purpose cyclone shelters, saline embankments, and Early Warning Dissemination Systems (EWDS).",
      "The 1977 Diviseema Cyclone Benchmark: Catastrophic 6-meter storm surge in Krishna district killed 10,000+ people, completely revolutionizing India's disaster management paradigm from reactive relief to proactive disaster preparedness.",
      "Coastal Regulation Zone (CRZ 2019 Notification): Regulates developmental activities within 500 meters of the High Tide Line (HTL) to protect fragile coastal ecosystems and minimize cyclone storm surge damage."
    ],
    "mains": [
      "Critically evaluate the multi-hazard vulnerability of Andhra Pradesh with special focus on tropical cyclones and coastal storm surges. Discuss the institutional measures and community resilience initiatives deployed by APSDMA. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Analyze AP's geographic exposure: 974 km coastline along the cyclone-prone Bay of Bengal and low-lying deltas creating intense vulnerability to storm surges (cite 1977 Diviseema, 2014 Hudhud, 2018 Titli); explain the institutional shift: creation of APSDMA under Disaster Management Act 2005, moving from post-disaster charity to proactive risk reduction; detail mitigation infrastructure: NCRMP multipurpose cyclone shelters, Early Warning Dissemination System (EWDS) using cell broadcast sirens, underground power cabling, and bio-shields (mangroves at Coringa); examine community preparedness: Aapda Mitra volunteer training, evacuation protocols, and emergency relief prepositioning."
    ],
    "mcqs": [
      "Q1. The catastrophic 1977 Diviseema Cyclone, which killed over 10,000 people and revolutionized India's cyclone preparedness paradigm, made landfall in which district?\n(a) Visakhapatnam\n(b) Krishna (Diviseema)\n(c) SPSR Nellore\n(d) Srikakulam\nCorrect Answer: (b) Krishna (Diviseema) [Explanation: The 1977 Andhra cyclone generated a 6-meter tidal wave that engulfed Diviseema in Krishna district on 19 November 1977, driving the modern cyclone shelter program.]",
      "Q2. The State Emergency Operation Centre (SEOC) of the Andhra Pradesh State Disaster Management Authority (APSDMA) is headquartered at:\n(a) Visakhapatnam\n(b) Kunchanapalli (Guntur district)\n(c) Tirupati\n(d) Kurnool\nCorrect Answer: (b) Kunchanapalli (Guntur district) [Explanation: The state-of-the-art emergency operations center of APSDMA is situated at Kunchanapalli near Tadepalli in Guntur district.]",
      "Q3. Coastal village Uppada in Kakinada district is renowned in disaster engineering for implementing which innovative coastal protection measure against severe sea erosion?\n(a) Concrete Groynes\n(b) Geotextile Tube (Geo-tube) Seawall\n(c) Breakwater Atoll\n(d) Mangrove Lagoon Channel\nCorrect Answer: (b) Geotextile Tube (Geo-tube) Seawall [Explanation: Uppada implemented India's pioneering Geo-tube synthetic textile revetment to arrest rapid coastal erosion caused by high wave energy.]",
      "Q4. Under Coastal Regulation Zone (CRZ) regulations in India, how many meters from the High Tide Line (HTL) on the landward side are legally designated as a regulated coastal buffer zone?\n(a) 100 meters\n(b) 200 meters\n(c) 500 meters\n(d) 1000 meters\nCorrect Answer: (c) 500 meters [Explanation: The CRZ notification demarcates coastal stretches within 500 meters of the High Tide Line (HTL) as strictly regulated zones to conserve marine ecology.]",
      "Q5. Which community-based volunteer training programme is implemented by the National Disaster Management Authority (NDMA) and APSDMA to train local youth in emergency flood and cyclone rescue?\n(a) Aapda Mitra Scheme\n(b) Bharat Rakshak\n(c) Sagar Kavach\n(d) Jal Suraksha Doot\nCorrect Answer: (a) Aapda Mitra Scheme [Explanation: The 'Aapda Mitra' scheme trains grassroots community volunteers in disaster-prone districts with basic search, rescue, and first-aid skills to serve as first responders.]"
    ]
  }
]

for t in topics:
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "Geography of India & Andhra Pradesh",
    "paper": "Mains Paper-II (Section C) & Screening Paper-I (Section B)",
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

print("Part 2 of Subject 3 generated successfully")
