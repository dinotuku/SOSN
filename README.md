# A brief history of programming

# Abstract
For most people doing coding today, Stack Overflow should not be an unfamiliar site. It is being used by thousands and potentially millions of people from all over the world each day to find solutions to problems. The main idea of our project is that it would be interesting to see what are the users of Stackoverflow really like and how are they distributed around the world? Which countries contribute the most to the site, and in which ways? The information could be very interesting to Stackoverflow itself, since it would allow them to understand the users potential areas for growth. Since Stackoverflow is such a large and widely used site for help in programming, it is also interesting in a wider perspective since the results could reflect something about how the programming community works as a whole. 

# Research questions
* How are the users distributed geographically? Which countries have the highest amount of users per-capita?
* What are the users like? E.g. how old are they, what are their salaries and how do these things correlate with each other and the home country of the user?
* How is the activity on the website distributed? In what countries are the users most active at asking questions and where are they most active at answering them? Are there countries where the users go to the site often but don't contribute that much? Do there exist patterns of questions asked in some countries being often answered in others?
* What are the factors that drive these effects, and what could be done to change them? For instance, the general English proficiency of the country will likely have an effect on the activity and amount of users.

# Dataset
* **Google BigQuery Stack Overflow.**
The dataset is hosted in Google BigQuery and we get 1TB of free BigQuery processing every month which means we can get 1TB of data per month. There are data of users, posts, comments, tags, votes, and badges from 2008 to 2019. We can use SQL queries to get the data we want and use the download feature to save it as CSV or JSON file. 
Stack Overflow Annual Developer Survey
* **Stack Overflow host surveys from 2016 to 2019.** 
They ask questions like Do you code as a hobby, Are you currently enrolled in a formal, degree-granting college or university program and many other kinds of questions. The respondents were recruited through onsite messaging, blog posts, email lists, meta posts, banner ads, and social media posts. According to the documentation, highly engaged users on Stack Overflow were more likely to notice the links for the survey and click to begin it. The dataset is in CSV format and about 50 - 200MB per year.
* **World Bank Open Data/UN Data/Kaggle. **
We are also going to use datasets that have information on the mean years of schooling, GDP per capita, population and number of internet users per country. 

# A list of internal milestones up until project milestone 3
* Studying correlations and figuring out how will we do more advanced analysis (on before 1/12)
* Trying out the more advanced data analysis (regression, clustering, question answer) (on / before 8/12)
* Deciding what are our results, after which we focus on refining them for milestone 3 (on / before 8/12)
* Starting work on the report / data story milestone (on / after 8/12)
* Finishing our report / datastory - milestone 3 (on / before 20/12)

# Questions for TAs
* Does the new focus seem valid?
* Do the mentioned fancier analysis methods seem doable? Like will clustering with categorical data be a good idea?

*Example* 
John: Plotting graphs during data analysis, crawling the data, preliminary data analysis; 
Mary: Problem formulation, coming up with the algorithm; 
Chris: Coding up the algorithm, running tests, tabulating final results; 
Eve: Writing up the report or the data story, preparing the final presentation.

# Milestone 3

## Contribution from each member:

* Data requirement

  1. Use google bigquery to fetch our dataset(Severi,Kuan )

  2. Fecth related dataset(Kuan?)

* Data Cleaning and preliminary analysis
  1. cleaning survey data of 4years, make them in the same schema (David)
  2. clean the google bigquery data(Severi )
  3. explore the survey data of 2015,2016(Saibo)
  4. explore the survey data of 2017,2018(David)
  5. explore the google bigquery data (Severi)

* ### Analysis and visualization of survey data (combine 4 years)

  1. dist of programming language ,(Severi)
  2. dist by visit freq ,analysis +plot(Severi)
  3. correlation of visit freq with level of experience ,analysis +plot(Saibo)
  4. correlation of visit freq with self-claimed programming ability,analysis +plot (Saibo)
  5. correlation of visit freq with job satisfaction,analysis +plot (Severi)
  6. dist of company size (maybe not but we have it)
  7. user dist by countries (actual numbers and per capita) (map -> Saibo, probably don’t include the pie chart)(  Saibo , David)
  8. Chinese stackoverflow user (Machine Learning (linear regression), find the actual active user in China) (Saibo)
  9. active user analysis (asian countries have higher active rate) (Saibo)
  10. dist by age range (only have 2019) (Saibo)
  11. correlation of visit freq with age (age only have 2019) (Saibo)
  12. Geographical distribution of user (absolute amount of actual users) (merge with map 7 - Saibo)

  ###  Analysis and visualization of  BigQuery
  
  1. Questions per user (David,Saibo)
  2. Questions per country (David,Saibo)
  3. Questions per user per country (David,Saibo)
  4. Answers per user (David,Saibo)
  5. Answers per country analysis +plot(David,Saibo)
  6. Answers per user per country analysis +plot(David,Saibo)
  7. Questions / Answers per user per country (tendency of asking questions) analysis +plot(David,Saibo)
  8. User: question and answer scatter plot (influence of experience)analysis +plot (David)
  9. Flow of information (directed graph)analysis +plot (David)
  10. Number of QA during weekday and weekend, analysis+plot (Severi)
11. QA frequency during working hour and outside working hour, analysis +plot (Kuan)
  
12. Use matrix factorisation(unsupervised learning) to detect clustering of programming lauguage / persona (Severi)
  

	
	###   Build webpage for data story
	- regroup the analysis and plots of the whole team, make them compatible, and build the webpage. (Kuan)

## Presentation

* The poster will be designed by the whole team
* The 3 minutes talk will be given by Saibo Geng