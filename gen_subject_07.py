import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "07_Science_Technology_Environment"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-STE-01",
    "filename": "01_national_science_policies_and_apex_research_institutes",
    "title": "National Science Policies & Apex Research Architecture",
    "mapping": "Science, Technology & Environment: Evolution of National Science Policies (SPR 1958, TPS 1983, STP 2003, STIP 2013, draft STIP 2020), Anusandhan National Research Foundation (ANRF Act 2023), Apex Research Bodies (CSIR, DST, DBT, DRDO, DAE, ICMR, ICAR), and R&D Expenditure in India.",
    "intro": "India's scientific and technological enterprise has evolved through visionary policy declarations and premier institutional networks designed to foster self-reliance, indigenous innovation, and industrial modernization. From Jawaharlal Nehru's Scientific Policy Resolution (SPR 1958) to the statutory enactment of the Anusandhan National Research Foundation (ANRF Act 2023), national science governance seeks to bridge the gap between academic R&D, patent creation, and market translation, targeting an increase in Gross Expenditure on R&D (GERD) above its current ~0.65% of GDP.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/CSIR_India_Headquarters.jpg", "caption": "Council of Scientific and Industrial Research (CSIR) headquarters in New Delhi, India's premier industrial R&D organisation.", "alt": "CSIR Headquarters New Delhi"},
    "table": {
      "caption": "Evolution of National Science & Technology Policies in India",
      "headers": ["Policy Landmark", "Promulgation Year", "Core Philosophical Thrust", "Strategic Outcomes & Institutions Spawned"],
      "rows": [
        ["Scientific Policy Resolution (SPR)", "1958", "Pure research, scientific temper, cultivation of basic sciences", "Expansion of IITs, National Laboratories, basic institutional funding"],
        ["Technology Policy Statement (TPS)", "1983", "Technological self-reliance, indigenous capacity, import substitution", "Indigenous industrial adaptation, technology absorption mandates"],
        ["Science & Technology Policy (STP)", "2003", "Integration of S&T with socio-economic sectors, R&D funding boost", "Fostered university-industry linkages, increased venture incentives"],
        ["Science, Technology & Innovation Policy (STIP)", "2013", "Positioning India among top 5 global scientific powers; Innovation ecosystem", "Inception of Atal Innovation Mission (AIM), Startup India, patent acceleration"],
        ["Anusandhan National Research Foundation (ANRF)", "2023 (Act)", "Rs 50,000 Cr outlay over 5 years (70% private sector); university research democratization", "Repeals SERB Act 2008; governed by Governing Board chaired by the Prime Minister"]
      ]
    },
    "points": [
      "Anusandhan National Research Foundation (ANRF Act 2023): Establishes an apex body to seed, grow, and promote R&D and foster a culture of research and innovation throughout India's universities, colleges, and research institutions. Governed by a Governing Board headed by the Prime Minister and an Executive Council chaired by the Principal Scientific Adviser (PSA).",
      "CSIR Network: Established in 1942, the Council of Scientific and Industrial Research encompasses 37 national laboratories and 39 outreach centers (e.g., CCMB Hyderabad, NCL Pune, NGRI Hyderabad). CSIR spearheaded landmark developments including Swaraj tractors, indelible voter ink, and generic pharmaceutical syntheses.",
      "Department of Science and Technology (DST) & DBT: DST coordinates national scientific missions, manages the Survey of India, and funds high-risk research. The Department of Biotechnology (DBT) regulates life sciences and promoted BIRAC (Biotechnology Industry Research Assistance Council) to foster biotech startups.",
      "GERD Challenge: India's Gross Expenditure on R&D (GERD) hovers at ~0.64% to 0.65% of GDP, notably lower than South Korea (4.8%), USA (3.4%), and China (2.4%). Crucially, the private sector contributes only ~36% of India's GERD compared to >70% in leading OECD economies.",
      "Deep Tech & Intellectual Property Rights: National IPR Policy 2016 ('Creative India, Innovative India') has dramatically streamlined patent examination timelines, elevating India's rank in the Global Innovation Index (GII) from 81st in 2015 to top 40 in 2023."
    ],
    "mains": [
      "Critically analyze how the Anusandhan National Research Foundation (ANRF) Act, 2023 seeks to democratize academic research in state public universities and bridge industry-academia partnerships. (250 Words, 15 Marks)",
      "India's Gross Expenditure on R&D (GERD) remains stagnant below 0.7% of GDP with an overwhelmingly public sector funding profile. Discuss the structural factors inhibiting private sector R&D investments in India. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE01-01",
        "q": "Who serves as the ex-officio President of the Governing Board of the Anusandhan National Research Foundation (ANRF) under the ANRF Act 2023?",
        "options": ["Union Minister for Science and Technology", "Principal Scientific Adviser to the Government of India", "Prime Minister of India", "President of India"],
        "ans": "c",
        "explanation": "Under Section 5 of the Anusandhan National Research Foundation Act 2023, the Prime Minister of India is the ex-officio President of the Governing Board."
      },
      {
        "id": "MCQ-STE01-02",
        "q": "Which existing statutory board established under a 2008 Act was repealed and subsumed into the Anusandhan National Research Foundation (ANRF)?",
        "options": ["Technology Development Board (TDB)", "Science and Engineering Research Board (SERB)", "National Innovation Foundation (NIF)", "Council of Scientific and Industrial Research (CSIR)"],
        "ans": "b",
        "explanation": "The ANRF Act 2023 repealed the Science and Engineering Research Board Act, 2008 and subsumed SERB into the newly established ANRF."
      },
      {
        "id": "MCQ-STE01-03",
        "q": "In which city is the premier CSIR institute 'Centre for Cellular and Molecular Biology (CCMB)' located?",
        "options": ["Bengaluru", "New Delhi", "Hyderabad", "Pune"],
        "ans": "c",
        "explanation": "The Centre for Cellular and Molecular Biology (CCMB), an apex national research laboratory under CSIR specializing in modern biology and genetics, is situated in Hyderabad, Telangana."
      },
      {
        "id": "MCQ-STE01-04",
        "q": "Who was the founding Director-General of the Council of Scientific and Industrial Research (CSIR) who worked closely with Jawaharlal Nehru?",
        "options": ["Dr. Homi J. Bhabha", "Dr. Shanti Swaroop Bhatnagar", "Dr. Vikram Sarabhai", "Sir C.V. Raman"],
        "ans": "b",
        "explanation": "Dr. Shanti Swaroop Bhatnagar was the founder Director-General of CSIR and is honored annually through India's premier science award, the Shanti Swaroop Bhatnagar Prize."
      },
      {
        "id": "MCQ-STE01-05",
        "q": "Approximately what percentage of India's Gross Domestic Product (GDP) is currently invested in Gross Expenditure on Research and Development (GERD)?",
        "options": ["0.64% – 0.65%", "1.25%", "2.10%", "3.00%"],
        "ans": "a",
        "explanation": "According to the Economic Survey and DST R&D Statistics, India's GERD currently stands at approximately 0.64% to 0.65% of GDP, with government funding accounting for roughly 60% of total spending."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-02",
    "filename": "02_information_technology_5g_ai_and_semiconductors",
    "title": "Information Technology: 5G, Artificial Intelligence & Semiconductors",
    "mapping": "Science, Technology & Environment: ICT Infrastructure, 5G and 6G Roadmaps, IndiaAI Mission, National Supercomputing Mission (NSM), India Semiconductor Mission (ISM, DLI/PLI Schemes), and National Quantum Mission (NQM).",
    "intro": "Frontier information technologies form the spine of modern geopolitical competitiveness and knowledge economies. India has transitioned from software services outsourcing to deep-technology mastery across telecom networks, foundational artificial intelligence, high-performance supercomputing, and indigenous semiconductor fabrication. Initiatives like the IndiaAI Mission, National Quantum Mission, and the $10 billion India Semiconductor Mission (ISM) position India as a trusted global technology powerhouse.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Silicon_wafer_semiconductor.jpg", "caption": "Silicon semiconductor wafer, the foundational building block of microelectronics promoted under the India Semiconductor Mission.", "alt": "Silicon wafer microelectronics"},
    "table": {
      "caption": "India's Flagship Frontier Deep-Technology Missions",
      "headers": ["National Mission", "Nodal Ministry / Agency", "Approved Outlay / Mandate", "Key Milestones & Deliverables"],
      "rows": [
        ["India Semiconductor Mission (ISM)", "Ministry of Electronics & IT (MeitY)", "Rs 76,000 Cr ($10 Billion)", "50% fiscal support for Silicon Fabs, Display Fabs, OSAT/ATMP units; Dholera, Sanand, Morigaon fabs"],
        ["IndiaAI Mission", "MeitY / Digital India Corporation", "Rs 10,372 Cr (Approved 2024)", "10,000+ GPU supercomputing capacity, foundational indigenous LLMs, AI datasets platform, AI Startup financing"],
        ["National Quantum Mission (NQM)", "Department of Science and Technology (DST)", "Rs 6,003 Cr (2023–2031)", "Development of 50–1000 physical qubit quantum computers, satellite quantum key distribution (QKD) over 2000 km"],
        ["National Supercomputing Mission (NSM)", "MeitY and DST (executed by C-DAC & IISc)", "Rs 4,500 Cr", "Grid of 70+ high-performance supercomputers; deployment of PARAM Shivay, PARAM Shakti, PARAM Siddhi-AI"]
      ]
    },
    "points": [
      "5G Deployment & Bharat 6G Vision: India witnessed one of the world's fastest 5G rollouts following the 2022 spectrum auction. The 'Bharat 6G Vision' document (2023) sets an apex roadmap for indigenous intellectual property creation and standardization in Terahertz communications by 2030.",
      "India Semiconductor Mission (ISM): Provides 50% capital expenditure support on pari passu basis across Silicon Fabs, Compound Semiconductors, and Packaging (ATMP/OSAT). Landmark approved units include Tata Electronics Fab in Dholera (Gujarat) in partnership with Taiwan's PSMC, and Micron OSAT unit in Sanand.",
      "IndiaAI Compute Capacity: IndiaAI establishes a sovereign AI ecosystem by procuring and subsidizing access to high-compute GPU clusters (>10,000 GPUs) for Indian researchers and startups, while democratizing sovereign datasets via the India Datasets Platform.",
      "National Quantum Mission (NQM) Thematic Hubs: Formulates 4 T-Hubs in Quantum Computing, Quantum Communication, Quantum Sensing & Metrology, and Quantum Materials & Devices, advancing secure quantum encryption resistant to post-quantum cryptanalysis.",
      "Open Source Digital Public Infrastructure (DPI): The 'India Stack' (Aadhaar, UPI, DigiLocker, Account Aggregator, ONDC) demonstrates scalable, population-scale digital public goods that have become a global benchmark studied by the G20 and IMF."
    ],
    "mains": [
      "Critically analyze the strategic significance of the India Semiconductor Mission (ISM) for safeguarding national technological sovereignty and mitigating global microchip supply-chain disruptions. (250 Words, 15 Marks)",
      "Discuss the transformative potential and ethical risks of Generative Artificial Intelligence in public service delivery in India. How does the IndiaAI Mission address these priorities? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE02-01",
        "q": "What is the total financial outlay approved by the Government of India for the India Semiconductor Mission (ISM) launched under MeitY?",
        "options": ["Rs 25,000 Crore", "Rs 50,000 Crore", "Rs 76,000 Crore (~$10 Billion)", "Rs 1,00,000 Crore"],
        "ans": "c",
        "explanation": "The Government of India approved a comprehensive program with an outlay of Rs 76,000 crore (~$10 billion) for the development of semiconductor and display manufacturing ecosystem in India."
      },
      {
        "id": "MCQ-STE02-02",
        "q": "Where is the first commercial mega commercial semiconductor fabrication plant being established by Tata Electronics in partnership with Powerchip (PSMC) of Taiwan?",
        "options": ["Sanand, Gujarat", "Dholera, Gujarat", "Sri City, Andhra Pradesh", "Morigaon, Assam"],
        "ans": "b",
        "explanation": "Tata Electronics, in partnership with Taiwan's Powerchip Semiconductor Manufacturing Corp (PSMC), is setting up India's first commercial semiconductor fabrication facility at Dholera Special Investment Region in Gujarat."
      },
      {
        "id": "MCQ-STE02-03",
        "q": "The National Quantum Mission (NQM) approved by the Union Cabinet in 2023 is implemented under the aegis of which nodal department?",
        "options": ["Department of Telecommunications", "Department of Space", "Department of Science and Technology (DST)", "Ministry of Electronics and Information Technology"],
        "ans": "c",
        "explanation": "The National Quantum Mission (NQM), with an outlay of over Rs 6,003 crore for 2023–2031, is piloted and executed by the Department of Science and Technology (DST)."
      },
      {
        "id": "MCQ-STE02-04",
        "q": "Which premier supercomputer was designed and installed by C-DAC under the National Supercomputing Mission (NSM) as India's fastest AI supercomputing system?",
        "options": ["PARAM 8000", "PARAM Shivay", "PARAM Siddhi-AI", "PARAM Yuva II"],
        "ans": "c",
        "explanation": "PARAM Siddhi-AI, built on NVIDIA DGX SuperPOD architecture by C-DAC under the National Supercomputing Mission, achieved global recognition among the world's top 100 most powerful supercomputers."
      },
      {
        "id": "MCQ-STE02-05",
        "q": "Under the IndiaAI Mission approved in 2024, what scale of GPU supercomputing capacity is planned to be established for Indian startups and academia?",
        "options": ["1,000 GPUs", "5,000 GPUs", "10,000 or more GPUs", "50,000 GPUs"],
        "ans": "c",
        "explanation": "The IndiaAI Mission has an approved outlay of Rs 10,372 crore, with a primary deliverable to build a scalable AI compute infrastructure of 10,000 or more Graphics Processing Units (GPUs) under public-private partnerships."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-03",
    "filename": "03_space_programme_isro_missions_and_launch_vehicles",
    "title": "Space Programme, ISRO Missions & Space Sector Reforms",
    "mapping": "Science, Technology & Environment: ISRO History and Infrastructure (Satish Dhawan Space Centre Sriharikota, AP), Launch Vehicles (PSLV, GSLV, LVM3, SSLV), Landmark Space Missions (Chandrayaan-1/2/3, Mangalyaan, Aditya-L1, Gaganyaan, XPoSat), NavIC Constellation, IN-SPACe and Indian Space Policy 2023.",
    "intro": "The Indian space program, founded under the vision of Dr. Vikram Sarabhai, stands as a triumph of cost-effective engineering and civilian application. Operating from its premier launch facility at Satish Dhawan Space Centre (SDSC SHAR) in Sriharikota, Andhra Pradesh, ISRO has mastered indigenous launch vehicle technology across PSLV, GSLV, and LVM3. With historic feats including the lunar south pole landing of Chandrayaan-3 and the solar observation mission Aditya-L1, India's space governance has opened to private commercial players via IN-SPACe and the Indian Space Policy 2023.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Chandrayaan-3_Launch_LVM3_M4.jpg", "caption": "Launch Vehicle Mark-III (LVM3 M4) lifting off from SDSC SHAR, Sriharikota, Andhra Pradesh carrying Chandrayaan-3.", "alt": "Chandrayaan-3 LVM3 launch from Sriharikota"},
    "table": {
      "caption": "ISRO Operational Launch Vehicles & Planetary Milestones",
      "headers": ["Vehicle / Mission", "Key Technological Configuration", "Payload Capacity (LEO / GTO)", "Historic Feats & Operational Status"],
      "rows": [
        ["PSLV (Workhorse)", "4-Stage (Solid-Liquid-Solid-Liquid); Vikas liquid engine", "1,750 kg to Sun-Synchronous Polar Orbit (SSPO)", "Launched Chandrayaan-1 (2008), Mars Orbiter Mission (2013); 50+ successful missions"],
        ["LVM3 (GSLV Mk III)", "3-Stage: 2 x S200 solid boosters, L110 core liquid, C25 Cryogenic", "8,000 kg to LEO / 4,000 kg to GTO", "Launched Chandrayaan-2, Chandrayaan-3; human-rated for the upcoming Gaganyaan mission"],
        ["SSLV (Small Sat)", "3-Stage all-solid vehicle with Liquid Velocity Trimming Module (VTM)", "500 kg to 500 km Low Earth Orbit", "Rapid turnaround (72 hours); on-demand commercial small satellite launches"],
        ["Chandrayaan-3", "Propulsion Module, Vikram Lander, Pragyan Rover", "Landed near Lunar South Pole (Shiv Shakti Point)", "Made India the 4th nation to soft-land on Moon and 1st near the lunar south polar region"],
        ["Aditya-L1", "Solar observatory payload placed at Sun-Earth Lagrange Point 1", "Continuously views Sun without eclipse/occultation", "Carries 7 payloads including VELC, SUIT; tracks Coronal Mass Ejections (CMEs) and solar flares"],
        ["Gaganyaan", "Orbital Module (Crew Module + Service Module) launched by LVM3", "Crew of 3 astronauts to 400 km LEO for 3 days", "India's maiden human spaceflight programme; TV-D1 abort test successfully demonstrated"]
      ]
    },
    "points": [
      "Satish Dhawan Space Centre (SDSC SHAR), Sriharikota: Located in Tirupati district (formerly Nellore) of Andhra Pradesh, SHAR serves as India's primary spaceport due to its proximity to the equator (providing eastward spin boost) and vast unpopulated launch azimuth over the Bay of Bengal.",
      "Chandrayaan-3 Lunar Triumph: On August 23, 2023, the Vikram lander executed an autonomous soft landing near the lunar south pole. The landing site was officially named 'Shiv Shakti Point', and August 23 was notified as 'National Space Day'.",
      "NavIC (Navigation with Indian Constellation): Autonomous regional satellite navigation system consisting of 7 satellites (3 in geostationary orbit, 4 in inclined geosynchronous orbit) delivering standard positioning service over India and extending 1,500 km beyond its borders.",
      "Indian Space Policy 2023 & Institutional Trifecta: Delineates clear roles: 1. ISRO focuses on advanced research, science, and human exploration; 2. IN-SPACe (Indian National Space Promotion and Authorization Centre) acts as single-window regulator for Non-Government Entities (NGEs); 3. NSIL (NewSpace India Limited) commercializes space assets and executes production contracts.",
      "Kulasekarapattinam Spaceport: Greenfield second launchport under construction in Tamil Nadu dedicated for SSLV launches, offering a direct southward trajectory for polar launches without requiring a dogleg maneuver around Sri Lanka."
    ],
    "mains": [
      "Analyze the strategic and scientific significance of ISRO's Chandrayaan-3 and Aditya-L1 missions in expanding India's deep-space exploratory footprint. (250 Words, 15 Marks)",
      "Discuss how the Indian Space Policy 2023 and the establishment of IN-SPACe are unlocking private commercial participation in the space sector. How does this enhance India's share in the global space economy? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE03-01",
        "q": "On which date did Chandrayaan-3 successfully soft-land near the lunar south pole, officially commemorated as 'National Space Day' in India?",
        "options": ["July 14, 2023", "August 15, 2023", "August 23, 2023", "September 2, 2023"],
        "ans": "c",
        "explanation": "Chandrayaan-3's Vikram Lander soft-landed on the Moon on August 23, 2023, prompting the Government of India to declare August 23 as National Space Day."
      },
      {
        "id": "MCQ-STE03-02",
        "q": "What is the name given to the Chandrayaan-3 lunar landing site near the South Pole of the Moon?",
        "options": ["Tiranga Point", "Jawahar Point", "Shiv Shakti Point", "Atal Point"],
        "ans": "c",
        "explanation": "Prime Minister Narendra Modi announced that the spot where the Chandrayaan-3 lander touched down on the Moon's surface would be known as 'Shiv Shakti Point' (Chandrayaan-2 crash site was named Tiranga Point)."
      },
      {
        "id": "MCQ-STE03-03",
        "q": "At which Lagrange Point was ISRO's solar observatory spacecraft 'Aditya-L1' successfully inserted in January 2024?",
        "options": ["Lagrange Point L1 (~1.5 million km from Earth)", "Lagrange Point L2", "Lagrange Point L4", "Lagrange Point L5"],
        "ans": "a",
        "explanation": "Aditya-L1 was inserted into a halo orbit around the Sun-Earth Lagrange Point 1 (L1), located approximately 1.5 million kilometers from Earth."
      },
      {
        "id": "MCQ-STE03-04",
        "q": "Which autonomous single-window nodal agency was established under the Department of Space to authorize and facilitate private space activities in India?",
        "options": ["Antrix Corporation", "NewSpace India Limited (NSIL)", "IN-SPACe", "Space Commission"],
        "ans": "c",
        "explanation": "IN-SPACe (Indian National Space Promotion and Authorization Centre) is the autonomous single-window regulator established to facilitate, authorize, and regulate private space sector activities in India."
      },
      {
        "id": "MCQ-STE03-05",
        "q": "How many total satellites constitute the baseline space constellation of NavIC (Navigation with Indian Constellation / IRNSS)?",
        "options": ["5 satellites", "7 satellites", "12 satellites", "24 satellites"],
        "ans": "b",
        "explanation": "NavIC's baseline constellation comprises 7 satellites: 3 in Geostationary Earth Orbit (GEO) and 4 in inclined Geosynchronous Orbit (GSO)."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-04",
    "filename": "04_defense_technology_drdo_missiles_and_indigenisation",
    "title": "Defense Technology: DRDO, Missiles & Indigenisation",
    "mapping": "Science, Technology & Environment: Defence Research and Development Organisation (DRDO), Integrated Guided Missile Development Programme (IGMDP: Prithvi, Agni, Trishul, Akash, Nag), BrahMos Supersonic Cruise Missile, Ballistic Missile Defence (BMD), Nuclear Submarines (INS Arihant), LCA Tejas, and Defence Indigenisation (Positive Indigenisation Lists, DAP 2020).",
    "intro": "Defense technology safeguards national sovereignty and underpins strategic deterrence. India's defense R&D, spearheaded by the Defence Research and Development Organisation (DRDO), achieved self-reliance milestones under Dr. A.P.J. Abdul Kalam's Integrated Guided Missile Development Programme (IGMDP). Modern defense manufacturing prioritizes indigenization ('Aatmanirbhar Bharat' in defense), indigenous supersonic cruise missiles (BrahMos), ballistic missile defense shields, nuclear triad ballistic missile submarines, and fifth-generation fighter development.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Agni-V_missile_at_Republic_Day_Parade.jpg", "caption": "Agni-V Intercontinental Ballistic Missile (ICBM) displayed during the Republic Day parade, showcasing India's credible minimum nuclear deterrence.", "alt": "Agni-V missile Republic Day parade"},
    "table": {
      "caption": "India's Premier Missile Systems & Deterrence Capabilities",
      "headers": ["Missile System", "Missile Classification", "Operational Strike Range", "Key Guidance & Propulsion Features"],
      "rows": [
        ["Prithvi Series", "Surface-to-Surface Short Range Ballistic (SRBM)", "150 km – 350 km", "Liquid/solid fuel; first missile developed under IGMDP; deployed by Army/Air Force"],
        ["Agni Series (I to V)", "Medium to Intercontinental Ballistic Missile (ICBM)", "700 km to >5,000 km (Agni-V)", "Solid propellant; composite rocket motor; canisterized launch; MIRV tested in Mission Divyastra"],
        ["Akash System", "Surface-to-Air Missile (SAM) Air Defense", "25 km – 30 km (Akash-NG: 60+ km)", "Ramjet rocket propulsion; multi-target engagement via Rajendra radar; exported to Armenia"],
        ["Nag / Helina", "3rd Gen Anti-Tank Guided Missile (ATGM)", "4 km (Nag) / 7 km (Helina / Dhruvastra)", "Fire-and-forget; Imaging Infrared (IIR) seeker; tandem warhead defeats explosive reactive armor"],
        ["BrahMos", "Supersonic Cruise Missile (Indo-Russian joint venture)", "290 km (extended to 450+ km)", "World's fastest operational supersonic cruise missile (Mach 2.8–3.0); land, sea, sub-sea, air launch"]
      ]
    },
    "points": [
      "IGMDP Five Core Missiles (PATNA Acronym): Conceived in 1983 under Dr. A.P.J. Abdul Kalam: Prithvi (surface-to-surface), Agni (re-entry vehicle ballistic), Trishul (short-range SAM), Akash (medium-range SAM), and Nag (fire-and-forget ATGM).",
      "Mission Divyastra & Agni-V MIRV Capability: In March 2024, DRDO conducted the maiden flight test of the indigenous Agni-V missile with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology, placing India in an elite club of nations capable of delivering multiple nuclear warheads to distinct targets from a single ICBM.",
      "Nuclear Triad Operationalization: The induction of nuclear-powered ballistic missile submarines (SSBNs) INS Arihant and INS Arighaat, armed with K-15 (Sagarika) and K-4 submarine-launched ballistic missiles (SLBMs), completes India's survivable second-strike nuclear triad under its 'No First Use' doctrine.",
      "Ballistic Missile Defence (BMD) Shield: Two-tiered interceptor system developed by DRDO: Prithvi Air Defence (PAD) / Pradyumna for exo-atmospheric interception (50–80 km altitude) and Advanced Air Defence (AAD) / Ashwin for endo-atmospheric interception (15–30 km altitude).",
      "Positive Indigenisation Lists: Under Defence Acquisition Procedure (DAP 2020), the Ministry of Defence notified multiple Positive Indigenisation Lists comprising over 5,000 military items and platforms banned from import, driving orders to domestic defense PSUs and private defense firms."
    ],
    "mains": [
      "Evaluate the strategic significance of 'Mission Divyastra' (Agni-V with MIRV capability) for India's nuclear deterrence doctrine. How does it alter the strategic balance in the Indo-Pacific region? (250 Words, 15 Marks)",
      "Discuss the policy measures taken under the 'Aatmanirbhar Bharat' initiative in defense manufacturing. What technological and testing bottlenecks continue to impede full defense self-reliance? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE04-01",
        "q": "What was the code name of the historic DRDO flight test in March 2024 that successfully demonstrated the Agni-V missile with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology?",
        "options": ["Mission Shakti", "Mission Divyastra", "Mission Sudarshan", "Mission Astra"],
        "ans": "b",
        "explanation": "In March 2024, DRDO successfully conducted 'Mission Divyastra', the maiden flight test of the indigenously developed Agni-V missile equipped with Multiple Independently Targetable Re-entry Vehicle (MIRV) technology."
      },
      {
        "id": "MCQ-STE04-02",
        "q": "Which of the following missiles was NOT one of the five core missile systems developed under the Integrated Guided Missile Development Programme (IGMDP)?",
        "options": ["Prithvi", "Akash", "BrahMos", "Trishul"],
        "ans": "c",
        "explanation": "BrahMos was developed as an Indo-Russian joint venture formed in 1998, whereas the five missiles developed under IGMDP (1983) were Prithvi, Agni, Trishul, Akash, and Nag."
      },
      {
        "id": "MCQ-STE04-03",
        "q": "What type of propulsion system powers the cruise stage of the BrahMos supersonic cruise missile?",
        "options": ["Scramjet Engine", "Liquid Fuel Ramjet Engine", "Solid Rocket Booster only", "Cryogenic Engine"],
        "ans": "b",
        "explanation": "BrahMos is a two-stage missile with a solid propellant booster engine as the first stage (bringing it to supersonic speed) and a liquid ramjet engine as the second stage maintaining Mach 2.8–3.0 cruise speed."
      },
      {
        "id": "MCQ-STE04-04",
        "q": "What is the name of India's first indigenously designed and built nuclear-powered ballistic missile submarine (SSBN) commissioned into the Indian Navy in 2016?",
        "options": ["INS Kalvari", "INS Arihant", "INS Chakra", "INS Vikrant"],
        "ans": "b",
        "explanation": "INS Arihant is India's first indigenous nuclear-powered ballistic missile submarine (SSBN), which completed its maiden deterrence patrol in 2018, operationalizing India's nuclear triad."
      },
      {
        "id": "MCQ-STE04-05",
        "q": "In DRDO's two-tier Ballistic Missile Defence (BMD) system, which interceptor is specifically designed for 'exo-atmospheric' (outside the atmosphere) interception?",
        "options": ["Advanced Air Defence (AAD / Ashwin)", "Prithvi Air Defence (PAD / Pradyumna)", "Akash-NG", "QRSAM"],
        "ans": "b",
        "explanation": "Prithvi Air Defence (PAD) / Pradyumna is designed for exo-atmospheric interception of incoming ballistic missiles at altitudes of 50 km to 80 km, while Advanced Air Defence (AAD) operates endo-atmospherically below 30 km."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-05",
    "filename": "05_nuclear_energy_three_stage_program_and_safety",
    "title": "Nuclear Energy: Three-Stage Program, Safety & Treaties",
    "mapping": "Science, Technology & Environment: Department of Atomic Energy (DAE), Homi J. Bhabha's Three-Stage Nuclear Power Programme (PHWR, FBR, Thorium Utilization), Prototype Fast Breeder Reactor (PFBR Kalpakkam), Civil Liability for Nuclear Damage Act (CLNDA 2010), Atomic Energy Regulatory Board (AERB), and Indo-US 123 Agreement.",
    "intro": "Nuclear energy represents an essential clean baseload pillar in India's long-term energy transition to Net Zero by 2070. Formulated by Dr. Homi J. Bhabha, India's Three-Stage Nuclear Power Programme is tailored to the nation's resource realities: modest domestic uranium reserves but vast deposits of thorium in coastal monazite sands. Operating under strict regulatory oversight by the Atomic Energy Regulatory Board (AERB), the program integrates closed fuel cycles, breeder reactors, and international civil nuclear commerce enabled by India's 2008 NSG waiver.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Kudankulam_Nuclear_Power_Plant.jpg", "caption": "Kudankulam Nuclear Power Plant in Tamil Nadu, India's highest-capacity operational nuclear power facility utilizing VVER-1000 reactors.", "alt": "Kudankulam Nuclear Power Plant"},
    "table": {
      "caption": "Dr. Homi Bhabha's Three-Stage Nuclear Power Programme",
      "headers": ["Stage", "Reactor Technology Used", "Primary Fuel & Moderator", "By-Product & Next-Stage Strategic Link"],
      "rows": [
        ["Stage 1: PHWRs", "Pressurized Heavy Water Reactors (PHWRs)", "Natural Uranium (U-238 + 0.7% U-235); Heavy Water ($D_2O$)", "Produces Plutonium-239 (Pu-239) via neutron capture in depleted U-238"],
        ["Stage 2: FBRs", "Fast Breeder Reactors (e.g., PFBR 500 MWe at Kalpakkam)", "Plutonium-239 and Uranium-238 (MOX Fuel); Liquid Sodium coolant", "'Breeds' more fissile Pu-239 than consumed; Thorium blanket breeds fissile Uranium-233"],
        ["Stage 3: AHWRs", "Advanced Heavy Water Reactors & Molten Salt Reactors", "Thorium-232 and Uranium-233 fuel cycle; Heavy Water / Molten Salts", "Taps vast monazite thorium reserves (>300,000 tonnes) to achieve sovereign energy independence"]
      ]
    },
    "points": [
      "PFBR Core Loading Milestone: In March 2024, core loading commenced for the indigenous 500 MWe Prototype Fast Breeder Reactor (PFBR) at Kalpakkam, Tamil Nadu, marking India's decisive entry into the critical second stage of its nuclear energy program.",
      "Thorium Geopolitics & Monazite Sands: India possesses ~25% of the world's thorium reserves, predominantly found in the beach monazite sands of Kerala, Tamil Nadu, Andhra Pradesh, and Odisha. Thorium-232 is fertile, not fissile, necessitating transmutation into Uranium-233 in fast neutron reactors.",
      "Civil Liability for Nuclear Damage Act (CLNDA 2010): Section 17(b) permits the plant operator (NPCIL) a 'right of recourse' against foreign equipment suppliers if an accident results from supplier-provided defective equipment—a unique provision globally that historically delayed foreign vendor contracts.",
      "AERB Safety Architecture: The Atomic Energy Regulatory Board (AERB) enforces stringent nuclear, industrial, and radiological safety standards, carrying out periodic safety audits, seismic reviews, and emergency preparedness drills across all nuclear installations.",
      "Small Modular Reactors (SMRs) & Private Investment: The Government has initiated policies to deploy indigenous 220 MWe PHWR-based SMRs to decarbonize captive industrial clusters (steel, cement) and amended atomic energy policies to invite private domestic capital for non-strategic components."
    ],
    "mains": [
      "Elucidate the scientific rationale and structural stages of India's Three-Stage Nuclear Power Programme. Why is the commissioning of the Prototype Fast Breeder Reactor (PFBR) critical for tapping India's vast thorium reserves? (250 Words, 15 Marks)",
      "Discuss the key challenges that have hindered the rapid expansion of nuclear power in India, with specific reference to the Civil Liability for Nuclear Damage Act (CLNDA 2010) and land acquisition controversies. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE05-01",
        "q": "Which mineral found extensively in the beach sands of coastal India is the primary source of fertile Thorium?",
        "options": ["Bauxite", "Monazite", "Pitchblende", "Ilmenite"],
        "ans": "b",
        "explanation": "Monazite sands, found along the coastal stretches of Kerala, Tamil Nadu, Andhra Pradesh, and Odisha, are the principal commercial source of rare earths and thorium."
      },
      {
        "id": "MCQ-STE05-02",
        "q": "What fuel combination and coolant are utilized in the 500 MWe Prototype Fast Breeder Reactor (PFBR) at Kalpakkam?",
        "options": ["Enriched Uranium with Light Water", "Natural Uranium with Heavy Water", "Plutonium-Uranium mixed oxide (MOX) with Liquid Sodium coolant", "Thorium-232 with Molten Lead"],
        "ans": "c",
        "explanation": "The PFBR at Kalpakkam utilizes Mixed Oxide (MOX) fuel comprising Plutonium-239 and Uranium-238, cooled by liquid sodium which enables fast neutron breeding without moderation."
      },
      {
        "id": "MCQ-STE05-03",
        "q": "In Stage 1 of India's nuclear power programme (PHWRs), what substance is utilized as both moderator and coolant?",
        "options": ["Light Water ($H_2O$)", "Heavy Water ($D_2O$ - Deuterium Oxide)", "Liquid Sodium", "Graphite"],
        "ans": "b",
        "explanation": "Pressurized Heavy Water Reactors (PHWRs) use Heavy Water ($D_2O$) as both coolant and moderator, which allows them to run on natural unenriched uranium."
      },
      {
        "id": "MCQ-STE05-04",
        "q": "Which section of the Civil Liability for Nuclear Damage Act (CLNDA) 2010 grants the operator a 'Right of Recourse' against foreign suppliers for defective equipment?",
        "options": ["Section 4", "Section 10", "Section 17(b)", "Section 46"],
        "ans": "c",
        "explanation": "Section 17(b) of CLNDA 2010 gives the Indian operator a statutory right of recourse against the supplier where the nuclear incident has occurred as the consequence of an act of supplier or his employee, which includes supply of equipment with latent defects."
      },
      {
        "id": "MCQ-STE05-05",
        "q": "What is the autonomous apex regulatory authority that enforces safety codes and regulates nuclear and radiation installations in India?",
        "options": ["Bhabha Atomic Research Centre (BARC)", "Nuclear Power Corporation of India Limited (NPCIL)", "Atomic Energy Regulatory Board (AERB)", "Uranium Corporation of India Limited (UCIL)"],
        "ans": "c",
        "explanation": "The Atomic Energy Regulatory Board (AERB) was established in 1983 to carry out regulatory and safety functions under the Atomic Energy Act, 1962 across all nuclear and radiation facilities."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-06",
    "filename": "06_renewable_energy_solar_green_hydrogen_and_transition",
    "title": "Renewable Energy: Solar, Green Hydrogen & Clean Transition",
    "mapping": "Science, Technology & Environment: Renewable Energy Targets (500 GW Non-Fossil by 2030), International Solar Alliance (ISA), PM-KUSUM, National Green Hydrogen Mission (SIGHT Scheme), National Wind-Solar Hybrid Policy, and Battery Energy Storage Systems (BESS).",
    "intro": "India is orchestrating one of the world's most ambitious clean energy transitions, aiming to install 500 GW of non-fossil power capacity by 2030 and achieve Net Zero carbon emissions by 2070. Anchored by the Ministry of New and Renewable Energy (MNRE), India has scaled solar and wind power, championed the International Solar Alliance (ISA) headquartered in Gurugram, and committed Rs 19,744 crore under the National Green Hydrogen Mission to decarbonize hard-to-abate industrial sectors (refineries, fertilizers, steel).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Solar_Park_Kurnool_Andhra_Pradesh.jpg", "caption": "Kurnool Ultra Mega Solar Park in Andhra Pradesh (1,000 MW capacity), one of the largest operational solar parks in India.", "alt": "Kurnool Ultra Mega Solar Park Andhra Pradesh"},
    "table": {
      "caption": "India's Clean Energy Pillars & Key Flagship Schemes",
      "headers": ["Policy / Mission", "Nodal Agency / Scheme Outlay", "Target Capacity / Output", "Strategic Focus & Economic Impact"],
      "rows": [
        ["Non-Fossil Capacity 2030 Target", "MNRE / Central Electricity Authority (CEA)", "500 GW non-fossil capacity by 2030", "Enables 50% cumulative electric power from non-fossil resources (NDC target)"],
        ["National Green Hydrogen Mission", "MNRE / SIGHT Scheme (Rs 19,744 Cr)", "5 MMT green hydrogen per annum by 2030", "Electrolyser manufacturing incentives and green hydrogen production subsidies"],
        ["PM-KUSUM", "MNRE (Pradhan Mantri Kisan Urja Suraksha)", "Over 35 GW agricultural solar capacity", "De-dieselization of farm irrigation; standalone solar pumps and solarization of feeders"],
        ["PM Surya Ghar: Muft Bijli Yojana", "MNRE (Rs 75,021 Cr outlay launched 2024)", "1 Crore households with rooftop solar", "Up to 300 units free electricity/month; up to Rs 78,000 central subsidy per rooftop"],
        ["Kurnool Ultra Mega Solar Park", "AP Solar Power Corporation (APSPCL)", "1,000 MW operational capacity", "Rayalaseema clean power hub integrating mega solar with Pinnapuram pumped hydro"]
      ]
    },
    "points": [
      "National Green Hydrogen Mission Architecture: Approved in January 2023 with an outlay of Rs 19,744 crore. Administers the Strategic Interventions for Green Hydrogen Transition (SIGHT) program offering financial incentives for domestic electrolyser manufacturing and green hydrogen production.",
      "Green Hydrogen Definitions: Defined in India as hydrogen produced through electrolysis of water using renewable power, or through biomass conversion, where the well-to-gate greenhouse gas emissions do not exceed 2 kg $CO_2$ equivalent per kg $H_2$.",
      "International Solar Alliance (ISA): Co-founded by India and France at COP21 in Paris, ISA is the first treaty-based intergovernmental organization headquartered in India (Gurugram, Haryana). Championing the 'One Sun, One World, One Grid' (OSOWOG) initiative to interconnect transnational solar grids.",
      "Pumped Storage Projects (PSP) & Grid Balancing: Because solar and wind are intermittent, Andhra Pradesh has emerged as a national frontrunner in Integrated Renewable Energy Storage Projects (IRESP), notably the 1,200 MW Pinnapuram Pumped Storage Project in Kurnool district combining solar, wind, and pumped hydro.",
      "Transmission Corridors & Green Energy Open Access: The Green Energy Corridor (GEC) project constructs intra-state and inter-state transmission networks with automated grid management to evacuate renewable power from arid generation belts in Rajasthan, Gujarat, and Andhra Pradesh."
    ],
    "mains": [
      "Analyze the objectives and strategic significance of the National Green Hydrogen Mission. What technological, water availability, and cost challenges must India overcome to become a global green hydrogen export hub? (250 Words, 15 Marks)",
      "Discuss the potential and challenges of rooftop solar adoption in India with specific reference to the 'PM Surya Ghar: Muft Bijli Yojana'. How can discoms balance rooftop adoption with grid stability? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE06-01",
        "q": "What annual Green Hydrogen production target does India aim to achieve by 2030 under the National Green Hydrogen Mission?",
        "options": ["1 Million Metric Tonnes (MMT)", "5 Million Metric Tonnes (MMT)", "10 Million Metric Tonnes (MMT)", "20 Million Metric Tonnes (MMT)"],
        "ans": "b",
        "explanation": "The National Green Hydrogen Mission targets building a green hydrogen production capacity of at least 5 Million Metric Tonnes (MMT) per annum by 2030, supported by ~125 GW of associated renewable energy capacity."
      },
      {
        "id": "MCQ-STE06-02",
        "q": "Where is the global headquarters of the International Solar Alliance (ISA) located?",
        "options": ["Paris, France", "Geneva, Switzerland", "Gurugram, Haryana (India)", "New Delhi, India"],
        "ans": "c",
        "explanation": "The headquarters of the International Solar Alliance (ISA) is situated at the National Institute of Solar Energy (NISE) campus in Gurugram, Haryana, India."
      },
      {
        "id": "MCQ-STE06-03",
        "q": "What is the national non-fossil electric power generation capacity target set by India to be achieved by the year 2030?",
        "options": ["175 GW", "350 GW", "500 GW", "750 GW"],
        "ans": "c",
        "explanation": "At COP26 in Glasgow, India announced its enhanced target to install 500 GW of non-fossil energy capacity by the year 2030 as part of its 'Panchamrit' climate pledges."
      },
      {
        "id": "MCQ-STE06-04",
        "q": "Under the PM Surya Ghar: Muft Bijli Yojana launched in 2024, how many households are targeted for rooftop solar installation?",
        "options": ["25 Lakh households", "50 Lakh households", "1 Crore (10 Million) households", "2.5 Crore households"],
        "ans": "c",
        "explanation": "The PM Surya Ghar: Muft Bijli Yojana was approved with an outlay of Rs 75,021 crore to provide free electricity up to 300 units/month by installing rooftop solar systems in 1 crore households."
      },
      {
        "id": "MCQ-STE06-05",
        "q": "In which district of Andhra Pradesh is the major 1,000 MW Ultra Mega Solar Park located?",
        "options": ["Ananthapuramu", "Kurnool", "YSR Kadapa", "Chittoor"],
        "ans": "b",
        "explanation": "The Kurnool Ultra Mega Solar Park, with an installed capacity of 1,000 MW, is located in Gani and Sakunala villages of Kurnool district, Andhra Pradesh."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-07",
    "filename": "07_biotechnology_genetic_engineering_and_healthcare",
    "title": "Biotechnology, Genetic Engineering & Modern Healthcare",
    "mapping": "Science, Technology & Environment: Department of Biotechnology (DBT), Recombinant DNA Technology, CRISPR-Cas9 Gene Editing, Genetically Modified (GM) Crops & Regulatory Framework (GEAC), Stem Cell Therapy, Vaccines (mRNA, DNA), Neglected Tropical Diseases, and Antimicrobial Resistance (AMR).",
    "intro": "Biotechnology and genetic engineering have revolutionized medicine, agriculture, and industrial manufacturing. Spearheaded by the Department of Biotechnology (DBT) and research councils like ICMR and CSIR, India's bio-economy exceeded $130 billion in 2024. From pioneering indigenous DNA vaccines during the COVID-19 pandemic to advancing CRISPR-Cas9 genome editing for sickle cell anemia and regulating Genetically Modified (GM) crops via the Genetic Engineering Appraisal Committee (GEAC), biotechnology plays a transformative role in national health and food security.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/DNA_Double_Helix_Model.jpg", "caption": "Double-helix model of DNA, the basis of modern recombinant genetics, CRISPR editing, and vaccine biotechnology.", "alt": "DNA Double Helix structure"},
    "table": {
      "caption": "Frontier Biotechnology Applications & Indian Regulatory Oversight",
      "headers": ["Biotech Domain", "Underlying Scientific Platform", "Key Breakthroughs & Indian Products", "Statutory Regulator / Framework"],
      "rows": [
        ["CRISPR-Cas9 Gene Editing", "Clustered Regularly Interspaced Short Palindromic Repeats; Cas9 molecular scissors", "Sickle-cell anemia therapies; indigenous CRISPR diagnostics (FELUDA test by CSIR-IGIB)", "National Guidelines for Stem Cell Research & Gene Therapy (ICMR/DBT)"],
        ["Agricultural GMOs", "Recombinant DNA insertion of alien genes (e.g., Cry1Ac endotoxin from Bacillus thuringiensis)", "Bt Cotton (only commercial GM crop); GM Mustard DMH-11 (GEAC environmental release approval)", "Genetic Engineering Appraisal Committee (GEAC) under MoEFCC (EPA 1986 Rules 1989)"],
        ["Vaccine Platforms", "Plasmids (DNA), Synthetic mRNA, Inactivated viral vectors, Protein sub-units", "ZyCoV-D (World's first DNA vaccine by Zydus); Covaxin (inactivated); GEMCOVAC-19 (mRNA)", "Central Drugs Standard Control Organisation (CDSCO) under Drugs and Cosmetics Act"],
        ["Stem Cell Therapy", "Pluripotent & Hematopoietic stem cell differentiation", "Bone marrow transplants; regenerative treatments for corneal damage (LV Prasad Eye Institute AP/TS)", "Prohibits commercial embryonic stem cell therapies; restricts to approved hematological indications"]
      ]
    },
    "points": [
      "CRISPR-Cas9 Genome Editing Revolution: Discovered by Emmanuelle Charpentier and Jennifer Doudna (Nobel Prize 2020), this targeted molecular scalpel allows precise deletion or insertion of genetic code. CSIR-IGIB developed 'FELUDA' (FnCas9 Editor Linked Uniform Detection Assay) for low-cost pathogen detection.",
      "GM Crop Regulatory Architecture: Functioning under the Environment (Protection) Act 1986 Rules 1989, the multi-tier biosafety system comprises: 1. Institutional Biosafety Committee (IBSC); 2. Review Committee on Genetic Manipulation (RCGM) under DBT; 3. Genetic Engineering Appraisal Committee (GEAC) under MoEFCC as the apex statutory authority approving field trials and commercial release.",
      "GM Mustard (Dhara Mustard Hybrid-11 / DMH-11): Developed by Delhi University using the 'barnase-barstar' gene system from soil bacterium Bacillus amyloliquefaciens to induce male sterility for high-yielding hybrid mustard seeds. Received GEAC environmental release recommendation in October 2022.",
      "Antimicrobial Resistance (AMR) & National Action Plan: India is combating the silent pandemic of multidrug-resistant 'superbugs' caused by antibiotic misuse in human health and livestock farming through the National Action Plan on AMR (NAP-AMR), Schedule H1 red-line antibiotic packaging, and surveillance via ICMR's AMR surveillance network.",
      "Sickle Cell Anemia Elimination Mission 2047: Launched to eliminate sickle cell disease among tribal populations across 17 high-prevalence states, deploying universal point-of-care genetic screening, pre-marital genetic counseling, and indigenous hydroxyurea/CRISPR treatment access."
    ],
    "mains": [
      "Explain the scientific mechanism of CRISPR-Cas9 genome editing technology. Discuss its clinical potential in eradicating genetic disorders like Sickle Cell Disease and Thalassemia in India. (250 Words, 15 Marks)",
      "Critically evaluate the environmental and biosecurity debates surrounding the commercial release of Genetically Modified (GM) food crops in India, with specific reference to GM Mustard (DMH-11). (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE07-01",
        "q": "Which statutory apex authority under the Ministry of Environment, Forest and Climate Change (MoEFCC) is empowered to approve environmental release and commercial cultivation of Genetically Modified (GM) organisms in India?",
        "options": ["Review Committee on Genetic Manipulation (RCGM)", "Genetic Engineering Appraisal Committee (GEAC)", "Department of Biotechnology (DBT)", "Food Safety and Standards Authority of India (FSSAI)"],
        "ans": "b",
        "explanation": "The Genetic Engineering Appraisal Committee (GEAC), constituted under the Rules 1989 of the Environment (Protection) Act 1986, is the apex statutory body for approval of activities involving large-scale use of hazardous microorganisms and environmental release of GM organisms."
      },
      {
        "id": "MCQ-STE07-02",
        "q": "Which is the only Genetically Modified (GM) crop currently approved for commercial commercial cultivation by farmers in India?",
        "options": ["Bt Brinjal", "Bt Cotton", "DMH-11 Mustard", "Golden Rice"],
        "ans": "b",
        "explanation": "Bt Cotton is the only genetically modified crop officially approved for commercial cultivation in India, approved by GEAC in 2002."
      },
      {
        "id": "MCQ-STE07-03",
        "q": "Which Indian company developed ZyCoV-D, the world's first needle-free plasmid DNA vaccine approved for emergency human use against COVID-19?",
        "options": ["Bharat Biotech", "Serum Institute of India", "Zydus Cadila", "Biological E"],
        "ans": "c",
        "explanation": "ZyCoV-D, developed by Zydus Cadila in partnership with the Department of Biotechnology, was the world's first plasmid DNA vaccine approved for emergency human immunization."
      },
      {
        "id": "MCQ-STE07-04",
        "q": "What bacterial gene system was utilized by Delhi University scientists to develop the hybrid Genetically Modified mustard DMH-11?",
        "options": ["Cry1Ac and Cry2Ab genes", "Barnase and Barstar gene system", "Cas9 and sgRNA system", "nif gene complex"],
        "ans": "b",
        "explanation": "DMH-11 was created using the 'barnase-barstar' gene system derived from the soil bacterium Bacillus amyloliquefaciens to facilitate outcrossing and hybrid seed production in self-pollinating mustard."
      },
      {
        "id": "MCQ-STE07-05",
        "q": "By which year does the National Sickle Cell Anemia Elimination Mission aim to eliminate Sickle Cell Disease from India's tribal and vulnerable populations?",
        "options": ["2030", "2035", "2040", "2047"],
        "ans": "d",
        "explanation": "The National Sickle Cell Anemia Elimination Mission, launched from Madhya Pradesh in 2023, specifically targets eliminating Sickle Cell Disease by the year 2047."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-08",
    "filename": "08_environmental_conservation_and_biodiversity_acts",
    "title": "Environmental Conservation & Biodiversity Legislation",
    "mapping": "Science, Technology & Environment: Environment (Protection) Act 1986, Wildlife (Protection) Act 1972 & 2022 Amendment, Forest (Conservation) Amendment Act 2023, Biological Diversity Act 2002 & 2023 Amendment, National Green Tribunal (NGT Act 2010), Project Tiger (50 Years) and Protected Area Network.",
    "intro": "India is one of the world's 17 megadiverse nations, harboring four global biodiversity hotspots (Western Ghats, Himalayas, Indo-Burma, Sundaland). Environmental governance rests on robust constitutional mandates (Articles 48A and 51A(g)) operationalized through pioneering statutory frameworks: the Wildlife (Protection) Act 1972, the Environment (Protection) Act 1986, the Biological Diversity Act 2002, and the specialized National Green Tribunal (NGT). Modern amendments harmonize wildlife conservation with CITES treaty compliance, access and benefit sharing (ABS), and sustainable developmental imperatives.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Bengal_Tiger_in_Kanha_National_Park.jpg", "caption": "Royal Bengal Tiger in Kanha Tiger Reserve, the flagship species protected under Project Tiger and the National Tiger Conservation Authority.", "alt": "Bengal Tiger in Indian national park"},
    "table": {
      "caption": "Apex Environmental Statutes & Recent Legislative Amendments",
      "headers": ["Legislation", "Original Enactment", "Recent Amendments (2022/2023)", "Core Provisions & Conservation Mechanisms"],
      "rows": [
        ["Wildlife (Protection) Act (WPA)", "1972", "WPA Amendment Act 2022 (Effective April 2023)", "Rationalized schedules from 6 to 4; aligned with CITES; created Management Authority for endangered fauna"],
        ["Biological Diversity Act (BDA)", "2002", "Biological Diversity Amendment Act 2023", "Three-tier architecture (NBA, SBB, BMC); streamlines Access & Benefit Sharing (ABS) for AYUSH practitioners"],
        ["Forest (Conservation) Act (FCA)", "1980", "Van (Sanrakshan Evam Samvardhan) Adhiniyam 2023", "Renamed statute; exempts linear strategic projects within 100 km of international borders from prior forest clearance"],
        ["National Green Tribunal Act (NGT)", "2010", "Operational under Article 21 constitutional jurisprudence", "Specialized environmental court with judicial and expert members; applies polluter pays and precautionary principles"],
        ["Project Tiger / NTCA", "1973 (50 Years completed 2023)", "Statutory status to NTCA in 2006", "Covers 55+ Tiger Reserves; tiger population grew from 1,411 in 2006 to over 3,682 in 2022 (75% of global wild tigers)"]
      ]
    },
    "points": [
      "Wildlife (Protection) Amendment Act 2022: Rationalized the earlier six schedules into four: Schedule I (highest protection for animal species), Schedule II (animal species with lesser protection), Schedule III (protected plant species), and Schedule IV (specimens listed under CITES Appendices). Deleted the separate 'Vermin' schedule, leaving vermin declaration to central notifications.",
      "Biological Diversity Act Three-Tier Governance: National Biodiversity Authority (NBA, Chennai) at the apex, State Biodiversity Boards (SBBs) in all states (including AP SBB in Guntur), and Biodiversity Management Committees (BMCs) at the local panchayat/municipal level preparing People's Biodiversity Registers (PBRs).",
      "Van (Sanrakshan Evam Samvardhan) Adhiniyam 2023: Narrows the application of the Forest Conservation Act strictly to notified government forests and lands recorded as forest in government records on or after October 25, 1980, modifying the expansive dictionary definition established in the Supreme Court's 1996 Godavarman judgement.",
      "National Green Tribunal (NGT): Established under NGT Act 2010 pursuant to India's Rio 1992 commitments and Article 21 right to a healthy environment. Mandated to dispose of environmental disputes within 6 months. Replaced traditional civil courts across seven environmental acts (excluding WPA and IFA).",
      "Protected Area Network in Andhra Pradesh: AP hosts Papikonda National Park, Sri Venkateswara National Park, and Nagarjunasagar-Srisailam Tiger Reserve (NSTR)—the largest tiger reserve in India spanning the Nallamala forest range across AP and Telangana."
    ],
    "mains": [
      "Analyze the key structural changes introduced by the Wildlife (Protection) Amendment Act, 2022. How does the rationalization of schedules align Indian domestic wildlife law with the CITES convention? (250 Words, 15 Marks)",
      "Critically examine the provisions and environmental concerns surrounding the Forest (Conservation) Amendment Act, 2023. Does the exemption of border infrastructure undermine ecological security in sensitive zones? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE08-01",
        "q": "Under the Wildlife (Protection) Amendment Act 2022, into how many schedules were protected flora and fauna rationalized?",
        "options": ["4 schedules", "6 schedules", "8 schedules", "10 schedules"],
        "ans": "a",
        "explanation": "The 2022 amendment rationalized the previous six schedules of the Wildlife (Protection) Act 1972 into four schedules: Schedule I (highest protection fauna), Schedule II (lesser protection fauna), Schedule III (plants), and Schedule IV (CITES specimens)."
      },
      {
        "id": "MCQ-STE08-02",
        "q": "Where is the headquarters of the statutory National Biodiversity Authority (NBA) of India located?",
        "options": ["New Delhi", "Kolkata", "Chennai", "Bengaluru"],
        "ans": "c",
        "explanation": "The National Biodiversity Authority (NBA), established in 2003 under Section 8 of the Biological Diversity Act 2002, is headquartered in Chennai, Tamil Nadu."
      },
      {
        "id": "MCQ-STE08-03",
        "q": "Which is the largest Tiger Reserve by geographical area in India, situated across the Nallamala hill ranges of Andhra Pradesh and Telangana?",
        "options": ["Jim Corbett Tiger Reserve", "Nagarjunasagar-Srisailam Tiger Reserve (NSTR)", "Bandipur Tiger Reserve", "Similipal Tiger Reserve"],
        "ans": "b",
        "explanation": "Nagarjunasagar-Srisailam Tiger Reserve (NSTR), covering an area of over 3,296 sq km across the Nallamala forests in Andhra Pradesh and Telangana, is the largest tiger reserve in India."
      },
      {
        "id": "MCQ-STE08-04",
        "q": "Under the NGT Act 2010, the National Green Tribunal is statutorily mandated to make an endeavor to dispose of environmental applications within what timeframe?",
        "options": ["30 days", "90 days", "6 months", "1 year"],
        "ans": "c",
        "explanation": "Section 18(3) of the National Green Tribunal Act 2010 mandates that the Tribunal shall make an endeavor for final disposal of applications or appeals within six months of their filing."
      },
      {
        "id": "MCQ-STE08-05",
        "q": "Which landmark 1996 Supreme Court judgement had broadened the definition of 'forest' under the Forest Conservation Act 1980 to include all areas conforming to the dictionary meaning?",
        "options": ["M.C. Mehta v. Union of India", "T.N. Godavarman Thirumulpad v. Union of India", "Vellore Citizens Welfare Forum case", "Subhash Kumar v. State of Bihar"],
        "ans": "b",
        "explanation": "In T.N. Godavarman Thirumulpad v. Union of India (1996), the Supreme Court ruled that 'forest' must be understood in accordance with its dictionary meaning, covering all statutorily recognized forests irrespective of ownership."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-09",
    "filename": "09_climate_change_unfccc_cop_summits_and_net_zero_2070",
    "title": "Climate Change, UNFCCC, COP Summits & Net Zero 2070",
    "mapping": "Science, Technology & Environment: UNFCCC, Kyoto Protocol, Paris Agreement (COP21), India's Updated Nationally Determined Contributions (NDCs), Glasgow COP26 'Panchamrit' Pledges, Net Zero by 2070, Mission LiFE (Lifestyle for Environment), Carbon Credit Trading Scheme (CCTS), and Carbon Border Adjustment Mechanism (CBAM).",
    "intro": "Anthropogenic climate change poses existential risks to global hydrological cycles, agricultural productivity, and human settlements. Guided by the UN Framework Convention on Climate Change (UNFCCC) and the landmark 2015 Paris Agreement, global climate action centers on limiting global temperature rise to well below 2°C above pre-industrial levels. Under the principle of Common But Differentiated Responsibilities and Respective Capabilities (CBDR-RC), India has updated its Nationally Determined Contributions (NDCs) and committed to achieving Net Zero greenhouse gas emissions by 2070.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/COP28_Dubai_Summit_Plenary.jpg", "caption": "Plenary hall of the UNFCCC Conference of the Parties (COP), the supreme decision-making body for global climate treaties.", "alt": "UNFCCC COP climate summit plenary"},
    "table": {
      "caption": "India's Enhanced Nationally Determined Contributions (NDCs) & Panchamrit Pledges",
      "headers": ["NDC Pillar / Target", "2015 Paris NDC Benchmark", "Updated 2022/2026 Enhanced Commitment", "Target Year & Implementation Framework"],
      "rows": [
        ["Emissions Intensity of GDP", "Reduce by 33% to 35% from 2005 levels", "Reduce by 45% from 2005 levels", "By 2030; already reduced by >33% by 2019 (achieved ahead of schedule)"],
        ["Non-Fossil Electric Power Share", "40% cumulative electric power from non-fossil", "50% cumulative electric power from non-fossil sources", "By 2030; accelerated via 500 GW renewable expansion target"],
        ["Carbon Sink Creation", "Additional 2.5 to 3.0 billion tonnes of $CO_2$ equivalent", "Maintained at 2.5 to 3.0 billion tonnes $CO_2$e through forest/tree cover", "By 2030; promoted via Green Credit Programme and MISHTI mangrove initiative"],
        ["Long-Term Net Zero Target", "No formal long-term net-zero timeline", "Net Zero greenhouse gas emissions", "By 2070; submitted in Long-Term Low-Emission Development Strategy (LT-LEDS)"],
        ["Mission LiFE (Lifestyle for Environment)", "Not formulated in 2015", "Pro-Planet People (P3) global citizen movement", "Promotes mindful resource consumption over mindless destructive consumerism"]
      ]
    },
    "points": [
      "Paris Agreement & CBDR-RC: Formulated at COP21 (2015) to hold global warming well below 2°C and pursue efforts to limit it to 1.5°C. Replaced the rigid top-down Kyoto Protocol annexes with bottom-up, self-determined Nationally Determined Contributions (NDCs) subject to 5-year Global Stocktake reviews.",
      "Panchamrit Pledges at Glasgow COP26: Prime Minister Narendra Modi unveiled five nectar elements: 1. 500 GW non-fossil energy capacity by 2030; 2. 50% energy requirements from renewables by 2030; 3. Reduce total projected carbon emissions by 1 billion tonnes by 2030; 4. Reduce emissions intensity of GDP by 45% by 2030; 5. Achieve Net Zero emissions by 2070.",
      "Carbon Credit Trading Scheme (CCTS): Established under the Energy Conservation (Amendment) Act 2022. Administered by the Bureau of Energy Efficiency (BEE) to create a domestic compliance and voluntary carbon market replacing the Perform, Achieve and Trade (PAT) scheme.",
      "Loss and Damage Fund: Operationalized at COP27 (Sharm el-Sheikh) and capitalized at COP28 (Dubai) to provide financial assistance to climate-vulnerable developing nations suffering catastrophic climate-induced disasters.",
      "EU Carbon Border Adjustment Mechanism (CBAM) Threat: The European Union's carbon tariff on imported carbon-intensive goods (steel, aluminum, cement, fertilizers, hydrogen) poses significant export challenges for Indian heavy manufacturers, accelerating the urgency of industrial decarbonization."
    ],
    "mains": [
      "Examine India's 'Panchamrit' climate pledges announced at COP26 and its updated Nationally Determined Contributions (NDCs). How does India balance its poverty alleviation imperatives with ambitious decarbonization commitments? (250 Words, 15 Marks)",
      "Discuss the implications of the European Union's Carbon Border Adjustment Mechanism (CBAM) for India's export competitiveness. What strategic policy options are available to protect Indian industrial interests? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE09-01",
        "q": "By which year has India formally committed to achieve Net Zero greenhouse gas emissions under its Long-Term Low Emissions Development Strategy (LT-LEDS)?",
        "options": ["2050", "2060", "2070", "2080"],
        "ans": "c",
        "explanation": "At the COP26 climate summit in Glasgow, India committed to achieving Net Zero carbon emissions by the year 2070."
      },
      {
        "id": "MCQ-STE09-02",
        "q": "In its updated Nationally Determined Contributions (NDCs) submitted to UNFCCC in 2022, what target did India set for reducing the emissions intensity of its GDP from 2005 levels by 2030?",
        "options": ["33%", "35%", "45%", "50%"],
        "ans": "c",
        "explanation": "India enhanced its emissions intensity reduction target from 33–35% (set in 2015) to 45% by 2030 compared to 2005 levels."
      },
      {
        "id": "MCQ-STE09-03",
        "q": "What is the core philosophy of 'Mission LiFE' launched by India in the presence of UN Secretary-General António Guterres?",
        "options": ["Industrial Carbon Sequestration", "Lifestyle for Environment – mindful and deliberate resource utilization", "Universal electric vehicle transition", "100% afforestation of degraded lands"],
        "ans": "b",
        "explanation": "Mission LiFE (Lifestyle for Environment) promotes individual and collective behavioral shifts toward mindful consumption rather than mindless consumerism to protect the global environment."
      },
      {
        "id": "MCQ-STE09-04",
        "q": "Which Indian statutory agency administers the domestic Carbon Credit Trading Scheme (CCTS) established under the Energy Conservation (Amendment) Act 2022?",
        "options": ["Central Pollution Control Board (CPCB)", "Bureau of Energy Efficiency (BEE)", "NITI Aayog", "National Green Tribunal (NGT)"],
        "ans": "b",
        "explanation": "The Bureau of Energy Efficiency (BEE), functioning under the Ministry of Power, is the designated administrator for developing and operating India's Carbon Credit Trading Scheme (CCTS)."
      },
      {
        "id": "MCQ-STE09-05",
        "q": "At which UNFCCC Conference of the Parties (COP) was the historic agreement reached to formally establish a dedicated 'Loss and Damage Fund' for vulnerable nations?",
        "options": ["COP21 (Paris)", "COP26 (Glasgow)", "COP27 (Sharm el-Sheikh)", "COP28 (Dubai)"],
        "ans": "c",
        "explanation": "The landmark decision to establish a dedicated fund for Loss and Damage to assist developing nations vulnerable to climate disasters was adopted at COP27 held in Sharm el-Sheikh, Egypt in 2022."
      }
    ]
  },
  {
    "id": "APPSC-G1-STE-10",
    "filename": "10_pollution_control_waste_management_and_coastal_regulation",
    "title": "Pollution Control, Waste Management & Coastal Regulation",
    "mapping": "Science, Technology & Environment: Central Pollution Control Board (CPCB), National Clean Air Programme (NCAP, AQI), Solid Waste Management Rules 2016, E-Waste Management Rules 2022, Plastic Waste Management Rules (Single-Use Plastic Ban, EPR), Coastal Regulation Zone (CRZ 2019 Notification), and Wetland Conservation (Ramsar Sites, Kolleru Lake in AP).",
    "intro": "Pollution control and ecosystem restoration are paramount for safeguarding public health, environmental justice, and ecological resilience. Regulated by the Central Pollution Control Board (CPCB) and State Pollution Control Boards (APPCB) under the Water Act 1974 and Air Act 1981, India's environmental apparatus enforces stringent mandates including the National Clean Air Programme (NCAP), Extended Producer Responsibility (EPR) across plastic and electronic waste, the Coastal Regulation Zone (CRZ 2019) framework, and Ramsar wetland conservation.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Kolleru_Lake_Pelican_sanctuary_AP.jpg", "caption": "Spot-billed pelicans and migratory birds at Kolleru Lake, a premier Ramsar wetland site in Andhra Pradesh.", "alt": "Kolleru Lake Ramsar site Andhra Pradesh"},
    "table": {
      "caption": "Statutory Waste Management Regimes & Environmental Guidelines",
      "headers": ["Environmental Domain", "Governing Rules / Notification", "Core Mandates & Prohibitions", "Regulatory Instruments & Enforcement"],
      "rows": [
        ["Air Pollution Control", "Air (Prevention & Control of Pollution) Act 1981; NCAP (2019)", "Targets 20–30% reduction in PM2.5/PM10 concentrations (enhanced to 40% by 2026)", "National Air Quality Index (AQI 8 pollutants); Commission for Air Quality Management (CAQM) in NCR"],
        ["Plastic Waste Management", "Plastic Waste Management Rules 2016 (Amended 2021/2022)", "Nationwide ban on identified Single-Use Plastics (effective July 1, 2022); thickness >= 120 microns", "Mandatory Extended Producer Responsibility (EPR) portal for Brand Owners, Producers, Importers"],
        ["E-Waste Management", "E-Waste (Management) Rules 2022", "Covers 106 electrical and electronic equipment (EEE) items; solar PV modules/cells", "Mandatory recycling targets for producers; restricts hazardous substances (RoHS)"],
        ["Coastal Regulation Zone", "CRZ Notification 2019 (under EPA 1986)", "Bifurcates CRZ-III into CRZ-III A (densely populated, 50 m NDZ) and CRZ-III B (200 m NDZ)", "State Coastal Zone Management Authorities (APSCZMA); balances port/tourism growth with mangrove safety"],
        ["Wetland Conservation", "Wetlands (Conservation and Management) Rules 2017", "Prohibits industrial setting, waste dumping, solid waste disposal in notified wetlands", "State Wetland Authorities; Ramsar Convention oversight (Kolleru Lake in AP)"]
      ]
    },
    "points": [
      "National Air Quality Index (AQI) Metrics: Launched in 2014 under 'One Number-One Colour-One Description'. Evaluates 8 criteria pollutants: $PM_{10}$, $PM_{2.5}$, Nitrogen Dioxide ($NO_2$), Sulphur Dioxide ($SO_2$), Carbon Monoxide ($CO$), Ozone ($O_3$), Ammonia ($NH_3$), and Lead ($Pb$).",
      "Single-Use Plastics (SUP) Ban: Effective July 1, 2022, India imposed an outright nationwide ban on manufacture, import, stocking, distribution, sale, and use of 19 identified single-use plastic items with low utility and high littering potential (including plastic cutlery, earbuds with plastic sticks, thermocol decoration). Minimum carry bag thickness raised to 120 microns.",
      "CRZ 2019 Notification Architecture: Classifies coastal stretches into: CRZ-I (ecologically sensitive like mangroves and coral reefs; strictly protected), CRZ-II (developed urban shoreline), CRZ-III (rural coastal areas, divided into III-A with 50 m No Development Zone and III-B with 200 m NDZ), and CRZ-IV (water area from Low Tide Line to 12 nautical miles territorial waters).",
      "Kolleru Lake Ramsar Wetland in Andhra Pradesh: Located between Krishna and Godavari deltas spanning Eluru and West Godavari districts. Declared a Ramsar Site in 2002 and Wildlife Sanctuary under WPA 1972. Confronts severe ecological threats from illegal aquaculture encroachment ('Operation Kolleru' demolition), agricultural pesticide runoff, and weed infestation.",
      "Extended Producer Responsibility (EPR) Portals: Implemented digitally by CPCB across Plastic Waste, E-Waste, Waste Tyres, and Used Oil. Producers who fail to meet mandatory recycling quotas face stringent Environmental Compensation (EC) fines based on the polluter-pays principle."
    ],
    "mains": [
      "Explain the key zonations and developmental relaxations introduced under the Coastal Regulation Zone (CRZ) Notification, 2019. How does it balance coastal economic infrastructure with marine disaster vulnerability? (250 Words, 15 Marks)",
      "Discuss the ecological significance of Kolleru Lake as a Ramsar wetland. What anthropogenic pressures threaten its biodiversity, and what conservation measures are imperative for its long-term revival? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-STE10-01",
        "q": "How many criteria air pollutants are monitored to determine the National Air Quality Index (AQI) formulated by the Central Pollution Control Board (CPCB)?",
        "options": ["5 pollutants", "6 pollutants", "8 pollutants", "12 pollutants"],
        "ans": "c",
        "explanation": "The National AQI monitors 8 criteria pollutants: PM10, PM2.5, NO2, SO2, CO, O3, NH3, and Pb."
      },
      {
        "id": "MCQ-STE10-02",
        "q": "On which date did the nationwide ban on identified single-use plastic (SUP) items of low utility and high littering potential take effect across India?",
        "options": ["January 26, 2022", "July 1, 2022", "October 2, 2022", "January 1, 2023"],
        "ans": "b",
        "explanation": "The nationwide ban on the manufacture, import, stocking, distribution, sale, and use of identified single-use plastic items came into force on July 1, 2022."
      },
      {
        "id": "MCQ-STE10-03",
        "q": "Kolleru Lake, a designated Ramsar wetland of international importance in Andhra Pradesh, is geographically situated between the deltas of which two rivers?",
        "options": ["Godavari and Krishna", "Krishna and Pennar", "Godavari and Vamsadhara", "Pennar and Nagavali"],
        "ans": "a",
        "explanation": "Kolleru Lake, one of the largest freshwater lakes in India and a Ramsar site, is located between the deltas of the Godavari and Krishna rivers in Andhra Pradesh."
      },
      {
        "id": "MCQ-STE10-04",
        "q": "Under the CRZ Notification 2019, what is the reduced No Development Zone (NDZ) seaward from the High Tide Line for densely populated rural coastal areas designated as CRZ-III A?",
        "options": ["20 meters", "50 meters", "100 meters", "200 meters"],
        "ans": "b",
        "explanation": "Under CRZ 2019, for CRZ-III A areas (densely populated rural coastal areas with a population density exceeding 2,161 per sq km), the No Development Zone (NDZ) was reduced from 200 meters to 50 meters from the High Tide Line."
      },
      {
        "id": "MCQ-STE10-05",
        "q": "What regulatory mechanism mandates electronics manufacturers and plastic brand owners to finance the end-of-life collection and recycling of their post-consumer products?",
        "options": ["Corporate Social Responsibility (CSR)", "Extended Producer Responsibility (EPR)", "Clean Energy Cess", "National Clean Development Mechanism"],
        "ans": "b",
        "explanation": "Extended Producer Responsibility (EPR) is the statutory environmental policy approach under which producers, importers, and brand owners bear financial and physical responsibility for the treatment or disposal of post-consumer products."
      }
    ]
  }
]

for t in topics:
  content_blocks = [
    {"type": "heading", "level": 1, "text": t["title"]},
    {"type": "paragraph", "text": t["intro"]},
    {"type": "image", "url": t["img"]["url"], "caption": t["img"]["caption"], "alt_text": t["img"]["alt"]},
    {"type": "heading", "level": 2, "text": "1. Scientific, Technological & Legal Architecture"},
    {"type": "table", "caption": t["table"]["caption"], "headers": t["table"]["headers"], "rows": t["table"]["rows"]},
    {"type": "heading", "level": 2, "text": "2. Key Policy Dimensions & Analytical Insights"},
    {"type": "list", "style": "bullet", "items": t["points"]},
    {"type": "heading", "level": 2, "text": "Previous Years Questions (PYQs) - APPSC Group-1"},
    {"type": "heading", "level": 3, "text": "Part A: Mains Analytical & Descriptive Questions"},
    {"type": "list", "style": "numbered", "items": t["mains"]},
    {"type": "heading", "level": 3, "text": "Part B: Screening / Prelims Objective Questions"},
    {"type": "list", "style": "bullet", "items": [f"**Q: {m['q']}**\n* (a) {m['options'][0]}\n* (b) {m['options'][1]}\n* (c) {m['options'][2]}\n* (d) {m['options'][3]}\n* **Answer: ({m['ans']})**\n* *Explanation:* {m['explanation']}" for m in t["mcqs"]]}
  ]
  
  full_text = t["intro"] + " " + " ".join(t["points"]) + " " + " ".join([m["q"] + " " + m["explanation"] for m in t["mcqs"]])
  words = len(full_text.split())
  
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "Science, Technology & Environment",
    "paper": "Mains Paper-V & Screening Paper-II",
    "topic_title": t["title"],
    "syllabus_mapping": t["mapping"],
    "last_updated": "2026-10",
    "content": content_blocks,
    "word_count": words,
    "estimated_read_time_mins": max(4, round(words / 150)),
    "file_name": f"{t['filename']}.json",
    "folder": FOLDER
  }
  
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

# Clean up old lumped files in 07_Science_Technology_Environment
old_files = [
  "01_national_policies_science_institutes.json",
  "02_ict_egovernance_cybersecurity.json",
  "03_space_programme_isro_drdo.json",
  "04_energy_resources_nuclear_policy.json",
  "05_environmental_conservation_climate_change.json",
  "06_biotechnology_nanotechnology_health.json"
]
for f in old_files:
  p = os.path.join(SUBJ_DIR, f)
  if os.path.exists(p):
    os.remove(p)
    print(f"Removed old file: {f}")

print("Subject 7 is fully segregated into 10 topics with 50 MCQs!")
