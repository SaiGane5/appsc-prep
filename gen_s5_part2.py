import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "05_Ethics_and_Law"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-ETH-05",
    "filename": "05_probity_in_governance_anti_corruption_mechanisms",
    "title": "Probity in Governance, Transparency & Anti-Corruption Framework",
    "mapping": "Probity in Governance: Philosophical Basis of Probity, Right to Information (RTI Act 2005), Codes of Ethics and Conduct, Citizen Charters, Work Culture, Quality of Service Delivery, Utilization of Public Funds, Anti-Corruption Institutional Framework (CVC, CBI, Lokpal, Lokayukta, Prevention of Corruption Act 1988/2018).",
    "intro": "Probity in governance signifies the unquestionable integrity, uprightness, and incorruptibility of administrative functionaries. Grounded in the ethical precept of trusteeship, probity demands that public authority and resources be exercised strictly for the common welfare. Transparency and accountability mechanisms—including the Right to Information, Citizen Charters, and multi-tier anti-corruption institutions like the Lokpal, CVC, and State Lokayuktas—form the bedrock of ethical public management in India.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Central_Vigilance_Commission_India.png", "caption": "Central Vigilance Commission (CVC) of India, apex integrity institution established following the Santhanam Committee recommendations.", "alt": "CVC India emblem"},
    "table": {
      "caption": "Institutional & Statutory Anti-Corruption Framework in India",
      "headers": ["Institution / Statute", "Constitutional / Statutory Origin", "Key Jurisdiction & Mandate", "Enforcement & Sanctioning Powers"],
      "rows": [
        ["Central Vigilance Commission (CVC)", "Santhanam Committee (1964); CVC Act 2003 (Statutory Body)", "Superintendence over CBI in corruption cases; advisory jurisdiction over Group-A central officials", "Recommends departmental inquiries; monitors vigilance cases across central ministries"],
        ["Lokpal & Lokayuktas Act 2013", "Statutory Body established under Lokpal Act 2013", "Inquiry into corruption allegations against PM, Ministers, MPs, and Central Group A-D officers", "Has own Inquiry and Prosecution wings; can recommend suspension and direct CBI investigations"],
        ["Central Bureau of Investigation (CBI)", "DPSE Act 1946; operates under DOPT (Vigilance division)", "Premier federal criminal investigation agency for serious economic crimes, corruption, and inter-state offenses", "Powers of search, arrest, seizure, and filing charge sheets in designated Special CBI Courts"],
        ["Prevention of Corruption (Amendment) Act 2018", "Statutory amendment to POCA 1988", "Expressly criminalizes bribe-giving as a distinct offense; introduces corporate liability for bribery", "Section 17A mandates prior approval for investigating public servants; Section 7 penalizes demand/acceptance"]
      ]
    },
    "points": [
      "Philosophical Foundations of Probity: Derived from the doctrine of public trusteeship articulated by Kautilya and Mahatma Gandhi, probity requires civil servants to remain immune to corrupt inducements, maintain institutional objectivity, and practice fiduciary stewardship over public treasuries.",
      "Right to Information (RTI Act 2005): Enacted to empower citizens, promote transparency, and curb bureaucratic opacity. Section 4 mandates proactive disclosure (suo motu disclosures), while Section 8 delineates limited exceptions (sovereignty, national security, commercial secrets). The Central and State Information Commissions adjudicate appeals as quasi-judicial authorities.",
      "Citizen's Charters & Service Delivery: Pioneered by the Department of Administrative Reforms and Public Grievances (DARPG), Citizen Charters specify performance standards, turnaround times, and grievance redressal mechanisms. Andhra Pradesh's Citizen Service Guarantees Act legally enforces time-bound service delivery across urban and rural local bodies.",
      "Whistle Blowers Protection Act 2014: Establishes a statutory mechanism to receive complaints relating to corruption or willful misuse of power against public servants and provides safeguards against administrative or physical victimization of whistleblowers through the CVC.",
      "Second Administrative Reforms Commission (2nd ARC 4th Report - 'Ethics in Governance'): Recommended mandatory codification of civil service values, constitution of National Public Service Authority, elimination of Section 17A delays, and asset declarations for all public servants."
    ],
    "mains": [
      "Examine the philosophical and institutional dimensions of 'Probity in Governance'. Critically analyze whether existing anti-corruption statutes and institutional mechanisms in India have been effective in deterring administrative graft. (250 Words, 15 Marks)",
      "'Transparency without accountability is an illusion, while accountability without transparency is tyranny.' In light of this statement, evaluate the performance and systemic bottlenecks of the RTI Act 2005 after nearly two decades of operation. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ETH05-01",
        "q": "Under the Prevention of Corruption (Amendment) Act, 2018, which section requires prior police investigation approval from the competent authority before probing decisions taken by a public servant?",
        "options": ["Section 13(1)(d)", "Section 17A", "Section 7B", "Section 19"],
        "ans": "b",
        "explanation": "Section 17A, introduced by the 2018 amendment to the Prevention of Corruption Act 1988, stipulates that no police officer shall conduct any enquiry or investigation into any offence alleged to have been committed by a public servant where the alleged offence is relatable to any recommendation made or decision taken in discharge of official functions, without previous approval of the competent authority."
      },
      {
        "id": "MCQ-ETH05-02",
        "q": "Which committee report first recommended the formal establishment of the Central Vigilance Commission (CVC) in 1964?",
        "options": ["Gorwala Committee on Public Administration", "Santhanam Committee on Prevention of Corruption", "Sarkaria Commission", "First Administrative Reforms Commission"],
        "ans": "b",
        "explanation": "The Committee on Prevention of Corruption, popularly known as the Santhanam Committee (1962–1964), recommended the setting up of the Central Vigilance Commission to tackle corruption in central government administration."
      },
      {
        "id": "MCQ-ETH05-03",
        "q": "Under the Right to Information Act, 2005, what is the maximum time limit mandated for providing information if it concerns the life or liberty of a person?",
        "options": ["24 hours", "48 hours", "7 days", "30 days"],
        "ans": "b",
        "explanation": "Section 7(1) of the RTI Act 2005 explicitly mandates that where the information sought concerns the life or liberty of a person, it must be provided within 48 hours of receipt of the request."
      },
      {
        "id": "MCQ-ETH05-04",
        "q": "Who heads the high-level selection committee for recommending the Chairperson and Members of the Lokpal under the Lokpal and Lokayuktas Act, 2013?",
        "options": ["President of India", "Chief Justice of India", "Prime Minister of India", "Cabinet Secretary"],
        "ans": "c",
        "explanation": "Under Section 4 of the Lokpal and Lokayuktas Act 2013, the Selection Committee is headed by the Prime Minister (Chairperson) and includes the Speaker of Lok Sabha, Leader of Opposition in Lok Sabha, Chief Justice of India (or a nominated SC Judge), and an eminent jurist nominated by the President."
      },
      {
        "id": "MCQ-ETH05-05",
        "q": "Which report of the Second Administrative Reforms Commission (2nd ARC) is exclusively titled 'Ethics in Governance'?",
        "options": ["1st Report", "4th Report", "6th Report", "10th Report"],
        "ans": "b",
        "explanation": "The 4th Report of the Second Administrative Reforms Commission (chaired by Veerappa Moily) is titled 'Ethics in Governance' and offers extensive recommendations on civil service values, anti-corruption machinery, and political funding reforms."
      }
    ]
  },
  {
    "id": "APPSC-G1-ETH-06",
    "filename": "06_basic_knowledge_of_criminal_laws_bns_bnss_bsa",
    "title": "New Criminal Law Framework: BNS, BNSS & BSA 2023",
    "mapping": "Basic Knowledge of Criminal Laws: Bharatiya Nyaya Sanhita (BNS) 2023, Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023, and Bharatiya Sakshya Adhiniyam (BSA) 2023; Decolonization of Criminal Jurisprudence, Zero FIR, Electronic Evidence, and Forensic Investigation Mandates.",
    "intro": "Effective July 1, 2024, India overhauled its colonial-era criminal jurisprudence by replacing the Indian Penal Code (IPC 1860), Code of Criminal Procedure (CrPC 1973), and Indian Evidence Act (IEA 1872) with three modernized statutes: the Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS), and Bharatiya Sakshya Adhiniyam (BSA). These laws prioritize citizen-centric justice, incorporate electronic and digital evidence, introduce community service as a penal sanction, and mandate forensic interventions for severe crimes.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Supreme_Court_of_India_New_Delhi.jpg", "caption": "The Supreme Court of India, guiding the judicial interpretation and implementation of the newly enacted criminal law framework.", "alt": "Supreme Court of India"},
    "table": {
      "caption": "Comparative Transition: Colonial Penal Codes vs Modern Criminal Acts (2023)",
      "headers": ["New Statute (2023)", "Replaced Law", "Key Doctrinal Reforms", "Procedural Innovations"],
      "rows": [
        ["Bharatiya Nyaya Sanhita (BNS) 2023", "Indian Penal Code (IPC) 1860", "Repeals sedition (replaces with acts endangering sovereignty); recognizes organized crime & terror; penalizes mob lynching", "Introduces community service for petty offenses; gender neutrality for certain sexual crimes; 358 sections vs 511"],
        ["Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023", "Code of Criminal Procedure (CrPC) 1973", "Mandatory forensic team visits for offenses punishable with 7+ years imprisonment; timeline for trial completion", "Statutory recognition of Zero FIR & e-FIR; audio-video recording of search & seizure; electronic summons"],
        ["Bharatiya Sakshya Adhiniyam (BSA) 2023", "Indian Evidence Act (IEA) 1872", "Primary evidentiary status for electronic and digital records (server logs, emails, smartphones, cloud data)", "Harmonizes electronic evidence admissibility without rigid secondary authentication; modernizes witness protection rules"]
      ]
    },
    "points": [
      "Substantive Reforms under BNS 2023: Replaces IPC Section 124A (Sedition) with Section 152 (Acts endangering sovereignty, unity, and integrity of India). Explicitly defines and criminalizes terrorist acts (Section 113) and organized crime syndicates (Section 111). Introduces death penalty or life imprisonment for mob lynching based on race, caste, or community.",
      "Community Service Sanctions: For the first time in Indian statutory law, community service is prescribed as an alternate sentence for six minor offences (such as public defamation, attempted suicide to restrain public servant, and minor theft under Rs 5,000 upon return of goods).",
      "Citizen-Friendly Procedures in BNSS 2023: Institutionalizes Zero FIR, permitting any citizen to file an FIR at any police station regardless of geographical jurisdiction, with mandatory transfer to the jurisdictional police station within 15 days. Digital preliminary inquiries are prescribed before arrest in minor offenses punishable with 3 to 7 years.",
      "Mandatory Forensic Collection: BNSS Section 176 mandates forensic experts to visit the crime scene and collect evidence for all offences punishable with imprisonment of seven years or more, driving scientific investigation standards across all states.",
      "Digital Records under BSA 2023: Sections 57 to 63 accord equal legal standing to digital records as physical documents, removing antiquated hurdles surrounding certificates for electronic records while protecting chain of custody."
    ],
    "mains": [
      "Analyze the key transformative features of the newly enacted criminal statutes (BNS, BNSS, and BSA 2023). How do they shift the balance from punitive colonial control to citizen-centric justice and scientific investigation? (250 Words, 15 Marks)",
      "Discuss the significance of introducing 'Community Service' and statutory 'Zero FIR' mechanisms under the new criminal codes. What logistical and administrative challenges will state police forces like Andhra Pradesh face in implementing them? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ETH06-01",
        "q": "On which date did the three new criminal statutes—Bharatiya Nyaya Sanhita (BNS), BNSS, and BSA—officially come into force across India?",
        "options": ["January 26, 2024", "July 1, 2024", "August 15, 2024", "October 2, 2024"],
        "ans": "b",
        "explanation": "The Central Government notified July 1, 2024, as the official commencement date for the Bharatiya Nyaya Sanhita (BNS) 2023, Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023, and Bharatiya Sakshya Adhiniyam (BSA) 2023."
      },
      {
        "id": "MCQ-ETH06-02",
        "q": "Under the Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023, for offences carrying what minimum punishment is forensic investigation and crime scene visit made mandatory?",
        "options": ["3 years or more", "5 years or more", "7 years or more", "Life imprisonment only"],
        "ans": "c",
        "explanation": "Section 176(3) of the BNSS mandates that for any offence punishable with imprisonment of seven years or more, a forensic team must visit the crime scene to collect scientific evidence and record the process on video/audio-video electronic media."
      },
      {
        "id": "MCQ-ETH06-03",
        "q": "Which former colonial offence under Section 124A of the Indian Penal Code (IPC) was replaced by provisions concerning 'acts endangering sovereignty, unity and integrity of India' in BNS?",
        "options": ["Blasphemy", "Sedition", "Criminal Defamation", "Thuggee"],
        "ans": "b",
        "explanation": "Sedition under IPC Section 124A was repealed and replaced under Section 152 of the Bharatiya Nyaya Sanhita (BNS), which penalizes acts endangering sovereignty, unity, and integrity of India rather than disaffection towards the government."
      },
      {
        "id": "MCQ-ETH06-04",
        "q": "Under the Bharatiya Nyaya Sanhita (BNS) 2023, 'Community Service' has been introduced as a punishment for which of the following categories of offences?",
        "options": ["Homicide by negligence", "Minor / Petty offences (e.g., small theft below Rs 5,000, defamation)", "Organized cyber fraud", "Grievous hurt"],
        "ans": "b",
        "explanation": "BNS 2023 introduces community service as an alternative penal measure for six petty offences, including defamation, misconduct by a drunken person, and theft of property valued under Rs 5,000 if the stolen property is restored."
      },
      {
        "id": "MCQ-ETH06-05",
        "q": "Under BNSS 2023, a 'Zero FIR' filed at any police station must be transferred to the jurisdictional police station within how many days?",
        "options": ["24 hours", "7 days", "15 days", "30 days"],
        "ans": "c",
        "explanation": "BNSS gives statutory sanction to Zero FIR, enabling registration irrespective of jurisdictional territory, and mandates its transfer to the jurisdictional police station within 15 days."
      }
    ]
  },
  {
    "id": "APPSC-G1-ETH-07",
    "filename": "07_civil_and_labour_laws_wage_codes_and_social_security",
    "title": "Civil & Labour Laws: CPC, 4 Labour Codes & Social Security",
    "mapping": "Civil & Labour Laws: Principles of Civil Procedure Code (CPC 1908), Res Judicata, Injunctions, Four Central Labour Codes (Code on Wages 2019, Industrial Relations Code 2020, Social Security Code 2020, OSHWC Code 2020), Gig & Platform Workers.",
    "intro": "Civil and labour legislation in India regulates the adjudication of private legal disputes and protects the socio-economic welfare of the industrial workforce. While the Code of Civil Procedure (CPC 1908) secures orderly dispute resolution through doctrines like Res Judicata and interim reliefs, the amalgamation of 29 archaic central labour statutes into Four Labour Codes represents a monumental reform balancing ease of doing business with universal social protection for formal, informal, and platform workers.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/eb/Indian_labourers_working.jpg", "caption": "Industrial and construction workers in India, brought under statutory social security umbrellas under the new Labour Codes.", "alt": "Indian labour workforce"},
    "table": {
      "caption": "The Four Central Labour Codes & Consolidating Architecture",
      "headers": ["Labour Code", "Acts Consolidated", "Primary Reform Focus", "Welfare & Coverage Enhancements"],
      "rows": [
        ["Code on Wages, 2019", "Equal Remuneration Act 1976, Minimum Wages Act 1948, Payment of Wages Act 1936, Payment of Bonus Act 1965", "Universal floor wage set by Central Government; mandatory wage revision timelines", "Covers 100% of workers (organized & unorganized); prohibits gender discrimination in hiring and wages"],
        ["Industrial Relations Code, 2020", "Trade Unions Act 1926, Industrial Employment (Standing Orders) Act 1946, Industrial Disputes Act 1947", "Raises threshold for retrenchment/closure without govt approval from 100 to 300 workers", "Legalizes fixed-term employment with pro-rata gratuity; requires 14-day notice before strike/lockout"],
        ["Code on Social Security, 2020", "EPF Act 1952, ESI Act 1948, Maternity Benefit Act 1961, Gratuity Act 1972, Unorganized Workers Act 2008", "Statutory recognition of gig workers, platform workers, and unorganized workforce", "Creates Social Security Fund financed by aggregator contributions (1-2% of annual turnover); universal ESIC"],
        ["OSH & Working Conditions Code, 2020", "Factories Act 1948, Mines Act 1952, Contract Labour Act 1970, Inter-State Migrant Workmen Act 1979", "Single license, single registration, and uniform safety standards across establishments", "Free annual health checks for workers aged 45+; permits women in night shifts with mandatory safety safeguards"]
      ]
    },
    "points": [
      "Code of Civil Procedure (CPC 1908) Essentials: Section 11 enshrines 'Res Judicata'—precluding courts from entertaining suits involving issues conclusively adjudicated between the same parties. Order XXXIX governs Temporary Injunctions based on a prima facie case, balance of convenience, and irreparable injury.",
      "Universal Floor Wage Mechanism: The Code on Wages empowers the Central Government to fix a mandatory 'National Floor Level Minimum Wage', taking into account geographical factors and minimal nutritional/living standards below which no state government can fix minimum wage rates.",
      "Social Protection for Gig and Platform Economy: The Social Security Code 2020 pioneeringly mandates delivery platform aggregators (e.g., e-commerce, ride-hailing, food delivery) to allocate 1% to 2% of their turnover (capped at 5% of amount paid to workers) into a National Social Security Fund for gig worker benefits.",
      "Retrenchment and Flexibility in Industrial Relations: By raising the threshold from 100 to 300 workers for government approval before layoff, retrenchment, or unit closure, the IR Code 2020 provides manufacturing flexibility while mandating a 20-day compensation fund for displaced workers.",
      "Inter-State Migrant Worker Protections: Broadened definitions incorporate self-employed or directly recruited migrants earning up to Rs 18,000/month, ensuring journey allowances, portability of public distribution benefits, and interstate helpline portals."
    ],
    "mains": [
      "Critically evaluate the transformative potential and trade-offs of the Four Labour Codes in India. Do they effectively reconcile economic competitiveness with robust worker welfare? (250 Words, 15 Marks)",
      "Explain the doctrine of 'Res Judicata' under the Code of Civil Procedure (CPC 1908). Differentiate it from the doctrine of 'Res Sub Judice' with illustrative examples. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ETH07-01",
        "q": "Under the Code of Civil Procedure, 1908, which section enshrines the doctrine of 'Res Judicata' (matter already adjudicated)?",
        "options": ["Section 9", "Section 10", "Section 11", "Section 89"],
        "ans": "c",
        "explanation": "Section 11 of the CPC contains the doctrine of Res Judicata, which bars any court from trying any suit or issue in which the matter directly and substantially in issue has been heard and finally decided by a court of competent jurisdiction in a former suit between the same parties."
      },
      {
        "id": "MCQ-ETH07-02",
        "q": "Under the Industrial Relations Code, 2020, what is the raised establishment workforce threshold above which prior government permission is mandatory for retrenchment, layoff, or closure?",
        "options": ["100 workers", "200 workers", "300 workers", "500 workers"],
        "ans": "c",
        "explanation": "The Industrial Relations Code 2020 raised the workforce threshold for requiring prior government permission for retrenchment, layoffs, and factory closures from 100 workers (under the 1947 Act) to 300 workers."
      },
      {
        "id": "MCQ-ETH07-03",
        "q": "The Code on Social Security, 2020 mandates aggregators (like ride-sharing and food-delivery companies) to contribute what percentage of their annual turnover to the Social Security Fund for gig workers?",
        "options": ["0.5% to 1%", "1% to 2% (capped at 5% of payout)", "3% to 5%", "7.5%"],
        "ans": "b",
        "explanation": "Under the Code on Social Security 2020, digital platform aggregators are required to contribute 1% to 2% of their annual turnover (subject to a maximum ceiling of 5% of the aggregate amount paid or payable to gig/platform workers) towards the social security fund."
      },
      {
        "id": "MCQ-ETH07-04",
        "q": "Which of the following is NOT one of the 4 consolidated Central Labour Codes passed by the Indian Parliament?",
        "options": ["Code on Wages, 2019", "Industrial Relations Code, 2020", "Code on Child Labour Elimination, 2021", "Occupational Safety, Health and Working Conditions Code, 2020"],
        "ans": "c",
        "explanation": "The four labour codes are: 1. Code on Wages (2019), 2. Industrial Relations Code (2020), 3. Code on Social Security (2020), and 4. Occupational Safety, Health and Working Conditions Code (2020). There is no separate 'Code on Child Labour Elimination 2021'."
      },
      {
        "id": "MCQ-ETH07-05",
        "q": "Under the Code of Civil Procedure, alternative dispute resolution (ADR) mechanisms like arbitration, conciliation, judicial settlement through Lok Adalat, and mediation are mandated under which section?",
        "options": ["Section 26", "Section 89", "Section 100", "Section 151"],
        "ans": "b",
        "explanation": "Section 89 of the CPC (introduced via the 1999 amendment) empowers civil courts to refer disputes to ADR processes including Arbitration, Conciliation, Judicial settlement including through Lok Adalat, or Mediation."
      }
    ]
  },
  {
    "id": "APPSC-G1-ETH-08",
    "filename": "08_cyber_laws_and_taxation_framework",
    "title": "Cyber Laws, Data Privacy & Taxation Framework",
    "mapping": "Cyber Laws & Taxation: Information Technology Act 2000, Section 66A & Free Speech, Digital Personal Data Protection Act 2023 (DPDP), Intermediary Guidelines; Direct & Indirect Taxation Architecture, GST Council & Dispute Resolution Mechanisms.",
    "intro": "The rapid digitalization of India's socio-economic fabric requires a robust legal architecture balancing cybersecurity, privacy, and economic dynamism. The Information Technology Act 2000, bolstered by the landmark Digital Personal Data Protection (DPDP) Act 2023, protects digital rights and operationalizes the fundamental right to privacy established in the Puttaswamy judgement. Concurrently, India's fiscal framework harmonizes revenue mobilization across direct income taxation and the unified Goods and Services Tax (GST) cooperative federal regime.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Cyber_Security_Concept.jpg", "caption": "Digital security and privacy protections, core components of India's modern legal and governance landscape.", "alt": "Cyber Security and Data Protection"},
    "table": {
      "caption": "Core Statutory Provisions: Cyber, Data Protection & Tax Frameworks",
      "headers": ["Statute / Body", "Core Focus Area", "Key Regulatory Provisions", "Penalties & Redressal Machinery"],
      "rows": [
        ["Information Technology Act, 2000", "Cyber offenses, digital transactions, electronic records", "Section 43 (Damage to computer systems), Section 66F (Cyber terrorism), Section 79 (Intermediary safe harbour)", "Adjudicating Officers; Cyber Appellate Tribunal (merged into TDSAT); life imprisonment for cyber terrorism"],
        ["Digital Personal Data Protection Act, 2023", "Personal digital data governance & privacy compliance", "Consent-centric processing; Data Principal rights; duties of Significant Data Fiduciaries (SDF)", "Data Protection Board of India (DPBI); monetary penalties up to Rs 250 crore per breach"],
        ["Goods and Services Tax (GST) Framework", "Dual destination-based consumption indirect tax", "Article 279A (GST Council); CGST, SGST, IGST split; Input Tax Credit (ITC) mechanism", "National Anti-profiteering Authority (subsumed into CCI); GST Appellate Tribunal (GSTAT)"],
        ["Income Tax Act, 1961 / Direct Taxes", "Taxation of individual and corporate income", "Faceless Assessment and Appeals; Section 148 reassessment norms; Advance Pricing Agreements (APA)", "Income Tax Appellate Tribunal (ITAT); High Court / Supreme Court constitutional appeals"]
      ]
    },
    "points": [
      "IT Act 2000 and the Landmark Shreya Singhal Judgement: In Shreya Singhal v. Union of India (2015), the Supreme Court struck down Section 66A of the IT Act as unconstitutionally vague and overbroad, upholding Article 19(1)(a) digital free speech. Section 79 safe harbor shields intermediaries provided they exercise due diligence.",
      "Digital Personal Data Protection Act (DPDP Act 2023): Implements the Puttaswamy privacy mandate across the digital economy. Enforces the principle of purpose limitation, requires verifiable parental consent for children's data, and empowers citizens (Data Principals) with the right to access, correction, and erasure.",
      "Data Protection Board of India (DPBI): Established as an independent digital-by-design regulatory and adjudicatory body empowered to direct urgent remediation in data breaches and impose penalties reaching up to Rs 250 crore for failures in implementing reasonable security safeguards.",
      "Goods and Services Tax (GST) Cooperative Federalism: Administered via the constitutional GST Council (Article 279A) chaired by the Union Finance Minister with state finance ministers as members. Decisions require a three-fourths weighted majority (one-third Union, two-thirds States).",
      "Faceless Assessment & Digital Dispute Redressal: Technology-driven tax administration eliminating physical interface between taxpayer and tax officer, utilizing dynamic jurisdiction and automated algorithm allocation to ensure transparency and eradicate rent-seeking."
    ],
    "mains": [
      "Analyze how the Digital Personal Data Protection (DPDP) Act 2023 strikes a balance between protecting individual data privacy and facilitating digital innovation and state governance. Highlight key concerns regarding government exemptions. (250 Words, 15 Marks)",
      "Evaluate the role of the GST Council as a successful institution of cooperative fiscal federalism in India. What structural and dispute resolution challenges continue to test its stability? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ETH08-01",
        "q": "In which landmark 2015 judgement did the Supreme Court of India strike down Section 66A of the Information Technology Act 2000 as unconstitutional?",
        "options": ["Justice K.S. Puttaswamy v. Union of India", "Shreya Singhal v. Union of India", "Anuradha Bhasin v. Union of India", "Maneka Gandhi v. Union of India"],
        "ans": "b",
        "explanation": "In Shreya Singhal v. Union of India (2015), the Supreme Court struck down Section 66A of the Information Technology Act 2000 in its entirety, holding that it violated the fundamental right to freedom of speech and expression under Article 19(1)(a)."
      },
      {
        "id": "MCQ-ETH08-02",
        "q": "What is the maximum monetary penalty that the Data Protection Board of India (DPBI) can impose for failure to take reasonable security safeguards under the DPDP Act 2023?",
        "options": ["Rs 25 Crore", "Rs 100 Crore", "Rs 250 Crore", "Rs 500 Crore"],
        "ans": "c",
        "explanation": "Under the Schedule of the Digital Personal Data Protection Act 2023, the Data Protection Board of India can impose penalties of up to Rs 250 crore for breach in observing obligation to take reasonable security safeguards to prevent personal data breach."
      },
      {
        "id": "MCQ-ETH08-03",
        "q": "Under the Information Technology Act 2000, which section prescribes punishment of up to life imprisonment for 'Cyber Terrorism'?",
        "options": ["Section 43A", "Section 66F", "Section 67", "Section 72A"],
        "ans": "b",
        "explanation": "Section 66F of the Information Technology Act (introduced in the 2008 amendment) defines and penalizes Cyber Terrorism, carrying a punishment extending to imprisonment for life."
      },
      {
        "id": "MCQ-ETH08-04",
        "q": "In the GST Council established under Article 279A of the Indian Constitution, what is the voting weight assigned to the Central Government and State Governments respectively?",
        "options": ["Union: 50%, States: 50%", "Union: One-third (33.3%), States: Two-thirds (66.7%)", "Union: One-fourth (25%), States: Three-fourths (75%)", "Every State and Union has equal single vote"],
        "ans": "b",
        "explanation": "Under Article 279A(9), the vote of the Central Government has a weightage of one-third of the total votes cast, and the votes of all State Governments taken together have a weightage of two-thirds of the total votes cast. Every decision requires a majority of not less than three-fourths of the weighted votes."
      },
      {
        "id": "MCQ-ETH08-05",
        "q": "Under the 'Safe Harbour' provisions of Section 79 of the IT Act 2000, an intermediary is exempt from liability for third-party content provided it fulfills which condition?",
        "options": ["It pre-censors all user posts", "It exercises due diligence and removes unlawful content upon receiving actual knowledge/court order", "It operates as a non-profit company", "It hosts all server infrastructure within India"],
        "ans": "b",
        "explanation": "Section 79 provides conditional immunity (Safe Harbour) to intermediaries provided they observe prescribed due diligence guidelines and expeditiously take down unlawful content upon receiving actual knowledge via a court order or government directive."
      }
    ]
  }
]

for t in topics:
  content_blocks = [
    {"type": "heading", "level": 1, "text": t["title"]},
    {"type": "paragraph", "text": t["intro"]},
    {"type": "image", "url": t["img"]["url"], "caption": t["img"]["caption"], "alt_text": t["img"]["alt"]},
    {"type": "heading", "level": 2, "text": "1. Institutional & Statutory Framework"},
    {"type": "table", "caption": t["table"]["caption"], "headers": t["table"]["headers"], "rows": t["table"]["rows"]},
    {"type": "heading", "level": 2, "text": "2. Key Dimensions & Critical Analysis"},
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
    "subject_title": "Ethics and Law",
    "paper": "Mains Paper-III (Section B) & Screening Paper-I (Section D)",
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

# Clean up old lumped files
old_files = [
  "01_ethics_human_interface_values.json",
  "02_human_values_attitude_emotional_intelligence.json",
  "03_public_service_ethics_codes_conduct_anticorruption.json",
  "04_basic_knowledge_civil_criminal_labour_laws.json",
  "05_cyber_and_tax_laws.json"
]
for f in old_files:
  p = os.path.join(SUBJ_DIR, f)
  if os.path.exists(p):
    os.remove(p)
    print(f"Removed old file: {f}")

print("Subject 5 is fully segregated into 8 topics!")
