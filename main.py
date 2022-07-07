import requests as re
from bs4 import BeautifulSoup as BS
from requests.api import request
from requests.models import Response
import pandas as pd

try:
    requests_data = re.get('https://icdcodelookup.com/icd-10/common-codes')
    soup = BS(requests_data.content, 'html.parser')

    a_set = set()
    code_set = set()
    li_list = []
    keys_list = []
    final_dict = {}
    list_for_dic = []
    list_of_last_word = []
    for specialty in soup.findAll('ul', class_="specialtyList"):

        for li_list in specialty.findAll('li'):

            for a_list in li_list.findAll('a'):
                a_set.add('https://icdcodelookup.com/' + str(a_list['href']))


    for url in a_set:
        list_of_last_word.append(url.rsplit('/', 1)[-1])
        print(f"This is heading {url.rsplit('/', 1)[-1]}" )

    result_dictionary = dict.fromkeys(list_of_last_word)



    for url in a_set:

        r = re.get(url)
        soup_ = BS(r.text, 'html.parser')
        chapter_list_class_data = soup_.findAll('div', class_='code')

        for span in chapter_list_class_data:
            list_for_dic.append(span.find('span').text)

        result_dictionary[url.rsplit('/', 1)[-1]] = list_for_dic
        list_for_dic = []

    # for x in result_dictionary:
        # print(x, '=> ',result_dictionary[x])
        # print("\n*******************************************************************\n")

    df = pd.DataFrame.from_dict(result_dictionary, orient='index')
    df = df.transpose()
    # df = pd.DataFrame(result_dictionary)
    print(df)
    df.to_csv('scrapped_specialty_icds.csv')

    # print(result_dictionary)
    # print(len(result_dictionary))

    # print(len(a_set))

    # r = re.get(a_set.pop())
    # print(r.url)

    # print("**************************************************************************************")
    # requests_data1 = re.get(r.url, 'html.parser')
    # soup1 = BS(requests_data1.text, 'html.parser')
    # chapter_list_class_data = soup1.findAll('div', class_='code')

    # for span in chapter_list_class_data:

    #     code_set.add(span.find('span').text)
    
    # last_word = r.url.rsplit('/', 1)[-1]
    # print(r.url.rsplit('/', 1)[-1])
    # keys_list.append(r.url.rsplit('/', 1)[-1])
    # final_dict[r.url.rsplit('/', 1)[-1]] = None    

    # for icd_10 in code_set:
 
    #     list_for_dic.append(icd_10)


    # final_dict[last_word] = list_for_dic 

    # print(len(final_dict[last_word]))



except Response.raise_for_status as e:
    print(e)
 
