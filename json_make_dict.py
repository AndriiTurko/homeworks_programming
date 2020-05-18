import json 

def json_read(path):
    '''
    Parses file of json type. 
    '''
    with open(path, 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text


def conti_with_count():
    names = json_read('names.json')
    continents = json_read('continent.json')
    result = {}
    for country in continents:
        if continents[country] not in result:
            result[continents[country]] = [names[country]]
        else:
            result[continents[country]].append(names[country])
    
    return result
