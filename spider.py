import html_outputer, url_manager, html_download, html_parser


class SpiderMain(object):
    def __init__(self):

        self.download = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.Outputer()
        self.urls = url_manager.UrlManagement()


    def craw(self,root_url):
        #count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():

            new_url=self.urls.get_new_url()
            html_cout=self.download.download(new_url)
            new_urls, new_data,new_address=self.parser.parse(new_url,html_cout)
            #print ('craw %d:%s'%(count,new_url))
            self.urls.add_new_urls(new_urls)
            print(new_url)
            self.outputer.collect_data(new_data,new_address)
            # count=count+1
            # if count==30:
            #      break


        self.outputer.output_html()

if __name__ == '__main__':
  root_url="http://www.yellowpages.com/search?search_terms=restaurant&geo_location_terms=Brooklyn%2C%20NY&page=2"
  obj_spider= SpiderMain()
  obj_spider.craw(root_url)