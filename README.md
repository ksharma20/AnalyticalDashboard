# Analytical Dashboard

Project Done as an Internship Assignment 

## Assignment For Python Django Developer

### Project Intro
In this assignment, the candidate is required to build a Responsive Django-powered analytics dashboard web application.

### DATA:
You are provided with a single json file.
https://s3.us-east-2.wasabisys.com/akshit/dataset-django/ft_assignment.json.
Here’s a little bit of explanation of the data structured in the json file. Json file has a list of objects, each object having information such as app name, package_id and metrics like daily_active_users, installs and revenue. Each metric will have data for each date from May 1, 2022 to July 12, 2022.
#### Product Layout:
- User login page, unauthorised page and one tab - Analytics.
#### Product Flow:
- First when a user accesses the dashboard, he/she must login through google sign in
- In the Analytics tab, there will be a form with input fields such as
- Apps dropdown ( user can select any single app )
- Date range ( user can select from and to date range, Example ( May 1, 2022
to May 30, 2022))
- Submit button
- After the submit button is clicked, users must be shown a line chart of each metric :- daily active users, installs and revenue. (Use ajax calls to do form request)
#### Data Scheduling:
- Schedule a script that updates the data every 5 min

### Tech stack to be used:
- UI - Html, css, bootstrap, javascript ( jquery, angular.js, react.js - optional )
- Analytics chart View - any interactive chart library chart.js, d3.js, plotly.js (preferred)
- Backend - Django, Postgresql for database ( Mongodb if possible ), google sign in api
- Deployment - Dockerize the application and deploy it in aws or heroku web server
- Scheduling - Cron Job or celery

## Solution

### Tech Stack Used:
- UI - Html, css, bootstrap, javascript
- Analytics chart View - anychartJS
- Backend - Django, Postgresql for database, google sign in api
- Deployment - Dockerize the application and deployed it on Docker HUB.

### Login Page:
![image](https://user-images.githubusercontent.com/72795959/183726963-225eb813-af81-4b8f-9163-1fad18167c51.png)

Simple Button in Center to login with Google

### Home Page/ Dashboard
![image](https://user-images.githubusercontent.com/72795959/183727226-7bb9d5a4-0a58-4600-b1de-991bf58a2b20.png)

Simple Home Page with Analytics Tab on top Left.
And A Simple web form at center to select appName & Range
![image](https://user-images.githubusercontent.com/72795959/183727555-9edbf144-8298-4f75-85db-6fbe02e0127b.png)

### Dashboard Chart view
![image](https://user-images.githubusercontent.com/72795959/183727734-0ef5aecd-6caf-4af9-8d7f-41cd047d37b6.png)

Simple Chart with crosshair (using anychartJS).
X-axis = Dates, Y-axis = Numbers in k's (1000), 3 Lines for installs, revenue & Daily active users

### Video Overview

https://user-images.githubusercontent.com/72795959/183731037-0c2c072b-add9-470d-af56-81f03334e73d.mp4

