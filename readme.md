## Movie-Blog Project

The movie-blog project is a web application that gathers information from Letterboxd, a social networking site for film enthusiasts, in a distributed manner using web scraping. The application utilizes the Python stack of Celery, Django, Redis, and BeautifulSoup, and is designed to provide a comprehensive and up-to-date movie database.
Features

### The main features of the movie-blog project are:

    - Scraping Letterboxd's movie catalog, popular comments, recent comments, and movie images to provide a comprehensive and up-to-date movie database.
    - Implementing custom endpoints using Django REST framework to provide the scraped data to a React frontend.
    - Dockerizing the application and celery-workers to facilitate deployment and scalability.

## Technologies Used

### The movie-blog project uses the following technologies:
    - Python
    - Celery
    - Django
    - Django REST framework
    - Redis
    - Selectolax (HTML parser)
    - Docker
    - React (Decoupled from backend. Will be on another repo.)