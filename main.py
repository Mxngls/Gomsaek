from src.Request import Requests as R
from src.Display import Displayer as D
from src.Parser import xml_parser
from src.CreateNote import Creator as C
from pprint import pprint

def main():

    inp = input('What word are you looking for: ')

    search_result = R().search_request(inp)
    target_codes = D().display_search_results(search_result)

    inp = int(input('Create a flash card for word number: '))
    view_data = R().view_request(target_codes[int(inp)][1])
    vocab = xml_parser(view_data)

    if 'Korean Learners Dictionary' not in C().invoke('deckNames'):
        C().invoke('createDeck', deck='Korean Learners Dictionary')

    C().invoke('addNote', note = {
            "deckName": 'Korean Learners Dictionary',
            "modelName": "Basic English Dictionary",
            "fields": {
                "hangul": vocab[0][0]['hangul'],
                "translation": vocab[0][1][target_codes[inp][2]]['translation'],
                "definition": vocab[0][1][target_codes[inp][2]]['definition'],
                "examples": ('').join(vocab[0][1][target_codes[inp][2]]['examples']),
                "tags": vocab[0][0]['vocabularyLevel'] + ' | ' + vocab[0][0]['subjectCategory']
            },
            "options": {
                "allowDuplicate": False,
                "duplicateScope": "deck",
                "duplicateScopeOptions": {
                    "deckName": "Korean Learners Dictionary",
                    "checkChildren": False
                }
            },
            "tags": [
                "Test"]
            })

if __name__ == '__main__':
    main()