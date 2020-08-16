import numpy as np
import pandas as pd
from tqdm import tqdm
import datetime
import warnings
import json
from gensim.models import KeyedVectors
import stanfordnlp
warnings.simplefilter("ignore")


def load_gensim_model(path, binary=False):
    print('Loading Gensim Model. Wait 10-15 minutes')
    model = KeyedVectors.load_word2vec_format(path, binary=True, unicode_errors='ignore') if binary \
                                                        else KeyedVectors.load_word2vec_format(path)
    print('Done loading Gensim Model!')
    print('---')
    return model


def load_stanfordnlp_model(path, lang='en'):
    nlp = stanfordnlp.Pipeline(lang=lang,
                               use_gpu=False,
                               processors='tokenize,mwt,pos,lemma,depparse',
                               pos_batch_size=1000,
                               models_dir=path)
    return nlp


def load_profile(nlp, path=r'data/profile.txt'):
    with open(path, mode='r', encoding='utf8') as f:
        profile = {}
        block = []
        key = 'start'
        for row in f:
            if ':' in row:
                profile[key] = block
                key = replacing_char(row)
                block = []
            else:
                if row != '\n':
                    row = replacing_char(row)
                    row = str2lemma(nlp, row)
                    block.append(row)
    return profile


def file_operation(path, write=False, data=None):
    mode = 'w' if write else 'r'
    with open(path, mode=mode, encoding='utf8') as f:
        if write:
            json.dump(data, f)
        else:
            data = json.load(f)
    return data


def parse_education(nlp, data):
    if not data:
        return 0
    new_data = []
    for block in data:
        if block and 'fieldsOfStudy' in block.keys() and block['fieldsOfStudy']:
            field = block['fieldsOfStudy'][0]
            field = replacing_char(field)
            field = str2lemma(nlp, field)
            new_data.append(field)
        if block and 'degree' in block.keys() and block['degree']:
            degree = block['degree']
            degree = replacing_char(degree)
            degree = str2lemma(nlp, degree)
            new_data.append(degree)
    if new_data:
        return new_data
    else:
        return 0


def parse_industry(nlp, data):
    if not data:
        return 0
    industry = data
    industry = replacing_char(industry)
    industry = str2lemma(nlp, industry)
    if industry:
        return industry
    else:
        return 0


def parse_workExperience(nlp, data):
    if not data:
        return 0
    new_data = []
    for block in data:
        if block and 'title' in block.keys() and block['title']:
            exp = 0

            title = block['title']
            title = replacing_char(title)
            title = title.split('-')[0]  # <=======
            title = str2lemma(nlp, title)
            if 'startedOn' in block.keys() and block['startedOn']:
                start = int(block['startedOn']['year'])
                if 'endedOn' in block.keys():
                    finish = int(block['endedOn']['year'])
                else:
                    finish = datetime.datetime.now().year
                exp = finish - start if finish - start != 0 else 1
            #             new_data.append([title, exp])
            new_data.append(title)
    if new_data:
        return tuple(new_data)
    else:
        return 0


def replacing_char(sentence):
    sentence = sentence.replace('\n', '')
    sentence = sentence.replace("'", ' ')
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')
    sentence = sentence.replace('&', '')
    sentence = sentence.replace('and', '')
    sentence = sentence.replace('/', ' ')
    sentence = sentence.replace('/', ' ')
    sentence = sentence.replace('+', ' ')
    sentence = sentence.replace('(', ' ')
    sentence = sentence.replace(')', ' ')
    sentence = sentence.replace('-', ' ')
    sentence = sentence.replace(';', '')
    sentence = sentence.replace(':', '')
    sentence = sentence.replace('  ', ' ').lower()
    return sentence


def str2lemma(nlp, sentence):
    new_sentence = []
    try:
        doc = nlp(sentence)
        for i in doc.sentences[0].words:
            if i.upos not in ['ADP', 'DET', 'PUNCT', 'SYM', 'PRON', 'NUM', 'CCONJ', 'PART']:
                if len(i.lemma) > 2:
                    new_sentence.append(i.lemma)
    except:
        pass
    return set(new_sentence)


def get_similarity(model, profile_fichs, resume_fiths):
    matrix = []
    for row in profile_fichs:
        temp = []
        for column in resume_fiths:
            try:
                t = model.n_similarity(set(row), set(column))
                temp.append(t)
            except:
                continue
        if temp:
            matrix.append(temp)
    if matrix:
        matrix = np.array(matrix)
        range_coef = np.median(matrix, axis=1)
        range_coef = np.median(range_coef)
        return range_coef
    else:
        return 0


def parse_all(model, nlp, data, profile):
    data_parsed = []
    for resume in tqdm(data[:]):
        temp_list = []

        parse = parse_industry(nlp=nlp, data=resume['industry'])
        try:
            temp_list.append(get_similarity(model=model, profile_fichs=profile['industry'], resume_fiths=parse))
        except:
            temp_list.append(0)

        parse = parse_education(nlp=nlp, data=resume['education'])
        try:
            temp_list.append(get_similarity(model=model, profile_fichs=profile['education'], resume_fiths=parse))
        except:
            temp_list.append(0)

        parse = parse_workExperience(nlp=nlp, data=resume['workExperience'])
        try:
            temp_list.append(get_similarity(model=model, profile_fichs=profile['work experience'], resume_fiths=parse))
        except:
            temp_list.append(0)

        data_parsed.append(temp_list)

    data_parsed = np.array(data_parsed)
    return data_parsed


def save2csv(candidates, koef, sort_inxs, max_candidates):
    sort_inxs = sort_inxs[::-1]
    sort_inxs = sort_inxs[:max_candidates]

    df = pd.DataFrame(columns=['First Name', 'Last Name', 'Title', 'Company Name', 'LinkedIn', 'Score'])

    for inx in sort_inxs:
        try:
            firstName = candidates[inx]['firstName']
        except:
            firstName = ''

        try:
            lastName = candidates[inx]['lastName']
        except:
            lastName = ''

        try:
            title = candidates[inx]['workExperience'][0]['title']
        except:
            title = ''

        try:
            companyName = candidates[inx]['workExperience'][0]['companyName']
        except:
            companyName = ''

        try:
            account = candidates[inx]['socialAccounts'][0]['linkedin']
        except:
            account = ''

        df = df.append({'First Name': firstName,
                        'Last Name': lastName,
                        'Title': title,
                        'Company Name': companyName,
                        'LinkedIn': account,
                        'Score': round(koef[inx] * 100, 1)}, ignore_index=True)

    df.to_csv('data/sorted_candidates.csv', mode='w', index=True, sep='|', encoding='utf8')


def sort_and_save_data(parse, candidates, koef_industry=1., koef_education=0.8, koef_workExperience=1.,
                       max_candidates=20, save_json=False):
    for inx in range(parse.shape[-1]):
        parse[:, inx] = (parse[:, inx] - parse[:, inx].min()) / (parse[:, inx].max() - parse[:, inx].min())
    koef = parse[:, 0] * koef_industry + parse[:, 1] * koef_education + parse[:, 2] * koef_workExperience
    koef /= 3.
    sort_inxs = np.argsort(koef)
    save2csv(candidates=candidates, koef=koef, sort_inxs=sort_inxs, max_candidates=max_candidates)
    if save_json:
        new_data = []
        inx = -1
        while inx != -len(sort_inxs):
            new_data.append(candidates[sort_inxs[inx]])
            inx -= 1
        _ = file_operation(path=r'data/sorted_candidates.json', write=True, data=new_data)
    print('Done Saving successful!')
