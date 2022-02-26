#This program scraps all the mutual fund data and their portfolios, this is different from
# another program which scraps the shares and get the mutual fund data

from bs4 import BeautifulSoup
from urllib import urlopen
a="http://www.moneycontrol.com/"
source = BeautifulSoup(urlopen(a))

#[i.get('href') for i in source.select('a[href^="/india/stockmarket/pricechartquote/"]')]

def return_source_code(web_url):
    while 1:
        try:
            print "return page of "+web_url
            content=BeautifulSoup(urlopen(web_url))
            #print "return page of "+web_url
            return content
            break
        except:
            print "another attempt"
            continue
            
#mf_link_file=open("mohit","w")

share={}
mf_link_dict={}

for j in range(65,91):    #[i.get('href') for i in source.select('a[href^="/india/stockmarket/pricechartquote/"]')]:
    print("http://www.moneycontrol.com/india/mutualfunds/mutualfundsinfo/snapshot/"+chr(j))
    dir_name='C:\\Deloitte\\fir_mf\\'+chr(j)
    f = open(dir_name,'w+')
    try:
        share_by_alpha=return_source_code("http://www.moneycontrol.com/india/mutualfunds/mutualfundsinfo/snapshot/"+chr(j))
        for each_share in [i.get('href') for i in share_by_alpha.find_all("a",class_="verdana12blue") if i.get('href')<>"javascript:;" ]:
			if each_share<>'': #to handle blank pages like Z
				each_share_page=return_source_code("http://www.moneycontrol.com"+each_share)
				mutual_fund_name=each_share_page.find("h1").string
				fund_family=each_share_page.find("div",class_="MT12 txtstrip").find("a").string
				fund_class=each_share_page.find("span",class_="PL10").text.split(":")[1]
				mutual_fund_rating=len(each_share_page.find("p",class_="MT2").findAll("span",class_="starO")) if not each_share_page.find("p",class_="MT2").string else "Not rated"
				if each_share_page.find("p",class_="MT10 tar"):
					for mf_link in [i.get('href') for i in each_share_page.find("p",class_="MT10 tar").findAll("a")]:
						share_mf_link = "http://www.moneycontrol.com"+mf_link
						#share[share_name]={share_sector:share_mf_link}
						#print share
						share_mf_detail=return_source_code(share_mf_link)
						table=share_mf_detail.find("table",class_="tblporhd")
						rows=table.findAll("tr")            
						for td in rows[1:]:
							#print td.get_text("|")
							#print mutual_fund_name+'|'+fund_family+'|'+fund_class+'|'+td.get_text("|")+'|'+str(mutual_fund_rating)
							f.write(mutual_fund_name+'|'+fund_family+'|'+fund_class+'|'+td.get_text("|")+'|'+str(mutual_fund_rating)+'\n')
							f.flush()
    except:
        print "Connection failed"
        continue 
    f.close()
