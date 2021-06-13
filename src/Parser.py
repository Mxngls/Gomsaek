import xml.etree.ElementTree as ET

def xml_parser(view_data):

    # Set an XML-tree and its root.
    root = view_data

    # Create an empty list to store the dictionary entries in and create a counter for each entry.
    vocab = []
    counter = 0

    # Start iterating over all the entries.
    for item in root.findall('item'):
            vocab.append([])
            if int(item.find('word_info').find('sup_no').text) > 0:
                vocab[counter] = [{'hangul': item.find('word_info').find('word').text + f"<sup style='font-size: 75%'>{item.find('word_info').find('sup_no').text}</sup"}]
            else:
                vocab[counter] = [{'hangul': item.find('word_info').find('word').text}]
            vocab[counter][0]['id'] = item.find('target_code').text
            vocab[counter][0]['vocabularyLevel'] = item.find('word_info').find('word_grade').text        
            vocab[counter][0]['wordForm'] = [item.find('word_info').find('word').text]
            for conj in item.find('word_info').findall('conju_info'):
                vocab[counter][0]['wordForm'].append(conj.find('conjugation_info').find('conjugation').text)
            vocab[counter][0]['subjectCategory'] = item.find('word_info').findall('category_info')[0].find('written_form').text 
            if item.find('word_info').find('pos').text == '동사' or item.find('word_info').find('pos').text == '형용사':
                for conj in item.find('word_info').findall('conju_info'):
                    vocab[counter][0]['wordForm'].append(conj.find('conjugation_info').find('conjugation').text)        

            vocab[counter].append([])
            conv = False

            for i, senseInfo in enumerate(item.find('word_info').findall('sense_info')):
                vocab[counter][1].append({})
                vocab[counter][1][i]['sense_id'] = i
                vocab[counter][1][i]['translation'] = senseInfo.find('translation').find('trans_word').text
                vocab[counter][1][i]['definition'] = senseInfo.find('translation').find('trans_dfn').text
                vocab[counter][1][i]['krDefintion'] = senseInfo.find('definition').text
                vocab[counter][1][i]['examples'] = []
                for j, example in enumerate(senseInfo.findall('example_info')):
                    for word in vocab[counter][0]['wordForm']:
                        if example.find('type').text == '구':
                            example_1 = f'''    <li>{example.find('example').text.replace(word, f'<span style="color: #9400D3">{word}</span>')}</li>'''
                            vocab[counter][1][i]['examples'].append(example_1)
                            break
                        elif example.find('type').text == '대화':
                            if conv == False:
                                example_1 = f'''    <li>나: {senseInfo.findall('example_info')[j].find("example").text.replace(word, f'<span style="color: #9400D3">{word}</span>')}'''
                                example_2 = f'''너: {senseInfo.findall('example_info')[j+1].find("example").text.replace(word, f'<span style="color: #9400D3">{word}</span>')}</li>'''
                                ex = example_1 + '</br>' + example_2
                                vocab[counter][1][i]['examples'].append(ex)
                            conv = True
                conv = False

    return vocab