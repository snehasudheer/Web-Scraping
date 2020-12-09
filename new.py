import requests
import csv
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup



html = requests.get('https://www.airbnb.co.in/s/Kochi--Kerala/homes?tab_id=all_tab&refinement_paths%5B%5D=%2Fhomes&query=Kochi%2C%20Kerala&place_id=ChIJv8a-SlENCDsRkkGEpcqC1Qs&checkin=2020-06-18&checkout=2020-07-31&source=structured_search_input_header&search_type=search_query')
#bs = BeautifulSoup(html.content, "html.parser")
file= "proj.csv"
base_url='https://www.airbnb.co.in/s/Kochi--Kerala/homes?tab_id=home_tab&amp;refinement_paths%5B%5D=%2Fhomes&amp;place_id=ChIJv8a-SlENCDsRkkGEpcqC1Qs&amp;source=structured_search_input_header&amp;search_type=pagination&amp;federated_search_session_id=c479fe18-754b-424f-8ce1-9c1af4983774&amp;query=Kochi%2C%20India&amp;section_offset=3&amp;items_offset='
base='https://www.airbnb.co.in'




    
    #next_page=bs.find_all("a",attrs = {'class': '_13n1po3b'})
    #print(next_page)
label=[]
hrefText=[]
price=[]
text=[]
ff=[]
rate=[]
price_num=[]
rate_num=[]
ppl=[]
people=[]
info=[]
bed=[]
bathroom=[]
guests=[]
bedroom=[]
heading=[]
text=[]
sub=[]
tag=[]
facility=[]
out=[]
tags=[]
tee=[]
gif=[]
headerr=[]

M=1
U=4
S=7
A=10

def opencodezscraping(webpage, page_number):
            nextpage = webpage + str(page_number)
            print(nextpage)
            response= requests.get(str(nextpage))
            bs = BeautifulSoup(response.content,"html.parser")
            a_tag=bs.find_all("div",attrs = {'class': '_3gn0lkf'})
            #print(a_tag,file=f)
            print('-------------------------------------------------------------------------')
           
            for i in a_tag:
                hh=i.find_all('a', href =True)
                #label.append(i.childen.find_all("href"))
                for j in hh:
                    label.append(j['aria-label'])
                for text in hh:
                    hrefText.append((text['href']))
                    for i in hrefText:
                        inner_page=base+i
                        #print(inner_page)
                        response= requests.get(str(inner_page))
                        ts = BeautifulSoup(response.content,"html.parser")
                        heading.append(ts.find_all(['h1']))
                        head=[]
                        for g in ts.find_all(['h1']):
                            head=head+[g.text]
                        headerr.append(head)
                        tag.append(ts.find_all('div',attrs={'class':'_1b3ij9t'}))
                        yup=[]
                        for y in ts.find_all('div',attrs={'class':'_1b3ij9t'}):
                            yup=yup+[y.text]
                        tags.append(yup)
                        #print(tag)
                        #for y in tag:
                            #sub.append(y.text)
                        facility.extend(ts.find_all('div',attrs={'class':'_1nlbjeu'}))
                        amenity=[]
                        for t in ts.find_all('div',attrs={'class':'_1nlbjeu'}):
                            amenity=amenity+[t.text]
                            
                        print('--------------------------------------------------------------')
                        out.append(amenity)
                        
                        tee.append(ts.find_all('div',attrs={'class':'_1ojpw5l'}))
                        inn=[]
                        for s in ts.find_all('div',attrs={'class':'_1ojpw5l'}):
                            inn=inn+[s.text]
                        gif.append(inn)
                print(sub)
                #print(heading)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                
                span=bs.find_all("span",attrs = {'class': '_1p7iugi'})
                for y in span:
                    price.append(y.get_text())
                price_num.extend(list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), price)))
                print(price_num)    
                #spa= bs.find_all("span",attrs = {'class': '_krjbj'})
                #print(spa,file=f)
                
                spa= bs.find_all("span",attrs = {'class': '_krjbj'})
                for t in spa:
                    ff.append(t.get_text())
                subs='Rating'
                rate.extend(i for i in ff if subs in i)
                rate_num.extend([float(re.findall("\d+\.\d+", i)[0]) for i in rate])
                
                

                ss=bs.find_all('span',attrs= {'class':'_a7a5sx'})
                for e in ss:
                    ppl.append(e.get_text())
                people.extend(list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), ppl)))
                
                div=bs.find_all("div",attrs ={'class':'_kqh46o'})
                
                for q in div:
                    info.append(q.get_text())
                for r in info:
                    guests.append(r.split(' ')[M-1] )
                for w in info:
                    bedroom.append(w.split(' ')[U-1])
                for m in info:
                    bed.append(m.split(' ')[S-1])
                for t in info:
                    bathroom.append(t.split(' ')[A-1])

                #print(text)
                print('-------------------------------------------------------------------------')
                #print(ff,file=f)
                #print(price,file=f)   
                print(hrefText)
                print('--------------------------------------------------------------------------')
                print(label)
                print('--------------------------------------------------------------------------')
            if page_number < 20:
                    page_number = page_number + 20
                    opencodezscraping(base_url, page_number)
                    

opencodezscraping(base_url, 0)
with open(file, 'w', encoding='utf-8') as f:
    header=['Label', 'URL','Price','Rating','Review','Guests','Beds','Bedroom','Bathroom']
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(zip(label,hrefText,price_num,rate_num,people,guests,bed,bedroom,bathroom))


with open('label.csv', 'w', encoding='utf-8') as f:
    header=['Label','Inner_label','Amenties','Description']
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(zip(headerr,tags,out,gif))

          
    
