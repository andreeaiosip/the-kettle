### PURPOSE

**The Kettle** e-commerce site is built for a fictional coffee and tea wholesale start-up that want to promote their business and sell their products online around the world. The products can be bought in bigger bathes at a lower cost than if you were to buy from the shop. The site is created to be intuitive and easy to navigate to make the user’s experience a pleasurable one, so they will come back to purchase again from the shop.

### Goals

#### Business goals:

- Promote their business online.
- Attract new customers and convert them to returning customers.
- Sell products at a lower price than the brick and mortar shops.
- Ship the products around the world to reach a wide audience.

### **USER EXPERIENCE**

#### Target audience:

- Coffee and tea lovers who want to buy the products at a lower cost.
- Coffee and tea businesses who want to purchase their products for their business from an ecommerce who can deliver the products worldwide.



#### User goals:

- Navigate easily through the website and view products. 
- Buy coffee, tea and brewing products online.
- View the details of coffee and tea and where the ingredients are coming from.
- Purchase the products in an easy and seamless way.

**Personas and User Stories:**

**The Coffee Shop Owner:**

*Need:* 

I want to be able to buy good quality coffee and tea for my café at a good price without the need to browsing through many types of coffees and teas.

**Coffee Addict:**

*Need:* 

I want to be to buy good quality coffee and tea to be able to prepare it at home without the need of buying the product in big bags like a wholesale shop. 

####  Visitor

- As a user, I want to access the website from any device.
- As a user, I want to easily navigate between the pages.
- As a user, I want to be able to search for a product.
- As a user, I want to be able to view the details of a product.
- As a user, I want to be able to buy products.
- As a user, I want to be able to change the quantity of products I want to purchase.
- As a user, I want to sign up and create an account.
- As a user, I want to be able to view the products from only one category
- As a user, I want to be able to see a history of all my orders.

 

#### **Admin**

- As administrator, I want to be able to log in into the backend of the site.
- As administrator, I want to be able to add, edit and delete products
- As administrator, I would like to be able to see all the orders that were placed on the site.

### Design Choices: 

I wanted to the site look clean, but with some earthy colours to represent the tea and coffee colours, so I have used 

#### Fonts:

I chose to use Open Sans and Roboto as the main font family for this website as it provides clean style for text and titles. In the essence of keeping the layout clean, but with a sense of calmness and inviting.

#### Images:

I have sourced images of the internet with license free. I wanted to use some images with pack of coffee and tea, but most of them were with licence.

#### Colours:

I have chose to use clean background with off white #fffff and the brownish colour #c48968 to add a bit of colour and reflect the theme of the website.

### Wireframes

[Balsamiq Wireframes](https://balsamiq.com/) tool was used to create all wireframes for the project.

Original wireframes for desktop, tablet and mobile can be found [here](https://github.com/andreeaiosip/the-kettle/tree/master/wireframes). The website was changed and evolved through the development process . The wireframes served as guidelines to keep in mind what kind of layout I want to have at the end.


### Technologies Used

The languages, frameworks, libraries and other tools utilised for building this web-app are:

- **Gitpod -** Gitpod is a cloud-based integrated development environment (IDE) that has been used to write, run, and debug the code used for the web-app. https://www.gitpod.io/
- **GitHub -** GitHub has been used for version control of the code by using Git functions in the control panel. Github was utilised frequently during the development of the web-app. https://github.com/
- **Heroku -** This is a cloud based application platform that allows deployment of an application to the web and connection to the database. https://heroku.com/
- **SQlite3 -** SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. https://www.sqlite.org/index.html
- **PostgreSQL -** PostgreSQL is a powerful, open source object-relational database system. https://www.postgresql.org/
- **Django -** Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. https://www.djangoproject.com/
- **Travis CI -** Built to integrate with GitHub and Heroku. Using OAuth for authentication. Travis syncs users permissions to the repositories you want them to have access to. Allowing greater control over security and to scale out your build infrastructure as needed.
- **Balsamiq -** Used for design of wireframes. https://balsamiq.com/

### Front-End Technologies

- **HTML 5 -** The web-app uses HTML5 as a fundamental basis for building the web-app. Where possible semantic HTML is used to give the user a better understanding.
- **CSS3 -** The web-app uses CSS3 for styling of elements within the website. It is linked from the page to the *style.css* file.
- **Bootstrap -** The open-source Bootstrap framework has been used to implement the layout of the site. Bootstrap is also utilised to accommodate the responsive and mobile first design of the dashboard. https://getbootstrap.com/
- **Django-forms-bootstrap** A simple bootstrap filter for Django forms. Extracted from the bootstrap theme. https://django-bootstrap3.readthedocs.io/en/latest/
- **JavaScript -** The web-app uses Javascript to provide dynamic interactivity, as it is a full-fledged versatile programming language. https://www.javascript.com/
- **jQuery -** The web-app uses jQuery, as it simplifies a lot of complicated tasks from JavaScript, such as AJAX calls and DOM manipulation. https://www.jquery.com/jquery-3.4.1

### Back-End Technologies

- **Python 3 -** Python emphasises readability, uses English keywords and is highly extensible. The core language itself is quite small, and it is easy to learn for beginners. https://www.python.org/
- **Gunicorn -** Gunicorn ‘Green Unicorn’ is a Python WSGI HTTP Server for UNIX. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy. https://docs.gunicorn.org/en/stable/
-  **Pillow -** The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. https://pillow.readthedocs.io/en/stable/handbook/overview.html
- **Psycopg2 -** Psycopg is the most popular PostgreSQL database adapter for the Python programming language. Its main features are the complete implementation of the Python DB API 2.0 specification and the thread safety. https://pypi.org/project/psycopg2/
-  **Stripe -** Checkout creates a secure, Stripe-hosted payment page that lets you collect payments quickly. It works across devices and is designed to increase conversion. Checkout makes it easy to build a first-class payments experience. https://stripe.com/docs/payments/checkout
-  **Whitenoise –** for saving the static files to render in the live app on Heroku.

### Deployment

**I developed the project with the online IDE Gitpod, I used GitHub for version control, and Heroku for hosting the deployed site**

**Connecting to GitHub**

- I logged into Github, and created a repository, named the-kettle.
- I have connected to Gitpod by clicking the green button beside the repo in Github
- Now I am connected to the repo, any small or major changes can be pushed to adhere to good version control.

**Creation of app in heroku, and connection**

- Log in to Heroku (account is required), within the dashboard, click the "new" button featured in the top right of the page.
- Pick the closest region to you
- Using the CLI, add the heroku app as the remote master branch | `heroku git: remote a [app name]`

**Deployment to heroku**

- In the created Heroku app, I installed Heroku Postgres (Free Plan) as an add-on in the Resources tab
- To use Postgres, I installed two packages in my project, dj_database_url and psycopg2 and added them to my requirements
- In the Heroku app, I set Config Vars, so any secret information was kept out of version control, the django secret key has been changed from the one that was exposed.
- In the settings.py file, I imported dj_database_url, and set it to be used in production environment
- I used loaddata to import the data from my fixture files into the data models used in production
- I created a superuser for use in production via the command line
- I installed gunicorn, for use as the web server, added it to requirements.txt
- Created a Procfile
- The deployed sites hostname was added to "ALLOWED_HOSTS"
- Before pushing to heroku, DISABLE_COLLECTSTATIC was set to 1, to stop static files being collected during deployment
- Before pushing to Heroku, I pushed my commits to Github
- I then procceded to push to heroku
- After the successful deploy set up Heroku to automatically deploy whenever I push the my project on github.
- I set the SECRET_KEY in settings.py to get it from the environment
- Debug is set to false when not in development environment

### Testing

During development of this project, I tested each function thoroughly for the expected outcome, to make sure everything is working as expected before each commit.

I performed all the manual tests below once my website was in a production environment and I felt was ready for submission.

Due to the time constraints, I could make a log of all the tests I have made.

**Important bugs** I have encountered that made me to reset my database, but was actually not necessary. Is because I've never used Stripe before , I didn't know that Stripe has uses for the card variable *name*, so I was using my own variable  *full_name* instead. It threw many errors and I have spent lots of time figuring out this issue.


### Credits

The images was taken of Unsplashed and text was taken of wikipedia and online blogs. 
Readme.md file was created with the help of inspiration of a few of my colleagues.

**Acknowledgements**

During this development I took a heavy amount of inspiration and guidance from the mini project featured in the learning material to learn about how to make production ready Django project, the planning and development were all aided by this project, the creator of the project is [ckz8780 Chris Z](https://github.com/ckz8780), a link to the project he made for Code Institute, [Botique Ado](https://github.com/ckz8780/boutique_ado_v1).

Thank you to Code Institute Tutors for their invaluable support during development.
Thank you to my mentor [Simen Daehlin](https://github.com/Eventyret) for his help and support!




