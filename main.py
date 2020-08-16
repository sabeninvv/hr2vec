import tools

def main():
    # nlp = tools.load_stanfordnlp_model(path=r'models/stanfornlp')
    # model = tools.load_gensim_model(path=r'models/gensim/numberbatch-en-19.08.txt.gz')

    nlp = tools.load_stanfordnlp_model(path=r'models/stanfornlp_rus', lang='ru')
    model = tools.load_gensim_model(path=r'models/gensim_rus/all.norm-sz100-w10-cb0-it1-min100.w2v', binary=True)


    profile = tools.load_profile(nlp=nlp)
    candidates = tools.file_operation(path=r'data/candidates.json')
    parsed_data = tools.parse_all(model=model, nlp=nlp, data=candidates, profile=profile)
    tools.sort_and_save_data(parse=parsed_data, candidates=candidates,
                             koef_industry=1., koef_education=0.8, koef_workExperience=1.,
                             max_candidates=20, save_json=False)


if __name__ == '__main__':
    main()
