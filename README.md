# hr2vec

### Description:
##### Search for similarities between the ideal job profile and potential candidate.
```
ideal_profile.txt => parse 
candidates_profiles.json => parse
            ||
            \/
search for similarities => ranging => save .csv/.json
```
___
### Packages installation:
```
- pip3 install numpy
- pip3 install tqdm
- pip3 install torch==1.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
- pip3 install gensim
- pip3 install stanfordnlp
```

```
I advise you to use anaconda or virtual environments
```
___
### Models download:
- Upload and put in models/gensim/:
    - [numberbatch-en-19.08.txt.gz](https://conceptnet.s3.amazonaws.com/downloads/2019/numberbatch/numberbatch-en-19.08.txt.gz)
- Upload and put inmodels/stanfornlp/en_ewt_models/:
    - [all files .pt](http://nlp.stanford.edu/software/stanfordnlp_models/0.2.0/en_ewt_models.zip)
___
### Rules:
- Files Must be:
    - data/profile.txt
    - data/candidates.json
    - models/gensim/numberbatch-en-19.08.txt.gz
    - models/stanfornlp/en_ewt_models/en_ewt.pretrain.pt
    - models/stanfornlp/en_ewt_models/en_ewt_lemmatizer.pt
    - models/stanfornlp/en_ewt_models/en_ewt_parser.pt
    - models/stanfornlp/en_ewt_models/en_ewt_tagger.pt
    - models/stanfornlp/en_ewt_models/en_ewt_tokenizer.pt
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
### Example profile.txt:
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
### Example candidates.json:
```
{
    "id": "is",
    "firstName": "firstName",
    "lastName": "lastName",
    "location": "location",
    "headline": "Business Development , Account management , AI & Data Analyst ",
    "summary": "...any text...\n\n",
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
            "description": "...any text...\n"
        },
        {
            "title": "Head Business Development and Sales ...any text...",
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
            "description": "...any text..."
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
### Run from cmd/powershell/another:
```
python main.py
```