# Stack Overflow as a Social Network

## Abstract
For most people doing coding today, Stack Overflow should not be an unfamiliar site. It is being used by thousands and potentially millions of people from all over the world each day to find solutions to problems. Users interact with each other on Stack Overflow almost like on social network, where they can raise questions, give answers, write comments etc. The main idea of our project is that it would be interesting to see what are the users of Stack Overflow (SO) really like and how they are interaction with each other across the world. Which countries contribute the most to the site, and in which ways? The information could be very interesting to us and also SO itself, since it would allow us to understand the users interaction behavior more. Since SO is such a large and widely used site for help in programming, it is also interesting in a wider perspective since the results could reflect something about how the programming community works as a whole. 

## Research Questions
* What are the users like? E.g. how old are they, what are their salaries and how do these things correlate with each other and the home country of the user?
* User participation analysis - how the users of SO are like and can we generalise some patterns of the programming community from SO data
* Time participation analysis - questions-answered rate of the past 4 years, when users used SO (day perspective and time perspective)
* Geographical participation analysis - participation tendency across countries on SO, interaction between countries on SO
* Things interesting along the way - China as a SO participation outlier, programming type clustering (types and type distribution along the world)

## Dataset
* **Google BigQuery Stack Overflow** (<a href='https://console.cloud.google.com/marketplace/details/stack-exchange/stack-overflow'>link</a>)
We used SQL queries to get the data we want and use the download feature to save it as CSV or JSON file. Information we queried includes: 
    * Users data - with information such as their country of residence, user id, name, account creation date etc. (for geographical analysis, we only make use of the users that contains a valid country field)
    * Questions - questions from 2016 to 2019, including information like question id, answer count, creation time, score (upvote), owner user id etc. 
    * Answers - answers from 2016 to 2019, including information like answer id, creation time, parent (question) id, score (upvote), owner user id etc.
    * <font size=2.5>Note: As Google BigQuery limit the data we can download for free, we do not query the text field of these databases (like the user description from Users data, question and answer content etc.) to reduce the size of the downloaded dataset.</font>
* **Stack Overflow Developer Surveys from 2016 to 2019**  (<a href='https://insights.stackoverflow.com/survey'>link</a>)
They ask questions like Do you code as a hobby, Are you currently enrolled in a formal, degree-granting college or university program and many other kinds of questions. The respondents were recruited through onsite messaging, blog posts, email lists, meta posts, banner ads, and social media posts. According to the documentation, highly engaged users on Stack Overflow were more likely to notice the links for the survey and click to begin it. The dataset is in CSV format and about 50 - 200MB per year.
* **World Bank Open Data / UN Data / Kaggle**
A variety of datasets are used to proide background information for the machine learning part of our analysis.
    * Mean years of Schooling by country.csv (<a href='http://data.uis.unesco.org/Index.aspx?queryid=242'>link</a>)
    * GDP per capita by country.csv (<a href='https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?view=map'>link</a>)
    * Population by country.csv (<a href='https://data.worldbank.org/indicator/sp.pop.totl'>link</a>)
    * list-of-countries-by-number-of-internet-users.csv (<a href='https://www.kaggle.com/tanuprabhu/list-of-countries-by-number-of-internet-users'>link</a>)


## Contribution
* Saibo : 
    Preliminary analysis on survey data, Analysis for the data story(user, country), Machine learning for China SO users
* Severi : 
    Query Big Query data, Cleaning Big Query data,     Preliminary analysis on Big Query data, Analysis for the data story (user, time, country), Clustering user programming type
* Kuan  :
    Preliminary analysis on Big Query data, Analysis for the data story (user, time), Writing up the website for the data story
* NgoYan : 
    Cleaning and unifying schema of user survey data, Preliminary analysis on survey data, Analysis for the data story (user, time, country), Building by country information-flow graph

## Presentation

* The poster will be designed by the whole team
* The 3 minutes talk will be given by Saibo Geng