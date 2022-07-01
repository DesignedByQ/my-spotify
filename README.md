# My Spotify App

Second QA Project

**CONTENTS**

[RESOURCES]([RESOURCES](https://github.com/DesignedByQ/my-spotify/edit/main/README.md))
1. RESOURCES
2. BRIEF & ADDITIONAL REQUIREMENTS
3. MY APPROACH 
4. RISK ASSESSMENT
5. JIRA BREAKDOWN
6. ERD
7. TECH USED & CICD PIPELINE
8. TESTING
9. HOW TO USE THE APP
10. KNOWN ISSUES
11. FUTURE IMPROVEMENTS
12. CONTRIBUTORS
13. ACKNOWLEDGEMENTS
14. LICENSES

**1. RESOURCES **

Jira: https://henryo.atlassian.net/jira/software/projects/PCA/boards/3?selectedIssue=PCA-46

Website: [IP Address](http://35.197.238.79:5000/)

GitHub: https://github.com/DesignedByQ/my-spotify

**2. BRIEF**

Overall objective with this project is the following:

To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

ADDITIONAL REQUIREMENTS

The requirements of the project are as follows:

1). A Trello board (or equivalent Kanban board tech) with full expansion
    on user stories, use cases and tasks needed to complete the project.
    It could also provide a record of any issues or risks that you faced
    creating your project.
    
2). A relational database used to store data persistently for the
    project, this database needs to have at least 2 tables in it, to
    demonstrate your understanding, you are also required to model a
    relationship.
    
3). Clear Documentation from a design phase describing the architecture
    you will use for you project as well as a detailed Risk Assessment.

4). A functional CRUD application created in Python, following best
    practices and design principles, that meets the requirements set on
    your Kanban Board.

5). Fully designed test suites for the application you are creating, as
    well as automated tests for validation of the application. You must
    provide high test coverage in your backend and provide consistent
    reports and evidence to support a TDD approach.
    
6). A functioning front-end website and integrated API's, using Flask.
    
7). Code fully integrated into a Version Control System using the
    Feature-Branch model which will subsequently be built through a CI
    server and deployed to a cloud-based virtual machine.
    
**3. MY APPROACH**

Music Database with Playlist Feature

My goal is to create an app that can be used like a basic spotify/ipod. It will contain songs that can be used to create playlists.

Users can add songs to a database, delete songs, view all songs in the database and update details of a songs.
Users can also add songs from the database to a particular playlist of their choice.
Users can also view all songs assigned to any playlist and filter songs by which playlist they're assigned to.
Users can create multiple playlists.

Requires two db to start

**4. MY RISK ASSESSMENT**

https://docs.google.com/document/d/1iqoWZ6W-6CRM-1ywy6ZZsdNVc5jbR1Qg_qtf30a_Uvs/edit?usp=sharing

![image](https://user-images.githubusercontent.com/32695213/176883529-041cad71-2835-4fd1-aab8-eab934292ddb.png)

**5. JIRA**

I decided to use Jira for my project tracking software. By using it I was able to breakdown the requirements of the project in smaller manageable tasks. Jira has features that allowed me to deploy the MoSCoW method with my project tracking a define which tasks would also be the hardest to complete. The must-have tasks were completed first while the features that would slightly improve functionality were left to the end of the project labeled as could-have and spent most of their time in the backlog.

![image](https://user-images.githubusercontent.com/32695213/176885385-ffac282e-67cb-4e0c-a73d-f23e78f820ca.png)

![image](https://user-images.githubusercontent.com/32695213/176886011-8e093d88-525b-4dd9-b42e-9b17e4744061.png)

**6. ENTITY RELATIONSHIP DIAGRAM**

My inittial thinking behind my first diagram was that each song will belong to only one album and an album can have many songs. Also a song can belong to many playlists and a playlist will have many songs. See below for proposed many-to-many ERD:

![image](https://user-images.githubusercontent.com/32695213/176886960-212c054a-1301-4bf4-b669-12ed3b37bf28.png)

After considering the amount of work it would take to implement the the above ERD and the limited time I had for the project I decided to go for something more simple like the two table one-to-many version shown below. With this diagram I only needed a table for songs which would serve as a main database and then a second table for playlists which songs can be added to with the additional criteria of 'playlist name'. This way the user could filter the songs in the playlist table to access a specific playlist or all playlists.

**7. TECHNOLOGY USED & CICD PIPELINE**

I used develpoment software such as python3 and the flask framework to build the application on a virtual machine hosted on google cloud platform. The source code was also pushed up to Github for version control as well as living on the VM. I would use Jira to create and schedule my development tasks and app features that were required to push them up to github on seperate branches as I went along. I also required the application to auto deploy and test everytime there was an alteration to the code and for this I used jenkins. The webhook feature on jenkins allowed me to setup the pipeline so everytime I pushed up to github the application would rebuild which included a full test with coverage report and deployment.

![image](https://user-images.githubusercontent.com/32695213/176937145-88004747-3942-4f0b-afb1-3f60dd9ba615.png)

**8. TESTING**[RESOURCES]([RESOURCES](https://github.com/DesignedByQ/my-spotify/edit/main/README.md))

I used pytest for my unit testing. I set out to test all the routes in my application however, I was unable to configue the integration tests. As it stands my tests pass at a rate of 72% and these tests were designed to check the end points of the of the routes and the CRUD functions run as expected. Below is a screenshot of my testing coverage report:

![image](https://user-images.githubusercontent.com/32695213/176922854-67620506-0ab7-42fc-8ab2-292c640581a7.png)

**9. HOW TO USE THE APP**

This application has been built as an MVP so has a very basic look built using HTML & Jinga2 syntax to access the back-end functions written with python.

9.1 Below is the front page, here the user will navigate to the main database to add songs and make available for adding them to a playlist.

![image](https://user-images.githubusercontent.com/32695213/176925478-9d7eb902-e689-4bc5-a0e0-989af9ac2912.png)

9.2 When you click through to the next page you can add a song of your choice and scroll down the page to see all available songs in the database.

![image](https://user-images.githubusercontent.com/32695213/176925877-3ed84ad8-fda2-40c8-88aa-6b2778afd1f6.png)

![image](https://user-images.githubusercontent.com/32695213/176926368-6333e70d-5fa2-4247-b7a6-0ae04e236b57.png)

9.3 Now you can go to the playlist section and add any song that exists in the songs database to a playlist of your choice.

![image](https://user-images.githubusercontent.com/32695213/176926642-d17889c8-1ea6-4c02-a6bf-667c7ac81ddc.png)

![image](https://user-images.githubusercontent.com/32695213/176927194-8b918886-0776-44bd-9c6d-b6c081cd5ec9.png)

9.4 The user can either view all playlists or filter by a specific playlist.

![image](https://user-images.githubusercontent.com/32695213/176927464-976f2b60-d50e-4e6b-a441-9128d25101cf.png)

**10. KNOWN ISSUES**

10.1 This error message "Please select from an available playlist!!!" is constant but I would only like it to show if the user enters a playlist name that doesn't exist.

10.2 I couldn't get integration tests to work at all.

10.3 Fix playlist count feature so it display number of songs in the playlist

10.4 The DB connection to GCP has been exported using pymysql however, the gcp open shell doesn't show the tables etc.

**11. FUTURE IMPROVEMENTS**

If I had more time I would make the following improvements:

11.1 Improve testing coverage.

11.2 Add a button to the songs db that will directly add it to a playlist.

11.3 Use CSS to improve the appearance of the application.

11.4 Add more functionality by incorporating more buttons and links thus improving the UI/UX aspect.

11.5 Use a drop down multi choice feature to select from multiple playlist options.

11.6 Setup user accounts for logins/password features.

**12. CONTRIBUTORS**

Henry Opara

GitHub: https://github.com/DesignedByQ

Linkedin: https://www.linkedin.com/in/henry-opara-81890a23/

**13. ACKNOWLEDGMENTS**

I would like to say thanks to the following QA Training staff - Ryan Wright, Reece Elder, Adam Gray and Victoria Sacre.

Each of the above contributed in my development that has allowed me to build this application and use all the required technologies.

I would also like to give a mention to the following websites which on a numer of occasions helped me to debug and overcome coding issues w3schools.com, stackoverflow.com and qa-community.co.uk.

**14. LICENCES**

The MIT License (MIT)

Copyright (c) 2013-present Pagar.me Pagamentos S/A

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

