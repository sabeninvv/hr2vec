# hr2vec

### Description:
##### Search for similarities between the ideal job profile and potential candidate.
```
ideal_profile.json => parse 
candidates_profiles.json => parse
            ||
            \/
search for similarities => ranging => save .json
```
___
### Steps packages installation:
```
- pip3 install numpy
- pip3 install torch==1.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
- pip3 install gensim
- pip3 install stanfordnlp
- pip3 install tqdm
```

```
I advise you to use anaconda or virtual environments
```
___
### Rules:
- profile.txt:
    - write requirements for the candidate clearly
    - do not use abbreviations
    - at the top indicate who you are looking (no title)
    - headings should be separated by a sign ":"
    - required headers:
        - Industry
        - Education
        - Work Experience
- candidates.json:
    - required headers:
        - industry
        - education
        - workExperience
___
### Examlpe profile.txt:
```
Looking for experienced Carrier Account manager for Supply chain and logistics client in Singapore
...any text
...any text

Job Summary:
...any text
...any text

Duties and Responsibilities:
...any text
...any text

Roles and Responsibility of Carrier Account Manager by Area of Carrier engagement in priority of ownership:
...any text
...any text

Education:
Bachelor of Arts / Bachelor of Science. 
Master of Science / master of business administration in Business.
International Business.

Industry:
Shipping

Work Experience:
Sales / Account Management. 10.
Ocean Carrier Sales
Customer Service Processes.
selling Enterprise Software for cross functions within the customer
Experience selling e-Commerce/Information Technologies solutions positioning
value added ecommerce solution provider.

Skills and Qualities:
...any text
...any text

Special Work Requirements:
...any text
...any text
```
___
### Examlpe candidates.json:
```
{
    "id": "is",
    "firstName": "firstName",
    "lastName": "lastName",
    "location": "location",
    "headline": "Business Development , Account management , AI & Data Analyst ",
    "summary": "I have a very good client relationship across regions with customers and am a go getter for business. I coach and encourage teamwork to ensure the company\u00e2\u20ac\u2122s goals are achieved and demonstrate team player skills. \n\nI have experience in SAS enterprise products to seek inference of valuable data to plan strategies. I make practical recommendations that drive business create value and impact to stakeholders.\n\nI lead a team specializing in New Business Acquisition. Overall Customer management, I leverage my relationships to generate business effectively from Fintech, Logistics, Banking, Agro, Medical, Shipping, Hospitality, Aviation, Manufacturing, Pharma, Aviation oil and gas, Information Technology, Real-estate and Biotech Industries. I am responsible to coach the team developing skills to achieve sales targets.  I validate potential pipeline opportunities using Business Data Analytics that develops business globally by increasing % of opportunities quickly resulting in profitable business.\n\nSkills:  Salesforce CRM, Oracle ERP, Cloud, SaaS \n\nI collaborate with stakeholders to provide specialist strategies in determining appropriate analytic techniques and solutions to achieve maximum revenue and profitability goals.\n\n",
    "industry": "Logistics and Supply Chain",
    "workExperience": [
        {
            "title": " Business Development , Account Management and AI Analytics",
            "location": "Singapore",
            "startedOn": {
                "year": 2018,
                "month": 8
            },
            "companyName": " Prism Mobility Pte",
            "description": "Highlights   : Business Development, Supply Chain Strategy/Sales & Operations Planning :\n\n\u00e2\u20ac\u00a2Interest in: Category Management, Control Tower, Supply Chain Strategy/Sales & Operations Planning Transportation & Warehouse Management\n\n\u00e2\u20ac\u00a2Excellent client relationship across regions with customers.\n\u00e2\u20ac\u00a2I have excellent communication skill and good command over language, I have a very pleasing personality,\n\u00e2\u20ac\u00a2Encourage teamwork to ensure the company\u00e2\u20ac\u2122s goals are achieved and demonstrate team player skills \n\u00e2\u20ac\u00a2Ability in SAS enterprise products to seek inference of valuable data to plan strategies. I make practical recommendations that drive business create value and impact to stakeholders.\n\u00e2\u20ac\u00a2Collaborate with stakeholders to provide specialist strategies in determining appropriate analytic techniques and solutions to achieve maximum revenue and profitability goals.\n\u00e2\u20ac\u00a2New Business Acquisition. Overall Customer management, I leverage my relationships to generate business effectively from Fintech, Logistics, Banking, Medical, Shipping, Hospitality, Aviation, Manufacturing, Retail, Pharma, oil and gas, Information Technology, Real-estate and Biotech Industries.\n\u00e2\u20ac\u00a2Review Reports with top Management and track revenue by co coordinating with finance teams\n\u00e2\u20ac\u00a2Jointly plan an operations Strategy, approve sale documentation & contracts.\n\u00e2\u20ac\u00a2Validate potential pipeline opportunities using Business Data Analytics globally by increasing % of opportunities to win resulting in profitable business.\n\n\u00e2\u20ac\u00a2Key Skills: Oracle PL SQL -  Salesforce CRM, SaaS, Global Mobility Sales specialist, Corporate Sales, New Business Development, Team Management, Team Handling, Cloud Management, Sales Management, Team Leadership, Direct Sales, Consulting, Incentive and People Management, ability to analyse, model and interpret data.   \n"
        },
        {
            "title": "Head Business Development and Sales  - India and South East Asia",
            "endedOn": {
                "year": 2017,
                "month": 11
            },
            "location": "Bengaluru Area, India",
            "startedOn": {
                "year": 2011,
                "month": 9
            },
            "companyUrn": "urn:li:fs_salesCompany:2583373",
            "companyName": "Santa Fe Group",
            "description": "Effectively managed end-to-end business development, marketing and sales activities.\nResponsible for generating business across the region that is profitable\nImplemented the strategies, change management aligned with Global Corporate initiatives.\nHandled strategic planning, deciding on hiring, budget & cost. \nLed the sales activities, empowered team in comprehensive sales discussions and demos, enabling clients to take faster decisions, thereby meeting revenue targets.\nI effectively managed end-to-end business development, marketing and sales activities \nImplemented the strategies, change management aligned with Global Corporate initiatives."
        },        
    ],
    "education": [
        {
            "degree": "Master of Business Administration - MBA",
            "endedOn": {
                "year": 2007
            },
            "startedOn": {
                "year": 2000
            },
            "schoolName": "Madurai Kamraj University, Madurai",
            "fieldsOfStudy": [
                "Marketing and Data analytics"
            ]
        }
    ],
    "skills": [
        {
            "name": "CRM",
            "numOfEndorsement": 6
        }
    ],
    "coursesTaken": [],
    "languages": [
        {
            "name": "English"
        }
    ],
    "awards": [
        {
            "title": "Sales Achivement awards",
            "issuer": "Santafe",
            "issuedOn": {
                "year": 2013
            },
            "description": "Sales Achivement Award ."
        }
    ],
    "emails": [
        {
            "dataSource": "LINKEDIN",
            "emailAddress": "emailAddress"
        }
    ],
    "phoneNumbers": null,
    "websites": [
        {
            "url": "www.prism-mobility.com",
            "category": "PERSONAL",
            "dataSource": "LINKEDIN"
        }
    ],
    "socialAccounts": [
        {
            "linkedin": "https://www.linkedin.com/in/"
        }
    ],
    "linkedinPremium": false
}
```