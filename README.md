#Vimeo user information store and seach with filter

**Assignment Objective:** To pull information from Vimeo users and provide a basic front-end to search various attributes of those users.

There is two parts in this assignment :

**1. write a script that crawls Vimeo to store the following information on 5,000 of these users in MySQL.** 

-Name <br />
-URL of their vimeo user page <br />
-Whether they are a paying user (yes/no) <br />
-Whether they have one or more videos that are a “Vimeo Staff Pick” (yes/no) <br />
-Whether they have one or more videos they have uploaded to Vimeo (yes/no)<br />

=======================================================================================================================

For this part I have written a script vimeo_crowl.py.


run script like below ...

**python \<filename\> \<start_user_id\> \<end_user_id\> \<total_no_user\>**

In vimeo,we can find every user page by his id like - http://vimeo.com/user150089

each user has unique id start from user1,user2, ... and so on last upto user16000000 (if total users in vimeo are 16 million )

but some user has deleted profile so profile page not exist error found. then we left that user's page and continue

if I want to store 50 user from id 18000 to 19000 then run script using command.....

python vimeo_crowl.py 18000 19000 50

Before run the script create database with name 'vimeodata' and create table vimeouser_vimeouser in that db using mysql.

sql command.....

**CREATE DATABASE vimeodata;**

**use vimeodata;**

**CREATE TABLE vimeouser_vimeouser ( id integer AUTO_INCREMENT NOT NULL PRIMARY KEY,name varchar(100) NOT NULL, url varchar(250) NOT NULL,paying_user bool NOT NULL, staff_pick_video bool NOT NULL,video_upload bool NOT NULL );**


after getting user page content then using beautifulsoup crowl that page and find user information and store into database.

but in user's profile page there is no information of staff pick video..... 
so there are two ways to find user has staff pick video or not 

1.check all video of each user (more than 50000 page fetching)<br />
2.visit http://vimeo.com/channels/staffpicks/videos and see all user id and map user from stored user data.(only 522 page fetching)

second method will take less time so I have used second method in my script.

after successfully stored data in database we run django project(vimeo_project)

=========================================================================================================================

**2.Create a one-page basic front-end using django and javascript(jquery)**

Before run django project change setting file .. use "vimeodata" database which have users information.

I have used ajax get call request to call url for search and filter with given search input data and filter.

for search in django I used name__istartswith query to get all user which name starts from given search data. 

for filter I used name__istartswith query with set any one (paying,staff_pick,video_uploaded) filter which are selected by user.

after search/filter we display the result on the same page....

tested link - http://vivekrungta.pythonanywhere.com/



