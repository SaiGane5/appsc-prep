import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "02_History_and_Culture_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-APHC-07",
    "filename": "07_qutub_shahis_of_golconda_and_composite_culture",
    "title": "Qutub Shahis of Golconda: Administration, Telugu Literature & Kuchipudi",
    "mapping": "History and Culture of Andhra Pradesh: Medieval Andhra - Qutub Shahi Dynasty of Golconda (1518–1687 CE), Administration, Patronage of Telugu Poets (Ibrahim Qutb Shah), Bhakta Ramadasu, Origin of Kuchipudi Dance (Siddhendra Yogi), Machilipatnam Maritime Port.",
    "intro": "The Qutub Shahi Sultanate of Golconda (1518–1687 CE), founded by Sultan Quli Qutb Shah, fostered an extraordinary era of composite Telugu-Persian cultural synthesis across Andhra and Telangana. Renowned for their secular administrative appointments (Madanna and Akkanna), royal patronage of Telugu literature under Ibrahim Qutb Shah ('Malkibharama'), the musical padas of Kancharla Gopanna (Bhakta Ramadasu) at Bhadrachalam, and the classical codification of Kuchipudi dance by Siddhendra Yogi, Golconda represented the peak of Deccan syncretism.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Golconda_Fort_Hyderabad.jpg", "caption": "The formidable acoustic ramparts of Golconda Fort, the imperial capital of the Qutub Shahi dynasty.", "alt": "Golconda Fort acoustic gateways"},
    "table": {
      "caption": "Cultural & Administrative Spectrum of the Golconda Sultanate",
      "headers": ["Monarch & Reign", "Administrative Milestone & Appointments", "Telugu Literary Patronage", "Cultural & Architectural Legacy"],
      "rows": [
        ["Sultan Quli Qutb Shah (1518–1543 CE)", "Declared independence from Bahmani Sultanate; fortified Golconda.", "Encouraged local Telugu officers and revenue collectors.", "Excavated Golconda hill citadel; introduced Perso-Arabic administrative vocabulary into Telugu."],
        ["Ibrahim Qutb Shah (1550–1580 CE)", "Long exile at Vijayanagara (1543–1550) gave him deep love for Telugu; allied with Deccan sultans at Talikota (1565).", "Warmly called 'Malkibharama' by Telugu poets; court poet Addanki Gangadhara Kavi dedicated 'Tapati Samvaranopadhyanamu'; patronized Ponnikanti Telaganarya who composed 'Yayati Charitra' (first Accha Telugu work without Sanskrit words).", "Constructed Hussain Sagar lake (built by Hussain Shah Wali) and Ibrahimpatnam tank; patronized Kuchipudi artists with royal land grants."],
        ["Muhammad Quli Qutb Shah (1580–1612 CE)", "Founded the city of Hyderabad (Bhagyanagar) in 1591 CE; Urdu poet (Kulliyat-i-Quli Qutb Shah).", "Maintained Telugu court poets; sponsored Telugu translations of medical texts.", "Constructed the monumental Charminar (1591) and Mecca Masjid; granted trading privileges to Dutch and British at Machilipatnam."],
        ["Abul Hasan Tana Shah (1672–1687 CE)", "Last Sultan; appointed Brahmin brothers Madanna as Prime Minister (Sur-i-Khel) and Akkanna as Commander-in-Chief.", "Kancharla Gopanna (Bhakta Ramadasu), appointed Tahsildar of Bhadrachalam, constructed the Bhadrachalam Rama Temple using state revenues and composed soul-stirring 'Dasarathi Satakam'.", "Heroically resisted 8-month Mughal siege by Aurangzeb until betrayed by Abdullah Khan Panni; Golconda annexed in 1687 CE."]
      ]
    },
    "bullets": [
      "Accha Telugu Literature: Ponnikanti Telaganarya dedicated 'Yayati Charitra' to Amin Khan of Patancheru (Ibrahim Qutb Shah's minister), marking the first poetry written in pure indigenous Telugu (Accha Telugu) without borrowing a single Sanskrit loanword.",
      "Kuchipudi Dance Tradition: Siddhendra Yogi composed the dance-drama 'Bhamakalapam' (story of Satyabhama) at Kuchipudi village (Krishna district); Ibrahim Qutb Shah and later Abul Hasan Tana Shah granted Kuchipudi village as an Agraharam (1678) exclusively to Brahmin Bhagavatulu dance families.",
      "Bhakta Ramadasu (Kancharla Gopanna): Imprisoned for 12 years in Golconda Fort by Tana Shah for utilizing 6 lakh varahas of state tax to build the Bhadrachalam temple and jewel ornaments; legend relates Rama and Lakshmana appeared in disguise to pay his ransom; composed celebrated Kirtanas and 'Dasarathi Satakam'.",
      "Machilipatnam (Bandar): Primary maritime gateway of the Sultanate; exported kalamkari printed textiles, diamonds from Kollur mine (Hope Diamond, Koh-i-Noor), and steel for Damascus swords."
    ],
    "mains": [
      "Critically evaluate the composite culture and religious harmony under the Qutub Shahis of Golconda with special reference to the patronage of Telugu literature and the evolution of Kuchipudi dance. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight the pluralistic nature of Golconda statecraft: employment of Hindu ministers (Madanna and Akkanna) in supreme executive commands; analyze royal patronage of Telugu literature under Ibrahim Qutb Shah ('Malkibharama') and the creation of Accha Telugu literature ('Yayati Charitra'); explain the Bhadrachalam temple episode and Tana Shah's respect for Bhakta Ramadasu; evaluate the classical institutionalization of Kuchipudi dance via royal agrahara grants by Tana Shah to Siddhendra Yogi's Bhagavatulu troupe; assess Machilipatnam's commercial glory exporting Kalamkari textiles."
    ],
    "mcqs": [
      "Q1. Which Qutub Shahi Sultan of Golconda was affectionately venerated by Telugu poets as 'Malkibharama' for his enthusiastic patronage of classical Telugu literature?\n(a) Sultan Quli Qutb Shah\n(b) Ibrahim Qutb Shah\n(c) Muhammad Quli Qutb Shah\n(d) Abdullah Qutb Shah\nCorrect Answer: (b) Ibrahim Qutb Shah [Explanation: Ibrahim Qutb Shah, having spent seven years in exile at Vijayanagara, patronized Telugu poets who fondly hailed him as 'Malkibharama'.]",
      "Q2. The groundbreaking literary work 'Yayati Charitra', recognized as the very first poetic work composed entirely in pure indigenous Telugu (Accha Telugu), was authored by:\n(a) Addanki Gangadhara Kavi\n(b) Ponnikanti Telaganarya\n(c) Sarangapani\n(d) Kancharla Gopanna\nCorrect Answer: (b) Ponnikanti Telaganarya [Explanation: Ponnikanti Telaganarya composed 'Yayati Charitra' in pure Accha Telugu without Sanskrit loanwords, dedicating it to Amin Khan of Patancheru during Ibrahim Qutb Shah's reign.]",
      "Q3. The sacred dance-drama 'Bhamakalapam', which laid the foundational classical choreography for Kuchipudi dance in Andhra Pradesh, was composed by:\n(a) Kshetrayya\n(b) Siddhendra Yogi\n(c) Tyagaraja\n(d) Annamacharya\nCorrect Answer: (b) Siddhendra Yogi [Explanation: Siddhendra Yogi composed 'Bhamakalapam' (enacting the love and pride of Satyabhama) at Kuchipudi village, training young Brahmin boys in the classical dance-drama.]",
      "Q4. Which Qutub Shahi Sultan appointed the prominent Hindu Brahmin brothers Madanna as Prime Minister and Akkanna as Commander-in-Chief?\n(a) Muhammad Quli Qutb Shah\n(b) Abdullah Qutb Shah\n(c) Abul Hasan Tana Shah\n(d) Subhan Quli Qutb Shah\nCorrect Answer: (c) Abul Hasan Tana Shah [Explanation: Abul Hasan Tana Shah entrusted supreme civil and military governance to Madanna (Sur-i-Khel) and Akkanna, showcasing secular administration before the Mughal conquest in 1687.]",
      "Q5. Saint-composer Kancharla Gopanna (Bhakta Ramadasu), who composed the devotional 'Dasarathi Satakam' while imprisoned in Golconda Fort, served as the Tahsildar of:\n(a) Kondapalli\n(b) Bhadrachalam\n(c) Khammam\n(d) Warangal\nCorrect Answer: (b) Bhadrachalam [Explanation: Kancharla Gopanna served as the revenue collector (Tahsildar) of Bhadrachalam and constructed the famous Sri Sita Ramachandra Swamy Temple using state tax revenues.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-08",
    "filename": "08_modern_andhra_under_company_rule_and_sir_arthur_cotton",
    "title": "Modern Andhra under Company Rule: Northern Circars & Sir Arthur Cotton",
    "mapping": "History and Culture of Andhra Pradesh: Modern Andhra - British Acquisition of Northern Circars (1765/1768) and Ceded Districts (1800), Sir Thomas Munro's Ryotwari Settlement, Great Guntur Famine (1832), Sir Arthur Cotton's Godavari and Krishna Anicuts.",
    "intro": "The British colonization of Andhra unfolded in stages: the acquisition of the Northern Circars from the Nizam in 1765–1768, followed by the acquisition of the Ceded Districts (Rayalaseema) in 1800. Plagued by ruthless revenue extortion and devastating famines (notably the Guntur Famine of 1832), the coastal Andhra delta was rescued from economic ruin by the visionary hydraulic engineering of Sir Arthur Cotton, whose anicuts on the Godavari and Krishna transformed coastal Andhra into the granary of South India.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Dowleswaram_Barrage.jpg", "caption": "The Dowleswaram Barrage on the Godavari River near Rajahmundry, engineered by Sir Arthur Cotton in 1852.", "alt": "Godavari Dowleswaram barrage weir"},
    "table": {
      "caption": "Colonial Administrative & Hydraulic Milestones in Modern Andhra",
      "headers": ["Colonial Milestone & Year", "Territory & Key British Actors", "Strategic Actions & Infrastructure", "Socio-Economic Outcomes in Andhra"],
      "rows": [
        ["Acquisition of Northern Circars (1765/1768)", "Coastal Andhra (Srikakulam to Guntur); Robert Clive & Nizam Ali Khan.", "Clive secured imperial Farman from Mughal Emperor Shah Alam II (1765); confirmed by 1768 treaty with Nizam; Guntur Circar ceded in 1788.", "Imposed Permanent Zamindari Settlement in coastal estates (Vizianagaram, Bobbili, Nuzvid, Pithapuram); triggered severe agrarian distress."],
        ["Ceded Districts Acquisition (1800)", "Rayalaseema (Bellary, Anantapur, Cuddapah, Kurnool); Lord Wellesley & Nizam.", "Ceded by Nizam to Company to pay for British subsidiary force; placed under Principal Collector Major Thomas Munro (1800–1807).", "Munro pacified turbulent Poligars (feudal palegars); surveyed 10 million acres; introduced the Ryotwari settlement directly with cultivators, earning the affectionate title 'Munro Sahib'."],
        ["Great Guntur Famine (Nandana Karuvu, 1832)", "Krishna-Godavari deltas and Guntur district.", "Total failure of monsoon exacerbated by ruthless revenue extraction and lack of irrigation; one-third of Guntur's population (150,000 people) perished.", "Devastated agriculture, depopulated fertile villages, and exposed the lethal vulnerability of rain-dependent coastal deltas."],
        ["Sir Arthur Cotton's Hydraulic Revolution (1847–1855)", "Godavari Anicut at Dowleswaram (1852) & Krishna Prakasam Barrage at Vijayawada (1855).", "Engineered 4-kilometer masonry weir across 4 arms of the Godavari at Dowleswaram; built Krishna anicut at Vijayawada with vast canal irrigation and navigation networks.", "Brought over 2 million acres under assured double-crop irrigation; eradicated famine in the deltas; transformed East and West Godavari into the 'Rice Bowl of India'; Cotton revered as 'Apara Bhagiratha'."]
      ]
    },
    "bullets": [
      "Thomas Munro's Legacy: Respected local traditions; granted tax remissions during bad harvests; allocated revenues to the Tirumala temple; revered in Rayalaseema folklore as 'Mandava Rishi' and 'Munro Sahib'.",
      "Sir Arthur Cotton ('Delta Cotton'): British military engineer who argued that water, not railways, was the true wealth of India; overcame severe bureaucratic resistance from the Court of Directors to complete the Dowleswaram Anicut in 1852; grateful Telugu farmers still perform 'Cotton Tarpanam' during Godavari Pushkarams.",
      "Resistance of Poligars: Fierce armed resistance against British tax collection led by Rayalaseema Poligars, most notably Uyyalawada Narasimha Reddy (Kurnool, 1846), who attacked colonial treasuries before being captured and hanged publicly at Koilkuntla on 22 February 1847.",
      "Commercialization & Ports: Kakinada, Visakhapatnam, and Machilipatnam developed as ports for rice, tobacco, and cotton exports; growth of local printing presses and urban intelligentsia."
    ],
    "mains": [
      "Critically evaluate the colonial acquisition of coastal Andhra and Rayalaseema, and assess the transformative impact of Sir Arthur Cotton's hydraulic projects on the agrarian economy of Andhra Pradesh. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the political annexation: Northern Circars via Clive's Farman (1765/1768) and Ceded Districts via Wellesley's Subsidiary Alliance (1800); analyze the socio-economic devastation of Company rule: Munro's high initial Ryotwari assessments and the catastrophic Guntur Famine of 1832 (Nandana Karuvu); evaluate Sir Arthur Cotton's hydraulic genius: constructing the Dowleswaram Anicut across the Godavari (1852) and Krishna anicut at Vijayawada (1855); explain how 2 million acres of drought-prone wasteland transformed into fertile double-cropped paddy deltas, sparking the economic surplus that later funded the 19th-century Andhra cultural renaissance."
    ],
    "mcqs": [
      "Q1. Which British hydraulic engineer, celebrated across Andhra as 'Apara Bhagiratha', designed and constructed the historic Dowleswaram Anicut across the Godavari River in 1852?\n(a) Sir Thomas Munro\n(b) Sir Arthur Cotton\n(c) Colonel Colin Mackenzie\n(d) Sir Alexander Read\nCorrect Answer: (b) Sir Arthur Cotton [Explanation: General Sir Arthur Cotton designed the landmark Dowleswaram Anicut (1847–1852) on the Godavari and the Krishna Barrage (1855), permanently banishing famines from the deltas.]",
      "Q2. The catastrophic 'Guntur Famine' of 1832, which wiped out over a third of the population of Guntur district, is traditionally remembered in Telugu folklore as:\n(a) Dhatubadi Karuvu\n(b) Nandana Karuvu\n(c) Pedda Karuvu\n(d) Rayalaseema Karuvu\nCorrect Answer: (b) Nandana Karuvu [Explanation: The Guntur Famine occurred in the Telugu cyclical year 'Nandana' (1832 CE) and is famously commemorated as 'Nandana Karuvu', which decimated the Krishna-Godavari region.]",
      "Q3. The four districts of Rayalaseema (Bellary, Anantapur, Cuddapah, Kurnool) acquired by the British from the Nizam of Hyderabad in 1800 were historically termed:\n(a) Northern Circars\n(b) Ceded Districts (Datta Mandalamulu)\n(c) Agency Tracts\n(d) Carnatic Territories\nCorrect Answer: (b) Ceded Districts (Datta Mandalamulu) [Explanation: In 1800, Nizam Ali Khan ceded these territories to the British to finance the Subsidiary force, earning them the title 'Ceded Districts' until renamed 'Rayalaseema' in 1928.]",
      "Q4. Which brave Rayalaseema Poligar led an armed rebellion against British East India Company oppression in 1846 and was publicly hanged at Koilkuntla in 1847?\n(a) Alluri Sitarama Raju\n(b) Uyyalawada Narasimha Reddy\n(c) Veerapandiya Kattabomman\n(d) Marthanda Varma\nCorrect Answer: (b) Uyyalawada Narasimha Reddy [Explanation: Polygar Uyyalawada Narasimha Reddy of Kurnool rebelled in 1846, raiding British treasuries; he was captured and hanged in February 1847, a decade before 1857.]",
      "Q5. Who was appointed as the first Principal Collector of the Ceded Districts in 1800, successfully pacifying the Poligars and introducing the Ryotwari settlement?\n(a) Sir Arthur Cotton\n(b) Major Thomas Munro\n(c) Lord Wellesley\n(d) Robert Clive\nCorrect Answer: (b) Major Thomas Munro [Explanation: Major (later Sir) Thomas Munro served as Principal Collector from 1800 to 1807, implementing fair Ryotwari assessments and winning the affection of the Rayalaseema peasantry.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-09",
    "filename": "09_social_reform_movement_veeresalingam_and_gurazada",
    "title": "Social Reform Movement in Andhra: Veeresalingam, Gurazada & Gidugu",
    "mapping": "History and Culture of Andhra Pradesh: Andhra Renaissance - Kandukuri Veeresalingam ('Father of Modern Andhra Renaissance', Widow Remarriage, Vivekavardhini), Gurazada Apparao (Kanyasulkam, Modern Telugu Poetry), Gidugu Ramamurthy (Spoken Telugu Movement), Raghupathi Venkataratnam Naidu.",
    "intro": "The late 19th and early 20th centuries witnessed the glorious flowering of the 'Andhra Cultural Renaissance'. Spearheaded by Kandukuri Veeresalingam Pantulu ('Gadya Tikkana'), the movement crusaded against child marriage, female illiteracy, and enforced widowhood. Simultaneously, Mahakavi Gurazada Apparao revolutionized drama with 'Kanyasulkam', Gidugu Ramamurthy democratized literature through the Spoken Telugu Movement (Vyavaharika Bhasha), and Sir Raghupathi Venkataratnam Naidu pioneered Brahmo social justice and anti-devadasi reforms.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Kandukuri_Veeresalingam.jpg", "caption": "Kandukuri Veeresalingam Pantulu, the pioneering architect of modern Andhra social reform and prose literature.", "alt": "Kandukuri Veeresalingam Pantulu portrait"},
    "table": {
      "caption": "Pioneers of the Andhra Renaissance & Their Transformative Contributions",
      "headers": ["Reformer / Pioneer", "Institutions & Publications", "Social Crusades & Ideological Mission", "Literary & Cultural Landmarks"],
      "rows": [
        ["Kandukuri Veeresalingam Pantulu (1848–1919)", "Rajahmundry Social Reform Association (1878), Hitakarini Samajam (1906); Journal: 'Vivekavardhini'.", "Crusaded against child marriage, corruption, and superstition; organized the historic First Widow Remarriage in Andhra on 11 Dec 1881; established widow shelters and girls' schools.", "Father of modern Telugu prose ('Gadya Tikkana'); authored first Telugu novel 'Rajasekhara Charitramu' (1880), first Telugu autobiography, and 'Andhra Kavula Charitra'."],
        ["Gurazada Venkata Apparao (1862–1915)", "Vijayanagaram; associated with Maharaja Ananda Gajapati; Spoken Telugu advocate.", "Attacked bride-price (Kanyasulkam), child marriage, and hypocrisy of orthodox patriarchs; advocated secular rational humanism.", "Authored the immortal social satire drama 'Kanyasulkam' (1892, first modern Telugu social play); pioneered modern spoken metre in poetry 'Mutyala Saralu'; patriotic anthem: 'Desamante Matti Kadoi, Desamante Manushuloyi'."],
        ["Gidugu Venkata Ramamurthy (1863–1940)", "Parlakhemundi; Journal: 'Telugu'; Savara language researcher.", "Spearheaded the 'Vyavaharika Bhashodhyamam' (Spoken Language Movement) against archaic grammatical Grandhika style, demanding textbooks in living spoken Telugu.", "Liberated Telugu prose from elitist shackles; published Savara-English dictionary; his birthday (29 August) is celebrated annually as 'Telugu Language Day' (Telugu Bhasha Dinotsavam)."],
        ["Raghupathi Venkataratnam Naidu (1862–1939)", "Brahmo Samaj, Social Purity Association; Principal of PR College, Kakinada; Vice-Chancellor of Madras University.", "Anti-Devadasi crusade (Abolition of nautch parties); education of untouchables and orphans; championed widow remarriage and social equality.", "Acclaimed as 'Brahmarshi'; donated entire wealth to educational and orphan charities."]
      ]
    },
    "bullets": [
      "First Widow Remarriage (11 December 1881, Rajahmundry): Veeresalingam solemnized the marriage of Gogulapati Sreeramulu and Rajalaxmi amid fierce orthodox opposition, guarded by police and student volunteers.",
      "Kanyasulkam (1892): Masterpiece play by Gurazada featuring the unforgettable characters Girisam (pseudo-modern fraud), Madhuravani (noble reformed courtesan), Ramappapanthulu, and Lubdhavadhanulu; celebrated for its razor-sharp colloquial Telugu dialogue.",
      "Komarraju Lakshmana Rao (1877–1923): Founded the 'Vignana Chandrika Mandali' in 1906 to publish modern science and historical books in Telugu; pioneered the Telugu encyclopaedia project ('Andhra Vijnana Sarvasvamu').",
      "Library Movement in Andhra: Started with the Krishna Deva Raya Andhra Bhasha Nilayam (Hyderabad 1901) and Saraswata Niketanam (Vetapalem); popularized by Gadicherla Harisarvothama Rao and Ayyanki Venkata Ramanayya."
    ],
    "mains": [
      "Evaluate the multidimensional contributions of Kandukuri Veeresalingam and Gurazada Apparao to the social and literary renaissance of Andhra Pradesh. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the socio-cultural decadence of late 19th-century Andhra (enforced widowhood, child marriage, kanyasulkam, koota-sastra hypocrisy); evaluate Veeresalingam's heroic crusade: publishing 'Vivekavardhini', founding Hitakarini Samajam, solemnizing the historic first widow remarriage (1881), and pioneering modern Telugu prose genres (first novel, first autobiography); examine Gurazada Apparao's literary-social revolution: using living spoken Telugu in 'Kanyasulkam' (1892) to expose bride-price and conservative greed; analyze his secular patriotic poetry ('Desamunu Preminchumanna') defining nation as living people rather than soil; conclude on how their twin crusades birthed modern progressive Andhra society."
    ],
    "mcqs": [
      "Q1. Which pioneer of the Andhra Renaissance solemnized the historic First Widow Remarriage in Andhra on 11 December 1881 at Rajahmundry?\n(a) Gurazada Apparao\n(b) Kandukuri Veeresalingam Pantulu\n(c) Raghupathi Venkataratnam Naidu\n(d) Gidugu Ramamurthy\nCorrect Answer: (b) Kandukuri Veeresalingam Pantulu [Explanation: Kandukuri Veeresalingam founded the Rajahmundry Social Reform Association and conducted the first widow remarriage on 11 December 1881.]",
      "Q2. The landmark modern Telugu satirical social drama 'Kanyasulkam', targeting the abhorrent practice of bride-price and child marriage, was authored in 1892 by:\n(a) Kandukuri Veeresalingam\n(b) Gurazada Venkata Apparao\n(c) Chilakamarti Lakshmi Narasimham\n(d) Panuganti Lakshminarasimha Rao\nCorrect Answer: (b) Gurazada Venkata Apparao [Explanation: Mahakavi Gurazada Apparao wrote 'Kanyasulkam' (1892) in colloquial spoken Telugu, immortalizing iconic characters like Girisam and Madhuravani.]",
      "Q3. The birthday of which visionary scholar, who spearheaded the 'Vyavaharika Bhasha' (Living Spoken Telugu) movement, is celebrated annually on 29 August as 'Telugu Language Day'?\n(a) Nannaya Bhatta\n(b) Gidugu Venkata Ramamurthy\n(c) C.P. Brown\n(d) Komarraju Lakshmana Rao\nCorrect Answer: (b) Gidugu Venkata Ramamurthy [Explanation: 29 August is celebrated across Andhra Pradesh as 'Telugu Bhasha Dinotsavam' in honour of Gidugu Ramamurthy's pioneering crusade for spoken Telugu.]",
      "Q4. Which was the very first full-length original novel published in the Telugu language, authored by Kandukuri Veeresalingam in 1880?\n(a) Kanyasulkam\n(b) Rajasekhara Charitramu\n(c) Malapalli\n(d) Chivaraku Migiledi\nCorrect Answer: (b) Rajasekhara Charitramu [Explanation: 'Rajasekhara Charitramu' (1880), modeled partly on Goldsmith's 'Vicar of Wakefield', was the first full-length novel written in the Telugu language by Veeresalingam.]",
      "Q5. Which eminent educationist and Brahmo leader, acclaimed as 'Brahmarshi', led the crusade against the Devadasi system and nautch parties in coastal Andhra?\n(a) Raghupathi Venkataratnam Naidu\n(b) Kasinadhuni Nageswara Rao\n(c) Mutnuri Krishna Rao\n(d) Tanguturi Prakasam\nCorrect Answer: (a) Raghupathi Venkataratnam Naidu [Explanation: Sir Raghupathi Venkataratnam Naidu founded the Social Purity Association and spearheaded the anti-devadasi and anti-nautch movement across the Madras Presidency.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-10",
    "filename": "10_freedom_struggle_in_andhra_vandemataram_to_salt_satyagraha",
    "title": "Freedom Movement in Andhra: Vandemataram to Salt Satyagraha",
    "mapping": "History and Culture of Andhra Pradesh: Freedom Struggle in Andhra - Vandemataram Movement (Bipin Chandra Pal's Tour 1907, Rajahmundry College Incident), Non-Cooperation (Chirala-Perala, Palnadu Forest Satyagraha, Pedanandipadu No-Tax Campaign), Salt Satyagraha and Tanguturi Prakasam.",
    "intro": "The nationalist freedom struggle found vibrant, militant expression across Andhra. Ignited by Bipin Chandra Pal's tour of coastal Andhra in 1907 during the Vandemataram Movement, the region mounted heroic mass struggles during the Non-Cooperation movement—most notably the historic Chirala-Perala municipal exodus, the Palnadu Forest Satyagraha, and the Pedanandipadu No-Tax campaign—culminating in the defiance of Tanguturi Prakasam Pantulu ('Andhra Kesari') during the Salt Satyagraha.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Tanguturi_Prakasam.jpg", "caption": "Tanguturi Prakasam Pantulu ('Andhra Kesari'), who bared his chest to British bayonets in Madras during the Simon Commission boycott (1928).", "alt": "Tanguturi Prakasam Pantulu portrait"},
    "table": {
      "caption": "Milestones of Mass Nationalist Movements in Andhra",
      "headers": ["National Movement & Epoch", "Geographical Centre & Key Leaders", "Mode of Protest & Tactical Innovation", "Colonial Repression & Historical Impact"],
      "rows": [
        ["Vandemataram Movement (1905–1911)", "Rajahmundry, Kakinada, Machilipatnam, Tenali; Bipin Chandra Pal, Gadicherla Harisarvothama Rao, Mutnuri Krishna Rao.", "B.C. Pal toured coastal Andhra in April 1907; students wore 'Vandemataram' badges at Rajahmundry Arts College under Mark Hunter; Tenali Bomb Case (1909); establishment of national schools (Andhra Jatheeya Kalasala, Machilipatnam 1910).", "Gadicherla Harisarvothama Rao imprisoned for editorial 'Cruel Cartridge'; student leaders expelled; ignited militant political consciousness across Telugu youth."],
        ["Chirala-Perala Struggle (1921)", "Chirala-Perala (Bapatla district); Duggirala Gopalakrishnayya ('Andhra Ratna') & his volunteer corps 'Ramadandu'.", "Protest against colonial government upgrading village into municipality with 10-fold tax hike; 15,000 residents completely evacuated their homes and built a parallel township named 'Ramanagar' on the town outskirts for 11 months.", "Refused municipal taxes; Duggirala imprisoned for one year; Gandhi acclaimed the non-violent evacuation as an unparalleled model of civil resistance."],
        ["Palnadu Forest Satyagraha (1921)", "Palnadu (Guntur district); Kannuganti Hanumanthu, Unnava Lakshminarayana.", "Protest against oppressive British forest laws (Madras Forest Act) and heavy grazing taxes (Pullari); peasants led cattle into reserved forests defying forest guards.", "Kannuganti Hanumanthu shot dead in police firing at Minchalapadu on 26 Feb 1922; movement symbolized grassroots tribal-peasant defiance."],
        ["Pedanandipadu No-Tax Campaign (1922)", "Pedanandipadu firka, Bapatla; Parvataneni Veeraiah Chaudhari ('Andhra Shivaji').", "Total civil disobedience: complete non-payment of land revenue; village officers (Karnams and Munsiffs) resigned en masse; complete boycott of British officials.", "Revenue administration collapsed entirely in the firka; Gandhi advised pausing until nation was ready, preventing immediate military slaughter."],
        ["Salt Satyagraha in Andhra (1930)", "Chinnapuram (Machilipatnam), Devarampadu, Kottapatnam, Madras; Tanguturi Prakasam, Konda Venkatappaiah, Durgabai Deshmukh.", "Sibirams (Satyagraha camps) set up across coastal districts; making contraband salt at Chinnapuram and Vadarevu; women joined in massive numbers under Durgabai Deshmukh.", "British police unleashed lathi charges; Prakasam earned the title 'Andhra Kesari' (Lion of Andhra) in 1928 for baring his chest to armed police in Madras defying the Simon Commission."]
      ]
    },
    "bullets": [
      "Tanguturi Prakasam Pantulu ('Andhra Kesari'): Bare-chested courage during Simon Commission protests in Madras on 3 Feb 1928 when police opened fire; dared officers to shoot him; later became Premier of Madras Presidency (1946) and the First Chief Minister of Andhra State (1953).",
      "Mutnuri Krishna Rao & 'Krishna Patrika': Founded in 1902 in Machilipatnam; fearless Telugu nationalist weekly newspaper that nurtured generations of freedom fighters and intellectual nationalists.",
      "Kasinadhuni Nageswara Rao: Founder of 'Amrutanjan' and the influential Telugu daily 'Andhra Patrika' (1908 in Bombay, shifted to Madras in 1914); established 'Andhra Grantha Mandali'; acclaimed as 'Desoddharaka'.",
      "Durgabai Deshmukh: Organized Salt Satyagraha in Madras city along with Prakasam; imprisoned for one year at Vellore; later founded the Andhra Mahila Sabha in Madras (1937) and served on the Planning Commission."
    ],
    "mains": [
      "Critically analyze the unique grassroots protest movements in Andhra during the Non-Cooperation era with special reference to the Chirala-Perala exodus and the Pedanandipadu No-Tax campaign. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight Andhra's radical response to Gandhi's Non-Cooperation call in 1921–1922; detail the Chirala-Perala struggle under Duggirala Gopalakrishnayya: total mass evacuation of 15,000 citizens to 'Ramanagar' refusing municipal taxation, organized through the disciplined Ramadandu volunteer corps; examine the Pedanandipadu No-Tax campaign under Parvataneni Veeraiah Chaudhari: complete stoppage of land revenue, mass resignation of village officers, and paralysis of British authority; assess why Gandhi advised caution to avert brutal colonial military suppression; conclude on how these protests showcased unprecedented mass civil discipline."
    ],
    "mcqs": [
      "Q1. Who organized the historic 11-month mass evacuation of Chirala-Perala in 1921, establishing the parallel township 'Ramanagar' with his volunteer corps 'Ramadandu'?\n(a) Parvataneni Veeraiah Chaudhari\n(b) Duggirala Gopalakrishnayya ('Andhra Ratna')\n(c) Konda Venkatappaiah\n(d) Tanguturi Prakasam\nCorrect Answer: (b) Duggirala Gopalakrishnayya ('Andhra Ratna') [Explanation: Duggirala Gopalakrishnayya led 15,000 residents out of Chirala to live in thatched huts at 'Ramanagar' rather than pay municipal taxes.]",
      "Q2. Which fearless nationalist leader earned the title 'Andhra Kesari' (Lion of Andhra) after baring his chest to armed British police bayonets during the Simon Commission boycott in Madras?\n(a) Tanguturi Prakasam Pantulu\n(b) Potti Sreeramulu\n(c) Gadicherla Harisarvothama Rao\n(d) Kasinadhuni Nageswara Rao\nCorrect Answer: (a) Tanguturi Prakasam Pantulu [Explanation: On 3 February 1928, Tanguturi Prakasam bared his chest before armed British soldiers in Madras, declaring: 'Shoot if you have the courage!', earning the title 'Andhra Kesari'.]",
      "Q3. Who led the heroic Palnadu Forest Satyagraha in Guntur district in 1921 against oppressive British forest grazing taxes (Pullari), attaining martyrdom in police firing at Minchalapadu?\n(a) Alluri Sitarama Raju\n(b) Kannuganti Hanumanthu\n(c) Parvataneni Veeraiah Chaudhari\n(d) Konda Venkatappaiah\nCorrect Answer: (b) Kannuganti Hanumanthu [Explanation: Kannuganti Hanumanthu led the Palnadu cattle-grazing tax resistance and was martyred when British police opened fire on his peasant gathering at Minchalapadu on 26 February 1922.]",
      "Q4. Which charismatic peasant leader, popularly acclaimed as 'Andhra Shivaji', organized the celebrated Pedanandipadu No-Tax campaign in 1922 that completely paralyzed British revenue collection?\n(a) Duggirala Gopalakrishnayya\n(b) Parvataneni Veeraiah Chaudhari\n(c) Konda Venkatappaiah\n(d) Bikkina Venkataratnam\nCorrect Answer: (b) Parvataneni Veeraiah Chaudhari [Explanation: Parvataneni Veeraiah Chaudhari organized the Pedanandipadu No-Tax campaign where all village revenue officers resigned, earning him the title 'Andhra Shivaji'.]",
      "Q5. Which historic nationalist Telugu daily newspaper was founded by Kasinadhuni Nageswara Rao in 1908 to advance the cause of Indian independence and Andhra culture?\n(a) Krishna Patrika\n(b) Andhra Patrika\n(c) Vivekavardhini\n(d) Desabhimani\nCorrect Answer: (b) Andhra Patrika [Explanation: 'Desoddharaka' Kasinadhuni Nageswara Rao founded 'Andhra Patrika' in Bombay in 1908 (shifted to Madras in 1914), serving as the paramount voice of the Telugu nationalist movement.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-11",
    "filename": "11_alluri_sitarama_raju_and_rampa_rebellion",
    "title": "Alluri Sitarama Raju & The Rampa Tribal Rebellion (1922–1924)",
    "mapping": "History and Culture of Andhra Pradesh: Tribal Uprisings - Madras Forest Act 1882, Exploitation of Muttadars and Girijans, Alluri Sitarama Raju, Guerilla Warfare in Agency Tracts (Rampa Rebellion 1922–1924), Police Station Raids and Martyrdom.",
    "intro": "The Rampa Rebellion (Manyam Viplavam) of 1922–1924, waged in the dense Agency hill tracts of the Eastern Ghats (Visakhapatnam and East Godavari), represents one of the most formidable anti-colonial guerrilla wars in modern Indian history. Led by the legendary young revolutionary Alluri Sitarama Raju, the tribal Koyas and Konda Reddis took up arms against the draconian Madras Forest Act of 1882 and colonial forced labor, holding the British Empire at bay for nearly two years.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Alluri_Sitarama_Raju_Stamp.jpg", "caption": "Commemorative postal stamp issued in 1986 honoring revolutionary tribal leader Alluri Sitarama Raju ('Manyam Veerudu').", "alt": "Alluri Sitarama Raju commemorative postage stamp"},
    "table": {
      "caption": "Chronology & Tactical Operations of the Rampa Rebellion (1922–1924)",
      "headers": ["Chronological Episode", "Geographical Location", "Military Action & Guerrilla Tactics", "Colonial Response & Historical Impact"],
      "rows": [
        ["Genesis & Tribal Grievances (Pre-1922)", "Manyam Agency (Chintapalli, Rampachodavaram, Gudem).", "Madras Forest Act 1882 curtailed traditional Podu (shifting) cultivation; banned gathering minor forest produce; ruthless forced labor (Vetti) for road building by Tahsildar Bastian.", "Alluri Sitarama Raju arrived in the hills, adopted ascetic sanyasi robes, organized tribal panchayats, and united Koyas and Konda Reddis under Gam Gantam Dora and Gam Mallu Dora."],
        ["Opening Police Station Raids (August 1922)", "Chintapalli, Krishnadevipeta, Rajavommangi police stations.", "Raju led 300 tribal guerrillas; raided police stations for rifles and ammunition; uniquely signed the police diary with his own signature, leaving advance warnings of his attacks.", "Captured hundreds of British .303 rifles and bayonets without harming Indian constables; exposed British intelligence paralysis in the Agency."],
        ["Battle of Onkar Ghat & Guerrilla Supremacy (Sept–Dec 1922)", "Damanapalli ghats, Peddavalasa.", "Ambushed British detachment led by Captain Tremenheere and Inspector Coward; killed British commanders Scott and Heighter at Damanapalli.", "Inflicted humiliating defeats on Madras Special Police; British deployed Assam Rifles and Malabar Special Police; Raju acclaimed as 'Manyam Veerudu' (Hero of the Jungles)."],
        ["British Escalation & Martyrdom (1923–May 1924)", "Kirrabu, Koyyuru, Mampa hills.", "Special Commissioner T.G. Rutherford appointed with martial law powers; encircled Agency tracts; cut off tribal food and salt supplies; captured Gam Mallu Dora.", "Raju voluntarily surrendered to Major Goodall at Mampa to spare innocent tribal villagers from brutal atrocities; taken to Koyyuru, tied to a tree, and shot dead on 7 May 1924 without trial."]
      ]
    },
    "bullets": [
      "Muttadari System: Feudal revenue system in the Agency where hereditary tribal headmen (Muttadars) collected land dues; British officials like Deputy Tahsildar Bastian exploited Muttadars and compelled tribals to perform unpaid hard labor (Vetti).",
      "Key Lieutenants of Raju: Gam Gantam Dora (fearless commander who fought till the end), Gam Mallu Dora (captured and imprisoned in Andaman Cellular Jail, later elected to Lok Sabha in 1952), and Aggiraju (Pericherla Suryanarayana Raju).",
      "Guerrilla Tactics: Indigenous knowledge of mountainous forest terrain, whistle communications, traditional bow-and-arrow combined with captured modern firearms, and deep intelligence networks among hill villagers.",
      "Nationalist Acclaim: Mahatma Gandhi wrote in 'Young India': 'Though I do not approve of his armed rebellion, I pay my homage to the bravery and sacrifice of the late Sitarama Raju'; Netaji Bose lauded him as a jewel of Indian patriotism."
    ],
    "mains": [
      "Critically examine the causes, trajectory, and military strategies of the Rampa Tribal Rebellion (1922–1924) under Alluri Sitarama Raju. Why is he celebrated as 'Manyam Veerudu' in Andhra history? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Analyze underlying structural causes: Madras Forest Act 1882 depriving tribal communities of ancestral Podu cultivation and minor forest produce, coupled with the exploitation of Muttadars and coercive Vetti labor by colonial officials like Bastian; detail Raju's leadership: mobilizing Koyas and Konda Reddis, weapon procurement through daring police station raids (Chintapalli, Rajavommangi); examine military warfare: masterly guerrilla ambush tactics defeating British commanders at Damanapalli; explain the brutal counter-insurgency under Rutherford deploying Assam Rifles; evaluate Raju's supreme sacrifice surrendering on 7 May 1924 to protect innocent tribals; conclude on his immortal legacy as 'Manyam Veerudu'."
    ],
    "mcqs": [
      "Q1. Which repressive colonial legislation enacted in 1882 severely restricted the traditional 'Podu' (shifting) agriculture of tribal communities, triggering the Rampa Rebellion?\n(a) Indian Forest Act 1878\n(b) Madras Forest Act 1882\n(c) Criminal Tribes Act 1871\n(d) Agency Civil Rights Act\nCorrect Answer: (b) Madras Forest Act 1882 [Explanation: The Madras Forest Act of 1882 banned shifting cultivation (Podu) and access to forest resources, sparking deep tribal unrest in the Godavari Agency.]",
      "Q2. The opening salvo of the Rampa Rebellion occurred on 22 August 1922 with an audacious armed raid on which British police station led by Alluri Sitarama Raju?\n(a) Krishnadevipeta Police Station\n(b) Chintapalli Police Station\n(c) Rajavommangi Police Station\n(d) Rampachodavaram Police Station\nCorrect Answer: (b) Chintapalli Police Station [Explanation: Raju initiated the armed struggle on 22 August 1922 by raiding the Chintapalli police station in Visakhapatnam district, seizing rifles and ammunition.]",
      "Q3. In which fierce mountain ambush in September 1922 did Alluri's guerrilla fighters defeat the British forces and kill commanders Scott and Heighter?\n(a) Battle of Onkar Ghat\n(b) Battle of Damanapalli\n(c) Battle of Kirrabu\n(d) Battle of Mampa\nCorrect Answer: (b) Battle of Damanapalli [Explanation: At the Damanapalli Ghats, Raju's guerrillas ambushed the British police column, killing senior commanders Scott and Heighter and capturing massive armaments.]",
      "Q4. Which ruthless British officer was appointed as the Special Commissioner in 1923 with sweeping martial powers to crush the Rampa Rebellion?\n(a) Major Goodall\n(b) T.G. Rutherford\n(c) Captain Tremenheere\n(d) J.A. Travers\nCorrect Answer: (b) T.G. Rutherford [Explanation: T.G. Rutherford was appointed Special Commissioner of the Agency in 1923, imposing blockades, burning villages, and deploying the Assam Rifles to trap Raju.]",
      "Q5. On which tragic date in May 1924 was Alluri Sitarama Raju captured near Mampa and shot dead by British police at Koyyuru without a legal trial?\n(a) 15 August 1924\n(b) 7 May 1924\n(c) 26 January 1924\n(d) 11 November 1924\nCorrect Answer: (b) 7 May 1924 [Explanation: Alluri Sitarama Raju was captured at Mampa and shot dead without a trial at Koyyuru on 7 May 1924 by Major Goodall's forces, attaining immortal martyrdom at age 27.]"
    ]
  },
  {
    "id": "APPSC-G1-APHC-12",
    "filename": "12_andhra_movement_formation_of_andhra_and_bifurcation_2014",
    "title": "Andhra Movement, Linguistic Statehood (1953/1956) & Bifurcation 2014",
    "mapping": "History and Culture of Andhra Pradesh: State Reorganization & Modern Era - Andhra Movement (Bapatla Mahasabha 1913), Sri Bagh Pact (1937), Potti Sreeramulu's Martyrdom, Andhra State (1953, Kurnool), Gentlemen's Agreement (1956), Formation of Andhra Pradesh (1956), AP Reorganisation Act 2014 (Bifurcation, Polavaram, Capital Issue).",
    "intro": "The modern political identity of Andhra Pradesh was forged through a century of struggles: the Andhra Movement initiated at the Bapatla Mahasabha (1913), the harmonious Sri Bagh Pact (1937), the supreme martyrdom of Amarajeevi Potti Sreeramulu resulting in the creation of Andhra State at Kurnool (1953), and the integration with Telangana under the Gentlemen's Agreement to form Andhra Pradesh (1956). In 2014, the Andhra Pradesh Reorganisation Act divided the state, creating Telangana and confronting residual Andhra Pradesh with deep fiscal, institutional, and capital city challenges.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Potti_Sreeramulu.jpg", "caption": "Amarajeevi Potti Sreeramulu, whose 58-day fast unto death resulted in the creation of Andhra State on 1 October 1953.", "alt": "Potti Sreeramulu portrait"},
    "table": {
      "caption": "Milestones in the Political Geography of Modern Andhra Pradesh",
      "headers": ["Historical Milestone & Year", "Key Leaders & Agreements", "Core Provisions & Resolutions", "Constitutional & Political Outcome"],
      "rows": [
        ["First Andhra Mahasabha (May 1913)", "Bapatla (Guntur); Bayya Narasimheswara Sarma (President), Konda Venkatappaiah.", "First formal demand for a separate Andhra Province carved out of multilingual Madras Presidency; promoted Telugu cultural unity.", "Pioneered the Andhra Movement; led to the formation of the Andhra Provincial Congress Committee in 1917."],
        ["Sri Bagh Pact (14 November 1937)", "Madras (residence of Kasinadhuni Nageswara Rao); Coastal leaders & Rayalaseema leaders (K. Koti Reddy, Kalluri Subba Rao).", "Consensus pact guaranteeing Rayalaseema equitable water allocation, university education, and choice between Capital and High Court.", "Bridged regional distrust; Rayalaseema leaders fully supported the separate Andhra demand."],
        ["Creation of Andhra State (1 October 1953)", "Potti Sreeramulu (58-day fast unto death, 19 Oct – 15 Dec 1952); Tanguturi Prakasam.", "Created India's first linguistic state; 11 Telugu-speaking districts carved out of Madras State.", "Capital inaugurated at Kurnool (Rayalaseema) per Sri Bagh Pact; High Court at Guntur; Tanguturi Prakasam became first Chief Minister, C.M. Trivedi first Governor."],
        ["Gentlemen's Agreement & AP Formation (1956)", "Hyderabad; 4 leaders of Andhra (Gopala Reddy, Sanjeeva Reddy, G. Latchanna, A. Satyanarayana Raju) & 4 of Telangana (Burgula Ramakrishna Rao, K.V. Ranga Reddy, Marri Channa Reddy, J.V. Narsing Rao).", "14-point safeguards for Telangana: regional development council, proportional expenditure, domicile quota (Mulki rules), reservation of ministerial portfolios.", "Merger of Andhra State and Telangana to form 'Andhra Pradesh' on 1 November 1956 with Hyderabad as capital; Neelam Sanjeeva Reddy first CM."],
        ["AP Reorganisation Act (2014)", "Parliament of India (Act 6 of 2014); bifurcated state on 2 June 2014 (Appointed Day).", "Created separate Telangana state with Hyderabad as joint capital for up to 10 years; Schedule IX (91 institutions) and Schedule X (142 institutions) assets division.", "Residual AP inherited 58.3% of population but lost Hyderabad's massive service-tax revenue; declared Polavaram a National Project; Special Category Status and capital city (Amaravati) debates."]
      ]
    },
    "bullets": [
      "Amarajeevi Potti Sreeramulu: Disciple of Mahatma Gandhi; commenced fast at Bulusu Sambamurti's house in Madras on 19 October 1952; died on 15 December 1952; sacrifice compelled Nehru to concede Andhra State four days later.",
      "Kurnool Capital Era (1953–1956): Tent offices and legislative assembly functioned in Kurnool; historic compromise under the Sri Bagh Pact.",
      "Telangana Agitations: 1969 Jai Telangana movement (Marri Channa Reddy) and 1972 Jai Andhra movement led to the Six-Point Formula (1973) and 32nd Constitutional Amendment (Article 371D).",
      "Andhra Pradesh Reorganisation Act 2014 Key Sections: Section 46 (special fiscal grants for Rayalaseema and North Coastal Andhra), Section 90 (Polavaram Irrigation Project as National Project funded 100% by Union government), Section 94 (tax incentives for industrial development), and Section 93 (creation of new capital, railway zone in Vizag, national educational institutes)."
    ],
    "mains": [
      "Trace the historical evolution of the Andhra Movement from the Bapatla Mahasabha of 1913 to the creation of Andhra State in 1953. Critically analyze the structural challenges facing residual Andhra Pradesh post-2014 bifurcation. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Trace the movement: Bapatla Mahasabha (1913) asserting linguistic identity, Andhra PCC (1917), the crucial Sri Bagh Pact (1937) reconciling Rayalaseema aspirations; describe Potti Sreeramulu's 58-day fast unto death in 1952 resulting in the birth of Andhra State on 1 October 1953 at Kurnool; analyze post-2014 bifurcation under the AP Reorganisation Act 2014: loss of revenue-rich Hyderabad, acute revenue deficit, pending asset division under Schedules IX and X, capital city infrastructure financing (Amaravati), execution of Polavaram National Project, and demand for Special Category Status."
    ],
    "mcqs": [
      "Q1. Where was the historic First Andhra Mahasabha held in May 1913 under the presidency of Bayya Narasimheswara Sarma, officially launching the Andhra Movement?\n(a) Vijayawada\n(b) Bapatla\n(c) Rajahmundry\n(d) Guntur\nCorrect Answer: (b) Bapatla [Explanation: The First Andhra Conference was held at Bapatla in Guntur district on 26–27 May 1913, formally giving birth to the organized Andhra movement.]",
      "Q2. The historic 'Sri Bagh Pact', signed on 14 November 1937 between leaders of Coastal Andhra and Rayalaseema to foster regional trust, was concluded at the residence of:\n(a) Tanguturi Prakasam\n(b) Kasinadhuni Nageswara Rao\n(c) Konda Venkatappaiah\n(d) Kalluri Subba Rao\nCorrect Answer: (b) Kasinadhuni Nageswara Rao [Explanation: The pact was signed at 'Sri Bagh', the Madras residence of Desoddharaka Kasinadhuni Nageswara Rao, guaranteeing university and capital concessions to Rayalaseema.]",
      "Q3. Under the historic 'Gentlemen's Agreement' signed in Delhi in February 1956, how many leaders from Andhra and Telangana respectively participated in formulating the safeguards?\n(a) 2 from each region\n(b) 4 from each region (total 8)\n(c) 6 from each region\n(d) 10 from each region\nCorrect Answer: (b) 4 from each region (total 8) [Explanation: Eight leaders (four from Andhra: Gopala Reddy, Sanjeeva Reddy, Latchanna, Satyanarayana Raju; and four from Telangana: Burgula, Ranga Reddy, Channa Reddy, Narsing Rao) signed the agreement.]",
      "Q4. Which multipurpose irrigation project on the Godavari River was declared as a 'National Project' by the Central Government under Section 90 of the AP Reorganisation Act 2014?\n(a) Nagarjuna Sagar Project\n(b) Polavaram Irrigation Project\n(c) Srisailam Project\n(d) Veligonda Project\nCorrect Answer: (b) Polavaram Irrigation Project [Explanation: Section 90 of the AP Reorganisation Act 2014 declared the Polavaram Multipurpose National Irrigation Project to be executed and financed by the Union government.]",
      "Q5. Who was sworn in as the first Chief Minister of the newly formed Andhra Pradesh state on 1 November 1956 with Hyderabad as its capital?\n(a) Tanguturi Prakasam Pantulu\n(b) Bezawada Gopala Reddy\n(c) Neelam Sanjeeva Reddy\n(d) Burgula Ramakrishna Rao\nCorrect Answer: (c) Neelam Sanjeeva Reddy [Explanation: Neelam Sanjeeva Reddy became the first Chief Minister of Andhra Pradesh on 1 November 1956, while Burgula Ramakrishna Rao was the last CM of Hyderabad State.]"
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

print("Part 3 of Subject 2 generated successfully")
