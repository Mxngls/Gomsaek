# Gomsaek
A small python scripts that works with the API of the Korean Learners Online Dictionary and lets you look up words from and immediately create Anki flash cards for them.

## Introduction
Just as another [script](https://github.com/Mxngls/Amgi) I wrote some days ago this one as well extends the functionality of the [Korean Learners Online Dictionary; KLOD](https://krdict.korean.go.kr/eng/dicSearchDetail/searchDetailActCategory?nation=eng&nationCode=6&searchFlag=N&sort=W&currentPage=1&ParaWordNo=&syllablePosition=&actCategoryList=&all_gubun=ALL&gubun=W&gubun=P&gubun=E&all_wordNativeCode=ALL&wordNativeCode=1&wordNativeCode=2&wordNativeCode=3&wordNativeCode=0&all_sp_code=ALL&sp_code=1&sp_code=2&sp_code=3&sp_code=4&sp_code=5&sp_code=6&sp_code=7&sp_code=8&sp_code=9&sp_code=10&sp_code=11&sp_code=12&sp_code=13&sp_code=14&sp_code=27&all_imcnt=ALL&imcnt=1&imcnt=2&imcnt=3&imcnt=0&all_multimedia=ALL&multimedia=P&multimedia=I&multimedia=V&multimedia=A&multimedia=S&multimedia=N&searchSyllableStart=&searchSyllableEnd=&searchOp=AND&searchTarget=word&searchOrglanguage=all&wordCondition=wordAll&query=&myViewWord=25039). For more information about [Anki](https://apps.ankiweb.net/) or the KLOD please refer to their respective websites or the other script mentioned where I introduce both of them very briefly.

## Prerequisites
In order connect to the API of the KLOD you have at first create an account at the [website](https://krdict.korean.go.kr/login/login) of the National Institute of the Korean Language. It's in Korean, but it's not too hard if you just use a common tool like [Google Translate](https://translate.google.de/) or [Papago](https://papago.naver.com/?sk=ko&tk=en). Then you need to apply to their API service and receive a key that lets you connect to their API.

In addition you should have Python (I used 3.9 but it should work up with older ones as well) as well as the [Anki Connect](https://github.com/FooSoft/anki-connect) addon for Anki.

## Installation
Just click on the big green button on upper right corner or run:

```git clone https://github.com/mxngls/Gmail-Cleaner.git```

Then open 'Request.py' and add the received key to the request parameters (I left it just empty).

## Usage
From the Gomsaek directory run: ```python3 main.py```

You will be prompted to type in the name of the word that you want to look up. You will then be provided with a list of results and prompted to choose one of them. Gomsaek will then automatically create an Anki flash card for it (be aware that Anki needs to be open when you run Gomsaek in order to be able to create flash cards).

See this example for the flash cards to be created: https://user-images.githubusercontent.com/59572969/121784451-5117d400-cbb4-11eb-8eb9-ff743828a6a6.jpeg

## Lisence
This project is licensed under the terms of the MIT license.
