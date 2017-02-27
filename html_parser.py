from bs4 import BeautifulSoup
import re
import urllib.parse
import fir_software
import gl


class HtmlParser():
    def is_num(self,s):
        try:
            num=float(s)
            return True
        except:
            return False

    def extract(self,string,index,text):
        length=len(string)
        index1=text.find('"',index+2+length)
        index2=text.find('"',index1+1)
        return text[index1+1:index2]

    def extractLine2(self,index,text):
        if text.find('addressLine2',index+1)!=-1:
            if (text.find('addressLine2',index+1)-index)<=40:
                return self.extract('addressLine2',text.find('addressLine2',index+1),text)+' '
            else:
                return ""
        else:
            return ""


    def get_new_urls(self,soup):
        new_urls= set()
        #/search?search_terms=restaurant&geo_location_terms=Brooklyn%2C%20NY&page=2
        #re_link='/search\?search_terms=restaurant&geo_location_terms=Manhattan%2CNY&page=\d+'
        #gl.edit1='http://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Brooklyn%2C%20NY&page=2'
        index1=gl.edit1.find('/',7)
        index2=gl.edit1.rfind('=')
        re_link=gl.edit1[index1:index2+1]+'\d+'

        index3=re_link.find('?')
        re_link=re_link[:index3]+"\\"+re_link[index3:]
        links=soup.find_all('a',href=re.compile(re_link))
        for link in links:
             new_url=link['href']
             new_full_url=urllib.parse.urljoin("http://www.yellowpages.com/",new_url)
             new_urls.add(new_full_url)

        return new_urls

    def get_new_data(self,page_url,soup):
        #res_data={}

        # res_data['url']=page_url
        #
        # node_title=soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1')
        # res_data['title']=node_title.get_text()
        #
        # node_summary=soup.find('div',class_="lemma-summary")
        # res_data['summary']=node_summary.get_text()
        coordinates=[]
        addresses=[]
        data=soup.find('script',type=None)
        text=data.get_text()

        count_indexla = 0
        count_indexlo = 0
        while True:

            index_la=text.find('latitude',count_indexla)
            if index_la==-1:
                break

            latitude=text[index_la+10:index_la+19]
            # latitude=latitude.replace(',','0')
            # latitude=latitude.replace('"','0')
            # latitude=latitude.replace('lon','0')
            # latitude=latitude.replace('longit','0')
            # latitude = latitude.replace('git', '0')
            index_lo=text.find('longitude',count_indexlo)
            longitude=text[index_lo+11:index_lo+20]
            # longitude=longitude.replace(',', '0')
            # longitude=longitude.replace('"', '0')
            # longitude=longitude.replace('lon', '0')
            # longitude=longitude.replace('longit', '0')
            # longitude = longitude.replace('git', '0')
            test1=self.is_num(latitude)
            test2=self.is_num(longitude)
            if self.is_num(latitude)==False or self.is_num(longitude)==False:
                address=[]
                index_ad=text.find('addressLine1',index_lo+1)
                index_ci=text.find('city',index_lo+1)
                index_st=text.find('state',index_lo+1)
                index_zi=text.find('zip',index_lo+1)
                addressLine1=self.extract('addressLine1',index_ad,text)
                addressLine2=self.extractLine2(index_ad,text)
                city=self.extract('city',index_ci,text)
                state=self.extract('state',index_st,text)
                zip=self.extract('zip',index_zi,text)
                full_address=addressLine1+' '+addressLine2+city+' '+zip
                address.append(addressLine1)
                address.append(addressLine2)
                address.append(city)
                address.append(state)
                address.append(zip)
                address.append(full_address)
                addresses.append(address)
            else:

                coordinate=[]
                coordinate.append(latitude)
                coordinate.append(longitude)
                coordinates.append(coordinate)

            count_indexla=index_la+1
            count_indexlo=index_lo+1



        return coordinates,addresses



    def parse(self,page_url,html_cout):
        if page_url is None or html_cout is None:
            return

        soup=BeautifulSoup(html_cout,"html.parser",from_encoding='utf-8')
        new_urls=self.get_new_urls(soup)
        new_data,new_address=self.get_new_data(page_url,soup)
        return new_urls,new_data,new_address