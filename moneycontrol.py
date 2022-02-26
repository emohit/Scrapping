from bs4 import BeautifulSoup
from urllib import urlopen
a="http://www.moneycontrol.com/"
source = BeautifulSoup(urlopen(a))

#[i.get('href') for i in source.select('a[href^="/india/stockmarket/pricechartquote/"]')]

def return_source_code(web_url):
	while 1:
		try:
			content=BeautifulSoup(urlopen(web_url),fromEncoding='latin1')
			return content
			break
		except:
			print "another attempt"
			continue
			
#mf_link_file=open("mohit","w")

share={}
mf_link_dict={}

for j in range(65,91):	#[i.get('href') for i in source.select('a[href^="/india/stockmarket/pricechartquote/"]')]:
	print("http://www.moneycontrol.com/india/stockmarket/pricechartquote/"+chr(j))
	dir_name='c:\\fir_mf\\'+chr(j)
	f = open(dir_name,'w+')
	try:
		share_by_alpha=return_source_code("http://www.moneycontrol.com/india/stockmarket/pricechartquote/"+chr(j))
		for each_share in [i.get('href') for i in share_by_alpha.find_all("a",class_="bl_12") if i.get('href')<>"javascript:;" ]:
			each_share_page=return_source_code(each_share)
			share_name=each_share_page.find("h1",class_="b_42").string
			share_sector=each_share_page.find("a",class_="gry10").string
			if each_share_page.find("div",class_="PT10 gL_11 FR"):
				print each_share
				for mf_link in [i.get('href') for i in each_share_page.find("div",class_="PT10 gL_11 FR").findAll('a')]:
					share_mf_link = "http://www.moneycontrol.com"+mf_link
					#share[share_name]={share_sector:share_mf_link}
					#print share
					share_mf_detail=return_source_code(share_mf_link)
					table=share_mf_detail.find("table",class_="tblfund2")
					rows=table.findAll("tr")			
					for tr in rows:
						cols=tr.findAll("td")
						i=1
						t=''
						#print share_name+';'+share_sector,
						for td in cols:
							if(td.find('a')):
								e=';'+td.find('a').get('href')
							else:
								e=''
							if(td.text=="Total"):
								break
							t+=td.text+';'
							#print t,
							if(i==1 and td.text<>"Total"):
								mf_link_dict[td.text]=e
								i+=1
						if(t<>''):
							print share_name+';'+share_sector+';'+t
							f.write(share_name+';'+share_sector+';'+t+'\n')
	except:
		print "Connection failed"
		continue 
	f.close()
