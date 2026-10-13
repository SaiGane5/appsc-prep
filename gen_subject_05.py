import os, json, glob

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "05_Ethics_and_Law"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-ETH-01",
    "filename": "01_ethics_and_human_interface_essence_and_consequences",
    "title": "Ethics & Human Interface: Essence, Determinants & Ethical Dilemmas",
    "mapping": "Ethics and Law: Ethics and Human Interface - Essence, Determinants and Consequences of Ethics in Human Action; Dimensions of Ethics; Ethics in Private and Public Relationships; Human Values and Socialization (Family, Society, Educational Institutions).",
    "intro": "Ethics examines moral principles that guide human conduct, distinguishing right actions from wrong. Operating at the interface of human consciousness and social obligation, ethics evaluates human actions through intentions, means, and consequences. In public administration, ethical principles ensure that discretionary bureaucratic power serves the common good with fairness, integrity, and compassion.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Ethics_scales_justice.jpg", "caption": "The scales of justice, symbolizing the delicate balance between ethical principles and public duty.", "alt": "Scales of justice symbol of ethics"},
    "table": {
      "caption": "Major Western & Indian Ethical Frameworks",
      "headers": ["Ethical Framework", "Key Philosophers & Traditions", "Core Moral Criterion", "Application in Public Administration"],
      "rows": [
        ["Deontology (Duty Ethics)", "Immanuel Kant; Bhagavad Gita (Nishkama Karma).", "Inherent rightness of the action regardless of consequences; Categorical Imperative; duty for duty's sake.", "Adherence to rule of law, honesty, non-discrimination, refusing bribes regardless of outcomes."],
        ["Consequentialism / Utilitarianism", "Jeremy Bentham ('Quantitative'), John Stuart Mill ('Qualitative').", "Greatest happiness of the greatest number; cost-benefit calculus based on outcomes.", "Public policy design: allocating welfare funds, building infrastructure for maximum public benefit."],
        ["Virtue Ethics", "Aristotle (Nicomachean Ethics, Golden Mean); Confucius.", "Cultivation of moral character and inner virtues (temperance, courage, justice, wisdom, phronesis).", "Building administrative integrity, ethical habits, and moral resilience against institutional corruption."],
        ["Indian Ethos & Dharma", "Kautilya (Arthashastra), Mahatma Gandhi (Satya & Ahimsa), Ashoka.", "Dharma (righteous moral duty), Nishkama Karma (selfless action), Sarvodaya (welfare of all), Antyodaya.", "Empathetic civil service committed to serving the poorest citizen (Taliman test)."]
      ]
    },
    "bullets": [
      "Determinants of Ethics: Individual conscience, family upbringing, religious and cultural traditions, legal statutes and societal norms, peer groups and educational institutions.",
      "Ethics in Private vs Public Relationships: Private ethics is governed by emotional bonds, affection, and personal loyalty; Public ethics demands universal neutrality, strict non-partisanship, transparency, and loyalty to the Constitution.",
      "Mahatma Gandhi's Seven Social Sins (Young India, 1925): Politics without principles, Wealth without work, Pleasure without conscience, Knowledge without character, Commerce without morality, Science without humanity, and Worship without sacrifice.",
      "Gandhi's Talisman: 'Recall the face of the poorest and the weakest man whom you may have seen, and ask yourself if the step you contemplate is going to be of any use to him'."
    ],
    "mains": [
      "Explain the essence and determinants of ethics in human actions. How does Mahatma Gandhi's concept of 'Sarvodaya through Antyodaya' guide ethical decision-making in public administration? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define ethics as the normative study of moral values governing human choice; analyze determinants: conscience, legal codes, socio-cultural socialization, and peer culture; evaluate deontological (Kant) vs teleological (Mill) approaches; explain Gandhi's ethical framework: synthesis of moral means and moral ends ('Means are after all everything'); explain Sarvodaya (universal upliftment) realized through Antyodaya (uplifting the last person in the line); apply Gandhi's Talisman to administrative discretion: ensuring government policies prioritize vulnerable and marginalized citizens."
    ],
    "mcqs": [
      "Q1. Which philosophical ethical school, founded by Jeremy Bentham and J.S. Mill, evaluates the morality of an action solely on the basis of producing the 'greatest happiness for the greatest number'?\n(a) Deontological Ethics\n(b) Utilitarianism (Consequentialism)\n(c) Virtue Ethics\n(d) Intuitionism\nCorrect Answer: (b) Utilitarianism (Consequentialism) [Explanation: Utilitarianism holds that actions are morally right to the extent that they promote the greatest overall happiness and minimize pain for the largest number of people.]",
      "Q2. The concept of 'Categorical Imperative'—acting only according to that maxim whereby you can at the same time will that it should become a universal law—was formulated by:\n(a) Aristotle\n(b) Immanuel Kant\n(c) John Locke\n(d) Thomas Hobbes\nCorrect Answer: (b) Immanuel Kant [Explanation: Immanuel Kant formulated the Categorical Imperative as the foundational unconditional moral law of Deontology, demanding duty without exceptions.]",
      "Q3. In which publication did Mahatma Gandhi articulate his famous list of the 'Seven Social Sins' in 1925, including 'Commerce without morality' and 'Politics without principles'?\n(a) Harijan\n(b) Young India\n(c) Indian Opinion\n(d) Navajivan\nCorrect Answer: (b) Young India [Explanation: On 22 October 1925, Mahatma Gandhi published the 'Seven Social Sins' in his weekly journal 'Young India', highlighting moral rot in modern civilization.]",
      "Q4. In the philosophy of the Bhagavad Gita, the doctrine of performing one's prescribed moral duty with devotion without attachment to the fruits of action is termed:\n(a) Svadharma\n(b) Nishkama Karma\n(c) Purushartha\n(d) Samadhi\nCorrect Answer: (b) Nishkama Karma [Explanation: Nishkama Karma (selfless action without expectation of reward) is the central ethical doctrine of the Gita, urging duty dedicated to the higher good.]",
      "Q5. Which among the following is recognized as the ultimate internal subjective determinant of ethical judgment in human beings?\n(a) Positive law\n(b) Conscience (Antaratma)\n(c) Public opinion\n(d) Social sanctions\nCorrect Answer: (b) Conscience (Antaratma) [Explanation: Conscience is the supreme inner moral faculty that assesses the ethical quality of human thoughts and actions against intrinsic moral values.]"
    ]
  },
  {
    "id": "APPSC-G1-ETH-02",
    "filename": "02_human_values_attitude_and_moral_thinkers",
    "title": "Attitude, Moral Thinkers & Philosophical Traditions: Indian & Western",
    "mapping": "Ethics and Law: Moral Psychology & Philosophy - Attitude (Content, Structure, CAB Model, Moral & Political Attitudes), Social Influence and Persuasion, Western Moral Thinkers (Socrates, Plato, Aristotle, Kant, Rawls), Indian Moral Thinkers (Kautilya, Vivekananda, Aurobindo, Gandhi, Tagore).",
    "intro": "Attitudes represent psychological tendencies that shape how individuals perceive and respond to social realities, structured through the ABC/CAB model (Cognitive, Affective, Behavioral). In governance, public servants require progressive moral and political attitudes, cultivated through social influence and grounded in the profound moral philosophies of Western thinkers (Plato, Aristotle, Kant, Rawls) and Indian visionaries (Kautilya, Vivekananda, Gandhi, Tagore).",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Plato_Aristotle_Raphael.jpg", "caption": "Plato and Aristotle in Raphael's 'The School of Athens', contrasting idealism with empirical virtue ethics.", "alt": "School of Athens fresco detail Plato and Aristotle"},
    "table": {
      "caption": "Contributions of Eminent Moral Thinkers to Governance Ethics",
      "headers": ["Philosopher & Tradition", "Core Philosophical Concept", "Ethical Doctrine & Treatise", "Administrative Relevance"],
      "rows": [
        ["Socrates (Ancient Greece)", "Intellectualism ('Virtue is Knowledge').", "Unexamined life is not worth living; Socratic questioning.", "Critical thinking, resisting bureaucratic groupthink, standing by truth despite pressure."],
        ["Plato (The Republic)", "Four Cardinal Virtues (Wisdom, Courage, Temperance, Justice).", "Concept of the Philosopher King; harmonious division of society.", "Meritocratic public leadership; rational policymaking; harmony among social classes."],
        ["John Rawls (Modern Western)", "Justice as Fairness; Theory of Justice (1971).", "Original Position behind the 'Veil of Ignorance'; Difference Principle (inequalities justified only if benefiting least advantaged).", "Justification for affirmative action (reservations), progressive taxation, and welfare schemes for marginalized citizens."],
        ["Swami Vivekananda (Modern Indian)", "Practical Vedanta & Self-Confidence.", "'Arise, awake, and stop not till the goal is reached'; service to Jiva is worship of Shiva.", "Dedicated youth leadership, compassion for the downtrodden, work as spiritual worship."],
        ["Rabindranath Tagore (Universal Humanism)", "Universal humanism, creative freedom.", "'Where the mind is without fear'; rejected xenophobic chauvinism.", "Cultural tolerance, empathy, holistic educational development."]
      ]
    },
    "bullets": [
      "The CAB Model of Attitude: Cognitive (beliefs, knowledge, facts), Affective (emotions, feelings), and Behavioral (tendency to act).",
      "Persuasion and Social Influence: Techniques used by administrators to alter harmful public behaviors (Swachh Bharat Abhiyan, pulse polio campaigns, helmet/seatbelt drives) via credible communicators, emotional framing, and social proof.",
      "Moral vs Political Attitudes: Moral attitudes are grounded in deep moral convictions (e.g. anti-corruption, gender equality, vegetarianism); Political attitudes determine political beliefs on nationalism, democracy, state welfarism, and social justice.",
      "Kautilya's Arthashastra on Administrative Ethics: 'In the happiness of his subjects lies the king's happiness; in their welfare his welfare; whatever pleases himself he shall not consider as good, but whatever pleases his subjects he shall consider as good'."
    ],
    "mains": [
      "Explain John Rawls' concept of the 'Veil of Ignorance' and the 'Difference Principle'. How does Rawlsian justice justify state affirmative action and welfare programs in India? (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Explain the thought experiment of the 'Original Position' where rational individuals decide principles of justice behind a 'Veil of Ignorance' (blind to their future caste, class, gender, intelligence, or wealth); evaluate the two principles derived: 1. Equal basic liberties for all, 2. Social and economic inequalities must satisfy the Difference Principle (arranged to the greatest benefit of the least advantaged members of society); demonstrate application to the Indian welfare state: justifying constitutional reservations (Articles 15(4), 16(4)), subsidized food grains (NFSA), progressive taxation, and free healthcare as morally obligatory instruments to elevate the least privileged."
    ],
    "mcqs": [
      "Q1. In social psychology, what does the 'CAB Model' of attitude structure specifically stand for?\n(a) Conscience, Action, Belief\n(b) Cognitive, Affective, Behavioral\n(c) Character, Attitude, Behavior\n(d) Competence, Aptitude, Benevolence\nCorrect Answer: (b) Cognitive, Affective, Behavioral [Explanation: The CAB (or ABC) model posits that attitudes comprise Cognitive (beliefs), Affective (feelings), and Behavioral (action tendencies) components.]",
      "Q2. The thought experiment of the 'Veil of Ignorance' to derive principles of distributive justice was formulated by which 20th-century political philosopher?\n(a) Robert Nozick\n(b) John Rawls\n(c) Michael Sandel\n(d) Amartya Sen\nCorrect Answer: (b) John Rawls [Explanation: John Rawls introduced the 'Veil of Ignorance' in his masterwork 'A Theory of Justice' (1971) to ensure impartial selection of fair social principles.]",
      "Q3. Which four Cardinal Virtues were identified by Plato in 'The Republic' as essential for the moral health of the individual and the ideal state?\n(a) Faith, Hope, Charity, Love\n(b) Wisdom, Courage, Temperance, Justice\n(c) Truth, Non-violence, Celibacy, Simplicity\n(d) Liberty, Equality, Fraternity, Dignity\nCorrect Answer: (b) Wisdom, Courage, Temperance, Justice [Explanation: Plato's four cardinal virtues are Prudence/Wisdom (Sophrosyne), Courage (Andreia), Temperance (Temperantia), and Justice (Dikaiosyne).]",
      "Q4. Who famously articulated the ideal of administrative statecraft stating: 'In the happiness of his subjects lies his happiness; in their welfare his welfare'?\n(a) Ashoka\n(b) Kautilya (Chanakya)\n(c) Tiruvalluvar\n(d) Manu\nCorrect Answer: (b) Kautilya (Chanakya) [Explanation: In the Arthashastra, Kautilya instructs the monarch that royal interest is subservient to public welfare ('Prajasukhe sukham rajnah').]",
      "Q5. The successful nationwide behavior-change campaign of 'Swachh Bharat Mission' utilized which psychological principle to eliminate open defecation?\n(a) Coercive penal taxation\n(b) Persuasion, community nudging, and social proof\n(c) Subsidized commercial advertising\n(d) Mandatory legal injunctions\nCorrect Answer: (b) Persuasion, community nudging, and social proof [Explanation: Swachh Bharat achieved mass behavior change through participatory social nudging, trigger mechanisms by Swachhagrahis, and emotional persuasion.]"
    ]
  },
  {
    "id": "APPSC-G1-ETH-03",
    "filename": "03_emotional_intelligence_concepts_and_administrative_utility",
    "title": "Emotional Intelligence: Dimensions, Utilities & Administrative Applications",
    "mapping": "Ethics and Law: Emotional Intelligence - Concept of Emotional Intelligence, Daniel Goleman's Five Dimensions, Utilities and Application in Administration and Governance, Stress Management and Conflict Resolution.",
    "intro": "Emotional Intelligence (EI) is the ability to perceive, evaluate, control, and channel emotions in oneself and in others. Popularized by Daniel Goleman, EI is recognized as a more potent predictor of public administrative success than raw cognitive intelligence (IQ). In public service, high emotional quotient enables civil servants to manage high-stress crises, maintain empathy for citizens, and lead teams through collaborative dispute resolution.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Empathy_listening.jpg", "caption": "Empathetic communication, the bedrock of citizen-centric public administration.", "alt": "Empathetic listening and counseling"},
    "table": {
      "caption": "Daniel Goleman's Five Dimensions of Emotional Intelligence",
      "headers": ["EI Dimension", "Psychological Definition", "Key Personal Attributes", "Application in Civil Services & Governance"],
      "rows": [
        ["Self-Awareness", "Recognizing and understanding one's own emotions, moods, triggers, and values.", "Emotional self-awareness, accurate self-assessment, self-confidence.", "Knowing personal biases and emotional weaknesses; preventing ego clashes during policy debates."],
        ["Self-Regulation", "Controlling or redirecting disruptive emotions and impulsive reactions.", "Integrity, adaptability, conscientiousness, emotional composure under pressure.", "Maintaining calm during violent mob protests, hostile media scrutiny, or political intimidation."],
        ["Motivation (Intrinsic)", "Passion for public service beyond money, status, or external rewards.", "Drive for excellence, resilience, optimism in the face of setbacks.", "Remaining dedicated to public welfare in remote rural postings despite poor infrastructure."],
        ["Empathy", "Understanding the emotional makeup of other people; walking in another's shoes.", "Active listening, sensitivity to cultural/gender diversity, perspective taking.", "Treating poor petitioners with dignity; designing disability-friendly and gender-sensitive welfare schemes."],
        ["Social Skills", "Managing relationships to move people in the desired direction; building networks.", "Conflict management, collaborative leadership, persuasive communication.", "Negotiating with strike leaders, inter-departmental coordination during disaster relief."]
      ]
    },
    "bullets": [
      "IQ vs EQ in Civil Services: While IQ gets an officer recruited into the civil service (analytical ability, technical law), EQ determines whether the officer succeeds as an empathetic, collaborative, and crisis-resilient district administrator.",
      "Crisis Management Applications: During natural disasters (cyclones, floods) and communal riots, emotionally intelligent officers manage collective panic, project calm authority, and build public trust.",
      "Workplace Burnout & Stress: Civil servants face round-the-clock political demands, long hours, and media trials; emotional intelligence fosters psychological hardiness, preventing burnout, cynicism, and depression.",
      "Techniques to Enhance EI: Mindful meditation (Vipassana), active listening training, 360-degree feedback, emotional journaling, and empathetic simulation exercises."
    ],
    "mains": [
      "Discuss Daniel Goleman's five dimensions of Emotional Intelligence. Illustrate how an emotionally intelligent District Magistrate can handle a volatile communal riot and resolve public strikes effectively. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Define EI (Peter Salovey, John Mayer, Daniel Goleman); detail Goleman's five domains: Self-Awareness, Self-Regulation, Intrinsic Motivation, Empathy, and Social Skills; illustrate riot management: Self-Regulation preventing panic or hasty lethal action; Empathy in understanding religious grievances without taking sides; Social Skills communicating with community elders through Peace Committees to calm rumors; illustrate labor strike resolution: Active listening to workers' wage demands, persuasive negotiation bringing management to arbitration, and maintaining composure under provocative slogans."
    ],
    "mcqs": [
      "Q1. Who authored the bestselling book 'Emotional Intelligence: Why It Can Matter More Than IQ' (1995), popularizing the modern five-domain framework of EI?\n(a) Howard Gardner\n(b) Daniel Goleman\n(c) Peter Salovey\n(d) John Mayer\nCorrect Answer: (b) Daniel Goleman [Explanation: Psychologist Daniel Goleman popularized Emotional Intelligence in 1995, outlining the five core competencies of self-awareness, self-regulation, motivation, empathy, and social skill.]",
      "Q2. The ability to control impulsive reactions, suspend hasty judgments, and remain composed during high-stress crises corresponds to which dimension of EI?\n(a) Self-Awareness\n(b) Self-Regulation\n(c) Empathy\n(d) Extrinsic Motivation\nCorrect Answer: (b) Self-Regulation [Explanation: Self-regulation involves managing disruptive emotional impulses, maintaining composure, and acting rationally rather than reactively during crises.]",
      "Q3. In psychological theory, which pioneer developed the 'Theory of Multiple Intelligences', recognizing Interpersonal and Intrapersonal intelligences?\n(a) Howard Gardner\n(b) Alfred Binet\n(c) Jean Piaget\n(d) Robert Sternberg\nCorrect Answer: (a) Howard Gardner [Explanation: Howard Gardner formulated the Theory of Multiple Intelligences in 1983, identifying Interpersonal and Intrapersonal capacities as distinct intelligences.]",
      "Q4. Which vital emotional attribute enables an administrator to accurately gauge public distress and design compassionate, citizen-centric welfare policies?\n(a) Cognitive Dissonance\n(b) Empathy\n(c) Authority\n(d) Dogmatism\nCorrect Answer: (b) Empathy [Explanation: Empathy—the capacity to understand and share the feelings of citizens—is the psychological foundation of compassionate and inclusive governance.]",
      "Q5. Which technique is widely recommended for civil servants to cultivate emotional stability, self-awareness, and psychological stress resilience?\n(a) Groupthink exercises\n(b) Vipassana and Mindfulness meditation\n(c) Authoritarian leadership training\n(d) Defensive rationalization\nCorrect Answer: (b) Vipassana and Mindfulness meditation [Explanation: Mindfulness and Vipassana meditation are empirically proven to enhance emotional regulation, impulse control, and psychological resilience in administrators.]"
    ]
  },
  {
    "id": "APPSC-G1-ETH-04",
    "filename": "04_public_service_values_and_ethics_in_administration",
    "title": "Public Service Values & Ethics in Administration: Dilemmas & Codes",
    "mapping": "Ethics and Law: Administrative Ethics - Status and Problems, Ethical Dilemmas in Governance, Laws, Rules and Conscience as Sources of Ethical Guidance, Accountability, Nolan Committee Principles, Codes of Conduct vs Codes of Ethics.",
    "intro": "Public service ethics defines the moral obligations, institutional integrity, and fiduciary duty of civil servants toward the republic. Public administrators constantly confront ethical dilemmas—reconciling administrative secrecy with public transparency, political loyalty with bureaucratic neutrality, and utilitarian development with human rights. Resolving these challenges requires internalizing core public service values, formalized in the Nolan Principles and enforceable civil service codes.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Nolan_principles.png", "caption": "The Seven Principles of Public Life formulated by the Nolan Committee (1995).", "alt": "Seven Principles of Public Life diagram"},
    "table": {
      "caption": "The Seven Principles of Public Life (Nolan Committee Standards, 1995)",
      "headers": ["Nolan Principle", "Ethical Definition", "Administrative Context & Behavior", "Violations / Breaches"],
      "rows": [
        ["1. Selflessness", "Holders of public office should act solely in terms of the public interest.", "Never taking decisions to gain financial or material benefits for self, family, or friends.", "Crony capitalism, nepotism in recruitment."],
        ["2. Integrity", "Avoid placing oneself under financial or other obligation to outside individuals/organizations.", "Refusing gifts, hospitality, or post-retirement corporate favors that might compromise official duty.", "Accepting kickbacks, post-retirement quid pro quo."],
        ["3. Objectivity", "Decisions must be taken impartially, fairly, and on merit without discrimination.", "Allocating contracts, tenders, and subsidies using clear, transparent, objective criteria.", "Favoritism, regional bias, political partisanship."],
        ["4. Accountability", "Holders of public office are accountable for their decisions to the public.", "Submitting to whatever scrutiny is appropriate to their office (CAG, PAC, RTI, media).", "Evasion of audit queries, shredding official records."],
        ["5. Openness", "Act and take decisions in an open and transparent manner.", "Giving reasons for decisions and restricting information only when the wider public interest clearly demands.", "Excessive classification of documents under Official Secrets Act."],
        ["6. Honesty", "Duty to declare any private interests relating to public duties.", "Resolving any conflict of interest immediately in a way that protects the public interest.", "Concealing shares in companies bidding for department tenders."],
        ["7. Leadership", "Exhibit and support these principles by leadership and personal example.", "Leading by personal ethical conduct; fostering an organizational culture of zero tolerance for corruption.", "Turning a blind eye to institutional malpractice."]
      ]
    },
    "bullets": [
      "Code of Conduct vs Code of Ethics: A Code of Ethics is a broad statement of philosophical values and aspirations (integrity, empathy, dedication); A Code of Conduct is a legally enforceable, specific set of behavioral dos and don'ts (bar on accepting expensive gifts, bar on political canvassing under Central Civil Services Conduct Rules 1964).",
      "Sources of Ethical Guidance: 1. Positive Laws, Acts and Statutory Regulations; 2. Institutional Rules and Precedents; 3. Conscience and Moral Intuition (Antaratma) when laws are silent or ambiguous.",
      "Civil Service Neutrality & Anonymity: Neutrality requires civil servants to execute policy loyally regardless of the political party in power; Anonymity (Masterman Committee) ensures ministers take parliamentary praise or blame while civil servants work behind the scenes.",
      "Conflict of Interest: Situations where personal pecuniary or familial interests clash with official duties; resolved through transparent recusal, blind trusts, and mandatory asset declarations."
    ],
    "mains": [
      "Analyze the Seven Principles of Public Life formulated by the Nolan Committee. Examine the classic ethical dilemmas confronted by civil servants in balancing political neutrality with executive compliance. (APPSC Group-1 Mains, 10 Marks)\n-> Model Approach: Detail the Nolan Committee (1995) principles: Selflessness, Integrity, Objectivity, Accountability, Openness, Honesty, Leadership; analyze classic ethical dilemmas in governance: 1. Discretion vs Rule-bound compliance (letter of the law vs spirit of justice), 2. Secrecy vs Transparency (whistleblowing vs Official Secrets Act), 3. Political Neutrality vs Committed Bureaucracy (resisting illegal verbal orders from political bosses vs risk of punitive transfer); propose institutional safeguards: statutory Civil Services Boards protecting tenure, recording verbal orders in writing per Supreme Court guidelines (T.S.R. Subramanian 2013), and creating independent ethics commissioners."
    ],
    "mcqs": [
      "Q1. Which historic committee in the United Kingdom formulated the celebrated 'Seven Principles of Public Life' (including Selflessness and Integrity) in 1995?\n(a) Masterman Committee\n(b) Nolan Committee (Committee on Standards in Public Life)\n(c) Fulton Committee\n(d) Northcote-Trevelyan Committee\nCorrect Answer: (b) Nolan Committee (Committee on Standards in Public Life) [Explanation: Chaired by Lord Nolan, the Committee on Standards in Public Life (1995) established the seven foundational ethical principles for holders of public office.]",
      "Q2. The administrative convention of 'Civil Service Anonymity', where the minister takes parliamentary responsibility while officials work behind the scenes, is rooted in the:\n(a) Westminster Model\n(b) Presidential System\n(c) French Prefect System\n(d) Soviet Nomenklatura\nCorrect Answer: (a) Westminster Model [Explanation: The British Westminster parliamentary system institutionalized civil service neutrality and anonymity to safeguard civil servants from political targeting.]",
      "Q3. In which landmark 2013 judgment did the Supreme Court mandate fixed tenures for civil servants and require all oral administrative orders to be recorded in writing?\n(a) Prakash Singh Case\n(b) T.S.R. Subramanian v. Union of India\n(c) Vineet Narain Case\n(d) Lily Thomas Case\nCorrect Answer: (b) T.S.R. Subramanian v. Union of India [Explanation: In T.S.R. Subramanian (2013), the Supreme Court directed the Centre and States to set up Civil Services Boards and mandated that all verbal directions must be recorded in writing.]",
      "Q4. What is the fundamental difference between a 'Code of Ethics' and a 'Code of Conduct' in public administration?\n(a) Code of Ethics is legally enforceable while Code of Conduct is voluntary\n(b) Code of Ethics outlines broad aspirational values while Code of Conduct specifies enforceable behavioral rules\n(c) Code of Conduct applies only to ministers while Code of Ethics applies to judges\n(d) There is no legal or conceptual difference\nCorrect Answer: (b) Code of Ethics outlines broad aspirational values while Code of Conduct specifies enforceable behavioral rules [Explanation: A Code of Ethics provides normative aspirational principles (e.g. empathy, justice), whereas a Code of Conduct details specific enforceable rules (e.g. gift limits).]",
      "Q5. When a public official's private personal, familial, or financial interests clash with their official public duties, this ethical dilemma is termed:\n(a) Moral Dissonance\n(b) Conflict of Interest\n(c) Bureaucratic Inertia\n(d) Arbitrary Discretion\nCorrect Answer: (b) Conflict of Interest [Explanation: Conflict of interest occurs when an official's personal interest threatens the objectivity or impartiality of public decision-making, requiring recusal.]"
    ]
  }
]

for t in topics:
  data = {
    "topic_id": t["id"],
    "subject_code": FOLDER,
    "subject_title": "Ethics and Law",
    "paper": "Mains Paper-III (Section B) & Screening Paper-I (Section D)",
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

print("Part 1 of Subject 5 generated successfully")
