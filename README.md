# MX BIKE STORE


* UX
* Project Goal
   - User Stories - Customers
   - User Stories - Administrator
* Wireframes
* Data Structure
* Design
  - Typography 
  - Colors
* Features
   - Home Page 
   - Store Page
   - Product Page
   - Product Management 
   - Contact Page
   - Shopping Cart/Order Summary
   - Administrator Features
* Features To Be Implemented
* Testing
* Deploymnet
    -  Local Deploymnet 
    - Deploymnet To Heroku
* Technologies 
* Tools Used 
* Credits
    - Acknoledgements
---
MX BIKE STORE is an online store for hypothetical dirt buke riders providing vide range of goods in different categoties. 
The purpose of this site is to provide simple and intuitive way for the petrol heads to browse and purchase products they are looking for.
additionally the site allowe the shoop owners/administrators to manage the products in the shop and to update necessery informations about the products.
![](/static/img/images/mockup.jpeg)
The site was deployed to Heroku, The site could be view [here](https://misza-django-mx-bike-store-app.herokuapp.com/).

# UX
## Project Goal
MX BIKE STORE is the final project on my Fullstack Development Course with Code Institute and the purpose of this project was to develope e- commerce site with use of Django framework, with fully functional payment system with Stripe, and static file hosting with AWS. The site is functional and could be used in real world, with additional security implementation to the checkout process, and furher features to product pages. 

## User Stories
### User Stories - Customers
As a customer of the online store I would like to:
* Get clear information what is the website aboout when land on the home page
* Browse for products 
* Search products by name or category if you are looking for specific product
* Have access to full description of the product 
* Have abillity to choose a product from the store and add it to the cart 
* Have ability to update quantity of the product or delete product from the cart
* Create a profile, so user can access past order history and update billing address information
if needed
* Buy a product and pay securly using a Stripe card payment functionality
* Recive an email confirmation once transaction is completed 
* Have ability to send an enquiry or compalin if needed

### User Stories - Administrator
As a store administrator I would like to:
* Have ability to add/delete or update products to product list without logging in to admin panel(front end)
* Have ability to add new promotional materials to the store home page,
 to keep users informed about latest realeses or promotions
* Have ability to read users enquiries or complains  
* Have ability to store informations about previous purchasess
* Have ability to view orders placed by users
* store users emails so in the future, emaails with promotional materials could be sent 


## Wireframes
The wireframes where created based on user stories, and provide a starting point 
and guidline in the development process, but they don't represent the end result of the whole process 
of creating the app. I built the wireframes for this project using [Balsamic](https://balsamiq.com/). 
![](/static/img/wireframes/home-page.png)![](/static/img/wireframes/cart.png)
![](/static/img/wireframes/add-product.png)![](/static/img/wireframes/cart.png)
![](/static/img/wireframes/payment.png)![](/static/img/wireframes/contact.png.png)
![](/static/img/wireframes/store.png)![](/static/img/wireframes/payment.png)

## Data Structure 
Order:

 Key   |  Value  
--- | ---
user  |  models.ForeignKey
items |  models.ManyToManyField(OrderItem)
ordered_date | models.DateTimeField(auto_now_add=True
ordered | models.BooleanField(default=False)
billing_addrres |  models.ForeignKey(
        'BillingAddress', on_delete=models.SET_NULL, blank=True, null=True)


Order Item:

Key  |  Value
---- | -----
ordered | models.BooleanField(default=False)
item | models.ForeignKey(Item, on_delete=models.CASCADE)
quantity  |  models.IntegerField(default=1)
user |  models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)


BillingAddress:

key  | Value
---- | ------ 
user              | models.ForeignKey(settings.AUTH_USER_MODEL
street_address    | models.CharField(max_length=100)
apartment_address |  models.CharField(max_length=100)
country           |  CountryField(multiple=False)
zip               |  models.CharField(max_length=100)


Item:

Key   | Value 
----- | ------
title | models.CharField(max_length=120)
price | models.FloatField(2)
discount_price | models.FloatField(blank=True, null=True)
category | models.CharField(choices=CATEGORY_CHOICES, max_length=2)
label | models.CharField(choices=LABEL_CHOICES, max_length=1)
slug  | models.SlugField()
description | models.TextField()
image | models.FileField(upload_to='product_image', null=True)
additional_information | models.TextField(null=True)


## Design
Colours picked for this project where carefully selected even though, it might look like the home page is overloaded with dark colours it was done on purpouse, contrasted colors where used to a headings to maintain balance. 
to contrast rather bright colours of the entire range of products.
![](/static/img/images/c.scheme.png)

Typography 

Two fonts from [Google Fonts](
Google Fontshttps://fonts.google.com) where used for the project Helvetica and Roboto.

Icons used in this project comes from [FontAwesome](https://fontawesome.com/)

# Features

Home Page 

- The home page display slideshow with descriptive images and headings which could be updated by  
store owner or administrator of the page depends on requireents in admin panel.
- home page presents minimalistic design with the newest product offers display on the carousel
 with call to action button placed in the left, bottom side of the page. 

Store Page

- On the store page user can view details of the product, which contains:
    • image of the product
    • brand 
    • category 
    • link to full description  
    • price
- on the second navbar user has opportunity to search for the product by name or category, 
once the card with the product is selected, user is rdirected to the product page.

Product Page

- On the product page user is presented with full description of the item, 
- two buttons on the page are giving an option to the user to add 
or remove item from the cart
- in the buttom part of the page there is a space for aditional info about the product 
or promotional materials, 

Cart Page

- Once item is selected user is redirected to order summary page 
- on the page there are basic informations about the items choosen by user,
 like list of products, containing name(link to full description), quantity, total price 
- two buttons: continoue shooping and proceed to checkout placed below the order summary table,
- depends on the user choice after choosing either option you will be redirected to the checkout or 
 back to store.
- there is also delete icon added beside each item details allowing user to remove product from order summary
- cart icon dispalying total number of items in the cart 
- although there is no image of each item added to the cart in order summary page, user will be presented with images and quantity 
of individual item on the checkout page


Profile Page

- after creating an account, user have an access to profile page where he can update his billing details and have a look at order history
if one exist


Add/update/delete Product Page 

- if user is loged in as an admin, he will have an access to product management page where products could be updated
 created or deleted depends on the requirements


Checkout Page

- on the checkout page the order is presented along with the image, checkout form to be filled out
with required information, like address country zip code etc. once the form is filled out and submitted,
user will be redirected to Stripe payment form with items list and images and card details
- once payment is submitted, user will receive confirmation message and will be redirected to Success page,
 where information about completion of the order will be presented and confirmation email sent to the user


Contact page

- contact page contains heading with paragraph and a form where user can send enquiry or complain 


## Features for further implementation

- more secure checkout form
- user ability to write review about purchased products
- more integrated payment 
- for site administration, automated stock control functionality will be added allowing 
owner to see the amount of stock in the wearhouse

## Testing 

Python - All Python code was checked with  the [PEP8](http://pep8online.com) online validator.
and is PEP8 compiant except few line length flags.

HTML - all pages were run though [W3C HTML Validator](https://validator.w3.org). Two errors were detected 
unourtunatelly, they are not corrected yet.

CSS validation with the [W3C Jigsaw Validator](https://jigsaw.w3.org/) returned some expected errors from vendor extensions. Code written by me tested by direct input didn' show any errors.
Which means the code is compliant with W3C standards. 

Extensive testing through out all pages was carryd out. All user stories are covered. User is able to search, for products, read descriptions,
add or delete product from the cart log in or register, complete checkout and payment and receive confirmation message with purchase details,
and also confirmation email. Once loged in as an admin there is additional functionality added, allowing user to add new products to the product list
and also update and delete them if not needed anymore or out of stock.
The website reach all user stories but more security implementations needs to be added. Broken links are also removed or updated for 
better user experience. 

## Deployment

Before deploying the application, make sure the following criteria are reached,
so the following needs to be installed:
- Pyhton3 
- PIP
- Git 
- Heroku ClI
Once the criteria above are reached then account for Stripe and Amazon have to be created as well.
In both cases multifactor authentication is recomended.

### Local Deployment

1. From the application repository in GitHub click the "code" button and download zip file of the repository.
2. Access the folder in terminal window and install the application's required modules with 
` python -m pip -r requirements.txt
`
3. Create  a file with your environmental variables called env.py at the root level of the application.
4. SECRET_KEY has to be updated with your own secret key, as well as Stripe SECRET_KEY.
5. In case of pushing the application to a public repository, make sure that your env.py file is added to .gitignore
to secure your credentials.
6. The application will be available in the browser at the port 8000. (http://localhost:8000), and to run locally 
type command ` python3 manage.py runserver`.

### Deployment to Heroku

1. Create new application in Heroku.
2. From dashboard in Heroku click on "Deploy", followed by " Deployment method", to connect your application to github repository 
select GitHub.
3. In resources tab, navigate to add-ons section and find Heroku Postgress. Choose hobby level for this application.
4. Click on the settings tab on the button labelled "Reveal Config Vars". The Postgress create a link to postgress database.
5. After adding all variables to the application you can deploy the application in Heroku dashboard.
6 To view the app, click "View App" button. 

# Technologies
- HTML
- CSS 
- Python
- Django
- JavaScript/jQuery



# Tools Used 

* Github
* VS Code
* Heroku 
* [Bootstrap MBD](https://mdbootstrap.com)
* [Google Fonts](https://fonts.google.com)
* [Font Awesome](https://fontawesome.com)

# Credits

## Aknowledgements
- This Site is for educational use.
- I would like to thank all of my fiends and familly who have helped to test appllication and 
and came back with constructive feedback
- Massive thank you to whole Code Institute team for continous support evennn when  things wheren't going as planned
 and a lot of doubts took over my head. I'm really greatfull for your understanding and motivation. Quite possibly 
 it was one of the best decission I've ever made despite all the odds. 
- I would like to thank Felipe Alarcon who was always there with his valuable feedback, and motivation. 
- I would like to thank Code Camp for fantastic Django E-commerce tutorial which i based my project on.
Unfortunately my project is not fully finished so as readme.md file. Specially testing and debugging part.
I went true many unexpected challenges working on this project and i would like to thank you to all people who 
helped me to overcome not only technicall battles but mostlly the menthal ones. Because i doubted myself a lot.
This project is far from what we have learned during the Walkthrough project we have done in the course but it 
brought me a lot of experience in problem solving.