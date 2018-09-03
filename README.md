# Stocks API

**Author**: Max McFarland
**Version**: 0.1.0

## Overview
This application protocol interface allows for users to make requests to the appropriate path, and on success will recieve relevant information about various company stocks. Users can make accounts, create portfolios that are tied to their account, and add stocks to the relevant portfolio.

## Getting Started
To run this program, a user must download Python 3.7 and set up a pip virtual environment. After pulling down the application from GitHub, the user must run 'pserve deployment.ini' in their command line. To interact with the majority of the application, HTTPie must be downloaded (this can be downloaded globally by installing using homebrew, or to this specific environment using pip).

## Architecture
This was applicaiton was written in python using VScode. It employs a pyramid framework to take in API requests, and return relevent responses.

## API
The following paths will allow you to interact with the API:
localhost:6543 - This will display the home route.
localhost:6543/api/v1/lookup/{stock symbol} - This will connect to the IEX API, and return information about the company searched for
localhost:6543/api/v1/stock - This will create a GET request to the local database and return all stocks in the database.
localhost:6543/api/v1/stock/{Company ID} - This will return the corresponding company information stored in the local database based on the matching company id within the database.
localhost:6543/api/v1/portfolio - This will return all the portfolios attached to the current users account
localhost:6543/api/v1/portfolio/{portfolio name} - This will return the portfolio searched for (must be owned by current user)
localhost:6543/api/v1/auth/register email={user email} password={user password} - This will register a new user in the local database.
localhost:6543/api/v1/auth/login email={user email} password={user password} - This will login a user, which searches for an existing user instance in the local database.

## Change Log

08-27-18 1:00pm - Began working with the pyramid framework
08-28-18 1:00pm - Began adding SQL database interaction
08-29-18 2:00pm - Added user authentication.
08-30-18 1:00pm - finished user authentication and authoriztion.
09-02-18 2:30pm - adding docstrings, readme, and cleaning up broken code regarding functionality.
