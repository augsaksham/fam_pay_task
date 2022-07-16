# Project Goal :

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Project API Details :
  
  The project supports two API's:

     1. search/   -> GET
        This API takes in request in from  raw form body ,the request params are ->
           1. query  -> A string type object for a particular video search
            
           2. match_description -> This is an optional parameter (Integer) to allow user to match the keywords in video description also (including the title) .

        The response of the API is in form of a JSON object containg the best matched video details.

      2. sort/    -> GET
        This API takes in request in from  raw form body ,the request params are ->
            1. page  -> This is an interger repreenting which page entry the user wants to acess.

        The Response of the API is in form of HttpsResonse pointing to the required page number.


# Functionalities :

1. Asyncronous request is made to the youtube data API to collect data.  ( query="football" ).
2. Data is stored in cloud database (firebase).
3. Multiple API support : Two youtube API keys are used to provide flawless experience.
4. KeyWord Matching : The serach query match the keywords if complete query is not found.
5. Tuneable Data fetching : The data fetched per request can be tuned.
6. Fully Dockerized project



# Installation :

 1. Local PC :
    
    * conda create --name env python==3.9
    * git clone https://github.com/augsaksham/fam_pay_task
    * cd fam_pay_task
    * conda activate env
    * cd pro
    * pip install -r reqiurements.txt
    * python manage.py makemigrations
    * python manage.py migrate
    * python manege.py runserver 8000


    Now make request at : http://127.0.0.1:8000/youtube/<query>


 2. Docker Image :

    Install docker windows client form : https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
    
    * docker build . -t dev
    * docker run -p 8001:8000 -it --rm dev 

    Now make request at : http://127.0.0.1:8001/youtube/<query>



# Sample Usage:
 
  1. sort/
  
  ![Screenshot (434)](https://user-images.githubusercontent.com/79015249/179352041-e16be298-7512-4e8c-9e23-11815ed1752d.png)
   
   2. search/ 
   
   ![Screenshot (435)](https://user-images.githubusercontent.com/79015249/179352048-1107716f-bf91-40be-92d5-4ac5d34de9d1.png)


    

