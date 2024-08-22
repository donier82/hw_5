from bs4 import BeautifulSoup
import requests   

count_news = 0
with open("kg_news.txt", "a", encoding='utf-8') as file:
    for page in range(1, 21):
        url = f'https://24.kg/page_{page}'
        response = requests.get(url=url)
                # print(response)

        soup = BeautifulSoup(response.text, 'lxml')
                            
        all_news = soup.find_all('div', class_='title')           
        
                                

    # for kg_news in all_news:
    #     count_news += 1
    #     file.write(kg_news.text) 
    #     kg_news.text
       
       
                          
                          
                          
                     


                        # print(count_news, news.text)
                        # pars_news=count_news, news.text

                    #     # print(pars_news)
