# reddit-crawling

This repository includes reddit crawling 2 different ways. Praw and BeautifulSoup. I crawled reddit praw and I use token. And I crawled reddit BeautifulSoup too. 
You need to enter the searched word from the console, and if you run main.py you should enter Reddit API token. 

for scraping with praw : main.py
for scraping with bs4 : alternativeMain.py

# STEP 1

## I generated Reddit API token. 
We need client_id, user_agent and secret.  
Link : https://www.reddit.com/prefs/apps  

## I added requirements.txt. 

Package Needs: 
pip install pika  
Praw 7.6.1
RabbitMQ 3.11.3
Erlang 25.1.2
pip install protobuf (I installed 4 version)  


# STEP 2

## I installed RabbitMQ and I used this project localhost for connect.  

I send json file but I fixed many things. Because I get error my json file. So I edit result.json file. 
I wrote the desired code for stage 2 in publisher.py  



