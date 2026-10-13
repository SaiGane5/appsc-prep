import os, json

BASE_DIR = "/Users/imandisaiganesh/Documents/appsc"
FOLDER = "06_Economy_India_and_AP"
SUBJ_DIR = os.path.join(BASE_DIR, FOLDER)
os.makedirs(SUBJ_DIR, exist_ok=True)

topics = [
  {
    "id": "APPSC-G1-ECO-01",
    "filename": "01_structure_and_growth_trends_of_indian_economy",
    "title": "Structure & Growth Trends of the Indian Economy",
    "mapping": "Economy - India & AP: National Income Accounting, Gross Domestic Product (GDP), Gross Value Added (GVA), Sectoral Composition (Primary, Secondary, Tertiary), Structural Transformation, Pre and Post-1991 Growth Trajectories, and Demographic Dividend.",
    "intro": "The Indian economy has undergone profound structural transformation from an agrarian-dominated post-independence framework to a dynamic, services-driven global major. National income accounting utilizes Gross Value Added (GVA) at basic prices and Gross Domestic Product (GDP) at market prices (base year 2011-12) to assess macroeconomic vitality. While the tertiary sector now drives over 54% of gross output, agriculture continues to absorb nearly 45% of the total labor force—signaling persistent structural dualism and the imperative to leverage India's demographic dividend.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e4/India_GDP_Sector_Share.svg", "caption": "Sectoral share of India's Gross Value Added (GVA) across agriculture, industry, and services sectors.", "alt": "India GVA sectoral share"},
    "table": {
      "caption": "Macroeconomic Sectoral Share & Employment Transitions in India",
      "headers": ["Economic Sector", "GVA Contribution (~2023-24)", "Workforce Share (PLFS 2023-24)", "Structural Role & Key Growth Catalysts"],
      "rows": [
        ["Agriculture & Allied (Primary)", "17.7%", "46.1%", "Food security, rural livelihood cushion; high disguised unemployment"],
        ["Industry & Manufacturing (Secondary)", "28.3%", "25.0%", "Value addition, export capacity; targeted by Make in India & PLI"],
        ["Services (Tertiary)", "54.0%", "28.9%", "IT-BPM, financial services, logistics, tourism; primary GDP growth engine"],
        ["National Aggregate (GDP/Total)", "100.0%", "100.0%", "Targeting $5 Trillion economy; 6.5–7.5% medium-term trend growth rate"]
      ]
    },
    "points": [
      "National Income Accounting Transition: In 2015, the Central Statistics Office (CSO, now NSO under MoSPI) revised the base year from 2004-05 to 2011-12, shifting headline growth measurement from GDP at factor cost to GDP at market prices (GDP = GVA at basic prices + Product Taxes - Product Subsidies).",
      "Structural Transformation Anomalies: Unlike East Asian economies that transitioned linearly from agriculture to manufacturing and then services, India bypassed manufacturing dominance, transitioning directly from agriculture into service sector expansion, leaving industrial labor absorption relatively constrained.",
      "Demographic Dividend Window: India's median age is ~28.4 years, with over 65% of the population in the working-age bracket (15–59 years). Maximizing this demographic window (projected until 2047) necessitates dramatic enhancements in vocational skilling, female labor force participation (FLFPR), and labor-intensive manufacturing.",
      "Post-1991 Reform Trajectory: The transition from the 'Hindu rate of growth' (~3.5% pre-1980s) to 7%+ post-LPG reforms reflected the elimination of the License Raj, reduction in industrial tariffs, devaluation and convertibility on the current account, and foreign capital liberalization.",
      "Viksit Bharat @ 2047 Roadmap: Envisions India scaling from a $3.75 trillion lower-middle-income economy to a high-income developed country ($30+ trillion GDP) through infrastructure acceleration, technological adoption, and green energy transition."
    ],
    "mains": [
      "Analyze the structural changes in the Indian economy since the 1991 economic reforms. Why has the transition of workforce from agriculture to manufacturing remained sluggish despite sustained GDP growth? (250 Words, 15 Marks)",
      "Discuss the concept of 'Demographic Dividend' in India. What policy interventions are critical to prevent this demographic opportunity from turning into a demographic liability? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO01-01",
        "q": "Under the revised National Income accounting methodology adopted by NSO in 2015, headline GDP is measured at which metric?",
        "options": ["GDP at Factor Cost", "GDP at Market Prices", "Net National Product at Factor Cost", "GVA at Producer Prices"],
        "ans": "b",
        "explanation": "Since the January 2015 revision (with base year 2011-12), India's headline GDP growth is officially measured as GDP at Market Prices, which incorporates Net Product Taxes (Product Taxes minus Product Subsidies) onto Gross Value Added (GVA) at basic prices."
      },
      {
        "id": "MCQ-ECO01-02",
        "q": "Which sector currently accounts for the largest share of India's Gross Value Added (GVA)?",
        "options": ["Agriculture and Allied Activities", "Manufacturing and Construction", "Services Sector", "Mining and Quarrying"],
        "ans": "c",
        "explanation": "The services sector (tertiary sector) constitutes the largest share of India's GVA, contributing approximately 54% of total gross value added."
      },
      {
        "id": "MCQ-ECO01-03",
        "q": "The famous phrase 'Hindu Rate of Growth' was coined by which economist to describe the ~3.5% annual growth rate of the Indian economy prior to the 1980s?",
        "options": ["Amartya Sen", "Raj Krishna", "Jagdish Bhagwati", "Manmohan Singh"],
        "ans": "b",
        "explanation": "Economist Raj Krishna coined the term 'Hindu Rate of Growth' in 1978 to characterize the sluggish 3.5% annual GDP growth rate experienced by India from the 1950s through the 1970s."
      },
      {
        "id": "MCQ-ECO01-04",
        "q": "In National Income accounting, Net National Product (NNP) at Factor Cost is identically equivalent to which aggregate?",
        "options": ["Gross National Disposable Income", "National Income", "Personal Income", "Private Income"],
        "ans": "b",
        "explanation": "In macroeconomics and national accounts, 'National Income' strictly refers to Net National Product at Factor Cost (NNP at FC)."
      },
      {
        "id": "MCQ-ECO01-05",
        "q": "According to the Periodic Labour Force Survey (PLFS), approximately what percentage of India's total workforce remains employed in the agriculture and allied sector?",
        "options": ["25%", "35%", "45% to 46%", "60%"],
        "ans": "c",
        "explanation": "PLFS data indicates that agriculture and allied activities employ roughly 45% to 46% of the country's total employed workforce, demonstrating significant employment dependence relative to its ~18% GDP contribution."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-02",
    "filename": "02_monetary_policy_rbi_and_banking_sector_reforms",
    "title": "Monetary Policy, RBI & Banking Sector Reforms",
    "mapping": "Economy - India & AP: Reserve Bank of India (RBI Act 1934), Monetary Policy Framework Agreement, Monetary Policy Committee (MPC), Inflation Targeting, Liquidity Management (Repo, Reverse Repo, SDF, CRR, SLR), Banking Reforms (Insolvency and Bankruptcy Code 2016, Asset Quality Review, Prompt Corrective Action).",
    "intro": "The Reserve Bank of India (RBI) exercises regulatory stewardship over India's monetary and financial system. Under the amended RBI Act 1934, monetary governance is anchored by the Flexible Inflation Targeting (FIT) regime, where a six-member Monetary Policy Committee (MPC) sets policy interest rates to maintain consumer price index (CPI) headline inflation at 4% within a +/-2% tolerance band while supporting sustainable economic growth.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/3/37/Reserve_Bank_of_India_Mumbai.jpg", "caption": "The Reserve Bank of India headquarters in Mumbai, the apex regulator of India's monetary and financial systems.", "alt": "Reserve Bank of India Mumbai"},
    "table": {
      "caption": "RBI Monetary Policy Instruments & Transmission Mechanisms",
      "headers": ["Policy Instrument", "Mechanism / Formula", "Current Operational Role", "Impact on Macroeconomic Liquidity"],
      "rows": [
        ["Policy Repo Rate", "Rate at which RBI lends short-term funds against govt collateral", "Anchor policy rate decided bi-monthly by the MPC", "Directly anchors commercial bank lending and deposit interest rates"],
        ["Standing Deposit Facility (SDF)", "Overnight deposit absorption without requiring collateral", "Floor of the Liquidity Adjustment Facility (LAF) corridor", "Absorbs excess banking liquidity without straining RBI sovereign bond holdings"],
        ["Marginal Standing Facility (MSF)", "Penal overnight borrowing rate (Repo + 25 bps)", "Ceiling of the LAF interest rate corridor", "Safety valve for acute overnight commercial bank liquidity shortfalls"],
        ["Cash Reserve Ratio (CRR)", "Mandatory non-interest-bearing cash reserve held with RBI", "Quantitative reserve requirement (typically 4.5%)", "Controls systemic high-powered money supply and credit creation capacity"],
        ["Statutory Liquidity Ratio (SLR)", "Percentage of NDTL invested in approved liquid assets (G-Secs)", "Prudential liquidity cushion (typically 18%)", "Ensures bank solvency while securing captive demand for government bonds"]
      ]
    },
    "points": [
      "Monetary Policy Committee (MPC) Structure: Established under Section 45ZB of the amended RBI Act 1934. Consists of 6 members: 3 from the RBI (Governor as ex-officio Chairperson, Deputy Governor in charge of monetary policy, and one officer) and 3 external experts appointed by the Central Government for a 4-year term. Decisions are taken by majority vote, with the Governor holding a casting vote in ties.",
      "Flexible Inflation Targeting (FIT): Mandates maintaining Headline CPI inflation at 4% with a tolerance band of 2% to 6%. Failure to maintain inflation target is defined as average inflation breaching the band for three consecutive quarters, requiring a formal explanatory report to Parliament.",
      "Banking Sector Asset Quality Overhaul: The 2015 Asset Quality Review (AQR) forced banks to recognize legacy non-performing assets (NPAs), ending regulatory forbearance. Gross NPAs peaked at 11.2% in 2018 before dropping below 3% by 2024 through resolution, recapitalization, and write-offs.",
      "Insolvency and Bankruptcy Code (IBC 2016): Introduced a creditor-in-control model replacing the debtor-in-possession regime. Adjudicated by National Company Law Tribunal (NCLT), IBC enforces a time-bound resolution window (180 days + 90-day extension) to prevent asset stripping.",
      "Prompt Corrective Action (PCA) Framework & Bad Bank (NARCL): PCA places restriction triggers on capital, asset quality, and leverage to prevent bank insolvencies. The National Asset Reconstruction Company Limited (NARCL) acts as the state-backed 'Bad Bank' aggregating and resolving stressed commercial loans exceeding Rs 500 crore."
    ],
    "mains": [
      "Evaluate the institutional effectiveness of the Monetary Policy Committee (MPC) and the Flexible Inflation Targeting framework in stabilizing macroeconomic volatility in India. (250 Words, 15 Marks)",
      "Discuss how the Insolvency and Bankruptcy Code (IBC 2016) has reshaped the credit culture and resolved the 'Twin Balance Sheet' crisis in India's banking and corporate sectors. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO02-01",
        "q": "Under the Flexible Inflation Targeting (FIT) framework in India, what is the statutory target for Consumer Price Index (CPI) inflation?",
        "options": ["3% with +/- 1% band", "4% with +/- 2% band (2% to 6%)", "5% with +/- 2% band", "6% flat target"],
        "ans": "b",
        "explanation": "Under the Monetary Policy Framework Agreement formalized in 2015 and notified under the RBI Act, the target for CPI headline inflation is 4% with an upper tolerance limit of 6% and a lower tolerance limit of 2%."
      },
      {
        "id": "MCQ-ECO02-02",
        "q": "How many total members constitute the Monetary Policy Committee (MPC) of the Reserve Bank of India?",
        "options": ["5 members", "6 members", "7 members", "9 members"],
        "ans": "b",
        "explanation": "The MPC consists of 6 members: the RBI Governor (Chairperson), Deputy Governor in charge of monetary policy, one nominated RBI official, and three independent external experts appointed by the Central Government."
      },
      {
        "id": "MCQ-ECO02-03",
        "q": "Which facility was introduced by RBI in 2022 as the new non-collateralized floor of the Liquidity Adjustment Facility (LAF) corridor?",
        "options": ["Reverse Repo Rate", "Standing Deposit Facility (SDF)", "Marginal Standing Facility (MSF)", "Bank Rate"],
        "ans": "b",
        "explanation": "In April 2022, RBI operationalized the Standing Deposit Facility (SDF) at 25 bps below the policy repo rate as the uncollateralized floor of the LAF corridor, replacing the fixed reverse repo rate."
      },
      {
        "id": "MCQ-ECO02-04",
        "q": "Under the Insolvency and Bankruptcy Code (IBC) 2016, which authority serves as the Adjudicating Authority for corporate insolvency resolution processes?",
        "options": ["Debt Recovery Tribunal (DRT)", "National Company Law Tribunal (NCLT)", "High Court of the respective state", "Serious Fraud Investigation Office (SFIO)"],
        "ans": "b",
        "explanation": "The National Company Law Tribunal (NCLT) is the designated Adjudicating Authority for Corporate Insolvency Resolution Processes (CIRP) and liquidation of corporate persons under the IBC 2016."
      },
      {
        "id": "MCQ-ECO02-05",
        "q": "When is the Reserve Bank of India considered to have failed in meeting the statutory inflation target under the RBI Act 1934?",
        "options": ["When inflation exceeds 6% in any single month", "When average inflation remains outside the 2%–6% band for two consecutive quarters", "When average inflation remains outside the 2%–6% band for three consecutive quarters", "When GDP growth drops below 4%"],
        "ans": "c",
        "explanation": "Under Regulation 7 of the RBI Monetary Policy Committee Regulations, the RBI is deemed to have failed in maintaining the inflation target if the average headline CPI inflation is above the upper tolerance level of 6% or below 2% for any three consecutive quarters."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-03",
    "filename": "03_fiscal_policy_public_debt_and_frbm_act",
    "title": "Fiscal Policy, Public Debt & FRBM Framework",
    "mapping": "Economy - India & AP: Fiscal Policy Objectives, Revenue vs Capital Expenditure, Fiscal Deficit, Revenue Deficit, Primary Deficit, Public Debt Sustainability, FRBM Act 2003, N.K. Singh Committee Recommendations, and Post-Pandemic Fiscal Glide Path.",
    "intro": "Fiscal policy represents the government's strategic utilization of taxation, public borrowing, and expenditure to promote economic growth, ensure income redistribution, and maintain macroeconomic stability. In India, fiscal discipline has historically been guided by the Fiscal Responsibility and Budget Management (FRBM) Act 2003. Managing the trade-off between growth-inducing capital investments and fiscal consolidation remains central to India's sovereign debt sustainability.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/North_Block_New_Delhi_Ministry_of_Finance.jpg", "caption": "North Block in New Delhi, housing the Union Ministry of Finance responsible for formulating India's fiscal policy and Union Budget.", "alt": "Ministry of Finance North Block"},
    "table": {
      "caption": "Key Deficit Concepts & Formulas in Indian Public Finance",
      "headers": ["Deficit Measure", "Mathematical Definition / Formula", "Economic Significance & Implications"],
      "rows": [
        ["Revenue Deficit (RD)", "Revenue Expenditure - Revenue Receipts", "Measures government borrowing used to fund recurring non-asset-creating consumption"],
        ["Effective Revenue Deficit (ERD)", "Revenue Deficit - Grants for Creation of Capital Assets", "Reflects consumption gap after isolating capital asset transfers made to States"],
        ["Fiscal Deficit (FD)", "Total Expenditure - (Revenue Receipts + Non-debt Capital Receipts)", "Total market borrowing requirement of the government in a given financial year"],
        ["Primary Deficit (PD)", "Fiscal Deficit - Net Interest Payments", "Reflects the current year fiscal stance excluding the burden of historical legacy debt servicing"]
      ]
    },
    "points": [
      "Fiscal Responsibility and Budget Management (FRBM) Act 2003: Enacted to institutionalize financial discipline, eliminate revenue deficit, and cap fiscal deficit at 3% of GDP by 2008-09 (disrupted by the 2008 global financial crisis). Mandates the annual presentation of Macroeconomic Framework, Medium-Term Fiscal Policy, and Fiscal Policy Strategy statements alongside the Union Budget.",
      "N.K. Singh FRBM Review Committee (2017): Recommended transitioning from pure fiscal deficit targeting to combined Public Debt-to-GDP targets: 60% combined debt (40% Central Government, 20% State Governments) by 2023, while keeping fiscal deficit at 2.5% of GDP for the Centre.",
      "Escape Clause Provisions: Section 4(2) of the amended FRBM Act permits deviations from annual fiscal deficit targets (up to 0.5% of GDP) during extraordinary triggers: acts of war, national calamity, collapse of agriculture, or structural reforms with unanticipated fiscal implications.",
      "Post-Pandemic Fiscal Glide Path: Following COVID-19 pandemic spending surges (fiscal deficit peaked at 9.2% of GDP in FY21), the Union Government committed to a consolidation glide path to bring the fiscal deficit below 4.5% of GDP by FY2025-26, while concurrently ramping up capital expenditure (Capex) to over 3.3% of GDP.",
      "Public Debt Sustainability Metrics: India's general government debt stands at ~81-83% of GDP. Sovereign debt sustainability is safeguarded by high domestic currency denomination (>95% rupee-denominated), predominantly long-term maturity profiles, and favorable growth-interest differentials (r - g < 0)."
    ],
    "mains": [
      "Critically analyze the fiscal consolidation roadmap recommended by the N.K. Singh Committee on FRBM. How has the post-COVID macroeconomic environment altered India's public debt management strategy? (250 Words, 15 Marks)",
      "Explain the distinction between Fiscal Deficit and Primary Deficit. Why is a rising ratio of capital expenditure over revenue expenditure considered desirable for fiscal health? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO03-01",
        "q": "What is the formula for calculating 'Primary Deficit' in government budgeting?",
        "options": ["Fiscal Deficit - Revenue Deficit", "Fiscal Deficit - Interest Payments", "Total Expenditure - Total Receipts", "Revenue Receipts - Capital Expenditure"],
        "ans": "b",
        "explanation": "Primary Deficit is calculated as Fiscal Deficit minus Net Interest Payments. It indicates the government borrowing required to finance expenditures other than legacy interest obligations."
      },
      {
        "id": "MCQ-ECO03-02",
        "q": "What combined General Government Debt-to-GDP ratio was recommended by the N.K. Singh FRBM Review Committee to be achieved?",
        "options": ["40% of GDP", "50% of GDP", "60% of GDP (40% Centre, 20% States)", "75% of GDP"],
        "ans": "c",
        "explanation": "The N.K. Singh Committee (2017) recommended a combined debt-to-GDP target of 60% by 2022-23, comprising 40% for the Central Government and 20% for State Governments."
      },
      {
        "id": "MCQ-ECO03-03",
        "q": "Under the FRBM Act 2003, what is the maximum deviation permitted in fiscal deficit under the statutory 'Escape Clause' during extraordinary national crises?",
        "options": ["0.25% of GDP", "0.50% of GDP", "1.00% of GDP", "2.00% of GDP"],
        "ans": "b",
        "explanation": "Under Section 4(2) of the amended FRBM Act, the escape clause allows the Central Government to exceed the annual fiscal deficit target by up to 0.5% of GDP on grounds of national security, war, national calamity, or severe structural economic reforms."
      },
      {
        "id": "MCQ-ECO03-04",
        "q": "Which of the following is categorized as 'Capital Expenditure' in the Union Budget?",
        "options": ["Payment of salaries to government employees", "Subsidies on food and fertilizers", "Loans and advances given to State Governments", "Interest payments on market debt"],
        "ans": "c",
        "explanation": "Loans and advances disbursed to State Governments and Union Territories create financial assets and are therefore classified as Capital Expenditure. Salaries, subsidies, and interest payments are recurring Revenue Expenditures."
      },
      {
        "id": "MCQ-ECO03-05",
        "q": "What target did the Union Finance Minister set for the fiscal deficit glide path to reach by FY 2025-26?",
        "options": ["Below 3.0% of GDP", "Below 3.5% of GDP", "Below 4.5% of GDP", "Below 5.0% of GDP"],
        "ans": "c",
        "explanation": "In the Union Budget 2021-22, the Finance Minister announced a fiscal glide path targeting to bring the Central Government's fiscal deficit below 4.5% of GDP by FY 2025-26."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-04",
    "filename": "04_government_budgeting_taxation_and_gst_council",
    "title": "Budgeting, Taxation Architecture & Finance Commissions",
    "mapping": "Economy - India & AP: Constitutional Budgeting (Articles 112 to 117), Direct and Indirect Tax Reforms, Goods and Services Tax (GST) Architecture, 15th and 16th Finance Commissions, Vertical and Horizontal Fiscal Devolution, and Centrally Sponsored Schemes.",
    "intro": "Government budgeting operationalizes democratic accountability and national socio-economic priorities. Enshrined in Article 112 of the Constitution as the 'Annual Financial Statement', the budget coordinates taxation and spending. Following historic tax reforms—most notably the implementation of the Goods and Services Tax (GST) and corporate tax rationalization—intergovernmental fiscal transfers are mediated by the constitutional Finance Commission (Article 280) to resolve vertical and horizontal fiscal imbalances.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Parliament_of_India_New_Delhi_2023.jpg", "caption": "The Parliament of India, where the Union Budget is introduced, debated, and passed into law under Articles 112–117.", "alt": "New Parliament Building India"},
    "table": {
      "caption": "15th Finance Commission Horizontal Devolution Criteria (2021–26)",
      "headers": ["Devolution Criterion", "Assigned Weight (%)", "Objective & Rationale for Inclusion"],
      "rows": [
        ["Income Distance", "45.0%", "Equity principle: compensates economically weaker states based on per capita GSDP gap"],
        ["Population (2011 Census)", "15.0%", "Addresses demographic scale while upholding uniform national census benchmarking"],
        ["Area of the State", "15.0%", "Compensates geographical size, administrative dispersion, and service delivery cost overheads"],
        ["Forest and Ecology", "10.0%", "Rewards dense forest preservation and carbon sequestration environmental services"],
        ["Demographic Performance", "12.5%", "Rewards progressive states that lowered Total Fertility Rates (TFR) to replacement levels"],
        ["Tax Effort", "2.5%", "Rewards efficiency in state own tax revenue mobilization relative to GSDP potential"]
      ]
    },
    "points": [
      "Constitutional Budgetary Procedures: Article 112 mandates the Annual Financial Statement; Article 113 governs Demands for Grants; Article 114 mandates the Appropriation Bill without which no money can be withdrawn from the Consolidated Fund of India (Article 266); Article 110/117 governs Finance Bills enacting tax measures.",
      "GST Dual Architecture & Cooperative Federalism: Implemented via the 101st Constitutional Amendment Act 2016, GST subsumed 17 central and state indirect taxes. Built on a dual model (CGST + SGST) and an integrated interstate levy (IGST), it is governed by the GST Council (Article 279A).",
      "15th Finance Commission Recommendations: Chaired by N.K. Singh, the 15th FC recommended a vertical devolution share of 41% of net divisible pool of taxes to States for 2021-26 (adjusted from 42% under 14th FC to account for Jammu & Kashmir and Ladakh UT reorganization).",
      "16th Finance Commission Mandate: Constituted in December 2023 under the Chairmanship of Dr. Arvind Panagariya, tasked with formulating fiscal devolution recommendations for the 5-year award period commencing April 1, 2026, alongside disaster management financing reviews.",
      "Direct Tax Simplification: Introduction of Section 115BAC (New Tax Regime with zero exemptions, higher slabs, and standard deductions) and Section 115BAA (concessional 22% corporate tax rate for domestic manufacturing) has substantially widened the direct tax base."
    ],
    "mains": [
      "Analyze the criteria adopted by the 15th Finance Commission for horizontal tax devolution. How does the inclusion of 'Demographic Performance' balance equity with efficiency across southern and northern states? (250 Words, 15 Marks)",
      "Evaluate the performance of the Goods and Services Tax (GST) as a unified indirect taxation system. Discuss its impact on state fiscal autonomy and cooperative federalism. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO04-01",
        "q": "Under Article 112 of the Indian Constitution, the Union Budget is officially designated as which document?",
        "options": ["Annual Budgetary Statement", "Annual Financial Statement", "National Revenue and Expenditure Plan", "Appropriation and Finance Statement"],
        "ans": "b",
        "explanation": "Article 112 of the Constitution of India formally terms the annual budget presented by the President before Parliament as the 'Annual Financial Statement'."
      },
      {
        "id": "MCQ-ECO04-02",
        "q": "What vertical tax devolution share from the divisible pool to States was recommended by the 15th Finance Commission chaired by N.K. Singh?",
        "options": ["32%", "38%", "41%", "42%"],
        "ans": "c",
        "explanation": "The 15th Finance Commission recommended that 41% of the net divisible tax pool be devolved to the States for the period 2021–26 (down 1% from the 14th FC's 42% due to the creation of the UTs of Jammu & Kashmir and Ladakh)."
      },
      {
        "id": "MCQ-ECO04-03",
        "q": "Who was appointed as the Chairman of the 16th Finance Commission of India constituted in December 2023?",
        "options": ["Dr. Arvind Panagariya", "Dr. Raghuram Rajan", "Dr. Y.V. Reddy", "N.K. Singh"],
        "ans": "a",
        "explanation": "The Government of India constituted the 16th Finance Commission with Dr. Arvind Panagariya (former Vice-Chairman of NITI Aayog) as its Chairman, to provide recommendations for the five years starting April 2026."
      },
      {
        "id": "MCQ-ECO04-04",
        "q": "Which Constitutional Amendment Act paved the way for the nationwide roll-out of the Goods and Services Tax (GST) in India?",
        "options": ["99th Amendment Act", "100th Amendment Act", "101st Amendment Act", "103rd Amendment Act"],
        "ans": "c",
        "explanation": "The 101st Constitutional Amendment Act, 2016 introduced Article 246A, 269A, and 279A, enabling Parliament and State Legislatures to concurrently levy Goods and Services Tax (GST) effective July 1, 2017."
      },
      {
        "id": "MCQ-ECO04-05",
        "q": "Which criterion carried the highest weightage (45%) in the horizontal tax devolution formula of the 15th Finance Commission?",
        "options": ["Population (2011)", "Forest and Ecology", "Income Distance", "Demographic Performance"],
        "ans": "c",
        "explanation": "Income Distance, measuring the gap between a state's per capita GSDP and that of the highest per capita state (Goa/Haryana benchmark), carried the highest weightage of 45% to ensure fiscal equalization."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-05",
    "filename": "05_inclusive_growth_poverty_unemployment_and_sdgs",
    "title": "Inclusive Growth, Poverty, Unemployment & SDGs",
    "mapping": "Economy - India & AP: Inclusive Growth Strategies, Poverty Estimation Methodologies (Tendulkar, Rangarajan Committees), NITI Aayog National Multidimensional Poverty Index (MPI), Types of Unemployment, PLFS Metrics (LFPR, WPR, UR), and Sustainable Development Goals (SDG India Index).",
    "intro": "Inclusive growth ensures that the fruits of economic expansion are broadly distributed across all strata of society, generating equitable opportunities and reducing deep-rooted structural disparities. In India, poverty estimation has evolved from basic calorie-consumption expenditure thresholds to multidimensional deprivation assessments. Concurrently, employment measurement through the Periodic Labour Force Survey (PLFS) and performance tracking through the NITI Aayog SDG India Index guide state and national social investments.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Sustainable_Development_Goals.svg", "caption": "The 17 United Nations Sustainable Development Goals (SDGs), monitored across Indian States by NITI Aayog.", "alt": "Sustainable Development Goals overview"},
    "table": {
      "caption": "Evolution of Poverty Estimation Methodologies in India",
      "headers": ["Expert Group / Committee", "Poverty Benchmark Criterion", "Rural / Urban Thresholds", "Salient Innovations & Methodological Shift"],
      "rows": [
        ["Lakdawala Committee (1993)", "Calorie norms (2400 rural / 2100 urban)", "State-specific CPI-AL & CPI-IW pricing", "Disaggregated poverty lines across states; relied on URP NSS consumption surveys"],
        ["Suresh Tendulkar Committee (2009)", "Uniform Poverty Line Basket (PLB) based on urban consumption", "Rs 816 rural / Rs 1,000 urban per capita/month (2011-12)", "Moved away from calorie anchor; incorporated private expenditure on health and education"],
        ["C. Rangarajan Committee (2014)", "Independent nutritional + essential non-food expenditure basket", "Rs 972 rural / Rs 1,407 urban per capita/month (2011-12)", "Calculated family expenditure for 5 members; estimated 29.5% poverty vs Tendulkar's 21.9%"],
        ["NITI Aayog National MPI (2021-23)", "Alkire-Foster method across Health, Education, Standard of Living (12 indicators)", "Multidimensionally poor if deprived in >= 33.3% of weighted indicators", "Non-income multidimensional measure: reported 13.5 crore Indians exited poverty between 2015-16 & 2019-21"]
      ]
    },
    "points": [
      "National Multidimensional Poverty Index (MPI): Formulated by NITI Aayog using NFHS microdata across 3 equally weighted dimensions (Health, Education, Standard of Living) and 12 indicators (including nutrition, child-adolescent mortality, maternal health, cooking fuel, sanitation, drinking water, electricity, housing, assets, bank accounts).",
      "Unemployment Measurements under PLFS: Conducted by NSO since 2017. Measures Labor Force Participation Rate (LFPR), Worker Population Ratio (WPR), and Unemployment Rate (UR) using Usual Status (ps+ss, 365-day recall) and Current Weekly Status (CWS, 7-day recall).",
      "Structural vs Frictional vs Disguised Unemployment: India's predominant labor market challenge is disguised unemployment in agriculture (marginal productivity of labor approaching zero) alongside youth educated unemployment driven by skill mismatch.",
      "SDG India Index Architecture: Developed by NITI Aayog to monitor national and sub-national progress across 17 SDGs. Classifies States and UTs into four categories: Achiever (100), Front Runner (65–99), Performer (50–64), and Aspirant (0–49).",
      "Safety Nets and Social Security Innovations: Direct Benefit Transfer (DBT) via the JAM Trinity (Jan Dhan, Aadhaar, Mobile), PM Garib Kalyan Anna Yojana (PMGKAY), and MGNREGS have established a resilient universal social safety net mitigating consumption shocks."
    ],
    "mains": [
      "Explain how NITI Aayog's National Multidimensional Poverty Index (MPI) differs from traditional consumption-expenditure poverty lines. Discuss the key drivers behind India's multidimensional poverty reduction in recent years. (250 Words, 15 Marks)",
      "Analyze the structural bottlenecks facing female labor force participation (FLFPR) in India. What targeted policy interventions are needed to boost women's formal employment? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO05-01",
        "q": "Which committee recommended shifting from calorie-consumption based poverty lines to a uniform poverty line basket incorporating health and education expenses?",
        "options": ["Alagh Committee", "Lakdawala Committee", "Suresh Tendulkar Committee", "C. Rangarajan Committee"],
        "ans": "c",
        "explanation": "The Suresh Tendulkar Committee (submitted in 2009) departed from the earlier calorie-norm approach and formulated poverty lines incorporating explicit spending on education and healthcare."
      },
      {
        "id": "MCQ-ECO05-02",
        "q": "How many indicators across how many dimensions are evaluated in NITI Aayog's National Multidimensional Poverty Index (MPI)?",
        "options": ["10 indicators across 3 dimensions", "12 indicators across 3 dimensions", "15 indicators across 4 dimensions", "17 indicators across 5 dimensions"],
        "ans": "b",
        "explanation": "NITI Aayog's National MPI evaluates 12 indicators across 3 equally weighted dimensions: Health (Nutrition, Child-Adolescent Mortality, Maternal Health), Education (Years of Schooling, School Attendance), and Standard of Living (Cooking Fuel, Sanitation, Drinking Water, Housing, Electricity, Assets, Bank Accounts)."
      },
      {
        "id": "MCQ-ECO05-03",
        "q": "In the Periodic Labour Force Survey (PLFS), how is the 'Unemployment Rate (UR)' officially defined?",
        "options": ["Percentage of total population without employment", "Percentage of persons unemployed among the persons in the labour force", "Percentage of working-age population without jobs", "Number of registered applicants in employment exchanges"],
        "ans": "b",
        "explanation": "Unemployment Rate (UR) is strictly defined as the percentage of unemployed persons among the persons in the labour force (Labour Force = Employed + Unemployed)."
      },
      {
        "id": "MCQ-ECO05-04",
        "q": "In the NITI Aayog SDG India Index classification, a state scoring between 65 and 99 points is categorized under which tier?",
        "options": ["Aspirant", "Performer", "Front Runner", "Achiever"],
        "ans": "c",
        "explanation": "States scoring 65–99 on the NITI Aayog SDG India Index are categorized as 'Front Runners'. Scores 50–64 are 'Performers', below 50 are 'Aspirants', and 100 represents 'Achievers'."
      },
      {
        "id": "MCQ-ECO05-05",
        "q": "What phenomenon occurs in agriculture when more workers are engaged than practically required, such that the marginal productivity of additional labor is near zero?",
        "options": ["Frictional Unemployment", "Cyclical Unemployment", "Disguised Unemployment", "Structural Unemployment"],
        "ans": "c",
        "explanation": "Disguised unemployment is characterized by redundant labor in a sector (particularly agrarian family farming) where surplus workers contribute zero marginal productivity to the total output."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-06",
    "filename": "06_agriculture_msp_food_security_and_pm_kisan",
    "title": "Agriculture, MSP Framework, Food Security & PM-KISAN",
    "mapping": "Economy - India & AP: Agricultural Production Trends, Minimum Support Price (MSP) Determination (CACP, A2+FL vs C2 formulas), National Food Security Act (NFSA 2013), PM-KISAN, PM Fasal Bima Yojana, Micro-Irrigation, and Agriculture Infrastructure Fund.",
    "intro": "Agriculture serves as the social anchor of India's rural economy, sustaining food security and generating rural demand. The procurement and price support architecture, mediated by the Commission for Agricultural Costs and Prices (CACP) through Minimum Support Prices (MSP), guarantees a price floor for 22 mandated crops and fair remunerative price (FRP) for sugarcane. Modern policy interventions increasingly emphasize income support (PM-KISAN), risk mitigating crop insurance (PMFBY), post-harvest infrastructure, and value-addition.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/4/43/Combine_harvester_in_Punjab.jpg", "caption": "Mechanized agricultural harvesting in India, reflecting technological shifts in cereal production and food grain management.", "alt": "Indian agriculture harvesting"},
    "table": {
      "caption": "Agricultural Price & Support Mechanisms in India",
      "headers": ["Policy Mechanism", "Institutional Authority", "Methodological Cost Formula", "Crops Covered & Strategic Mandate"],
      "rows": [
        ["Minimum Support Price (MSP)", "CACP recommends; Cabinet Committee on Economic Affairs (CCEA) approves", "At least 1.5 times the cost of production (A2 + FL formula)", "22 mandated crops (14 Kharif, 6 Rabi, 2 commercial crops) plus FRP for Sugarcane"],
        ["PM-KISAN", "Ministry of Agriculture and Farmers Welfare", "Direct cash transfer of Rs 6,000/year (3 tranches of Rs 2,000)", "Universal income support to all landholding farmer families via Aadhaar-linked DBT"],
        ["National Food Security Act (NFSA 2013)", "Department of Food & Public Distribution / FCI", "Highly subsidized grains (now 100% free under PMGKAY)", "Covers 75% rural and 50% urban population (Antyodaya Anna Yojana + Priority Households)"],
        ["PM Fasal Bima Yojana (PMFBY)", "Empanelled General Insurance Companies", "Capped premium: 2% Kharif, 1.5% Rabi, 5% Commercial/Horticultural", "Comprehensive yield and localized risk coverage from pre-sowing to post-harvest"]
      ]
    },
    "points": [
      "Cost Methodologies in MSP Determination: CACP considers three cost benchmarks: 1. Cost A2 (actual paid-out costs on seeds, fertilizer, labor, fuel); 2. Cost A2+FL (Cost A2 plus imputed value of unpaid Family Labor); 3. Cost C2 (Comprehensive cost including A2+FL plus imputed rent on owned land and interest on owned fixed capital). The Government benchmarks MSP at 1.5 times Cost A2+FL.",
      "Fair and Remunerative Price (FRP) for Sugarcane: Determined under the Sugarcane (Control) Order 1966. Sugar mills are legally mandated to pay FRP to farmers, linked to a basic sugar recovery rate (typically 10.25%).",
      "Public Distribution System (PDS) & FCI Buffer Stocking: The Food Corporation of India (FCI) procures wheat and paddy through centralized and decentralized procurement (DCP). Under the unified PM Garib Kalyan Anna Yojana (PMGKAY), free food grains (5 kg per person/month for priority households; 35 kg per family/month for AAY) are distributed to ~81.35 crore beneficiaries.",
      "Agriculture Infrastructure Fund (AIF): A Rs 1 lakh crore financing facility providing medium-to-long term debt financing for post-harvest management infrastructure and community farming assets, with a 3% interest subvention for loans up to Rs 2 crore.",
      "e-NAM (National Agriculture Market): Pan-India electronic trading portal networking existing APMC mandis to create a unified national market for agricultural commodities, facilitating transparent price discovery and reducing intermediary margins."
    ],
    "mains": [
      "Critically analyze the debates surrounding granting legal guarantee to Minimum Support Price (MSP) based on the Swaminathan Commission's C2+50% formula. What are the fiscal and market implications for the Indian economy? (250 Words, 15 Marks)",
      "Examine the role of the National Food Security Act (NFSA 2013) and PM Garib Kalyan Anna Yojana in ensuring nutritional and food security. Discuss the supply-chain and leakage challenges confronting the PDS in India. (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO06-01",
        "q": "Which body recommends the Minimum Support Prices (MSP) for mandated agricultural crops in India?",
        "options": ["NITI Aayog", "Food Corporation of India (FCI)", "Commission for Agricultural Costs and Prices (CACP)", "Cabinet Committee on Economic Affairs (CCEA)"],
        "ans": "c",
        "explanation": "The Commission for Agricultural Costs and Prices (CACP) recommends MSPs, which are subsequently approved and announced by the Cabinet Committee on Economic Affairs (CCEA) chaired by the Prime Minister."
      },
      {
        "id": "MCQ-ECO06-02",
        "q": "For how many mandated agricultural crops is the Minimum Support Price (MSP) officially announced every year (excluding sugarcane FRP)?",
        "options": ["18 crops", "22 crops", "25 crops", "28 crops"],
        "ans": "b",
        "explanation": "CACP recommends MSPs for 22 mandated crops (14 Kharif, 6 Rabi, and 2 commercial crops) along with the Fair and Remunerative Price (FRP) for sugarcane."
      },
      {
        "id": "MCQ-ECO06-03",
        "q": "What cost formula does the Government of India currently utilize to implement its policy of fixing MSP at a minimum of 150% (1.5 times) of the cost of production?",
        "options": ["1.5 times Cost A2", "1.5 times Cost A2 + FL", "1.5 times Cost C2", "1.5 times Market Clearing Price"],
        "ans": "b",
        "explanation": "The Union Government benchmarks MSP at 1.5 times the Cost A2+FL (actual paid-out costs plus imputed value of unpaid family labor), in accordance with the commitment announced in the Union Budget 2018-19."
      },
      {
        "id": "MCQ-ECO06-04",
        "q": "Under the Pradhan Mantri Kisan Samman Nidhi (PM-KISAN) scheme, what annual income support is transferred directly to eligible farmer families?",
        "options": ["Rs 5,000 in two installments", "Rs 6,000 in three equal four-monthly installments of Rs 2,000", "Rs 8,000 in four installments", "Rs 10,000 in a single lump sum"],
        "ans": "b",
        "explanation": "PM-KISAN provides Rs 6,000 per year per eligible beneficiary farmer family, credited directly into their bank accounts in three equal installments of Rs 2,000 every four months."
      },
      {
        "id": "MCQ-ECO06-05",
        "q": "What maximum insurance premium is payable by farmers for foodgrain and oilseed crops during the Kharif season under PM Fasal Bima Yojana (PMFBY)?",
        "options": ["1.5%", "2.0%", "3.5%", "5.0%"],
        "ans": "b",
        "explanation": "Under PMFBY, the maximum premium paid by farmers is capped at 2.0% of the sum insured for Kharif food and oilseed crops, 1.5% for Rabi food and oilseed crops, and 5.0% for annual commercial/horticultural crops."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-07",
    "filename": "07_industrial_policy_manufacturing_pli_and_msmes",
    "title": "Industrial Policy, Manufacturing, PLI & MSME Sector",
    "mapping": "Economy - India & AP: Industrial Policies (1948 to Post-1991), National Manufacturing Policy, Production Linked Incentive (PLI) Schemes, MSME Classification Criteria 2020, PM Gati Shakti, Logistics Performance, and Start-up Ecosystem.",
    "intro": "Industrialization drives value addition, technology absorption, and productive labor reallocation in emerging economies. India's industrial trajectory has evolved from inward-oriented import substitution under the 1956 Industrial Policy Resolution to market-driven liberalization post-1991. Contemporary industrial policy focuses on deep manufacturing competitiveness through Production Linked Incentive (PLI) schemes across 14 frontier sectors, revised composite MSME frameworks, and multimodal connectivity via PM Gati Shakti.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ec/Manufacturing_India_automobile.jpg", "caption": "High-tech automotive and manufacturing facility in India, supported by the Production Linked Incentive (PLI) scheme.", "alt": "Automobile manufacturing in India"},
    "table": {
      "caption": "Composite MSME Classification Criteria (Notified July 1, 2020)",
      "headers": ["Enterprise Category", "Investment in Plant & Machinery / Equipment", "Annual Turnover Limit (Excluding Exports)", "Key Regulatory & Credit Privileges"],
      "rows": [
        ["Micro Enterprise", "Not more than Rs 1 Crore", "Not more than Rs 5 Crore", "Priority Sector Lending (PSL); access to collateral-free CGTMSE loans"],
        ["Small Enterprise", "Not more than Rs 10 Crore", "Not more than Rs 50 Crore", "Mandatory 25% public procurement quota by CPSEs; TReDS bill discounting"],
        ["Medium Enterprise", "Not more than Rs 50 Crore", "Not more than Rs 250 Crore", "Eligible for technology upgradation subsidies; exclusion of export turnover"]
      ]
    },
    "points": [
      "Revised Composite MSME Criteria: Effective July 1, 2020, the classification eliminated the distinction between manufacturing and services sectors, introducing a composite formula based on both 'Investment in Plant & Machinery' and 'Annual Turnover'. Export turnover is explicitly excluded when computing enterprise limits.",
      "Production Linked Incentive (PLI) Schemes: Rolled out with an aggregate outlay exceeding Rs 1.97 lakh crore across 14 champion sectors (including mobile phones, pharmaceuticals, automobiles, advanced chemistry cell batteries, and textiles) offering 4% to 6% incentives on incremental sales over base years.",
      "PM Gati Shakti National Master Plan: A digital GIS-based platform integrating infrastructure planning across 16 central ministries (Railways, Roadways, Ports, Aviation) to eliminate departmental silos, streamline right-of-way approvals, and lower India's logistics cost from ~13% of GDP toward global benchmarks (~8%).",
      "National Logistics Policy (NLP 2022): Complements PM Gati Shakti by establishing the Unified Logistics Interface Platform (ULIP) and Ease of Logistics (ELOG) to integrate freight visibility across rail, road, and maritime transit.",
      "Startup India & Angel Tax Abolition: With over 130,000 DPIIT-recognized startups and 110+ unicorns, India hosts the third-largest startup ecosystem globally. The abolition of Angel Tax (Section 56(2)(viib) of the Income Tax Act) in Union Budget 2024 eliminates tax uncertainty on venture capital investments."
    ],
    "mains": [
      "Critically evaluate the Production Linked Incentive (PLI) scheme as an instrument of strategic industrial policy. Has it successfully transformed India into a global manufacturing export hub? (250 Words, 15 Marks)",
      "Discuss the significance of the revised composite criteria for classifying Micro, Small, and Medium Enterprises (MSMEs). What structural challenges continue to hinder MSME access to formal credit and global supply chains? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO07-01",
        "q": "Under the revised composite classification effective July 2020, what are the investment and turnover limits for a 'Small Enterprise'?",
        "options": ["Investment <= Rs 1 Cr and Turnover <= Rs 5 Cr", "Investment <= Rs 10 Cr and Turnover <= Rs 50 Cr", "Investment <= Rs 50 Cr and Turnover <= Rs 250 Cr", "Investment <= Rs 20 Cr and Turnover <= Rs 100 Cr"],
        "ans": "b",
        "explanation": "A Small Enterprise is defined as an enterprise where investment in plant and machinery does not exceed Rs 10 crore and turnover does not exceed Rs 50 crore."
      },
      {
        "id": "MCQ-ECO07-02",
        "q": "Across how many champion manufacturing sectors were the Production Linked Incentive (PLI) schemes rolled out by the Government of India?",
        "options": ["8 sectors", "10 sectors", "14 sectors", "20 sectors"],
        "ans": "c",
        "explanation": "The Government of India rolled out Production Linked Incentive (PLI) schemes across 14 key manufacturing sectors with an announced outlay of ~Rs 1.97 lakh crore."
      },
      {
        "id": "MCQ-ECO07-03",
        "q": "When calculating the annual turnover limit for MSME classification under the 2020 guidelines, which component is explicitly excluded?",
        "options": ["Revenue from online sales", "Export turnover", "Subsidies received from government", "Inter-state sales turnover"],
        "ans": "b",
        "explanation": "Under the notification dated June 26, 2020, export turnover of goods or services or both is strictly excluded when calculating the turnover of any enterprise for MSME classification purposes."
      },
      {
        "id": "MCQ-ECO07-04",
        "q": "What is the primary technological platform utilized by the PM Gati Shakti National Master Plan for multimodal infrastructure coordination?",
        "options": ["Blockchain ledger", "GIS-based spatial planning platform developed by BISAG-N", "Artificial intelligence facial recognition portal", "Centralized quantum communication network"],
        "ans": "b",
        "explanation": "PM Gati Shakti operates on a dynamic GIS-based spatial planning portal developed by BISAG-N (Bhaskaracharya National Institute for Space Applications and Geo-informatics), integrating layered spatial maps of all infrastructure ministries."
      },
      {
        "id": "MCQ-ECO07-05",
        "q": "Under Public Procurement Policy for MSEs, what mandatory minimum percentage of annual purchases must Central Ministries and CPSEs procure from Micro and Small Enterprises?",
        "options": ["10%", "15%", "20%", "25%"],
        "ans": "d",
        "explanation": "Under the Public Procurement Policy for MSEs Order 2018, it is mandatory for Central Ministries, Departments, and Central Public Sector Enterprises (CPSEs) to procure a minimum of 25% of their total annual purchases from Micro and Small Enterprises (with sub-targets of 4% from SC/ST MSEs and 3% from Women MSEs)."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-08",
    "filename": "08_foreign_trade_balance_of_payments_and_fdi_trends",
    "title": "Foreign Trade, Balance of Payments & FDI Trends",
    "mapping": "Economy - India & AP: Balance of Payments (BoP) Structure (Current Account vs Capital Account), Foreign Trade Policy (FTP 2023), Export Promotion Schemes (RoDTEP, SEZs), Foreign Direct Investment (FDI) & FPI Trends, Foreign Exchange Reserves, and Rupee Internationalisation.",
    "intro": "External sector stability ensures a country's financial resilience and integration with the global economy. The Balance of Payments (BoP) records all cross-border economic transactions between residents and the rest of the world. While India traditionally runs a structural trade deficit on its Merchandise Current Account, it is cushioned by robust services exports and overseas remittances. With forex reserves hovering around $650–700 billion, external vulnerabilities remain tightly contained as India advances rupee internationalization.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Visakhapatnam_Port_container_terminal.jpg", "caption": "Visakhapatnam Port Container Terminal, a vital maritime gateway for India's merchandise exports to Southeast Asia and the Pacific.", "alt": "Visakhapatnam Port Container Terminal"},
    "table": {
      "caption": "Balance of Payments (BoP) Structure: Current vs Capital Account",
      "headers": ["BoP Component", "Sub-Accounts / Items Included", "India's Traditional Net Balance", "Key Macro Drivers & Dynamics"],
      "rows": [
        ["Current Account: Merchandise", "Export & Import of tangible physical goods (Crude oil, gold, electronics, gems)", "Substantial structural deficit (-$200B to -$250B)", "Driven by import dependence on crude petroleum, coal, and electronic components"],
        ["Current Account: Invisibles", "Services (IT/BPM), Transfers (Remittances), and Income (Profits/Dividends/Interest)", "Substantial structural surplus (+$150B to +$180B)", "India is world's #1 remittance recipient ($120B+); stellar net IT-BPM exports"],
        ["Capital Account: Foreign Investment", "Foreign Direct Investment (FDI) & Foreign Portfolio Investment (FPI)", "Consistent substantial net surplus", "Driven by automatic FDI route in manufacturing and vibrant equity markets"],
        ["Capital Account: Debt Flows", "External Commercial Borrowings (ECBs), NRI Deposits, Short-term trade credit", "Modest to moderate net surplus", "Regulated by RBI ceilings, interest rate caps, and end-use restrictions"]
      ]
    },
    "points": [
      "Foreign Trade Policy (FTP 2023): Shifted away from fixed 5-year cyclical policies to a dynamic, open-ended policy framework targeting $2 trillion in aggregate exports ($1 trillion merchandise + $1 trillion services) by 2030. Focuses on four pillars: Incentive to Remission, Export promotion through collaboration, Ease of doing business, and Emerging sectors (e-commerce exports and Districts as Export Hubs).",
      "Remission of Duties and Taxes on Exported Products (RoDTEP): Replaced the WTO-inconsistent Merchandise Exports from India Scheme (MEIS). Reimburses unrefunded embedded central, state, and local duties/taxes incurred in the manufacture and distribution of exported goods.",
      "Remittances Hegemony: India continues to rank as the largest recipient of inward personal remittances worldwide, surpassing $125 billion annually according to World Bank Migration and Development Briefs, with high inflows from GCC countries, the US, and the UK.",
      "Foreign Direct Investment (FDI) Regimes: Over 90% of inward FDI arrives via the Automatic Route (without prior approval from Government or RBI). Major source nations include Singapore, Mauritius, USA, Netherlands, and Japan, with computer software, hardware, services, and trading sectors absorbing the lion's share.",
      "Internationalisation of the Indian Rupee: Operationalization of Special Rupee Vostro Accounts (SRVA) under RBI circulars allows bilateral trade settlement in INR with partner countries (e.g., Russia, UAE), insulating bilateral trade from SWIFT sanctions and US Dollar exchange rate volatility."
    ],
    "mains": [
      "Analyze the structural composition of India's Current Account Deficit (CAD). How do software services exports and inward remittances shield India from global crude oil price shocks? (250 Words, 15 Marks)",
      "Discuss the strategic objectives of the Foreign Trade Policy (FTP) 2023. What institutional steps are required to boost e-commerce exports and establish 'Districts as Export Hubs'? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO08-01",
        "q": "What total export target (merchandise plus services combined) does India's Foreign Trade Policy (FTP 2023) aim to achieve by the year 2030?",
        "options": ["$1 Trillion", "$1.5 Trillion", "$2 Trillion", "$3 Trillion"],
        "ans": "c",
        "explanation": "FTP 2023 explicitly sets a target to scale India's total exports to $2 trillion by 2030, comprising $1 trillion in merchandise exports and $1 trillion in services exports."
      },
      {
        "id": "MCQ-ECO08-02",
        "q": "Which scheme was notified in 2021 to replace the WTO-disputed MEIS by refunding embedded central, state, and local taxes to exporters?",
        "options": ["SEIS (Service Exports Scheme)", "RoDTEP (Remission of Duties and Taxes on Exported Products)", "EPCG (Export Promotion Capital Goods)", "Advance Authorization Scheme"],
        "ans": "b",
        "explanation": "The RoDTEP scheme replaced MEIS (which was ruled WTO-inconsistent) to ensure that taxes and duties suffered on export products at central, state, and local levels are rebated in WTO-compliant manner."
      },
      {
        "id": "MCQ-ECO08-03",
        "q": "In the Balance of Payments (BoP) accounting, where are inward remittances sent by non-resident Indian citizens residing abroad recorded?",
        "options": ["Capital Account - External Commercial Borrowing", "Current Account - Invisibles (Transfers)", "Capital Account - Foreign Direct Investment", "Current Account - Merchandise Trade"],
        "ans": "b",
        "explanation": "Overseas private remittances sent home are classified as 'Unilateral Transfers' under the Invisibles category of the Current Account in the Balance of Payments."
      },
      {
        "id": "MCQ-ECO08-04",
        "q": "Which special banking account arrangement was authorized by RBI to facilitate settlement of international trade in Indian Rupees (INR)?",
        "options": ["NRE Account", "Special Rupee Vostro Account (SRVA)", "FCNR(B) Account", "Offshore ESCROW Account"],
        "ans": "b",
        "explanation": "In July 2022, the RBI permitted authorized dealer banks to open Special Rupee Vostro Accounts (SRVA) for partner countries' banks to settle cross-border export-import transactions directly in Indian Rupees."
      },
      {
        "id": "MCQ-ECO08-05",
        "q": "Which country has consistently emerged as the top source of Foreign Direct Investment (FDI) equity inflows into India in recent financial years?",
        "options": ["United States", "Singapore", "United Kingdom", "United Arab Emirates"],
        "ans": "b",
        "explanation": "Singapore has consistently been the leading source of FDI equity inflows into India, followed by Mauritius and the United States, according to DPIIT data."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-09",
    "filename": "09_andhra_pradesh_state_economy_gsdp_and_fiscal_health",
    "title": "Andhra Pradesh State Economy, GSDP & Fiscal Health",
    "mapping": "Economy - India & AP: Andhra Pradesh State Economy, GSDP Growth Trends, Per Capita Income, Sectoral Performance (Agriculture, Industry, Services), Post-Bifurcation Fiscal Challenges (AP Reorganisation Act 2014, Resource Gap), State Debt, Deficits, and Revenue Mobilization.",
    "intro": "The economy of reorganized Andhra Pradesh presents a distinctive development trajectory marked by strong agricultural and allied sector performance, a lengthy coastline (974 km), and profound post-bifurcation fiscal challenges. Following bifurcation under the AP Reorganisation Act 2014, the state lost Hyderabad's high-yielding IT and commercial tax revenue base, inheriting a structural revenue deficit. Managing high welfare expenditure while mobilizing capital investment for industrial infrastructure and fiscal consolidation defines AP's state finances.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Amaravati_Secretariat_Velagapudi.jpg", "caption": "Andhra Pradesh State Secretariat complex at Velagapudi, Amaravati, the administrative nerve centre of AP state governance.", "alt": "AP State Secretariat Velagapudi Amaravati"},
    "table": {
      "caption": "Andhra Pradesh Macroeconomic & Fiscal Indicators (~2023-24)",
      "headers": ["Macroeconomic / Fiscal Metric", "Value / Trend Estimate", "Comparative National Benchmark", "Structural Context & Analysis"],
      "rows": [
        ["GSDP Growth Rate (Constant Prices)", "7.0% – 7.5%", "India GDP Growth: ~7.2%", "Driven by robust agriculture (aquaculture, horticulture) and services growth"],
        ["Per Capita Income (Current Prices)", "~Rs 2,42,000", "India Per Capita: ~Rs 2,12,000", "Higher than national average, driven by coastal economic prosperity"],
        ["Agriculture & Allied Share in GSDP", "~34.5%", "National Average: ~17.7%", "Exceptionally high primary sector footprint; vulnerable to monsoon & input shocks"],
        ["Industry Sector Share in GSDP", "~23.0%", "National Average: ~28.3%", "Constrained manufacturing base; post-bifurcation loss of heavy industrial cluster"],
        ["Services Sector Share in GSDP", "~42.5%", "National Average: ~54.0%", "Dominated by trade, transport, tourism, and real estate; low high-end IT presence"],
        ["State Outstanding Debt-to-GSDP", "~33% – 34%", "15th FC Recommended Ceiling: 25%", "Elevated debt servicing obligations; substantial off-budget borrowings via state corporations"]
      ]
    },
    "points": [
      "Bifurcation Shocks & AP Reorganisation Act 2014: Bifurcation apportioned assets geographically but divided liabilities and population on a population ratio basis (58.32% to AP, 41.68% to Telangana), causing severe vertical revenue asymmetries and an initial resource deficit exceeding Rs 16,000 crore.",
      "Primary Sector Resilience: Unlike the national economy where agriculture contributes under 18% of GVA, Andhra Pradesh's agriculture and allied sector contributes over 34% of GSDP, earning AP the title 'Egg Bowl of Asia' and India's undisputed leader in brackish-water shrimp and fish aquaculture exports.",
      "Fiscal Health & FRBM Compliance: Andhra Pradesh Fiscal Responsibility and Budget Management (APFRBM) Act targets a fiscal deficit within 3% of GSDP (relaxed to 3.5% with power sector reform milestones). High committed expenditures on salaries, pensions, debt servicing, and unconditional welfare transfers constrain capital outlay.",
      "Off-Budget Borrowing Scrutiny: Borrowings raised by state public sector undertakings (like AP State Beverages Corporation, AP Power Finance Corporation) without legislative appropriation have drawn central finance ministry and CAG scrutiny, resulting in borrowing cap deductions under Article 293(3).",
      "Own Tax Revenue (OTR) Dynamics: State Goods and Services Tax (SGST), State Excise Duty, Stamp Duty & Registration Fees, and Sales Tax/VAT on petroleum products and alcohol comprise over 70% of AP's Own Tax Revenue, necessitating broader tax base widening."
    ],
    "mains": [
      "Analyze the structural impact of the Andhra Pradesh Reorganisation Act, 2014 on the fiscal health and economic base of Andhra Pradesh. What policy steps are imperative to achieve fiscal consolidation? (250 Words, 15 Marks)",
      "Evaluate the sectoral composition of Andhra Pradesh's GSDP. Why does the primary sector contribute a significantly higher proportion to state output compared to the national average? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO09-01",
        "q": "Under the Andhra Pradesh Reorganisation Act, 2014, on what ratio was the debt and liability of the undivided state divided between Andhra Pradesh and Telangana?",
        "options": ["50 : 50 equal share", "Population ratio (58.32% AP : 41.68% Telangana)", "Geographical area ratio", "GSDP revenue contribution ratio"],
        "ans": "b",
        "explanation": "Under Section 59 and the Eighth Schedule of the AP Reorganisation Act 2014, public debt and liabilities of the undivided state were apportioned between AP and Telangana based on population ratio (58.32% for AP and 41.68% for Telangana as per 2011 Census)."
      },
      {
        "id": "MCQ-ECO09-02",
        "q": "What is the approximate contribution of the Agriculture and Allied sector to Andhra Pradesh's Gross State Value Added (GSVA)?",
        "options": ["Around 18%", "Around 25%", "Around 34% to 35%", "Around 50%"],
        "ans": "c",
        "explanation": "Agriculture and allied activities contribute approximately 34% to 35% of Andhra Pradesh's GSVA, which is almost double the national average of ~18%."
      },
      {
        "id": "MCQ-ECO09-03",
        "q": "Under Article 293(3) of the Indian Constitution, why must the State Government of Andhra Pradesh obtain prior consent from the Government of India before raising open market loans?",
        "options": ["All state borrowings are subject to compulsory Presidential assent", "Because the State has outstanding loans or guarantees advanced by the Central Government", "Because AP is a bifurcated state under special category status", "Because state fiscal deficits are monitored by NITI Aayog"],
        "ans": "b",
        "explanation": "Article 293(3) explicitly mandates that a State may not raise any loan without the consent of the Government of India if there is still outstanding any part of a loan which has been made to the State by the Central Government or in respect of which a guarantee has been given by the Central Government."
      },
      {
        "id": "MCQ-ECO09-04",
        "q": "Which sector within Andhra Pradesh's allied agriculture sector has emerged as a premier national leader in value output and merchandise exports?",
        "options": ["Sericulture", "Brackish water Aquaculture and Fisheries", "Floriculture", "Mushroom Cultivation"],
        "ans": "b",
        "explanation": "Andhra Pradesh is the undisputed leader in India's aquaculture and marine fisheries sector, contributing over 25% of total marine production and over 35% of India's seafood and shrimp export earnings."
      },
      {
        "id": "MCQ-ECO09-05",
        "q": "What is the normal annual Fiscal Deficit ceiling prescribed for States as a percentage of GSDP under the 15th Finance Commission recommendations?",
        "options": ["2.0% of GSDP", "3.0% of GSDP (with 0.5% extra tied to power sector reforms)", "4.5% of GSDP", "5.0% of GSDP"],
        "ans": "b",
        "explanation": "The 15th Finance Commission recommended a fiscal deficit limit of 3.0% of GSDP for states, with an extra borrowing space of 0.5% of GSDP contingent on states undertaking specified performance reforms in the power distribution sector."
      }
    ]
  },
  {
    "id": "APPSC-G1-ECO-10",
    "filename": "10_agriculture_ports_and_industrial_corridors_in_ap",
    "title": "Agriculture, Ports & Industrial Corridors in Andhra Pradesh",
    "mapping": "Economy - India & AP: Agriculture Dynamics in AP (Cropping Pattern, Horticulture, Aquaculture, Rayalaseema Drought Mitigation), Irrigation Projects (Polavaram), Port-led Development (Visakhapatnam, Krishnapatnam, Machilipatnam, Ramayapatnam, Bhavanapadu), Industrial Corridors (VCIC, CBIC, HYBIC), and Flagship State Welfare Schemes.",
    "intro": "Andhra Pradesh leverages its strategic peninsular location, 974 km coastline, and fertile river deltas of the Godavari and Krishna to spearhead agro-industrial and port-led economic development. Key initiatives include completing the Polavaram National Irrigation Project to stabilize water supply across deltaic and upland regions, executing greenfield non-major ports (Ramayapatnam, Machilipatnam, Mulapeta/Bhavanapadu), and anchoring industrial nodes along the Visakhapatnam-Chennai (VCIC) and Chennai-Bengaluru (CBIC) Industrial Corridors.",
    "img": {"url": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Polavaram_Project_Dam_construction.jpg", "caption": "Polavaram National Irrigation Project on the Godavari River, Andhra Pradesh's lifeline for multi-basin water security.", "alt": "Polavaram Project Godavari Dam"},
    "table": {
      "caption": "Major Maritime Ports & Industrial Corridors in Andhra Pradesh",
      "headers": ["Infrastructure Asset / Node", "Geographical Location / Reach", "Operational Status & Scale", "Strategic Economic Contribution"],
      "rows": [
        ["Visakhapatnam Port Authority (VPA)", "Visakhapatnam District", "Major Port under Central Port Authority Act; handles 75+ MMT cargo", "Key eastern seaboard maritime hub for coal, iron ore, crude oil, and container freight"],
        ["Krishnapatnam Port", "SPSR Nellore District", "Deep-water private port operated by Adani Ports; 18.5 m draft", "Handles heavy dry bulk and container cargo serving South AP, Bengaluru, and Chennai hinterlands"],
        ["Ramayapatnam Port", "Prakasam District", "Greenfield non-major port under AP Maritime Board", "Serves industrial clusters of central Andhra Pradesh and granite export belts"],
        ["Machilipatnam Port & Mulapeta Port", "Krishna District & Srikakulam District", "Under active development by AP Maritime Board", "Catalyzes deltaic cargo evacuation, pharma logistics, and north coastal manufacturing"],
        ["Visakhapatnam-Chennai Corridor (VCIC)", "Spans coastal AP (9 districts)", "India's first coastal corridor under ADB financing; nodes at Vizag, Kakinada, Srikalahasti", "Promotes export-oriented electronics, auto components, pharma, and petrochemical clusters"],
        ["Chennai-Bengaluru Corridor (CBIC)", "Krishnapatnam & Orvakal nodes", "National Industrial Corridor Development Corporation (NICDC)", "Fosters manufacturing linkages between Rayalaseema, Chennai port, and Bengaluru tech hubs"]
      ]
    },
    "points": [
      "Polavaram Irrigation Project (National Project): Declared a National Project under Section 90 of the AP Reorganisation Act 2014. Located on the Godavari river at Polavaram, it creates an irrigation potential of 7.2 lakh acres, diverts 80 TMC of Godavari water to the Krishna basin, generates 960 MW hydro power, and provides 23.44 TMC drinking water to Visakhapatnam.",
      "Rayalaseema Drought Mitigation Projects: Includes the Handri-Neeva Sujala Sravanthi (HNSS), Galeru-Nagari Sujala Sravanthi (GNSS), and Veligonda Project designed to lift Krishna floodwaters from Srisailam reservoir to arid Rayalaseema and Prakasam uplands.",
      "Aquaculture & Marine Dominance: Andhra Pradesh contributes over 70% of India's farmed shrimp (Litopenaeus vannamei) exports. Aquaculture clusters in West Godavari, Krishna, and Bapatla generate massive rural employment and foreign exchange.",
      "Horticulture Expansion: Known as the 'Fruit Bowl of the South', AP ranks first nationally in the production of oil palm, chillies, cocoa, lime, and tomato, alongside significant banana and mango yields.",
      "Flagship Welfare & Farmer Schemes: The Rythu Bharosa / Annadata Sukhibhava income support scheme supplements central PM-KISAN funds with state top-ups. Free crop insurance, Rythu Bharosa Kendras (RBKs) as village-level input supply kiosks, and subsidized power for aquaculture and farm pump sets form the cornerstone of rural outreach."
    ],
    "mains": [
      "Examine the socio-economic and regional development significance of the Polavaram Multipurpose Project for Andhra Pradesh. What environmental and rehabilitation challenges (R&R) surround its execution? (250 Words, 15 Marks)",
      "Discuss the concept of 'Port-Led Development' in the context of Andhra Pradesh's 974 km coastline. How can industrial corridors like VCIC and CBIC integrate with non-major ports to accelerate state manufacturing? (200 Words, 10 Marks)"
    ],
    "mcqs": [
      {
        "id": "MCQ-ECO10-01",
        "q": "Under which section of the Andhra Pradesh Reorganisation Act, 2014 was the Polavaram Multipurpose Project declared a National Project?",
        "options": ["Section 45", "Section 75", "Section 90", "Section 108"],
        "ans": "c",
        "explanation": "Section 90 of the Andhra Pradesh Reorganisation Act 2014 explicitly declares the Polavaram Irrigation Project to be a National Project, where the Central Government is responsible for executing and funding the project."
      },
      {
        "id": "MCQ-ECO10-02",
        "q": "What is the approximate total length of Andhra Pradesh's coastline, making it the second-longest mainland coastline in India after Gujarat?",
        "options": ["720 km", "850 km", "974 km", "1,050 km"],
        "ans": "c",
        "explanation": "Andhra Pradesh has a coastline of approximately 974 km along the Bay of Bengal, the second-longest coastline among mainland Indian states after Gujarat."
      },
      {
        "id": "MCQ-ECO10-03",
        "q": "Which international multilateral bank provided primary financial and technical support for developing the Visakhapatnam-Chennai Industrial Corridor (VCIC)?",
        "options": ["World Bank", "Asian Development Bank (ADB)", "Asian Infrastructure Investment Bank (AIIB)", "New Development Bank (NDB)"],
        "ans": "b",
        "explanation": "The Asian Development Bank (ADB) is the primary multilateral development partner funding and supporting the development of the Visakhapatnam-Chennai Industrial Corridor (VCIC), India's first coastal economic corridor."
      },
      {
        "id": "MCQ-ECO10-04",
        "q": "Which greenfield port in Srikakulam district was renamed 'Mulapeta Port' by the Government of Andhra Pradesh?",
        "options": ["Kalingapatnam Port", "Bhavanapadu Port", "Machilipatnam Port", "Ramayapatnam Port"],
        "ans": "b",
        "explanation": "The Bhavanapadu Port in Santhabommali mandal of Srikakulam district was officially rechristened as Mulapeta Port by the Government of Andhra Pradesh."
      },
      {
        "id": "MCQ-ECO10-05",
        "q": "What major industrial node under the Chennai-Bengaluru Industrial Corridor (CBIC) is situated in the Kurnool district of Andhra Pradesh?",
        "options": ["Donakonda Node", "Orvakal Industrial Node", "Srikalahasti Node", "Kopparthy Node"],
        "ans": "b",
        "explanation": "The Orvakal Industrial Hub in Kurnool district is developed as a major manufacturing mega industrial node under the Chennai-Bengaluru Industrial Corridor (CBIC)."
      }
    ]
  }
]

for t in topics:
  content_blocks = [
    {"type": "heading", "level": 1, "text": t["title"]},
    {"type": "paragraph", "text": t["intro"]},
    {"type": "image", "url": t["img"]["url"], "caption": t["img"]["caption"], "alt_text": t["img"]["alt"]},
    {"type": "heading", "level": 2, "text": "1. Macroeconomic Framework & Indicators"},
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
    "subject_title": "Economy - India & AP",
    "paper": "Mains Paper-IV & Screening Paper-II",
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

# Clean up old lumped files in 06_Economy_India_and_AP
old_files = [
  "01_challenges_of_indian_economy.json",
  "02_resource_mobilization_monetary_fiscal_policy.json",
  "03_government_budgeting_finance_commissions.json",
  "04_inclusive_growth_social_welfare.json",
  "05_agriculture_and_rural_development_india_ap.json",
  "06_industrial_development_infrastructure_india_ap.json"
]
for f in old_files:
  p = os.path.join(SUBJ_DIR, f)
  if os.path.exists(p):
    os.remove(p)
    print(f"Removed old file: {f}")

print("Subject 6 is fully segregated into 10 topics with 50 MCQs!")
