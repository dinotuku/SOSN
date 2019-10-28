# A brief history of programming

# Abstract
For most people doing coding today, Stack Overflow should not be an unfamiliar site. It is being used by thousands and potentially millions of people from all over the world each day to find solutions to problems, and in some sense it acts like a miniature version of the programming community. The main idea behind our project is indeed that it would be very interesting to try to generalize trends and behaviors on Stack Overflow to gain some insights into the wider community of programming in the world. In particular, the usage of different programming languages and the types of questions and answers they get are good resources that could help us find out interesting patterns. In the project, we are going to analyze the users, posts and comments data, as well as the annual developer survey from Stack Overflow, hoping to understand how the community we’re all a part of has evolved over the years. 

# Research questions
* Statistical data exploration on Stack Overflow
* How many users / posts are there?
* What is the distribution of tags?
* How has the demographics of Stack Overflow changed over time?
* How has the popularity of different programming languages changed over time, and what are the potential reasons driving the trend?
* Are questions or answers with positive sentiment getting answered or picked more frequently? Is there a relationship between quality and sentiment?
* What are the characteristics of questions that get downvoted a lot?


# Dataset
* **Google BigQuery Stack Overflow.**
The dataset is hosted in Google BigQuery and we get 1TB of free BigQuery processing every month which means we can get 1TB of data per month. There are data of users, posts, comments, tags, votes, and badges from 2008 to 2019. We can use SQL query to get the data we want and use the download feature to save it as CSV or JSON file.
Stack Overflow Annual Developer Survey
* **Stack Overflow host surveys from 2011 to 2019.** 
They ask questions like Do you code as a hobby, Are you currently enrolled in a formal, degree-granting college or university program and many other kinds of questions. The respondents were recruited through onsite messaging, blog posts, email lists, meta posts, banner ads, and social media posts. According to the documentation, highly engaged users on Stack Overflow were more likely to notice the links for the survey and click to begin it. The dataset is in CSV format and about 50 - 200MB per year.

# A list of internal milestones up until project milestone 2
* Exploration and querying of data (on / before 3/11)
* Cleaning (we have already spotted a lot of dirty fields) (on / before 17/11)
* Basic statistical analysis on the users - milestone 2 (on / before 25/11)


# Questions for TAs
* Do you have any particular questions regarding stackoverflow from your daily usage and expect us to answer?
