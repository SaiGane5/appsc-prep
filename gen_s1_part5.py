import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-HIST-21",
    "filename": "21_colonial_land_revenue_systems_and_economic_drain",
    "title": "Colonial Economy: Land Revenue Systems & Drain of Wealth",
    "mapping": "History and Culture of India: British Colonial Economy - Land Revenue Settlements (Permanent Settlement, Ryotwari, Mahalwari), De-industrialization, Commercialization of Agriculture and Drain of Wealth Theory.",
    "intro": "British rule transformed the traditional self-sufficient Indian agrarian economy into a colonial appendage servicing metropolitan industrial capital. Through three extractive land revenue settlements—the Permanent Settlement (1793), Ryotwari System (1820), and Mahalwari System (1822)—and the systematic de-industrialization of handicrafts, the colonial state extracted massive agrarian surpluses, documented by nationalist economic historians as the 'Drain of Wealth'.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/2/23/Dadabhai_Naoroji_colour.jpg", "caption": "Dadabhai Naoroji ('Grand Old Man of India'), pioneer of the Drain of Wealth thesis in 'Poverty and Un-British Rule in India'.", "alt": "Dadabhai Naoroji portrait"},
    "table": {
      "caption": "Comparative Analysis of Colonial Land Revenue Settlements",
      "headers": ["Settlement System", "Architect & Year Introduced", "Geographical Coverage & Ownership", "Revenue Assessment & Socio-Economic Impact"],
      "rows": [
        ["Permanent Settlement (Zamindari)", "Lord Cornwallis & John Shore (1793).", "Bengal, Bihar, Orissa, Northern Circars of AP, Varanasi (approx 19% of British India). Zamindars recognized as absolute hereditary owners.", "State revenue demand fixed permanently at 10/11th, with 1/11th retained by Zamindar; 'Sunset Law' triggered auctions if unpaid by sunset of due date; spawned absentee landlordism, sub-infeudation, and peasant misery."],
        ["Ryotwari System", "Thomas Munro & Alexander Read (1820).", "Madras, Bombay, parts of Assam and Coorg (approx 51% of British India). Peasants (Ryots) recognized as registered landholders.", "Direct settlement between State and individual cultivator; revenue revised periodically (every 20–30 years); exorbitant rates (45%–55% of gross produce) led to heavy indebtedness to local Marwari/Chettiar moneylenders."],
        ["Mahalwari System", "Holt Mackenzie (1822) & Robert Merttins Bird (1833).", "North-Western Provinces, Central Provinces, Punjab (approx 30% of British India). Joint ownership by village community (Mahal).", "Entire village/estate jointly and severally responsible for revenue payment through the village headman (Lambardar); survey based on village field maps; high tax pressure triggered peasant destitution."]
      ]
    },
    "bullets": [
      "Drain of Wealth Theory: Articulated by Dadabhai Naoroji in 'Poverty and Un-British Rule in India' (1867/1901), R.C. Dutt in 'Economic History of India', and M.G. Ranade; defined as unrequited transfer of Indian resources to Britain without any equivalent economic or material return.",
      "Constituents of the Drain: Home Charges (salaries, pensions, and leave allowances of British civil/military officers in London), interest on foreign debt, guaranteed 5% return on British railway investments, store purchases for the India Office, and outward remittances of British corporate profits.",
      "De-Industrialization & Commercialization: One-way free trade destroyed the world-famous Indian artisanal handloom textile industry (Dacca muslin, Surat calico); forced cultivation of cash crops (indigo, cotton, opium, tea) distorted local food security and caused catastrophic famines (1866, 1876–78, 1896–97).",
      "Famine Commissions: Campbell Commission (1866), Strachey Commission (1880 - created Famine Code), Lyall Commission (1897), and MacDonnell Commission (1901)."
    ],
    "mains": [
      "Critically evaluate the 'Drain of Wealth' thesis expounded by early Indian nationalist leaders. How did British economic policies dismantle the traditional agrarian and artisanal fabric of India? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define the Drain of Wealth thesis formulated by Dadabhai Naoroji and R.C. Dutt; outline its primary components: Home Charges, guaranteed railway returns, imperial military expenditures abroad, and profits of British managing agencies; analyze structural de-industrialization: influx of cheap machine-made Manchester textiles destroying weaving crafts without modern industrial absorption; examine agrarian commercialization: coercive land revenue settlements and cash-crop export mandates triggering recurrent rural famines; conclude on how this economic critique undermined the moral justification of British rule."
    ],
    "mcqs": [
      "Q1. Who authored the seminal economic treatise 'Poverty and Un-British Rule in India' (1901), systematically detailing the Drain of Wealth mechanism?\n(a) Romesh Chunder Dutt\n(b) Dadabhai Naoroji\n(c) Mahadev Govind Ranade\n(d) Gopal Krishna Gokhale\nCorrect Answer: (b) Dadabhai Naoroji [Explanation: Dadabhai Naoroji expounded the Drain Theory in his 1867 paper and published the comprehensive book 'Poverty and Un-British Rule in India' in 1901.]",
      "Q2. The controversial 'Sunset Law', stipulating that an estate would be confiscated and auctioned if taxes were not paid by sunset on the appointed date, was a feature of:\n(a) Ryotwari Settlement\n(b) Permanent Settlement of Bengal\n(c) Mahalwari System\n(d) Malguzari Settlement\nCorrect Answer: (b) Permanent Settlement of Bengal [Explanation: Under Cornwallis's Permanent Settlement, the Sunset Law mandated that if a Zamindar failed to pay his revenue installment by sunset on the specified date, his zamindari was auctioned off.]",
      "Q3. The Ryotwari land revenue system, establishing direct fiscal settlement between the colonial state and individual peasant cultivators, was initiated in Madras by:\n(a) Lord Cornwallis\n(b) Thomas Munro and Alexander Read\n(c) Holt Mackenzie\n(d) John Shore\nCorrect Answer: (b) Thomas Munro and Alexander Read [Explanation: Captain Alexander Read introduced Ryotwari on an experimental basis in the Baramahal region (1792), later generalized across the Madras Presidency by Governor Sir Thomas Munro in 1820.]",
      "Q4. Which Famine Commission, appointed under the chairmanship of Sir Richard Strachey in 1880, formulated the principles that led to the creation of the Indian Famine Code?\n(a) Campbell Commission\n(b) Strachey Commission\n(c) Lyall Commission\n(d) MacDonnell Commission\nCorrect Answer: (b) Strachey Commission [Explanation: The Strachey Commission (1880) established foundational guidelines for famine relief works, suspension of land revenue, and government responsibility during famines, creating the Famine Code.]",
      "Q5. In the context of British colonial accounts, what did the fiscal category 'Home Charges' specifically encompass?\n(a) Taxes on domestic real estate in Calcutta and Bombay\n(b) Expenditures incurred in Britain on behalf of India by the Secretary of State\n(c) Subsidies paid to princely states under Subsidiary Alliances\n(d) Customs tariffs collected on British textile imports\nCorrect Answer: (b) Expenditures incurred in Britain on behalf of India by the Secretary of State [Explanation: Home Charges represented expenditures incurred in London from Indian revenues, including India Office expenses, pensions of British civil/military officers, and guaranteed interest on Indian railways.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-22",
    "filename": "22_1857_revolt_causes_leaders_and_consequences",
    "title": "The Revolt of 1857: Causes, Key Leaders, Suppression & Aftermath",
    "mapping": "History and Culture of India: The Revolt of 1857 - Multiple Causes, Outbreak at Meerut, Leading Figures (Bahadur Shah, Nana Saheb, Rani Lakshmibai, Kunwar Singh), Reasons for Failure and Crown Governance under Queen's Proclamation (1858).",
    "intro": "The Great Uprising of 1857 was South Asia's first widespread armed rebellion against British East India Company rule. Sparked by sepoy disaffection over the greased Enfield cartridges at Barrackpore and Meerut, the revolt quickly enveloped northern and central India, uniting dispossessed royal houses, peasants, and sepoys under the nominal banner of Mughal Emperor Bahadur Shah Zafar.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Rani_of_jhansi.jpg", "caption": "Rani Lakshmibai of Jhansi, who led the rebel forces in Central India and died fighting at Gwalior.", "alt": "Rani of Jhansi equestrian portrait"},
    "table": {
      "caption": "Centres, Leadership & British Suppression Officers of the 1857 Revolt",
      "headers": ["Centre of Rebellion", "Indian Rebel Leadership", "British Suppression Commanders", "Key Historical Facts & Outcomes"],
      "rows": [
        ["Delhi", "Bahadur Shah Zafar (Emperor) & General Bakht Khan.", "John Nicholson (killed), Hudson.", "Zafar exiled to Rangoon; Hudson murdered princes Mirza Mughal and Khizr Sultan at Khooni Darwaza."],
        ["Kanpur", "Nana Saheb (Dhondu Pant), Tatya Tope, Azimullah Khan.", "Sir Hugh Wheeler, Colin Campbell.", "Nana Saheb escaped to Nepal; Wheeler's entrenchment surrendered; Tatya Tope launched guerrilla operations."],
        ["Lucknow (Awadh)", "Begum Hazrat Mahal & son Birjis Qadr, Maulvi Ahmadullah.", "Henry Lawrence (killed at Residency), Colin Campbell, James Outram.", "Begum Hazrat Mahal escaped to Nepal; intense civilian participation by Awadh peasantry."],
        ["Jhansi & Gwalior", "Rani Lakshmibai & Tatya Tope.", "Sir Hugh Rose.", "Sir Hugh Rose called Rani Lakshmibai 'the bravest and best military leader of the rebels'; fell in battle at Kotah-ki-Serai near Gwalior (18 June 1858)."],
        ["Arrah / Jagdishpur (Bihar)", "Kunwar Singh (80-year-old Zamindar) & brother Amar Singh.", "William Taylor and Vincent Eyre.", "Defeated British detachments repeatedly; died of battle wounds in April 1858 after severing his wounded arm."],
        ["Faizabad", "Maulvi Ahmadullah Shah ('Danka Shah').", "Colin Campbell.", "Fierce guerrilla preacher from Madras; British offered 50,000 rupees bounty; betrayed and killed by Raja of Pawayn."]
      ]
    },
    "bullets": [
      "Underlying Causes: Political (Doctrine of Lapse, Annexation of Awadh 1856, pension termination of Nana Saheb); Economic (ruin of peasants under heavy land revenue, destruction of artisans); Religious-Social (General Service Enlistment Act 1856 requiring overseas service, Christian missionary proselytization, Religious Disabilities Act 1856); Immediate trigger: introduction of Enfield rifle greased with cow and pig fat.",
      "Mangal Pandey (29 March 1857): Sepoy of 34th Bengal Native Infantry at Barrackpore who shot British officers Baugh and Hearsey; hanged on 8 April 1857.",
      "Reasons for Failure: Limited geographical scope (mostly North and Central India; South, West, and Punjab remained largely peaceful); absence of modern unified ideology; lack of support from educated middle class and princely rulers (Scindia, Holkar, Nizam aided British - Lord Canning called them 'breakwaters to the storm'); superior British logistics, arms, and electric telegraph communication.",
      "Constitutional Aftermath: Government of India Act 1858 (ended EIC rule; Crown assumed direct sovereignty via Secretary of State for India and Viceroy); Queen Victoria's Proclamation (1 Nov 1858) promising non-annexation of princely states; Peale Commission reorganized Indian Army (ratio of European to Indian troops raised to 1:2 in Bengal, divide-and-rule 'martial race' theory)."
    ],
    "mains": [
      "Critically evaluate the nature of the Revolt of 1857. Was it merely a 'Sepoy Mutiny' or the 'First War of Indian Independence'? Discuss its administrative consequences under the Act of 1858. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast colonial British historiography (Sir John Lawrence, Sir John Kaye calling it an unpatriotic, selfish sepoy mutiny) with nationalist perspectives (V.D. Savarkar characterizing it as the 'First War of Indian Independence' and R.C. Majumdar's nuanced view); emphasize mass civilian participation across Awadh, Bihar, and Bundelkhand; analyze constitutional aftermath: Government of India Act 1858 ending Company rule, appointment of Viceroy, Queen's Proclamation of 1858 renouncing territorial expansion, and military reorganization under the Peale Commission based on the 'martial race' paradigm."
    ],
    "mcqs": [
      "Q1. Which heroic sepoy of the 34th Bengal Native Infantry fired at his British commanding officers at Barrackpore on 29 March 1857, igniting the 1857 uprising?\n(a) Bakht Khan\n(b) Mangal Pandey\n(c) Ishwar Pandey\n(d) Mata Din\nCorrect Answer: (b) Mangal Pandey [Explanation: Sepoy Mangal Pandey of the 34th BNI revolted at Barrackpore parade ground on 29 March 1857 protesting greased cartridges, becoming the opening martyr of the revolt.]",
      "Q2. The octogenarian Rajput zamindar who led the 1857 armed resistance in Jagdishpur (Arrah, Bihar) and inflicted repeated defeats on British forces was:\n(a) Amar Singh\n(b) Kunwar Singh\n(c) Pir Ali\n(d) Khan Bahadur Khan\nCorrect Answer: (b) Kunwar Singh [Explanation: Babu Kunwar Singh, the 80-year-old chieftain of Jagdishpur in Bihar, displayed extraordinary military leadership and guerrilla warfare against British detachments.]",
      "Q3. British commander Sir Hugh Rose, after capturing Gwalior, paid tribute to which rebel leader as 'the only man among the rebels' and 'the bravest and best military leader'?\n(a) Begum Hazrat Mahal\n(b) Rani Lakshmibai\n(c) Tatya Tope\n(d) Nana Saheb\nCorrect Answer: (b) Rani Lakshmibai [Explanation: General Sir Hugh Rose, who commanded the Central India Field Force, lauded Rani Lakshmibai of Jhansi for her unparalleled valor after she fell in battle at Kotah-ki-Serai.]",
      "Q4. Which British monarchial declaration, read out by Lord Canning at the Allahabad Darbar on 1 November 1858, announced the direct assumption of Indian governance by the British Crown?\n(a) Charter Act of 1858\n(b) Queen Victoria's Proclamation\n(c) Royal Titles Act\n(d) Government of India Manifesto\nCorrect Answer: (b) Queen Victoria's Proclamation [Explanation: Lord Canning read Queen Victoria's Proclamation at Allahabad on 1 November 1858, guaranteeing respect for ancient rights and pledging no further territorial annexations.]",
      "Q5. Which commission was constituted immediately after the 1857 Revolt to reorganize the Indian Army and ensure higher ratios of European troops?\n(a) Hunter Commission\n(b) Peale Commission\n(c) Fraser Commission\n(d) Welby Commission\nCorrect Answer: (b) Peale Commission [Explanation: The Peale Commission (1858) recommended maintaining a strict 1:2 European-to-Indian soldier ratio in Bengal and 1:3 in Madras/Bombay, pioneering the 'martial vs non-martial' recruitment doctrine.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-23",
    "filename": "23_socio_religious_reform_movements",
    "title": "19th Century Socio-Religious Reform Movements: Bengal, West & South India",
    "mapping": "History and Culture of India: Socio-Religious Reform Movements of the 19th Century - Brahmo Samaj, Arya Samaj, Ramakrishna Mission, Theosophical Society, Satyashodhak Samaj, Aligarh Movement and Social Reform Legislation.",
    "intro": "The 19th century witnessed an intellectual and socio-religious awakening across India, often termed the 'Indian Renaissance'. Driven by western scientific rationalism and a critical re-evaluation of indigenous traditions, reform movements challenged caste hierarchy, untouchability, idol worship, and the subjugation of women (Sati, female infanticide, child marriage, and enforced widowhood).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Raja_Ram_Mohun_Roy.jpg", "caption": "Raja Ram Mohan Roy ('Father of Modern Indian Renaissance'), founder of the Brahmo Samaj.", "alt": "Raja Ram Mohan Roy portrait"},
    "table": {
      "caption": "Major Socio-Religious Reform Organizations & Pioneers",
      "headers": ["Reform Movement & Year", "Founding Leader(s)", "Core Doctrinal Philosophy", "Social Crusades & Achievements"],
      "rows": [
        ["Brahmo Samaj (1828)", "Raja Ram Mohan Roy, Debendranath Tagore, Keshab Chandra Sen; Calcutta.", "Monotheism; rejected idol worship, polytheism, and priestly mediation; synthesized Upanishadic monism with western ethical rationalism.", "Crusade against Sati led to Bengal Sati Regulation XVII of 1829 under William Bentinck; published 'Sambad Kaumudi' and 'Mirat-ul-Akhbar'."],
        ["Arya Samaj (1875)", "Swami Dayananda Saraswati; Bombay (headquarters shifted to Lahore).", "'Go back to the Vedas' (Vedas are infallible and self-revealed); denounced Purana myths, idol worship, child marriage, and hereditary caste; supported Shuddhi movement (reconversion).", "Authored 'Satyarth Prakash'; established DAV (Dayanand Anglo-Vedic) schools and Gurukuls (Kangri); supported widow remarriage."],
        ["Ramakrishna Mission (1897)", "Swami Vivekananda (Narendranath Datta); Belur Math, Bengal.", "Practical Vedanta; synthesis of spiritual philosophy and service to suffering humanity ('Daridra Narayana' - service to Jiva is worship of Shiva).", "Parliament of World's Religions at Chicago (1893); bridged Indian spirituality with western social work."],
        ["Satyashodhak Samaj (1873)", "Jyotirao Govindrao Phule & Savitribai Phule; Pune, Maharashtra.", "Anti-Brahminical crusade for social justice; liberation of Shudras, Ati-Shudras, and women from priestly deception.", "Opened first girls' school in Pune (1848); authored 'Gulamgiri' (Slavery) and 'Shetkaryacha Asud'; Savitribai championed female education."],
        ["Aligarh Movement (1875)", "Sir Syed Ahmad Khan; Aligarh, UP.", "Rational interpretation of Quran; scientific modern education for Muslims; opposed religious dogmatism and purdah.", "Founded Muhammadan Anglo-Oriental College (1875, later AMU); published 'Tahzib-ul-Akhlaq'."]
      ]
    },
    "bullets": [
      "Ishwar Chandra Vidyasagar: Principal of Sanskrit College; dedicated crusade for widow rehabilitation culminated in the Hindu Widows' Remarriage Act XV of 1856 under Lord Canning; opened 35 girls' schools in Bengal.",
      "Prarthana Samaj (1867): Founded in Bombay by Atmaram Pandurang with M.G. Ranade and R.G. Bhandarkar; focused on social reform rather than breaking from Hinduism; advocated inter-caste dining, widow remarriage, and depressed classes upliftment.",
      "Theosophical Society: Founded in New York (1875) by Madame Blavatsky and Col. Olcott; headquarters at Adyar, Madras (1886); popularized by Annie Besant who founded Central Hindu College at Varanasi (1898).",
      "Key Reform Legislation: Abolition of Sati (1829), Hindu Widows' Remarriage Act (1856), Native Marriage / Civil Marriage Act (1872), Age of Consent Act (1891 - raised girl's marriage age to 12 under B.M. Malabari's crusade), and Sarda Act / Child Marriage Restraint Act (1929 - fixed minimum marriage age at 14 for girls and 18 for boys)."
    ],
    "mains": [
      "Critically evaluate the contributions of Raja Ram Mohan Roy and Ishwar Chandra Vidyasagar towards women's emancipation in 19th-century India. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight Raja Ram Mohan Roy's intellectual campaign using scriptural exegesis and humanitarian reasoning against Sati, leading to Regulation XVII of 1829; his defense of women's inheritance rights; examine Vidyasagar's philological proof that Vedic texts permitted widow remarriage, translating into the Hindu Widows' Remarriage Act of 1856; detail his personal sacrifice financing widow marriages and establishing Bethune College and 35 female vernacular schools; conclude that their work laid the institutional foundations for modern gender equality in India."
    ],
    "mcqs": [
      "Q1. Which British Governor-General enacted the historic Regulation XVII of December 1829 declaring the practice of Sati illegal and punishable as culpable homicide?\n(a) Lord Cornwallis\n(b) Lord William Bentinck\n(c) Lord Dalhousie\n(d) Lord Wellesley\nCorrect Answer: (b) Lord William Bentinck [Explanation: Supported by the tireless advocacy of Raja Ram Mohan Roy, Lord William Bentinck promulgated the Sati Regulation Act in 1829, banning Sati in Bengal.]",
      "Q2. The groundbreaking Marathi treatise 'Gulamgiri' (Slavery), dedicated to the American abolitionist movement against Negro slavery, was authored in 1873 by:\n(a) B.R. Ambedkar\n(b) Jyotirao Phule\n(c) Gopal Hari Deshmukh ('Lokahitawadi')\n(d) Mahadev Govind Ranade\nCorrect Answer: (b) Jyotirao Phule [Explanation: Mahatma Jyotirao Phule wrote 'Gulamgiri' in 1873, drawing a parallel between the oppression of lower-caste Shudras in India and African-American slaves in the US.]",
      "Q3. Who raised the stirring revivalist slogan 'Go back to the Vedas' and authored the seminal philosophical treatise 'Satyarth Prakash'?\n(a) Swami Vivekananda\n(b) Swami Dayananda Saraswati\n(c) Sri Ramakrishna Paramahamsa\n(d) Keshab Chandra Sen\nCorrect Answer: (b) Swami Dayananda Saraswati [Explanation: Swami Dayananda Saraswati, founder of the Arya Samaj (1875), authored 'Satyarth Prakash' and called for a return to the pure monotheistic teachings of the Vedas.]",
      "Q4. Through the relentless social crusade of Ishwar Chandra Vidyasagar, which milestone social reform act was enacted into law in July 1856?\n(a) Hindu Widows' Remarriage Act (Act XV of 1856)\n(b) Age of Consent Act\n(c) Female Infanticide Prevention Act\n(d) Special Marriage Act\nCorrect Answer: (a) Hindu Widows' Remarriage Act (Act XV of 1856) [Explanation: Drafted under Dalhousie and passed by Lord Canning, Act XV of 1856 legalized the remarriage of Hindu widows, vindicating Vidyasagar's legal crusade.]",
      "Q5. Which social reformer and journalist published the reformist Urdu journal 'Tahzib-ul-Akhlaq' (Social Reformer) to promote modern scientific thinking among Indian Muslims?\n(a) Maulana Abul Kalam Azad\n(b) Sir Syed Ahmad Khan\n(c) Mirza Ghulam Ahmad\n(d) Altaf Hussain Hali\nCorrect Answer: (b) Sir Syed Ahmad Khan [Explanation: Sir Syed Ahmad Khan founded the journal 'Tahzib-ul-Akhlaq' in 1870 to awaken Indian Muslims to Western science, rationalism, and modern educational ethics.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-24",
    "filename": "24_early_nationalism_inc_and_swadeshi_movement",
    "title": "Early Nationalism: Foundation of INC, Moderates, Extremists & Swadeshi",
    "mapping": "History and Culture of India: Growth of Nationalism - Pre-Congress Associations, Foundation of Indian National Congress (1885), Moderate Phase vs Extremist Ideology, Surat Split (1907), Partition of Bengal (1905) and Swadeshi Movement.",
    "intro": "The final quarter of the 19th century witnessed the organized institutionalization of Indian nationalism. Beginning with pre-Congress regional associations and culminating in the founding of the Indian National Congress in 1885, Indian politics evolved through the constitutional agitation of the Moderates, the radical mass mobilization of the Extremists (Lal-Bal-Pal), and the explosive mass protests of the Swadeshi and Boycott Movement (1905–1908).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/First_Session_of_INC_1885.jpg", "caption": "Delegates at the historic First Session of the Indian National Congress at Bombay in December 1885.", "alt": "First INC session group photograph"},
    "table": {
      "caption": "Ideological & Methodological Comparison: Moderates vs Extremists",
      "headers": ["Dimension", "Moderate Nationalists (1885–1905)", "Extremist / Radical Nationalists (1905–1918)"],
      "rows": [
        ["Prominent Leaders", "Dadabhai Naoroji, Gopal Krishna Gokhale, Pherozeshah Mehta, W.C. Bonnerjee, Surendranath Banerjea.", "Bal Gangadhar Tilak, Bipin Chandra Pal, Lala Lajpat Rai ('Lal-Bal-Pal'), Aurobindo Ghosh."],
        ["Political Objective", "Self-government within the British Empire (Dominion Status); administrative reforms, expansion of legislative councils.", "Swaraj (complete self-rule/independence); Tilak declared: 'Swaraj is my birthright and I shall have it!'."],
        ["Methods of Agitation", "Constitutional agitation within the law; 3 P's: Petitions, Prayers, and Protests; believing in British sense of justice.", "Direct mass action; Passive resistance; Boycott of British goods and government institutions; Promotion of Swadeshi and National Education."],
        ["Social Base & Appeal", "Narrow urban educated middle-class elite, lawyers, journalists, wealthy merchants.", "Broad mass base including youth, students, lower middle class, urban artisans, and rural peasantry."],
        ["Cultural Philosophy", "Anglophile orientation; drew inspiration from Western liberal philosophers (Mill, Burke, Spencer).", "Pride in ancient Indian cultural heritage; revived Ganapati and Shivaji festivals (Tilak); religious symbolism (Durga, Vande Mataram)."]
      ]
    },
    "bullets": [
      "Pre-Congress Bodies: Landholders' Society (1838), British Indian Association (1851), Indian Association of Calcutta (1876, Surendranath Banerjea and Anandamohan Bose), Poona Sarvajanik Sabha (1870, M.G. Ranade), Madras Mahajana Sabha (1884), Bombay Presidency Association (1885).",
      "Foundation of INC (1885): Founded by retired British civil servant A.O. Hume; First Session held at Gokuldas Tejpal Sanskrit College, Bombay (28–31 Dec 1885) under President W.C. Bonnerjee with 72 delegates; 'Safety Valve Theory' proposed by Lala Lajpat Rai vs 'Lightning Conductor' reality.",
      "Partition of Bengal (16 Oct 1905): Enacted by Viceroy Lord Curzon on administrative grounds but strategically intended to drive a religious wedge between Hindu-majority West Bengal and Muslim-majority East Bengal.",
      "Swadeshi & Boycott Movement: Rabindranath Tagore composed 'Amar Sonar Bangla' and led Raksha Bandhan rituals; boycott of Manchester cloth and Liverpool salt; National Council of Education established (1906, Bengal National College with Aurobindo Ghosh as principal); chemical industrialization by Acharya P.C. Ray (Bengal Chemicals).",
      "Surat Split (1907): Fierce confrontation between Moderates (led by Rash Behari Ghosh) and Extremists (Tilak) over extending Swadeshi nationwide, causing an open rupture that weakened Congress for a decade."
    ],
    "mains": [
      "Analyze the ideological and tactical divide between the Moderates and Extremists within the Indian National Congress. How did the Swadeshi Movement (1905) mark a watershed in mass political mobilization? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast the class composition, faith in British justice, and constitutional petitions (3 P's) of the Moderates with the radical demand for Swaraj and passive resistance of the Extremists (Lal-Bal-Pal); explain Curzon's imperialist motive behind the 1905 Partition of Bengal; analyze the Swadeshi upsurge: leap from elite drawing-room politics to mass street mobilization involving students, women, and urban workers; detail cultural revitalization (Tagore's songs, national schools) and economic self-reliance (boycott of Manchester textiles); explain how this prepared the ground for the Gandhian mass era despite the 1907 Surat Split."
    ],
    "mcqs": [
      "Q1. Who presided over the historic First Session of the Indian National Congress held at Bombay in December 1885?\n(a) Allan Octavian Hume\n(b) Womesh Chandra Bonnerjee\n(c) Dadabhai Naoroji\n(d) Badruddin Tyabji\nCorrect Answer: (b) Womesh Chandra Bonnerjee [Explanation: W.C. Bonnerjee was elected president of the inaugural INC session at Gokuldas Tejpal Sanskrit College, Bombay, attended by 72 delegates.]",
      "Q2. On which date did the Partition of Bengal take effect, observed across Bengal as a day of national mourning ('Day of Raksha Bandhan' and fasting)?\n(a) 15 August 1905\n(b) 16 October 1905\n(c) 11 December 1905\n(d) 1 January 1906\nCorrect Answer: (b) 16 October 1905 [Explanation: The Partition of Bengal took effect on 16 October 1905; crowds tied Rakhis as a symbol of unshakeable Bengali unity and sang 'Amar Sonar Bangla'.]",
      "Q3. The famous Surat Split of the Indian National Congress in 1907 took place under the presidency of which Moderate leader?\n(a) Gopal Krishna Gokhale\n(b) Rash Behari Ghosh\n(c) Pherozeshah Mehta\n(d) Surendranath Banerjea\nCorrect Answer: (b) Rash Behari Ghosh [Explanation: The 1907 Surat session, presided over by Dr. Rash Behari Ghosh, dissolved into chaos and ended with the formal expulsion of the Extremists led by Tilak.]",
      "Q4. Which nationalist pioneer established the popular public festivals of Ganapati (1893) and Shivaji (1895) to mobilize mass political consciousness against colonial rule?\n(a) Lala Lajpat Rai\n(b) Bal Gangadhar Tilak\n(c) Bipin Chandra Pal\n(d) V.D. Savarkar\nCorrect Answer: (b) Bal Gangadhar Tilak [Explanation: Lokmanya Tilak transformed the domestic religious festivals of Ganeshotsav and Shiv Jayanti into vibrant public platforms for patriotic mobilization.]",
      "Q5. Who was the first Muslim President of the Indian National Congress, presiding over the Third Session at Madras in 1887?\n(a) Sir Syed Ahmad Khan\n(b) Badruddin Tyabji\n(c) Rahimtulla M. Sayani\n(d) Abul Kalam Azad\nCorrect Answer: (b) Badruddin Tyabji [Explanation: Badruddin Tyabji served as the first Muslim President of the INC at the Madras session in 1887, urging Indian Muslims to unite with their fellow countrymen.]"
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

print("Part 5 of Subject 1 generated successfully")
