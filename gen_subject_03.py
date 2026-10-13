import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "03_Geography_India_and_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-GEOG-01",
    "filename": "01_physiography_and_geomorphology_of_india",
    "title": "Physiography of India & Andhra Pradesh: Structural Divisions & Geomorphology",
    "mapping": "Geography of India & Andhra Pradesh: Physical Geography - Major Physiographic Divisions of India (Himalayas, Northern Plains, Peninsular Plateau, Coastal Plains, Islands) and Geomorphology of Andhra Pradesh.",
    "intro": "The Indian subcontinent exhibits extraordinary geomorphological diversity shaped by plate tectonics—from the collision of the Indian and Eurasian plates giving birth to the young fold mountains of the Himalayas, to the ancient Archean peninsular shield. Andhra Pradesh is characterized by three distinct physiographic provinces: the Coastal Plains along its 974 km coastline, the dissected Eastern Ghats, and the semi-arid Rayalaseema plateau.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Eastern_Ghats_Araku.jpg", "caption": "The dissected ridges of the Eastern Ghats in the Araku Valley, Andhra Pradesh.", "alt": "Araku Valley Eastern Ghats landscape"},
    "table": {
      "caption": "Comparative Physiographic Profile of India and Andhra Pradesh",
      "headers": ["Physiographic Province", "Geological Age & Rock System", "Key Structural Ranges & Features", "Economic / Ecological Significance"],
      "rows": [
        ["Himalayan Mountain System", "Tertiary folding (Cenozoic); sedimentary & metamorphic.", "Himadri (Greater), Himachal (Lesser), Shiwaliks (Outer); highest peaks (Kanchenjunga, Nanda Devi).", "Perennial river headwaters, climatic barrier against Central Asian blizzards, tourism, hydro-electric potential."],
        ["Indo-Gangetic-Brahmaputra Plain", "Pleistocene alluvium deposition in foredeep basin.", "Bhabar (porous gravel), Tarai (marshy), Bhangar (older alluvium, kankar), Khadar (fertile floodplains).", "Agricultural heartland of India, intensive tubewell irrigation, maximum demographic concentration."],
        ["Peninsular Plateau", "Pre-Cambrian Archean crystalline shield (Gondwanaland).", "Deccan Trap (basaltic black soil), Malwa, Chota Nagpur plateau (mineral heartland), Western & Eastern Ghats.", "Richest mineral storehouse (iron, coal, bauxite); Western Ghats UNESCO biodiversity hotspot."],
        ["Coastal Plains & Eastern Ghats of AP", "Dharwar & Cuddapah formations; Coastal alluvium.", "Eastern Ghats (dissected by Godavari & Krishna; Armakonda / Jindhagada peak 1,690m), Coastal Plains (974 km coastline).", "Paddy agriculture in K-G delta, bauxite reserves in Visakhapatnam, major ports and coastal economic zones."]
      ]
    },
    "bullets": [
      "Armakonda (Jindhagada Peak): Situated in the Araku region of Alluri Sitharama Raju district; at 1,690 meters, it is the highest peak in the Eastern Ghats and Andhra Pradesh.",
      "Cuddapah Supergroup: Proterozoic crescent-shaped sedimentary basin in Rayalaseema; rich in limestone, quartzites, and the world's largest barytes deposits at Mangampeta.",
      "Coastal Geomorphology: Andhra Pradesh possesses the second-longest mainland coastline in India (974 km, after Gujarat); characterized by the twin deltaic protrusions of Godavari and Krishna with freshwater Kolleru lake and brackish Pulicat lagoon.",
      "Islands: Andaman and Nicobar volcanic/coral chain (Barren Island active volcano, Indira Point 6°45' N); Lakshadweep atoll archipelago in the Arabian Sea."
    ],
    "mains": [
      "Examine the major physiographic divisions of Andhra Pradesh and evaluate the ecological and mineral significance of the Eastern Ghats. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Divide AP into three physiographic units: Coastal Plains (974 km coast), Eastern Ghats (dissected by Godavari and Krishna into discontinuous hill blocks like Nallamalas, Erramalas, Seshachalam, Papi Hills), and the Rayalaseema Peneplain; evaluate the Eastern Ghats: mineral wealth (high-grade bauxite in Visakhapatnam, barytes in Kadapa), biodiversity (Seshachalam Biosphere Reserve, red sanders / Pterocarpus santalinus endemic to Rayalaseema), and water catchment feeding coastal rivers; discuss threats of deforestation and mining."
    ],
    "mcqs": [
      "Q1. Which is the highest mountain peak in the Eastern Ghats, situated in the Araku Valley region of Andhra Pradesh?\n(a) Mahendragiri\n(b) Jindhagada (Armakonda)\n(c) Doddabetta\n(d) Anamudi\nCorrect Answer: (b) Jindhagada (Armakonda) [Explanation: Jindhagada Peak (Armakonda), rising to 1,690 meters in the Visakhapatnam-Araku region, is the highest peak in the Eastern Ghats.]",
      "Q2. What is the total length of the mainland coastline of Andhra Pradesh, which ranks as the second longest in India?\n(a) 7516 km\n(b) 974 km\n(c) 1214 km\n(d) 580 km\nCorrect Answer: (b) 974 km [Explanation: Andhra Pradesh has a mainland coastline of 974 km, ranking second in India after Gujarat (1,214 km).]",
      "Q3. The crescent-shaped geological formation in Rayalaseema, renowned for massive deposits of limestone, slab stone, and barytes, is known as:\n(a) Gondwana Basin\n(b) Cuddapah Basin\n(c) Dharwar Craton\n(d) Vindhyan Basin\nCorrect Answer: (b) Cuddapah Basin [Explanation: The Proterozoic Cuddapah Basin is world-famous for its mineral wealth, containing the world's largest bedded barytes deposit at Mangampeta.]",
      "Q4. In the geomorphology of the Northern Plains of India, the narrow porous belt where Himalayan streams disappear underground into boulder gravels is termed:\n(a) Tarai\n(b) Bhabar\n(c) Bhangar\n(d) Khadar\nCorrect Answer: (b) Bhabar [Explanation: The Bhabar is an 8–10 km wide piedmont gravel belt along the Shiwalik foothills where streams sink and flow sub-surface before re-emerging in the wet Tarai.]",
      "Q5. Which island in the Andaman and Nicobar archipelago contains India's only confirmed active volcano?\n(a) Narcondam Island\n(b) Barren Island\n(c) Havelock Island\n(d) Neil Island\nCorrect Answer: (b) Barren Island [Explanation: Barren Island, situated 135 km northeast of Port Blair in the Andaman Sea, is the only active volcano in South Asia.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-02",
    "filename": "02_river_systems_and_drainage_india_and_ap",
    "title": "Drainage Systems of India & Andhra Pradesh: Rivers, Deltas & Interlinking",
    "mapping": "Geography of India & Andhra Pradesh: Drainage Systems - Himalayan (Ganga, Brahmaputra, Indus) vs Peninsular Rivers, River Basins of AP (Godavari, Krishna, Pennar, Vamsadhara, Nagavali), Polavaram & River Interlinking.",
    "intro": "India's drainage network is divided into perennial antecedent Himalayan river systems and rain-fed graded Peninsular river systems. In Andhra Pradesh, the drainage is dominated by the 'Dakshin Ganga' Godavari, the Krishna, the Pennar, and the north-coastal Vamsadhara and Nagavali rivers, which form fertile agricultural deltas and are central to landmark river-linking initiatives like the Pattiseema Lift Irrigation and the Polavaram Multipurpose Project.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Prakasam_Barrage.jpg", "caption": "The Prakasam Barrage on the Krishna River at Vijayawada, regulating delta canal irrigation networks.", "alt": "Prakasam Barrage across Krishna River at Vijayawada"},
    "table": {
      "caption": "Hydrological Matrix of Major River Basins in Andhra Pradesh",
      "headers": ["River Basin & Origin", "Length & Flow in AP", "Key Tributaries", "Major Multipurpose Projects in AP"],
      "rows": [
        ["Godavari ('Dakshin Ganga'; Trimbakeshwar, Maharashtra)", "1,465 km total (approx 580 km in AP/TG); drains 312,812 sq km.", "Manjira, Pranhita, Indravati, Sabari, Sileru.", "Polavaram Multipurpose National Project, Sir Arthur Cotton Barrage (Dowleswaram), Chintalapudi Lift."],
        ["Krishna (Mahabaleshwar, Maharashtra)", "1,400 km total (approx 450 km in AP/TG); drains 258,948 sq km.", "Koyna, Bhima, Tungabhadra, Ghataprabha, Malaprabha, Musi, Munneru.", "Srisailam Dam (hydro-electric), Nagarjuna Sagar (joint with TG), Prakasam Barrage (Vijayawada), Veligonda Project."],
        ["Pennar / Pinakini (Nandi Hills, Karnataka)", "597 km total (flows through Anantapur, Kadapa, Nellore).", "Jayamangali, Chitravati, Papagni, Cheyyeru, Kundu.", "Somasila Reservoir (Nellore), Mylavaram Dam, Gandikota Reservoir."],
        ["Vamsadhara & Nagavali (Eastern Ghats, Odisha)", "Vamsadhara (254 km), Nagavali (256 km); Srikakulam & Vizianagaram.", "Mahendratanaya, Suvarnamukhi, Vegavati.", "Gotta Barrage (Vamsadhara Stage II), Thotapalli Barrage on Nagavali."]
      ]
    },
    "bullets": [
      "Polavaram National Irrigation Project: Multipurpose project on Godavari river in Eluru district; includes an Earth-Cum-Rock-Fill (ECRF) dam, 960 MW hydro-power station, Left Canal (supplying water to Visakhapatnam industrial hub), and Right Canal.",
      "Pattiseema Lift Irrigation Project: India's first operational river-interlinking project (completed in record time in 2015), lifting 80 TMC of surplus Godavari flood waters from Pattiseema into the Polavaram Right Main Canal to discharge into the Krishna delta upstream of Prakasam Barrage.",
      "Himalayan vs Peninsular Drainage: Himalayan rivers are perennial, antecedent, prone to meandering and shifting courses (Kosi - 'Sorrow of Bihar'); Peninsular rivers are non-perennial, rain-dependent, flow through graded mature fault valleys with fixed channels.",
      "Deltaic Morphology: Godavari and Krishna form arcuate lobate deltas into the Bay of Bengal, sandwiching the shallow freshwater Kolleru Lake between their alluvium lobes."
    ],
    "mains": [
      "Examine the drainage network of Andhra Pradesh with special focus on the Godavari and Krishna basins. Analyze the significance of the Polavaram Project and river-interlinking in resolving Rayalaseema's water crisis. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Map out the major river basins of AP (Godavari, Krishna, Pennar, Vamsadhara); evaluate Godavari's surplus yield vs Krishna's deficit allocation; analyze the strategic significance of the Polavaram National Project (194 TMC capacity) providing drinking water to Vizag, generating 960 MW, and irrigating 7.2 lakh acres; explain the interlinking mechanism: diverting 80 TMC of Godavari water via Polavaram Right Canal to Krishna basin at Vijayawada, thereby releasing equivalent upstream Krishna waters from Srisailam for the drought-prone Rayalaseema region via Pothireddypadu head regulator and Handri-Neeva Sujala Sravanthi (HNSS)."
    ],
    "mcqs": [
      "Q1. Which multipurpose project in Andhra Pradesh executed the historic first operational river-linking in India by connecting the Godavari and Krishna rivers in 2015?\n(a) Polavaram Project\n(b) Pattiseema Lift Irrigation Project\n(c) Chintalapudi Project\n(d) Handri-Neeva Project\nCorrect Answer: (b) Pattiseema Lift Irrigation Project [Explanation: The Pattiseema Lift Irrigation Scheme on the Godavari lifted surplus waters into the Krishna basin at Ibrahimpatnam, achieving India's first functional river interlinking.]",
      "Q2. The Somasila Multipurpose Dam, the largest water reservoir constructed on the Pennar River, is located in which district of Andhra Pradesh?\n(a) YSR Kadapa\n(b) SPSR Nellore\n(c) Anantapur\n(d) Prakasam\nCorrect Answer: (b) SPSR Nellore [Explanation: The Somasila Dam is built across the Pennar River in Nellore district, storing 78 TMC of water for irrigation and drinking supplies.]",
      "Q3. Which major left-bank tributary of the Godavari River forms the boundary between Andhra Pradesh, Odisha, and Chhattisgarh before joining near Kunavaram?\n(a) Manjira\n(b) Sabari\n(c) Pranhita\n(d) Indravati\nCorrect Answer: (b) Sabari [Explanation: The Sabari River rises in the Sinkaram hills of Odisha and flows through AP, joining the Godavari at Kunavaram alongside its tributary, the Sileru.]",
      "Q4. Which natural freshwater lake in Andhra Pradesh is geographically sandwiched between the alluvial deltas of the Godavari and Krishna rivers?\n(a) Pulicat Lake\n(b) Kolleru Lake\n(c) Pakhal Lake\n(d) Kondakarla Ava\nCorrect Answer: (b) Kolleru Lake [Explanation: Kolleru Lake, designated as a Ramsar wetland, is one of the largest freshwater lakes in India, located between the Godavari and Krishna deltas in Eluru district.]",
      "Q5. Which river in northern Andhra Pradesh originates in the Eastern Ghats near Thuamul Rampur in Odisha and drains through Srikakulam into the Bay of Bengal?\n(a) Vamsadhara\n(b) Nagavali (Langulya)\n(c) Gosthani\n(d) Sarada\nCorrect Answer: (b) Nagavali (Langulya) [Explanation: The Nagavali River (ancient Langulya) originates in Kalahandi district, Odisha, and flows through Vizianagaram and Srikakulam districts, joining the sea at Kalingapatnam.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-03",
    "filename": "03_climate_monsoons_and_el_nino_mechanics",
    "title": "Climate of India & AP: Monsoon Mechanism, El Niño & Cyclones",
    "mapping": "Geography of India & Andhra Pradesh: Climate - Mechanism of Indian Monsoons (South-West and North-East Monsoons), Tropical Jet Streams, El Niño, La Niña, Indian Ocean Dipole (IOD) and Tropical Cyclones in Andhra Pradesh.",
    "intro": "The climate of India is classified as Tropical Monsoon, driven by differential heating between the Indian Ocean and the Asian landmass, seasonal reversals of low-level planetary winds, and upper-tropospheric jet streams. Andhra Pradesh experiences a transitional climatic regime benefiting from both the Southwest Monsoon (June–September) and the retreating Northeast Monsoon (October–December), while remaining acutely vulnerable to devastating post-monsoon Bay of Bengal tropical cyclones.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cyclone_Hudhud_satellite.jpg", "caption": "Satellite view of Extremely Severe Cyclonic Storm Hudhud making landfall at Visakhapatnam in October 2014.", "alt": "Cyclone Hudhud NASA satellite imagery"},
    "table": {
      "caption": "Climatic Mechanisms & Atmospheric Phenomena Impacting India & AP",
      "headers": ["Phenomenon", "Mechanism & Driving Forces", "Seasonal Timing", "Impact on Rainfall in India & Andhra Pradesh"],
      "rows": [
        ["Southwest Monsoon (Advancing)", "Differential heating; shift of ITCZ over Gangetic plain; Somali Jet; heating of Tibetan plateau.", "June to September (enters Kerala ~1 June; Rayalaseema ~5 June).", "Accounts for 75% of India's annual precipitation; brings moderate rain to coastal AP and Rayalaseema (rain-shadow effect)."],
        ["Northeast Monsoon (Retreating)", "High pressure over Central Asia; withdrawal of ITCZ; winds blow from land to sea picking moisture over Bay of Bengal.", "October to December.", "Brings primary annual rainfall to South Coastal AP (Nellore, Prakasam) and Tamil Nadu (Coromandel coast); major cyclonic season."],
        ["El Niño Southern Oscillation (ENSO)", "Abnormal warming of sea surface temperatures in the central/eastern equatorial Pacific Ocean.", "Multi-year cycle (every 3–7 years).", "Weakens Walker Circulation; creates descending dry air over India; historically correlated with 60%+ of major Indian droughts."],
        ["La Niña", "Abnormal cooling of central/eastern equatorial Pacific waters.", "Multi-year cycle.", "Enhances convection over Indian subcontinent; correlated with robust surplus monsoon rainfall and flooding."],
        ["Indian Ocean Dipole (IOD)", "Difference in sea surface temperatures between western Arabian Sea and eastern Indian Ocean (Sumatra).", "Annual / Seasonal.", "Positive IOD warms western Indian Ocean, counteracting El Niño and boosting monsoon rainfall; Negative IOD suppresses rainfall."]
      ]
    },
    "bullets": [
      "Tropical Cyclones in Bay of Bengal: Fuelled by warm sea-surface temperatures (>26.5°C), Coriolis force, and low vertical wind shear; recurving tracks frequently make landfall along the coastal arc of Andhra Pradesh (Nellore to Srikakulam).",
      "Historic Andhra Cyclones: 1977 Diviseema Cyclone (tidal wave killed 10,000+), 1990 Machilipatnam Cyclone, 2014 Cyclone Hudhud (ravaged Visakhapatnam city with 215 km/h winds), and 2018 Cyclone Titli in Srikakulam.",
      "Koppen's Climate Classification for AP: Coastal AP classified as 'Aw' (Tropical Savanna with dry winters) and interior Rayalaseema as 'BSh' (Semi-arid Steppe climate with high evapotranspiration).",
      "Western Disturbances: Extratropical cyclonic storms originating in the Mediterranean Sea carried by Subtropical Westerly Jet Stream; bring vital winter rain/snow to NW India (Punjab, J&K), essential for Rabi wheat crops."
    ],
    "mains": [
      "Explain the meteorological mechanism of the Indian Southwest Monsoon and evaluate how global oceanic phenomena like El Niño, La Niña, and the Indian Ocean Dipole (IOD) influence rainfall variability in India. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain monsoon dynamics: differential heating between land and sea, northward migration of the ITCZ, heating of the Tibetan plateau generating Tropical Easterly Jet (TEJ), and low-level Somali jetstream over Arabian Sea; analyze El Niño: warming of Pacific suppressing Indian monsoon convection via altered Walker circulation; explain La Niña: cooling Pacific strengthening monsoon rains; detail the Indian Ocean Dipole (IOD): Positive IOD warming the western Indian Ocean and offsetting adverse El Niño impacts; conclude on climate change intensifying erratic precipitation patterns."
    ],
    "mcqs": [
      "Q1. Which oceanic-atmospheric phenomenon characterized by abnormal warming of the equatorial Pacific Ocean is historically correlated with weak monsoon rains and droughts in India?\n(a) La Niña\n(b) El Niño\n(c) Positive IOD\n(d) Madden-Julian Oscillation\nCorrect Answer: (b) El Niño [Explanation: El Niño causes warming of the central and eastern Pacific Ocean, weakening the Walker circulation and suppressing ascending air over the Indian subcontinent, triggering droughts.]",
      "Q2. The southern coastal districts of Andhra Pradesh, particularly Nellore and Prakasam, receive the bulk of their annual rainfall during which season?\n(a) Southwest Monsoon (June–Sept)\n(b) Northeast Monsoon (October–December)\n(c) Pre-Monsoon Thundershowers (April–May)\n(d) Western Disturbances (Jan–Feb)\nCorrect Answer: (b) Northeast Monsoon (October–December) [Explanation: South coastal Andhra Pradesh lies on the Coromandel belt and receives over 60% of its annual rainfall from retreating Northeast monsoonal winds and Bay of Bengal cyclones.]",
      "Q3. Category 4 Super Cyclone 'Hudhud' made devastating landfall in October 2014 directly over which coastal city of Andhra Pradesh with winds exceeding 200 km/h?\n(a) Machilipatnam\n(b) Visakhapatnam\n(c) Kakinada\n(d) Nellore\nCorrect Answer: (b) Visakhapatnam [Explanation: Cyclone Hudhud made landfall at Visakhapatnam on 12 October 2014, causing catastrophic structural and environmental damage to the port city.]",
      "Q4. In Koppen's climatic classification of India, the semi-arid drought-prone Rayalaseema plateau of Andhra Pradesh is designated under which climatic code?\n(a) Amw\n(b) Aw\n(c) BShw (Semi-arid Steppe)\n(d) Cwg\nCorrect Answer: (c) BShw (Semi-arid Steppe) [Explanation: Rayalaseema experiences a tropical semi-arid steppe climate with low erratic rainfall, coded as 'BShw' in Koppen's climate classification.]",
      "Q5. Winter rainfall in northwestern India (Punjab, Haryana, western UP), vital for the cultivation of Rabi wheat, is brought by:\n(a) Northeast Monsoon\n(b) Western Disturbances\n(c) Kalbaisakhi\n(d) Mango Showers\nCorrect Answer: (b) Western Disturbances [Explanation: Western Disturbances are extratropical low-pressure systems originating in the Mediterranean region that bring essential winter showers to North-West India.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-04",
    "filename": "04_soils_and_natural_vegetation_india_and_ap",
    "title": "Soils & Natural Vegetation of India & AP: Forests & Red Sanders",
    "mapping": "Geography of India & Andhra Pradesh: Pedology & Biogeography - Major Soil Types (Alluvial, Black/Regur, Red, Laterite), Forest Types, Mangroves (Coringa), Endemic Flora (Red Sanders / Pterocarpus santalinus).",
    "intro": "The pedological and ecological landscape of India reflects the interplay of underlying geology, relief, and rainfall gradients. Andhra Pradesh features fertile riverine alluvium in its deltas, extensive black cotton soils in the Krishna-Tungabhadra plains, and red sandy loams across Rayalaseema. Its forests range from moist deciduous canopies in the Eastern Ghats to the world's second-largest mangrove formation at Coringa and the endangered endemic Red Sanders (Pterocarpus santalinus) in Seshachalam.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Red_sanders_wood.jpg", "caption": "Cross-section of Red Sanders (Pterocarpus santalinus), the precious endemic timber tree unique to the Seshachalam Hills of Andhra Pradesh.", "alt": "Red Sanders log wood cross section"},
    "table": {
      "caption": "Pedological Taxonomy of Major Soils in India and Andhra Pradesh",
      "headers": ["Soil Type", "Parent Rock & Mineral Composition", "Geographical Distribution in AP & India", "Agricultural Characteristics & Crops"],
      "rows": [
        ["Alluvial Soil (Khadar & Bhangar)", "Fluvial deposition by river systems; rich in potash and lime; deficient in nitrogen and phosphorus.", "Indo-Gangetic plains; Godavari, Krishna, and Pennar delta deltas in AP (20% of state area).", "Highest natural fertility; ideal for wet paddy, sugarcane, banana, pulses, and vegetables."],
        ["Black Soil (Regur / Black Cotton)", "Weathering of Deccan basaltic trap; high clay content; self-ploughing (cracks when dry, sticky when wet); rich in iron, lime, magnesium; deficient in nitrogen.", "Maharashtra, Gujarat, MP; Guntur, Prakasam, Kurnool, Anantapur in AP (approx 25% area).", "Exceptional moisture-retentive capacity; principal soil for cotton, chillies, tobacco, jowar, and oilseeds."],
        ["Red Soils (Red Sandy / Loamy)", "Archean crystalline granites and gneisses; red color due to ferric oxide diffusion; permeable, friable; poor in nitrogen, phosphorus, humus.", "Tamil Nadu, Karnataka, Odisha; covers 65%+ of Andhra Pradesh (Rayalaseema and upland coastal plains).", "Responsive to irrigation and chemical fertilizers; suitable for groundnut, millets, pulses, castor, and mango orchards."],
        ["Laterite Soil", "Intense leaching in tropical areas of high rainfall and temperature; rich in iron and aluminium oxides; acidic; infertile.", "Western Ghats, Meghalaya; localized patches in Srikakulam, Visakhapatnam, and Nellore in AP.", "Requires heavy manuring; ideal for cashew nut, coffee, and rubber plantations."]
      ]
    },
    "bullets": [
      "Red Sanders (Pterocarpus santalinus): Endemic forest tree restricted entirely to the Seshachalam and Veligonda hills of Rayalaseema (Kadapa, Chittoor, Nellore); precious dense timber used in traditional East Asian acoustics, carvings, and medicines; protected under CITES Appendix II.",
      "Coringa Mangrove Wetland: Located in the Kakinada bay on the Godavari estuary; second largest mangrove forest formation in India after the Sundarbans; home to fishing cats, smooth-coated otters, and olive ridley sea turtle nesting beaches.",
      "Forest Cover in AP: According to the India State of Forest Report (ISFR 2021), Andhra Pradesh has a recorded forest area of 29,784 sq km (approx 18.28% of geographical area); leading districts: YSR Kadapa and Visakhapatnam.",
      "Forest Classifications in AP: Southern Tropical Dry Deciduous (Nallamalas), Tropical Moist Deciduous (Agency hills of Visakhapatnam/East Godavari), Littoral and Swamp (Mangroves of Coringa and Nizampatnam), and Southern Tropical Thorn scrub (Rayalaseema)."
    ],
    "mains": [
      "Examine the pedological characteristics and spatial distribution of major soils in Andhra Pradesh. Discuss the ecological significance and conservation challenges of Red Sanders (Pterocarpus santalinus) in the Seshachalam Biosphere Reserve. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Classify AP soils: Red soils (dominant 65% area, dryland farming), Black Regur soils (moisture-retentive, cotton and tobacco farming), and Deltaic Alluvium (intensive paddy-sugarcane belt); analyze Red Sanders: strict endemism to the dry quartzite slopes of Seshachalam, Palkonda, and Veligonda ranges; high global demand in China and Japan for wood carving and dye; examine conservation crises: rampant illegal felling by international smuggling syndicates, forest fires, and slow regeneration; evaluate state countermeasures: Red Sanders Anti-Smuggling Task Force (RSASTF), geo-tagging, and CITES export quotas."
    ],
    "mcqs": [
      "Q1. Which precious commercial timber tree species is geographically endemic exclusively to the Seshachalam and Veligonda hill ranges of Andhra Pradesh?\n(a) Teak (Tectona grandis)\n(b) Red Sanders (Pterocarpus santalinus)\n(c) Sandalwood (Santalum album)\n(d) Rosewood (Dalbergia latifolia)\nCorrect Answer: (b) Red Sanders (Pterocarpus santalinus) [Explanation: Red Sanders (Yerra Chandanam) is strictly endemic to the Seshachalam biosphere reserve and adjoining hill tracts of Rayalaseema.]",
      "Q2. The Coringa Wildlife Sanctuary, which protects India's second-largest contiguous mangrove forest formation, is located on the estuary of which river?\n(a) Krishna Estuary\n(b) Godavari Estuary\n(c) Pennar Estuary\n(d) Vamsadhara Estuary\nCorrect Answer: (b) Godavari Estuary [Explanation: The Coringa Mangroves near Kakinada span over 235 sq km on the Godavari delta estuary, ranking second only to the Sundarbans.]",
      "Q3. Which soil type, characterized by high clay content, deep fissures when dry ('self-ploughing'), and moisture-retentive capacity, is predominant in Guntur and Kurnool?\n(a) Laterite Soil\n(b) Black Soil (Regur)\n(c) Red Sandy Soil\n(d) Saline Soil\nCorrect Answer: (b) Black Soil (Regur) [Explanation: Black Cotton Soil (Regur) exhibits high montmorillonite clay content, swelling when wet and cracking deeply when dry, ideal for cotton, tobacco, and chillies.]",
      "Q4. Which soil covers the largest geographical area (over 65%) across the state of Andhra Pradesh, especially dominant in Rayalaseema?\n(a) Black Cotton Soil\n(b) Red Soil\n(c) Delta Alluvial Soil\n(d) Laterite Soil\nCorrect Answer: (b) Red Soil [Explanation: Red soils (sandy loams and gravels), derived from ancient Archean granites, cover approximately two-thirds of Andhra Pradesh's total area.]",
      "Q5. Which district of Andhra Pradesh possesses the largest total area of recorded forest cover according to the Forest Survey of India?\n(a) Chittoor\n(b) YSR Kadapa\n(c) Visakhapatnam\n(d) East Godavari\nCorrect Answer: (b) YSR Kadapa [Explanation: YSR Kadapa district, encompassing extensive stretches of the Nallamala, Seshachalam, and Palkonda ranges, holds the largest forest area in the state.]"
    ]
  },
  {
    "id": "APPSC-G1-GEOG-05",
    "filename": "05_agriculture_cropping_patterns_and_irrigation_ap",
    "title": "Agriculture & Irrigation in Andhra Pradesh: Cropping Systems & Agrarian Economy",
    "mapping": "Geography of India & Andhra Pradesh: Agriculture - Cropping Patterns, Food Grains (Rice, Millets/Shree Anna), Commercial Crops (Chilli, Tobacco, Cotton, Oilseeds), Horticulture and Major Irrigation Projects (Polavaram, HNSS, GNSS).",
    "intro": "Agriculture forms the foundational backbone of Andhra Pradesh's economy, earning the state the title 'Annapurna' and the 'Rice Bowl of India'. With diverse agro-climatic zones ranging from high-rainfall deltaic plains to dry semi-arid plateaus, Andhra Pradesh leads the nation in paddy, chillies, oil palm, tobacco, and marine aquaculture, supported by major river irrigation networks and mission-mode micro-irrigation.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Paddy_field_Andhra.jpg", "caption": "Lush green paddy fields in the Godavari delta, the agrarian heart of Andhra Pradesh.", "alt": "Green paddy field in coastal Andhra"},
    "table": {
      "caption": "Major Agricultural & Horticultural Crops of Andhra Pradesh",
      "headers": ["Crop / Category", "Key Cultivating Districts", "Agro-Climatic Requirements", "National Standing & Economic Role"],
      "rows": [
        ["Paddy (Rice)", "East Godavari, West Godavari, Krishna, Guntur, Nellore.", "High temperature (>25°C), heavy rainfall/irrigation (100–150 cm), alluvial clay soils.", "Ranks among India's top rice producers; 'Rice Bowl of India'; extensive double-cropping under canals."],
        ["Dry Chillies", "Guntur, Prakasam, Kurnool.", "Warm, dry climate during maturity; well-drained black/loamy soils.", "Guntur Chilli Yard is Asia's largest spice market; Guntur Sannam chilli holds GI tag; major export earner."],
        ["Tobacco (FCV)", "Prakasam, West Godavari, Guntur.", "Light sandy soils; controlled moisture.", "Andhra produces over 80% of India's Flue-Cured Virginia (FCV) tobacco; Tobacco Board headquartered at Guntur."],
        ["Groundnut & Millets", "Anantapur, Kurnool, Chittoor (Rayalaseema).", "Low rainfall (40–60 cm), red sandy soil, drought-tolerant.", "Anantapur has India's largest single-district groundnut acreage; millets (Ragi, Jowar) promoted under 'Shree Anna' mission."],
        ["Horticulture & Oil Palm", "Anantapur (banana/sweet orange), Kadapa, West Godavari (oil palm).", "Drip irrigation, tropical sun, loamy soils.", "AP ranks 1st in India in Oil Palm, Papaya, and Chillies; 2nd in Mango; leading exporter of Banganapalle mangoes (GI Tag)."]
      ]
    },
    "bullets": [
      "Aqua-Hub of India: Andhra Pradesh accounts for over 70% of India's cultured shrimp (Vannamei) exports; coastal belt from Nellore to Srikakulam leads national marine and freshwater fisheries output.",
      "Handri-Neeva Sujala Sravanthi (HNSS): Longest lift canal project in AP (565 km); lifts flood waters from Srisailam reservoir to provide drinking and irrigation water to drought-prone Rayalaseema districts (Kurnool, Anantapur, Chittoor, Kadapa).",
      "Galeru-Nagari Sujala Sravanthi (GNSS): Irrigation canal transferring flood waters from the Krishna at Pothireddypadu head regulator through the Veligonda tunnel to the Pennar basin.",
      "Community Managed Natural Farming (APCNF): Andhra Pradesh leads India's transition to Zero Budget Natural Farming (ZBNF), involving over 700,000 farmers practicing chemical-free regenerative agriculture."
    ],
    "mains": [
      "Analyze the spatial cropping patterns and agrarian challenges in Andhra Pradesh. How have major lift irrigation projects like HNSS and GNSS helped mitigate regional imbalances between Coastal Andhra and Rayalaseema? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast the coastal delta agrarian economy (assured canal irrigation, high-yield paddy, aquaculture, commercial tobacco/chilli) with the rainfed, drought-prone Rayalaseema agro-ecology (fragile groundnut mono-cropping, erratic monsoons, falling water tables); analyze the strategic design of mega lift schemes: Handri-Neeva (HNSS) and Galeru-Nagari (GNSS) lifting floodwaters from the Krishna at Srisailam across high ridgelines into Anantapur and Chittoor; evaluate outcomes: stabilised drinking water, revived minor irrigation tanks, and boosted horticulture; discuss unresolved issues: power consumption costs, canal lining, and equitable water distribution."
    ],
    "mcqs": [
      "Q1. Which city in Andhra Pradesh houses Asia's largest dedicated market yard for dry red chillies, renowned globally for the GI-tagged 'Guntur Sannam' chilli?\n(a) Vijayawada\n(b) Guntur\n(c) Ongole\n(d) Kurnool\nCorrect Answer: (b) Guntur [Explanation: The Guntur Mirchi Yard is the largest spice market in Asia, trading premium dry chilli varieties exported across the globe.]",
      "Q2. In which major horticultural plantation crop does Andhra Pradesh rank first in India, accounting for over 85% of total domestic production?\n(a) Rubber\n(b) Oil Palm\n(c) Coffee\n(d) Tea\nCorrect Answer: (b) Oil Palm [Explanation: Andhra Pradesh leads India in oil palm cultivation and palm oil processing, centered primarily in West Godavari and Krishna districts.]",
      "Q3. The famous 'Banganapalle Mango' (Benishan), which was granted a prestigious Geographical Indication (GI) tag, originates from which district of Andhra Pradesh?\n(a) Chittoor\n(b) Nandyal / Kurnool\n(c) Krishna\n(d) Kadapa\nCorrect Answer: (b) Nandyal / Kurnool [Explanation: Banganapalle mangoes, celebrated for their fiberless pulp and sweet aroma, originate from the Banganapalle princely estate in Kurnool/Nandyal district.]",
      "Q4. Which district of Andhra Pradesh historically contains the single largest acreage under rain-fed groundnut cultivation in the entire country?\n(a) Prakasam\n(b) Anantapur\n(c) Guntur\n(d) Srikakulam\nCorrect Answer: (b) Anantapur [Explanation: Anantapur district dedicates over 800,000 hectares to rain-fed groundnut cultivation, making it India's premier groundnut basin despite low rainfall.]",
      "Q5. The Handri-Neeva Sujala Sravanthi (HNSS) project lifts surplus flood waters from which major reservoir to supply irrigation and drinking water to Rayalaseema?\n(a) Nagarjuna Sagar Dam\n(b) Srisailam Reservoir\n(c) Tungabhadra Dam\n(d) Somasila Dam\nCorrect Answer: (b) Srisailam Reservoir [Explanation: HNSS lifts water from the backwaters of Srisailam reservoir at Malyala, channeling it through a 565 km canal network to Kurnool, Anantapur, Kadapa, and Chittoor.]"
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

print("Part 1 of Subject 3 generated successfully")
