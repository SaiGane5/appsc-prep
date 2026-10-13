import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "01_History_and_Culture_India"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)

topics = [
  {
    "id": "APPSC-G1-HIST-25",
    "filename": "25_revolutionary_movement_for_freedom",
    "title": "Revolutionary Movement for Freedom: Ghadar, HSRA, Bhagat Singh & Surya Sen",
    "mapping": "History and Culture of India: Revolutionary Movement for Freedom - Phase I (Anushilan Samiti, Yugantar, Ghadar Party, Madam Cama), Phase II (HRA, HSRA, Kakori Action, Bhagat Singh, Central Assembly Bombing, Chittagong Armoury Raid).",
    "intro": "Parallel to mainstream constitutional and non-violent congress agitations, the revolutionary movement provided a radical, militant dimension to India's freedom struggle. Evolving across two distinct phases—from early secret societies (Anushilan, Yugantar) and international anti-colonial networks (Ghadar, Berlin Committee) to the socialist-inspired Hindustan Socialist Republican Association (HSRA) and Surya Sen's Chittagong uprising—revolutionary martyrs inspired uncompromising anti-imperialist patriotism.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/5/54/Bhagat_Singh_1929.jpg", "caption": "Shaheed Bhagat Singh in 1929, ideological leader of the Hindustan Socialist Republican Association (HSRA).", "alt": "Shaheed Bhagat Singh portrait with hat"},
    "table": {
      "caption": "Evolutionary Matrix of the Indian Revolutionary Movement",
      "headers": ["Phase & Organizations", "Key Leaders & Ideological Focus", "Major Actions & Conspiracies", "Historical Significance & Legacy"],
      "rows": [
        ["Phase I: Secret Societies (1900–1915)", "Aurobindo Ghosh, Barindra Kumar Ghosh, Bhupendranath Dutta (Anushilan Samiti & Yugantar in Bengal); Chapekar Brothers, V.D. Savarkar (Abhinav Bharat 1904 in Maharashtra).", "Alipore Bomb Conspiracy (1908, Khudiram Bose & Prafulla Chaki); Curzon Wyllie assassination by Madan Lal Dhingra in London (1909); Delhi Conspiracy Case (1912, Rash Behari Bose bombed Viceroy Lord Hardinge).", "Individual heroic action to terrorize colonial bureaucracy, shatter the myth of British invincibility, and awaken patriotic youth."],
        ["Phase I: Overseas Networks (1905–1919)", "Lala Har Dayal, Sohan Singh Bhakna, Kartar Singh Sarabha (Ghadar Party 1913 in San Francisco); Madam Bhikaji Cama; Shyamji Krishna Varma (India House).", "Komagata Maru Incident (1914); Ghadar Mutiny plan in Punjab (1915); Berlin Committee & Hindu-German Conspiracy; Madam Cama unfurled first Indian tricolor at Stuttgart (1907).", "Internationalized India's independence demand; secular vanguard mobilizing Punjabi Sikh diaspora and global anti-imperialist solidarity."],
        ["Phase II: Socialist Revolution (1924–1935)", "Ram Prasad Bismil, Ashfaqulla Khan, Sachindra Sanyal (HRA 1924); Bhagat Singh, Chandrashekhar Azad, Sukhdev, Rajguru, Bhagwati Charan Vohra (HSRA 1928 at Feroz Shah Kotla, Delhi).", "Kakori Train Action (1925); Saunders assassination (Lahore 1928, avenging Lala Lajpat Rai); Central Legislative Assembly bombing (8 April 1929 by Bhagat Singh & B.K. Dutt: 'To make the deaf hear'); Lahore Conspiracy Case.", "Shift from individual assassination to mass socialist revolution; adoption of Marxism; Bhagat Singh defined revolution not as the cult of bomb/pistol, but the overthrow of human exploitation and capitalism."],
        ["Chittagong Armoury Raid (1930)", "Surya Sen ('Masterda'), Ambika Chakraborty, Ganesh Ghosh, Lokenath Bal, Pritilata Waddedar, Kalpana Datta.", "Chittagong Armoury Raid (18 April 1930); Battle of Jalalabad Hills; proclaimed Indian Republican Army (Chittagong Branch) provisional government; Pahartali European Club raid by Pritilata.", "Pioneered mass guerrilla warfare involving armed female revolutionaries; shattered British police and military prestige in Eastern India."]
      ]
    },
    "bullets": [
      "Bhagat Singh's Ideological Legacy: Authored 'Why I am an Atheist' in Lahore Central Jail; rejected religious communalism; embraced scientific socialism; martyred alongside Rajguru and Sukhdev on 23 March 1931 ('Shaheed Diwas').",
      "Jatin Das's Martyrdom: 63-day hunger strike in Lahore Central Jail protesting horrific prison conditions and demanding political prisoner status; died a martyr on 13 September 1929.",
      "Chandrashekhar Azad: Commander-in-chief of HSRA; vowed never to be captured alive by the British; died in heroic gunfight against police at Alfred Park, Allahabad on 27 February 1931.",
      "Women in Revolutionary Movement: Pritilata Waddedar (sacrificed life by cyanide after leading Pahartali raid), Kalpana Datta, Bina Das (shot Bengal Governor Stanley Jackson at Calcutta University convocation in 1932), Suniti Choudhury and Santi Ghose (assassinated Comilla district magistrate Charles Stevens)."
    ],
    "mains": [
      "Trace the ideological evolution of the revolutionary movement from individual assassination to scientific socialism under the Hindustan Socialist Republican Association (HSRA). (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Contrast Phase I methods (Anushilan, Yugantar) focused on individual heroism, religious symbolism (Goddess Kali, Gita oaths), and targeted assassinations of tyrannical colonial officers; analyze the post-Non-Cooperation transformation: disillusioned youth adopting socialist literature after the Russian Revolution; explain the renaming of HRA to HSRA in 1928 at Feroz Shah Kotla under Bhagat Singh and Azad; highlight Bhagat Singh's ideological writings ('Philosophy of the Bomb' by Vohra, 'Why I am an Atheist') defining revolution as dismantling class exploitation and establishing a peasant-worker socialist republic; conclude on how their courtroom trials popularized anti-colonial slogans like 'Inquilab Zindabad'."
    ],
    "mcqs": [
      "Q1. Who unfurled the first design of the Indian National Flag on foreign soil at the International Socialist Congress held in Stuttgart, Germany in 1907?\n(a) Sarojini Naidu\n(b) Bhikaji Cama\n(c) Annie Besant\n(d) Kalpana Datta\nCorrect Answer: (b) Bhikaji Cama [Explanation: Madam Bhikaji Cama proudly hoisted the tricolor 'Flag of Indian Independence' at the International Socialist Conference in Stuttgart, Germany on 22 August 1907.]",
      "Q2. The revolutionary organization 'Hindustan Republican Association' (HRA), founded in Kanpur in 1924, was reconstituted as 'Hindustan Socialist Republican Association' (HSRA) in 1928 at:\n(a) Kakori\n(b) Feroz Shah Kotla, Delhi\n(c) Alfred Park, Allahabad\n(d) Lahore Central Jail\nCorrect Answer: (b) Feroz Shah Kotla, Delhi [Explanation: In September 1928, under the leadership of Chandrashekhar Azad and Bhagat Singh, the HRA was reorganized at Feroz Shah Kotla, Delhi, adding 'Socialist' to its name.]",
      "Q3. Who accompanied Bhagat Singh in throwing non-lethal smoke bombs and leaflets ('To make the deaf hear') into the Central Legislative Assembly in Delhi on 8 April 1929?\n(a) Rajguru\n(b) Batukeshwar Dutt\n(c) Sukhdev\n(d) Jatin Das\nCorrect Answer: (b) Batukeshwar Dutt [Explanation: Bhagat Singh and Batukeshwar Dutt hurled non-lethal bombs into the empty benches of the Central Legislative Assembly to protest the repressive Public Safety and Trade Disputes Bills.]",
      "Q4. Which legendary revolutionary, revered as 'Masterda', led the audacious Chittagong Armoury Raid on 18 April 1930 and proclaimed a Provisional Revolutionary Government?\n(a) Rash Behari Bose\n(b) Surya Sen\n(c) Jatindranath Mukherjee (Bagha Jatin)\n(d) Sachindra Nath Sanyal\nCorrect Answer: (b) Surya Sen [Explanation: Surya Sen ('Masterda'), a schoolteacher, organized the Indian Republican Army and executed the famous raid on the British police and auxiliary armouries at Chittagong.]",
      "Q5. Revolutionary freedom fighter Jatin Das attained martyrdom after an epic 63-day hunger strike in Lahore Central Jail in September 1929 demanding:\n(a) Release of all political prisoners\n(b) Civil rights and political prisoner status for undertrial revolutionaries\n(c) Commutation of Bhagat Singh's death sentence\n(d) Immediate repeal of the Rowlatt Act\nCorrect Answer: (b) Civil rights and political prisoner status for undertrial revolutionaries [Explanation: Jatin Das died on 13 September 1929 following a 63-day fast demanding humane prison conditions, hygienic food, and dignified status as political prisoners rather than common criminals.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-26",
    "filename": "26_gandhian_era_early_experiments_and_non_cooperation",
    "title": "Gandhian Era: Early Satyagrahas, Khilafat & Non-Cooperation Movement",
    "mapping": "History and Culture of India: Gandhian Mass Movements - Arrival in India (1915), Early Satyagrahas (Champaran, Ahmedabad, Kheda), Rowlatt Satyagraha, Jallianwala Bagh (1919), Khilafat Issue and Non-Cooperation Movement (1920–1922).",
    "intro": "The return of Mohandas Karamchand Gandhi to India in January 1915 fundamentally revolutionized the Indian National Movement. Testing his South African techniques of Truth (Satya) and Non-Violence (Ahimsa) in Champaran, Ahmedabad, and Kheda, Gandhi transformed the freedom struggle from an elite constitutional discourse into a mass popular upsurge, culminating in the nationwide Non-Cooperation and Khilafat Movement (1920–1922).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/7/7a/Mahatma-Gandhi%2C_studying%2C_1931.jpg", "caption": "Mahatma Gandhi, who synthesized moral non-violence with grassroots mass civil disobedience.", "alt": "Mahatma Gandhi reading portrait"},
    "table": {
      "caption": "Evolutionary Milestones of Gandhi's Early Mass Mobilizations",
      "headers": ["Movement / Episode & Year", "Geographical Focus & Adversaries", "Core Grievance & Tactical Methods", "Historical Outcome & Significance"],
      "rows": [
        ["Champaran Satyagraha (1917)", "Champaran, Bihar; European Indigo Planters.", "Coercive 'Tinkathia' system (forcing peasants to cultivate indigo on 3/20th of land); First Civil Disobedience in India.", "Gandhi refused magistrate's order to leave; Champaran Agrarian Committee formed; Tinkathia abolished with 25% compensation refunded to peasants."],
        ["Ahmedabad Mill Strike (1918)", "Ahmedabad, Gujarat; Textile Mill Owners.", "Discontinuation of Plague Bonus; Gandhi's First Hunger Strike in India; advocated 35% wage hike based on trusteeship.", "Mill owners arbitrated and conceded the full 35% wage increase; established the Textile Labour Association."],
        ["Kheda Satyagraha (1918)", "Kheda, Gujarat; Colonial Revenue Administration.", "Severe crop failure (yield below 25% of normal); revenue officials refused land tax suspension; First Non-Cooperation in India.", "Government issued secret instructions to suspend revenue collection for all destitute cultivators; Sardar Vallabhbhai Patel emerged as key leader."],
        ["Rowlatt Satyagraha & Jallianwala Bagh (1919)", "Punjab & Nationwide; Anarchical and Revolutionary Crimes Act 1919 (Rowlatt Act - detention without trial for 2 years).", "Rowlatt Satyagraha Sabha; arrest of Dr. Saifuddin Kitchlew and Dr. Satyapal led to Jallianwala Bagh gathering (13 April 1919, Baisakhi day).", "General Dyer opened fire on unarmed crowd, killing 1,000+; Rabindranath Tagore renounced Knighthood; Hunter Commission whitewash; triggered loss of moral legitimacy for British rule."],
        ["Non-Cooperation & Khilafat Movement (1920–1922)", "Pan-Indian; Alliance of Congress and Khilafat Committee (Ali Brothers - Shaukat Ali, Mohammad Ali).", "Tripartite goal: Redressal of Punjab wrongs, Khilafat restoration (Ottoman Caliphate), and achievement of Swaraj within one year.", "Surrender of British titles (Gandhi returned Kaiser-i-Hind); boycott of government schools, courts, and foreign cloth; picketing of liquor shops; foundation of National Universities (Kashi Vidyapeeth, Jamia Millia, Gujarat Vidyapith)."]
      ]
    },
    "bullets": [
      "Nagpur Session of INC (December 1920): Ratified the Non-Cooperation program under C. Vijayaraghavachariar; reorganized Provincial Congress Committees on linguistic lines; introduced 4-anna nominal membership fee, opening Congress to the rural masses; established 15-member Congress Working Committee (CWC).",
      "Mass Upsurge Dynamics: Peasant revolts (Awadh Kisan Sabha led by Baba Ramchandra, Eka Movement), tribal protests (Manyam rebellion under Alluri Sitarama Raju in AP), working-class strikes in tea plantations (Assam) and railways, and student walkouts.",
      "Chauri Chaura Incident (4 February 1922): Violent clash in Gorakhpur district, UP, where an enraged mob set fire to a police station, killing 22 policemen inside.",
      "Withdrawal of Movement: Gandhi unilaterally suspended the Non-Cooperation Movement on 12 February 1922 via the Bardoli Resolution, maintaining that India was not yet adequately trained in non-violence; deeply disappointed younger leaders (Nehru, Subhas Bose).",
      "Birth of Swaraj Party (January 1923): Formed by C.R. Das (President) and Motilal Nehru (Secretary) as 'Pro-Changers' advocating council entry to 'wreck the colonial legislature from within', opposing 'No-Changers' (Rajagopalachari, Rajendra Prasad, Vallabhbhai Patel) who focused on constructive work."
    ],
    "mains": [
      "Discuss the significance of the Non-Cooperation Movement (1920–1922) in India's freedom struggle. Why did Mahatma Gandhi decide to unilaterally suspend the movement following the Chauri Chaura incident? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Highlight how Non-Cooperation transformed Congress from an urban elite petitioning body into a mass nationalist movement cutting across peasants, workers, Muslims (Khilafat alliance), and students; detail its destructive and constructive dimensions (boycott of foreign cloth, hand-spinning of Khadi, anti-untouchability, national schools); explain the Chauri Chaura incident (4 Feb 1922); analyze Gandhi's rationale for sudden withdrawal: steadfast commitment to non-violence as an absolute moral principle, understanding that state repression would crush a violent movement, and protecting the unarmed rural masses from brutal military reprisal; assess the immediate demoralization leading to the rise of the Swaraj Party."
    ],
    "mcqs": [
      "Q1. Which local peasant leader from Bihar persistently persuaded Mahatma Gandhi at the 1916 Lucknow Congress to visit Champaran and investigate the grievances of indigo ryots?\n(a) Raj Kumar Shukla\n(b) Brajkishore Prasad\n(c) Anugrah Narayan Sinha\n(d) J.B. Kripalani\nCorrect Answer: (a) Raj Kumar Shukla [Explanation: Raj Kumar Shukla, an indigo cultivator from Champaran, persistently urged Gandhi to visit Bihar, leading to Gandhi's historic First Civil Disobedience at Champaran in 1917.]",
      "Q2. Following the gruesome Jallianwala Bagh Massacre on 13 April 1919, who renounced his British Knighthood in an impassioned protest letter to Viceroy Lord Chelmsford?\n(a) Mahatma Gandhi\n(b) Rabindranath Tagore\n(c) Sir Syed Ahmad Khan\n(d) Subhas Chandra Bose\nCorrect Answer: (b) Rabindranath Tagore [Explanation: Rabindranath Tagore renounced his Knighthood in May 1919, declaring that the time had come when badges of honour make our shame glaring in the incongruous context of suffering.]",
      "Q3. The Non-Cooperation program was formally endorsed and the constitution of the Indian National Congress reorganized on linguistic lines at which historic annual session in December 1920?\n(a) Calcutta Special Session\n(b) Nagpur Annual Session\n(c) Ahmedabad Session\n(d) Gaya Session\nCorrect Answer: (b) Nagpur Annual Session [Explanation: The December 1920 Nagpur Congress session, presided over by C. Vijayaraghavachariar, ratified the Non-Cooperation program and reorganized Congress committees along linguistic boundaries.]",
      "Q4. Following the violent death of 22 policemen at Chauri Chaura on 4 February 1922, Mahatma Gandhi suspended the Non-Cooperation Movement through which historic resolution?\n(a) Lucknow Resolution\n(b) Bardoli Resolution\n(c) Delhi Manifesto\n(d) Wardha Resolution\nCorrect Answer: (b) Bardoli Resolution [Explanation: The Congress Working Committee met at Bardoli on 12 February 1922 and passed the Bardoli Resolution formally terminating the civil disobedience and Non-Cooperation movement.]",
      "Q5. In January 1923, Chittaranjan Das and Motilal Nehru founded which political party to contest elections and wreck the 1919 Montagu-Chelmsford legislative councils from within?\n(a) Independent Labour Party\n(b) Swaraj Party (Congress-Khilafat Swarajya Party)\n(c) Forward Bloc\n(d) Justice Party\nCorrect Answer: (b) Swaraj Party (Congress-Khilafat Swarajya Party) [Explanation: C.R. Das and Motilal Nehru founded the Congress-Khilafat Swarajya Party (Swaraj Party) in January 1923 to enter legislative councils and obstruct colonial governance from within.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-27",
    "filename": "27_civil_disobedience_movement_and_round_table_conferences",
    "title": "Civil Disobedience: Dandi March, Round Table Conferences & Poona Pact",
    "mapping": "History and Culture of India: Civil Disobedience Movement (1930–1934) - Simon Commission Boycott, Nehru Report, Lahore Resolution (Purna Swaraj), Dandi March, Gandhi-Irwin Pact, Round Table Conferences, Communal Award and Poona Pact (1932).",
    "intro": "The Civil Disobedience Movement (1930–1934) marked the second great nationwide mass campaign of the Indian freedom struggle. Catalyzed by the boycott of the all-white Simon Commission (1927), the declaration of 'Purna Swaraj' (Complete Independence) at the Lahore Congress (1929), and Gandhi's historic Dandi Salt March (12 March – 6 April 1930), the movement challenged British imperial authority across the salt pans, forest tracts, and urban centres of India.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Dandi_March.jpg", "caption": "Mahatma Gandhi leading the historic 240-mile Salt March from Sabarmati Ashram to Dandi in March 1930.", "alt": "Mahatma Gandhi marching with staff during Dandi Salt March"},
    "table": {
      "caption": "Chronological Milestones of the Civil Disobedience Era",
      "headers": ["Chronological Milestone & Year", "Key Actors & Geographical Epicentre", "Constitutional / Strategic Issues", "Outcomes & Historical Significance"],
      "rows": [
        ["Simon Commission Boycott (1927–1928)", "All-white 7-member Indian Statutory Commission under Sir John Simon; Lala Lajpat Rai; Madras (Tanguturi Prakasam).", "Appointed to review 1919 GoI Act without a single Indian member ('Simon Go Back'); Lala Lajpat Rai assaulted by James Scott in Lahore, dying of injuries (17 Nov 1928).", "United all political parties in protest; triggered challenge by Birkenhead leading to the Nehru Report."],
        ["Nehru Report (August 1928)", "All Parties Conference; Motilal Nehru (Chairman), Jawaharlal Nehru (Secretary).", "First indigenous constitutional draft; demanded Dominion Status, 19 Fundamental Rights, universal adult suffrage, rejection of separate electorates.", "Rejected by Jinnah who formulated his 'Fourteen Points'; younger radicals (Jawaharlal, Subhas Bose) demanded Complete Independence."],
        ["Lahore Congress & Purna Swaraj (Dec 1929)", "Jawaharlal Nehru (President); banks of river Ravi at Lahore.", "Adopted 'Purna Swaraj' (Complete Independence) as the sole national goal; tri-colour unfurled at midnight on 31 Dec 1929.", "26 January 1930 observed nationwide as the First Independence Day (Purna Swaraj Day); authorized Gandhi to launch Civil Disobedience."],
        ["Dandi Salt March (12 March – 6 April 1930)", "Gandhi & 78 handpicked ashramites; 240 miles from Sabarmati Ashram to Dandi seashore.", "Broke colonial Salt Monopoly law by picking a fistful of natural salt; targeted salt tax affecting every starving peasant.", "Sparked nationwide salt satyagrahas: C. Rajagopalachari (Vedaranyam March), K. Kelappan (Payyanur), Sarojini Naidu (Dharasana Salt Works raid), Khan Abdul Ghaffar Khan (Khudai Khidmatgars at Peshawar)."],
        ["Gandhi-Irwin Pact & Karachi Session (March 1931)", "Mahatma Gandhi & Viceroy Lord Irwin; Karachi Congress (Sardar Patel President).", "Suspension of Civil Disobedience; release of non-violent political prisoners; right to make domestic salt; Congress agreed to attend Second Round Table Conference.", "Karachi Session endorsed the Pact, ratified Purna Swaraj, and adopted landmark resolutions on Fundamental Rights and the National Economic Programme (drafted by Nehru)."],
        ["Communal Award & Poona Pact (1932)", "British PM Ramsay MacDonald; Dr. B.R. Ambedkar & Mahatma Gandhi (Yerwada Jail fast).", "MacDonald's Communal Award (Aug 1932) granted separate electorates to Depressed Classes; Gandhi launched fast-unto-death in Yerwada Jail to prevent Hindu social vivisection.", "Poona Pact (24 Sept 1932) abandoned separate electorates in favor of joint electorates, while dramatically increasing reserved legislative seats for Depressed Classes from 71 to 148 in provincial councils."]
      ]
    },
    "bullets": [
      "The Three Round Table Conferences (London): First RTC (1930 - boycotted by Congress; attended by Ambedkar, Tej Bahadur Sapru, Muslim League); Second RTC (1931 - attended solely by Gandhi representing INC, ended in deadlock over minority separate electorates); Third RTC (1932 - boycotted by Congress; culminated in White Paper leading to the Government of India Act 1935).",
      "Khan Abdul Ghaffar Khan ('Frontier Gandhi'): Organized the non-violent 'Khudai Khidmatgars' (Red Shirts) in NWFP; Garhwali soldiers under Chandra Singh Garhwali refused to open fire on unarmed Muslim satyagrahis at Peshawar.",
      "Government of India Act 1935: Enacted provincial autonomy; abolished provincial dyarchy and introduced dyarchy at the Centre; created an All-India Federation (never implemented); established Federal Court and Reserve Bank of India; 1937 provincial elections saw Congress form ministries in 7 out of 11 provinces."
    ],
    "mains": [
      "Critically evaluate the historical circumstances leading to the Poona Pact of 1932 between Mahatma Gandhi and Dr. B.R. Ambedkar. How did it shape the constitutional representation of Depressed Classes in modern India? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain Ramsay MacDonald's Communal Award (Aug 1932) extending separate electorates to the Depressed Classes, treating them as a distinct minority from Hindus; analyze Gandhi's moral-political objection: belief that separate electorates would permanently alienate untouchables and prevent Hindu social reform, leading to his fast-unto-death in Yerwada Jail; examine Ambedkar's pragmatic stance defending political rights against upper-caste oppression; detail the terms of the Poona Pact (24 Sept 1932): replacement of separate electorates with joint electorates with reserved seats, doubling reserved provincial seats from 71 to 148; conclude on how this established the modern constitutional framework of political reservations."
    ],
    "mcqs": [
      "Q1. At which historic annual session of the Indian National Congress in December 1929 was the resolution for 'Purna Swaraj' (Complete Independence) officially adopted under the presidency of Jawaharlal Nehru?\n(a) Madras Session\n(b) Lahore Session\n(c) Karachi Session\n(d) Calcutta Session\nCorrect Answer: (b) Lahore Session [Explanation: The historic Lahore Congress of December 1929, presided over by Jawaharlal Nehru, proclaimed Purna Swaraj (Complete Independence) as the ultimate national goal.]",
      "Q2. The historic Dandi Salt March commenced from Sabarmati Ashram on 12 March 1930 with how many chosen ashramite volunteers accompanying Mahatma Gandhi?\n(a) 50 volunteers\n(b) 72 volunteers\n(c) 78 volunteers\n(d) 100 volunteers\nCorrect Answer: (c) 78 volunteers [Explanation: Gandhi marched 240 miles from Sabarmati Ashram to the Dandi coastline accompanied initially by 78 handpicked ashramite satyagrahis, reaching Dandi on 5 April 1930.]",
      "Q3. In Tamil Nadu, who led the parallel coastal Salt Satyagraha march from Tiruchirappalli to Vedaranyam in April 1930?\n(a) K. Kamaraj\n(b) C. Rajagopalachari\n(c) Subramania Bharati\n(d) V.O. Chidambaram Pillai\nCorrect Answer: (b) C. Rajagopalachari [Explanation: C. Rajagopalachari (Rajaji) led a group of 100 Congress volunteers from Trichy to Vedaranyam on the Tanjore coast to break the salt law in April 1930.]",
      "Q4. Which Indian leader attended all three Round Table Conferences held in London between 1930 and 1932 to advocate for the rights of the Depressed Classes?\n(a) Mahatma Gandhi\n(b) Dr. B.R. Ambedkar\n(c) Jawaharlal Nehru\n(d) Sardar Vallabhbhai Patel\nCorrect Answer: (b) Dr. B.R. Ambedkar [Explanation: Dr. B.R. Ambedkar and Sir Tej Bahadur Sapru attended all three Round Table Conferences in London (1930, 1931, and 1932).]",
      "Q5. The historic Poona Pact, signed on 24 September 1932 between representatives of caste Hindus and the Depressed Classes, replaced separate electorates with:\n(a) Universal adult franchise without reservations\n(b) Joint electorates with reserved seats for Depressed Classes\n(c) Proportional representation by single transferable vote\n(d) Nomination by the Governor-General\nCorrect Answer: (b) Joint electorates with reserved seats for Depressed Classes [Explanation: The Poona Pact discarded separate electorates in favor of joint electorates with reserved seats, increasing legislative seats for the Depressed Classes from 71 to 148.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-28",
    "filename": "28_quit_india_ina_and_transfer_of_power",
    "title": "Quit India Movement, Subhas Chandra Bose & Transfer of Power",
    "mapping": "History and Culture of India: Final Phase of Freedom Struggle (1940–1947) - August Offer, Cripps Mission, Quit India Movement ('Do or Die'), Subhas Chandra Bose and INA (Azad Hind Fauj), RIN Mutiny (1946), Cabinet Mission and Mountbatten Plan.",
    "intro": "The 1940s brought the climactic denouement of the Indian freedom struggle. Triggered by the failure of the Cripps Mission (1942), the Quit India Movement unleashed an unprecedented spontaneous mass rebellion under the clarion call 'Do or Die'. Simultaneously, Netaji Subhas Chandra Bose's Indian National Army (INA) challenged British arms across Southeast Asia and the Manipur frontier, precipitating post-war naval mutinies that convinced the British that transfer of power was unavoidable.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Subhas_Chandra_Bose_INA.jpg", "caption": "Netaji Subhas Chandra Bose reviewing soldiers of the Azad Hind Fauj (Indian National Army) in Singapore.", "alt": "Netaji Subhas Chandra Bose in military uniform"},
    "table": {
      "caption": "Milestones in the Final Transition to Indian Independence",
      "headers": ["Episode / Mission & Year", "Key Actors & Leaders", "Constitutional Proposals & Actions", "Outcomes & Historical Impact"],
      "rows": [
        ["Cripps Mission (March 1942)", "Sir Stafford Cripps; Winston Churchill government.", "Offered Dominion Status post-WWII; constituent assembly; right of provinces to secede.", "Rejected by Congress (Gandhi called it 'a post-dated cheque on a crashing bank') and Muslim League; cleared path for Quit India."],
        ["Quit India Movement (August 1942)", "Mahatma Gandhi, Aruna Asaf Ali, Jayaprakash Narayan, Ram Manohar Lohia, Usha Mehta.", "All India Congress Committee passed Quit India Resolution at Gowalia Tank, Bombay (8 Aug 1942); Gandhi's mantra: 'Do or Die' (Karo ya Maro).", "Top leaders arrested on 9 Aug (Operation Zero Hour); spontaneous mass rebellion; communications severed; parallel governments (Jatiya Sarkar in Tamluk, Prati Sarkar in Satara, Ballia under Chittu Pandey)."],
        ["Indian National Army (INA / Azad Hind Fauj)", "Netaji Subhas Chandra Bose, Rash Behari Bose, Mohan Singh; Singapore & Rangoon.", "Provisional Government of Free India (Arzi Hukumat-e-Azad Hind, 21 Oct 1943); slogan: 'Chalo Delhi', 'Jai Hind'; Rani of Jhansi women's regiment (Captain Lakshmi Sahgal).", "Advanced into Kohima and Imphal alongside Japanese; INA Red Fort Trials (1945–46: Prem Sehgal, Gurbaksh Dhillon, Shahnawaz Khan defended by Bhulabhai Desai) aroused unprecedented patriotic fervor."],
        ["Royal Indian Navy (RIN) Mutiny (Feb 1946)", "Naval ratings of HMIS Talwar, Bombay; BC Dutt, MS Khan.", "Struck over racial discrimination, unpalatable food, and INA trials; spread to 78 ships and 20 shore establishments across Karachi and Calcutta.", "Ratings hoisted Congress, League, and Communist flags; demonstrated armed forces were no longer loyal to the Crown; Patel and Jinnah persuaded them to surrender."],
        ["Cabinet Mission & Mountbatten Plan (1946–1947)", "Cabinet Mission: Pethick-Lawrence, Stafford Cripps, A.V. Alexander; Lord Mountbatten.", "Cabinet Mission proposed 3-tier federation and Constituent Assembly; Mountbatten Plan (3 June 1947) accepted Partition of India and Pakistan; Indian Independence Act passed on 18 July 1947.", "India achieved independence at midnight on 15 August 1947; marked by tragic partition violence and displacement of millions across Punjab and Bengal."]
      ]
    },
    "bullets": [
      "August Offer (8 August 1940, Viceroy Linlithgow): Promised Dominion status in unspecified future and expansion of Viceroy's Executive Council; rejected by Congress, which launched Individual Satyagraha (first satyagrahi: Vinoba Bhave, second: Jawaharlal Nehru).",
      "Underground Movement in 1942: Aruna Asaf Ali hoisted the national flag at Gowalia Tank; Usha Mehta operated the clandestine 'Congress Radio' broadcasting from Bombay; Jayaprakash Narayan escaped Hazaribagh jail to organize Azad Dasta guerrilla squads.",
      "Direct Action Day (16 August 1946): Muslim League under Jinnah launched Direct Action Day to demand Pakistan, unleashing catastrophic communal pogroms ('Great Calcutta Killings') spreading to Noakhali and Bihar, where Gandhi walked barefoot on peace missions.",
      "Radcliffe Line: Sir Cyril Radcliffe chaired the Boundary Commissions that partitioned Punjab and Bengal into India and Pakistan, dividing communities with hurried cartographic borders."
    ],
    "mains": [
      "Analyze the multifaceted factors—including the Quit India Movement, the INA trials, and the Royal Indian Navy Mutiny—that made British withdrawal from India inevitable post-World War II. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the total erosion of colonial legitimacy following the 1942 Quit India mass rebellion; analyze the international and economic exhaustion of post-WWII Britain under Clement Attlee's Labour government; evaluate the transformative impact of the INA Red Fort trials uniting all communities across India; analyze the Royal Indian Navy (RIN) Mutiny of February 1946 which proved that the armed forces, police, and bureaucracy—the essential instruments of colonial coercion—could no longer be relied upon to suppress Indians; conclude that the British were forced to orchestrate a rapid, graceful transfer of power."
    ],
    "mcqs": [
      "Q1. At the Gowalia Tank Maidan in Bombay on 8 August 1942, Mahatma Gandhi delivered which historic clarion call to the nation while launching the Quit India Movement?\n(a) 'Swaraj is my birthright'\n(b) 'Do or Die' (Karo ya Maro)\n(c) 'Inquilab Zindabad'\n(d) 'Give me blood, and I shall give you freedom'\nCorrect Answer: (b) 'Do or Die' (Karo ya Maro) [Explanation: Gandhi gave the memorable mantra 'Do or Die' at Gowalia Tank on 8 August 1942, declaring: 'We shall either free India or die in the attempt.']",
      "Q2. Who operated an underground clandestine radio transmission network ('Secret Congress Radio') during the Quit India Movement of 1942 to broadcast uncensored news?\n(a) Aruna Asaf Ali\n(b) Usha Mehta\n(c) Sucheta Kripalani\n(d) Sarojini Naidu\nCorrect Answer: (b) Usha Mehta [Explanation: Dr. Usha Mehta and her associates set up the clandestine 'Congress Radio' broadcasting patriotic bulletins from shifting locations across Bombay during 1942.]",
      "Q3. Netaji Subhas Chandra Bose established the Provisional Government of Free India ('Arzi Hukumat-e-Azad Hind') in exile on 21 October 1943 in:\n(a) Tokyo\n(b) Berlin\n(c) Singapore\n(d) Rangoon\nCorrect Answer: (c) Singapore [Explanation: Netaji proclaimed the Provisional Government of Free India (Arzi Hukumat-e-Azad Hind) at Cathay Cinema hall in Singapore on 21 October 1943.]",
      "Q4. Which all-women combat regiment was created within the Indian National Army (INA) under the commanding leadership of Captain Lakshmi Sahgal?\n(a) Jhansi Ki Rani Regiment\n(b) Kasturba Regiment\n(c) Sarojini Naidu Brigade\n(d) Durga Bhabhi Battalion\nCorrect Answer: (a) Jhansi Ki Rani Regiment [Explanation: Netaji raised the pioneering all-women combat unit 'Rani of Jhansi Regiment' in 1943, commanded by Captain Lakshmi Swaminathan (Sahgal).]",
      "Q5. The Royal Indian Navy (RIN) Mutiny of February 1946, which signaled the final collapse of military loyalty to the British Raj, commenced on which naval ratings ship in Bombay?\n(a) HMIS Vikrant\n(b) HMIS Talwar\n(c) HMIS Shivaji\n(d) HMIS Ganga\nCorrect Answer: (b) HMIS Talwar [Explanation: On 18 February 1946, 1,100 naval ratings aboard the signal training ship HMIS Talwar in Bombay went on strike against racial discrimination, unpalatable food, and the abuse of Indian sailors.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-29",
    "filename": "29_integration_of_princely_states_and_constitution",
    "title": "Integration of Princely States & The Making of the Indian Constitution",
    "mapping": "History and Culture of India: Post-Independence Integration - Sardar Vallabhbhai Patel and V.P. Menon, Integration of 565 Princely States (Junagadh, Hyderabad - Operation Polo, Kashmir), Drafting of the Indian Constitution (Constituent Assembly, Dr. B.R. Ambedkar).",
    "intro": "On the eve of independence in August 1947, India faced the existential threat of Balkanization into over 565 autonomous princely fiefdoms following the lapse of British Paramountcy. Through the consummate diplomatic finesse, statesmanship, and firm resolve of Deputy Prime Minister Sardar Vallabhbhai Patel and States Secretary V.P. Menon, the princely states were successfully integrated into the Indian Union, while the Constituent Assembly under Dr. B.R. Ambedkar framed the world's most comprehensive written democratic constitution.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Sardar_patel.jpg", "caption": "Sardar Vallabhbhai Patel ('Iron Man of India'), the architect of national integration.", "alt": "Sardar Vallabhbhai Patel portrait"},
    "table": {
      "caption": "Resolution of Crucial Princely State Integration Crises (1947–1949)",
      "headers": ["Princely State", "Ruler & Demographics", "Integration Crisis & Deadlock", "Resolution Mechanism & Historical Milestone"],
      "rows": [
        ["Junagadh (Gujarat)", "Nawab Muhammad Mahabat Khan III; Hindu-majority population (80%+).", "Nawab announced accession to Pakistan in August 1947, defying geographical contiguity; public uprising (Arzi Hukumat formed under Samaldas Gandhi).", "Nawab fled to Karachi; Indian forces entered in November 1947; comprehensive plebiscite held in February 1948 voted 99% in favor of joining India."],
        ["Hyderabad (Deccan)", "Nizam Mir Osman Ali Khan (Asaf Jah VII); Hindu-majority (85%+); Razakar militia led by Kasim Razvi.", "Nizam signed 1-year Standstill Agreement (Nov 1947) while secretly negotiating arms; brutal Razakar terror and Telangana peasant armed rebellion against feudal Deshmukhs.", "'Operation Polo' (Police Action, 13–18 Sept 1948) commanded by Major General J.N. Chaudhuri; Nizam surrendered on 18 Sept 1948 and acceded to the Indian Union; appointed Rajpramukh."],
        ["Jammu & Kashmir", "Maharaja Hari Singh; Muslim-majority population.", "Maharaja desired sovereign neutrality and offered Standstill Agreement; invaded by Pakistan-backed tribal Pashtun raiders in October 1947.", "Maharaja signed Instrument of Accession on 26 October 1947; Indian Army airlifted to Srinagar, repelling invaders; special constitutional framework under Article 370."]
      ]
    },
    "bullets": [
      "Instruments of Accession & Privy Purses: Rulers surrendered Defence, Foreign Affairs, and Communications to the Indian Union; granted transitional tax-free Privy Purses and royal titles (abolished in 1971 by the 26th Constitutional Amendment under Indira Gandhi).",
      "Constituent Assembly Composition: 389 members initially (299 post-partition) elected indirectly by Provincial Assemblies; First Meeting on 9 December 1946 (Dr. Sachchidananda Sinha interim President; Dr. Rajendra Prasad elected permanent President on 11 Dec); B.N. Rau appointed Constitutional Advisor.",
      "Objectives Resolution (13 December 1946): Moved by Jawaharlal Nehru; laid down ideological foundation of an Independent Sovereign Republic committed to justice, liberty, and equality; adopted on 22 January 1947; formed the basis of the Preamble.",
      "Drafting Committee: Appointed on 29 August 1947 under the chairmanship of Dr. B.R. Ambedkar ('Chief Architect of the Constitution'); 7 members (Ambedkar, N. Gopalaswami Ayyangar, Alladi Krishnaswamy Iyer, K.M. Munshi, Mohammad Saadulla, B.L. Mitter / N. Madhava Rau, D.P. Khaitan / T.T. Krishnamachari).",
      "Adoption & Commencement: Took 2 years, 11 months, and 18 days across 11 sessions; adopted on 26 November 1949 (celebrated as National Constitution Day); came into full legal effect on 26 January 1950 (Republic Day)."
    ],
    "mains": [
      "Examine the monumental challenge of princely state integration confronting India in 1947. How did Sardar Vallabhbhai Patel and V.P. Menon successfully prevent the Balkanization of the Indian subcontinent? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the constitutional crisis created by Section 7 of the Indian Independence Act 1947 declaring the lapse of British paramountcy, granting 565 princely rulers technical freedom to join either dominion or declare independence; assess Sardar Patel's diplomatic strategy of the 'Carrot and Stick': appealing to patriotism while pointing out the perils of isolation; analyze the three accession portfolios (Defence, External Affairs, Communications) via the Instrument of Accession; examine the complex resolution of Junagadh (plebiscite), Hyderabad (Operation Polo), and Kashmir (accession under invasion); conclude that Patel's statecraft unified 28% of India's population and 48% of its territory without large-scale bloodshed."
    ],
    "mcqs": [
      "Q1. Which civil servant served as the Secretary of the Ministry of States and worked in close partnership with Sardar Vallabhbhai Patel in negotiating the integration of 565 princely states?\n(a) V.P. Menon\n(b) B.N. Rau\n(c) H.M. Patel\n(d) G.S. Bajpai\nCorrect Answer: (a) V.P. Menon [Explanation: V.P. Menon, Secretary of the Ministry of States under Sardar Patel, drafted the Instrument of Accession and handled delicate diplomatic negotiations with princely rulers.]",
      "Q2. The military police action launched by the Indian Army in September 1948 to liberate and integrate the princely state of Hyderabad into the Indian Union was codenamed:\n(a) Operation Vijay\n(b) Operation Polo\n(c) Operation Cactus\n(d) Operation Blue Star\nCorrect Answer: (b) Operation Polo [Explanation: Operation Polo (13–18 September 1948) was the military action commanded by Maj. Gen. J.N. Chaudhuri that forced the surrender of Nizam Mir Osman Ali Khan and dismantled the Razakar militia.]",
      "Q3. Who served as the Constitutional Advisor to the Constituent Assembly, preparing the initial foundational draft of the Indian Constitution?\n(a) Dr. B.R. Ambedkar\n(b) Sir B.N. Rau\n(c) Alladi Krishnaswamy Iyer\n(d) K.M. Munshi\nCorrect Answer: (b) Sir B.N. Rau [Explanation: Sir Benegal Narsing Rau (B.N. Rau), eminent jurist and judge of the International Court of Justice, served as the Constitutional Advisor to the Constituent Assembly.]",
      "Q4. On which historic date was the Constitution of India formally adopted by the Constituent Assembly, celebrated annually across India as 'Samvidhan Diwas' (Constitution Day)?\n(a) 15 August 1947\n(b) 26 November 1949\n(c) 26 January 1950\n(d) 2 October 1950\nCorrect Answer: (b) 26 November 1949 [Explanation: The Constituent Assembly adopted the Constitution on 26 November 1949 (commemorated as National Constitution Day), while it came into full force on 26 January 1950.]",
      "Q5. The famous 'Objectives Resolution', which articulated the philosophy and guiding ideals of the Indian Republic and formed the Preamble, was moved in the Constituent Assembly by:\n(a) Dr. Rajendra Prasad\n(b) Jawaharlal Nehru\n(c) Dr. B.R. Ambedkar\n(d) Maulana Abul Kalam Azad\nCorrect Answer: (b) Jawaharlal Nehru [Explanation: Pandit Jawaharlal Nehru moved the historic Objectives Resolution on 13 December 1946, which was unanimously adopted on 22 January 1947 and shaped the Preamble.]"
    ]
  },
  {
    "id": "APPSC-G1-HIST-30",
    "filename": "30_post_independence_consolidation_and_states_reorganisation",
    "title": "Post-Independence Consolidation: Linguistic Reorganisation & Foreign Enclaves",
    "mapping": "History and Culture of India: Post-Independence India - Linguistic Reorganisation of States (Dhar Commission, JVP Committee, Potti Sreeramulu's Sacrifice, Creation of Andhra State 1953, States Reorganisation Act 1956), Integration of French and Portuguese Enclaves (Goa, Pondicherry).",
    "intro": "The post-independence consolidation of India required resolving deep regional, linguistic, and colonial anomalies. Following the supreme sacrifice of Amarajeevi Potti Sreeramulu in 1952, the creation of Andhra State (1953) catalyzed the nationwide linguistic reorganization of states under the Fazal Ali Commission (1956). Concurrently, diplomatic negotiations and military liberation (Operation Vijay in Goa) integrated remaining foreign enclaves of France and Portugal into the sovereign Indian Republic.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Potti_Sreeramulu.jpg", "caption": "Amarajeevi Potti Sreeramulu, whose 58-day fast unto death led to the creation of Andhra State in 1953.", "alt": "Potti Sreeramulu portrait"},
    "table": {
      "caption": "Evolutionary Commissions on Linguistic Reorganisation of States",
      "headers": ["Commission / Committee & Year", "Members / Composition", "Key Mandate & Recommendation", "Historical Outcome & Political Aftermath"],
      "rows": [
        ["Dhar Commission (June 1948)", "Justice S.K. Dhar (Chairman), J.N. Lal, Panna Lall.", "Examined feasibility of linguistic provinces; recommended reorganization strictly based on administrative convenience, financial viability, and geographical continuity, rejecting language as sole criterion.", "Sparked intense popular resentment in South India, especially in the Andhra and Maharashtra regions."],
        ["JVP Committee (December 1948)", "Jawaharlal Nehru, Vallabhbhai Patel, Pattabhi Sitaramayya (JVP).", "Re-examined linguistic demand; advised postponing linguistic states to prioritize national unity, security, and economic development, though conceded Andhra if non-contentious.", "Reaffirmed central reluctance, escalating public protests in Telugu-speaking districts of Madras Presidency."],
        ["Martyrdom of Potti Sreeramulu (1952)", "Amarajeevi Potti Sreeramulu (19 Oct – 15 Dec 1952).", "Embarked on a 58-day fast unto death in Madras demanding immediate separate Andhra State for Telugu people; died a martyr on 15 Dec 1952.", "Triggered massive civil unrest across coastal Andhra and Rayalaseema; PM Nehru announced creation of Andhra State on 19 Dec 1952; inaugurated at Kurnool on 1 Oct 1953 (First Linguistic State in India)."],
        ["States Reorganisation Commission (SRC, 1953)", "Justice Fazal Ali (Chairman), K.M. Panikkar, Hriday Nath Kunzru.", "Submitted report in 1955; accepted language as the predominant basis of state reorganization, while rejecting 'One Language, One State' dogma.", "Passed States Reorganisation Act 1956 (7th Constitutional Amendment); abolished Part A, B, C, D states; created 14 States and 6 Union Territories; Andhra State merged with Telangana to form Andhra Pradesh (1 Nov 1956)."],
        ["Integration of Foreign Enclaves (1954–1961)", "French Enclaves (Pondicherry, Karaikal, Mahe, Yanam); Portuguese (Goa, Daman, Diu, Dadra & Nagar Haveli).", "France transferred settlements de facto in Nov 1954 (de jure treaty 1956/1962); Portugal's dictator Salazar refused negotiations; Indian Armed Forces launched 'Operation Vijay' (18–19 Dec 1961).", "Goa, Daman, and Diu liberated from 451 years of Portuguese colonial rule, completing the territorial unification of India."]
      ]
    },
    "bullets": [
      "Classification of States in 1950 Constitution: Part A (9 former Governor's provinces), Part B (9 former large princely states under Rajpramukhs), Part C (10 former Chief Commissioner's provinces and small princely states), and Part D (Andaman and Nicobar Islands).",
      "7th Constitutional Amendment Act 1956: Implemented the SRC recommendations; repealed the four-fold classification, establishing a uniform constitutional structure for Indian states and Union Territories.",
      "Post-1956 State Reorganizations: Bifurcation of bilingual Bombay into Maharashtra and Gujarat (1960); creation of Nagaland (1963); Punjab reorganization into Punjab, Haryana, and UT Chandigarh (1966 under Shah Commission); Meghalaya, Manipur, and Tripura statehood (1972); Sikkim integration as 22nd state (1975, 36th Amendment); Goa statehood (1987); creation of Chhattisgarh, Uttarakhand, and Jharkhand (2000); and Andhra Pradesh bifurcation creating Telangana (2014).",
      "Foreign Enclaves: Dadra and Nagar Haveli liberated in 1954 by local nationalist volunteers; Pondicherry integrated via peaceful bilateral treaty; Operation Vijay in December 1961 conducted under Defence Minister V.K. Krishna Menon."
    ],
    "mains": [
      "Discuss the genesis, mandate, and recommendations of the States Reorganisation Commission (Fazal Ali Commission) of 1953. How did the creation of Andhra State in 1953 trigger the nationwide linguistic remapping of India? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Trace the historical background: resistance to linguistic provinces by Dhar and JVP committees; describe Amarajeevi Potti Sreeramulu's 58-day fast unto death and the subsequent popular uprising compelling Nehru to inaugurate Andhra State on 1 October 1953 as India's first linguistic state; analyze the domino effect: surging demands in Maharashtra, Gujarat, Karnataka, and Punjab leading to the appointment of the Fazal Ali Commission; detail the SRC recommendations: balancing linguistic affinity with national security, administrative cohesion, and economic viability; outline the States Reorganisation Act 1956 creating 14 states and 6 UTs."
    ],
    "mcqs": [
      "Q1. Which revered freedom fighter undertook a historic 58-day fast unto death, attaining martyrdom on 15 December 1952, which forced the creation of the first linguistic state of Andhra?\n(a) Tanguturi Prakasam Pantulu\n(b) Potti Sreeramulu\n(c) Konda Venkatappaiah\n(d) Bhogaraju Pattabhi Sitaramayya\nCorrect Answer: (b) Potti Sreeramulu [Explanation: Amarajeevi Potti Sreeramulu's 58-day fast unto death in Madras galvanized the Telugu people, compelling the Union government to carve out Andhra State in 1953.]",
      "Q2. The first linguistic state in independent India, Andhra State, was formally inaugurated on 1 October 1953 with its capital at which city?\n(a) Vijayawada\n(b) Kurnool\n(c) Visakhapatnam\n(d) Hyderabad\nCorrect Answer: (b) Kurnool [Explanation: Andhra State was inaugurated on 1 October 1953 with Kurnool as its capital and Tanguturi Prakasam Pantulu as its first Chief Minister.]",
      "Q3. Who served as the Chairman of the States Reorganisation Commission (SRC) appointed by the Government of India in December 1953?\n(a) Justice S.K. Dhar\n(b) Justice Fazal Ali\n(c) K.M. Panikkar\n(d) Hriday Nath Kunzru\nCorrect Answer: (b) Justice Fazal Ali [Explanation: Justice Fazal Ali headed the three-member States Reorganisation Commission, with eminent diplomat K.M. Panikkar and scholar H.N. Kunzru as members.]",
      "Q4. Which military action was launched by the Indian Armed Forces on 18–19 December 1961 to liberate Goa, Daman, and Diu from 451 years of Portuguese colonial rule?\n(a) Operation Polo\n(b) Operation Vijay\n(c) Operation Meghdoot\n(d) Operation Brasstacks\nCorrect Answer: (b) Operation Vijay [Explanation: Operation Vijay was the 36-hour military action executed in December 1961 that forced Portuguese Governor-General Manuel Vassalo e Silva to surrender Goa to India.]",
      "Q5. Which Constitutional Amendment Act implemented the recommendations of the States Reorganisation Commission, establishing 14 states and 6 Union Territories in 1956?\n(a) 1st Constitutional Amendment Act 1951\n(b) 7th Constitutional Amendment Act 1956\n(c) 12th Constitutional Amendment Act 1962\n(d) 24th Constitutional Amendment Act 1971\nCorrect Answer: (b) 7th Constitutional Amendment Act 1956 [Explanation: The 7th Constitutional Amendment Act of 1956 abolished the classification of Part A, B, C, D states and reorganized India into 14 States and 6 Union Territories.]"
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

print("Part 6 of Subject 1 generated successfully")
