# Meta Back-End Developer Capstone
Hello, Reviewers!

You can run available unittests from VS terminal using command: python manage.py test tests/
Don't forget to activate pipenv virtual env and cd into littlelemon directory before running unit-tests command.

## To run unit tests this command may be used
python manage.py test tests 

## This path can be used to check that web application serves static HTML content with images and styles
/restaurant

You can use the following API paths for testing purposes using Insomnia or Postman clients
OR just browse using your favorite browser.

## djoser endpoint, for example, to make POST request and create new user
/auth/users/ 

## to login and auth get token
/api-token-auth/ 
## to login using djoser endpoint
/auth/token/login 

## menu items
/restaurant/menu/
/restaurant/menu/{menuItemId}
