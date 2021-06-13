import xml.etree.ElementTree as ET

class Displayer:

    def display_search_results(self, search_data):
        c = 0
        target_codes = []
        for i, item in enumerate(search_data.findall('item')):
            for sense in item.findall('sense'):
                word = item.find('word').text
                sense_ord = sense.find('sense_order').text
                eng = sense.find('translation').find('trans_word').text
                print(f"{c:<2} {word:\u3164<6}"+f"eng({sense_ord}):{eng}")
                target_codes.append([c, search_data.findall('item')[i].find('target_code').text, int(sense_ord)-1])
                c += 1
        return target_codes