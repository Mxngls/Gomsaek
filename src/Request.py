import requests as r
import xml.etree.ElementTree as ET

class Requests:

    def search_request(self, word):

        search_params = {
        'key': '',
        'q': word,
        'sort': 'popular',
        'translated': 'y',
        'trans_lang': '1'
        }
        search_response = r.get('https://krdict.korean.go.kr/api/search' , search_params)
        search_result = search_response.text
        search_result_stripped = "\n".join([ll.rstrip() for ll in search_result.splitlines() if ll.strip()])
        search_data = ET.fromstring(search_result_stripped)
        # You can create an XML-file to examine the data retrieved from the API.
        # ET.ElementTree(element=search_data).write(open('search_data.xml', 'a'), encoding='unicode')

        return search_data

    def view_request(self, target_code):

        view_params = {
        'key': '',
        'method': 'target_code',
        'q': target_code,
        'translated': 'y',
        'trans_lang': '1'
        }
        view_response = r.get('https://krdict.korean.go.kr/api/view' , view_params)
        view_result = view_response.text
        view_result_stripped = "\n".join([ll.rstrip() for ll in view_result.splitlines() if ll.strip()])
        view_data = ET.fromstring(view_result_stripped)
        # You can create an XML-file to examine the data retrieved from the API.
        # ET.ElementTree(element=view_data).write(open('view_data.xml', 'a'), encoding='unicode')

        return view_data


