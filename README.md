# visualize-mobile-data
Visualize the latest mobiles based on rating 

<h3>Introduction</h3>
Purpose of this program is to scrape the latest mobiles listed in 'http://www.themobileindian.com/' and visualize the data in a chart using plotly.All details related to each mobile are scraped and yielded.The data is represented in real time after scraping.The data could also be saved to database if needed.

<h3>Setting up project</h3>
1.Clone the project</br>
2.Create virtual </br>
3.Install the requirements</br>
4.Run the spider as scrapy crawl 'spider_name'</br> 
eg:scrapy crawl mobiledata

<h3>A glimpse through project</h3>
A spider is created for fetching and yielding the data in mobile_scrapy file.The start url contain a list of latest mobiles.This url is given as the first link to parse.From the parse method, each request is yielded for each mobile and then then each details are fetched and stored.

The graph is plotted with mobile names as x-axis and rating as y-axis after the spider closed as an html.The file will be opened in browser automatically.An api key is needed for this operation which has been already supplied in settings file.You could also update the settings file with your own api key referring to https://plot.ly/ documentation.

