import tools

def main():
    nlp = tools.load_stanfordnlp_model(path=r'models\stanfornlp')
    model = tools.load_gensim_model(path=r'models\gensim\numberbatch-en-19.08.txt.gz')

    profile = tools.load_profile(nlp=nlp)
    candidates = tools.file_operation(path=r'data\candidates.json')
    parsed_data = tools.parse_all(model=model, nlp=nlp, data=candidates, profile=profile)
    tools.sort_and_save_data(parse=parsed_data, candidates=candidates,
                             koef_industry=1., koef_education=0.8, koef_workExperience=1.)


if __name__ == '__main__':
    main()
