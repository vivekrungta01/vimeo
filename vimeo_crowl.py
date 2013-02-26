from urllib2 import urlopen,URLError,HTTPError
from bs4 import BeautifulSoup
import MySQLdb
j=0;
#mysql database connection

connection=MySQLdb.connect(user='root',passwd='fasttrack',db='vimeodata')
cursor=connection.cursor()
connection.set_character_set('utf8')
cursor.execute('SET NAMES utf8;') 
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')

#check command line argument
import sys
if(len(sys.argv)!=4):
	print "Usage : python <filename> <star_user_id> <end_user_id> <total_user>"
	exit()
try:
	start_id=int(sys.argv[1])
	end_id=int(sys.argv[2])+1
	total_id_fetch=int(sys.argv[3])
except:
	print "Usage : python <filename> <star_user_id> <end_user_id> <total_user>"
	exit()
else:
	if ((start_id>end_id) or total_id_fetch>(end_id-start_id)):
		print "Usage : python <filename> <star_user_id> <end_user_id> <total_user>"
		exit()
		
#main program starts from here 

user=[]
for i in range(start_id,end_id):
	if j==total_id_fetch: #if fetched total user given in input break from loop
		break
	try:
		profile=urlopen('http://www.vimeo.com/user'+str(i)).read()
	except HTTPError:      # if user profile deleted then page does not exist(HTTPError)  leave that page
		continue
	else:
		#used BeautifulSoup to crowl the website and find information of user 
		
		soup=BeautifulSoup(profile)
		pf_bx=soup.find('div',{'id':'profile'})
		name=pf_bx.h1.span.text   
		url=pf_bx.meta['content']  
		user_id=url.split('/')[-1] 
		paying_user=(pf_bx.h1.find('a',{'href':'/plus'})!=None)
		video_upload=soup.find('li',{'data-type':"video"})!=None
		user.append(user_id)
		
		# Entry in database  
		cursor.execute('''insert into vimeouser_vimeouser (name,url,paying_user,video_upload,staff_pick_video) values (%s, %s, %s, %s, %s )''',(name,url,paying_user,video_upload,False))
		j=j+1



#fetch all user of vimeo staff pick video and if user found then set entry in database for that user

i=1
while 1:
	
	""" fetch vimeo staff pick video page in detail format so page fetch reduce 522 and find all user one by one and map with database user which is store in user list"""
	
	try: 
		video_page=urlopen('http://www.vimeo.com/channels/staffpicks/videos/page:'+str(i)+'/format:detail').read()
	except HTTPError:
		break
	else:
		soup=BeautifulSoup(video_page)
		all_video=soup.find('ol',{'id':'browse_list'}).findAll('p',{'class':'meta'})
		for video in all_video:
			user_id=video.a['href'].lstrip('/')
			url="http://vimeo.com"+video.a['href']
			if user_id in user:
				cursor.execute ('''UPDATE vimeouser_vimeouser SET staff_pick_video = %s WHERE url = %s''',(True,url))
	i=i+1
connection.close()





	





