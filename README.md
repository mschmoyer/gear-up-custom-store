(Start of only human written block)

  This was a project to see how GPT-4 could build something complex. Humans wrote 0 lines of code. 
  
(End of only human written block)

# GearUp Engineers Store

This Flask web application serves as an online store for engineering products. The key features and components of this application include:

1. **Frontend Interface**: Displays a list of available products.
2. **Search Functionality**: Allows users to search for specific products.
3. **ShipStation API Integration**: Fetches product information from ShipStation.
4. **Caching Mechanism**: Implements `flask_caching` to cache the results of API calls for a specified duration.
5. **SQLite Database**: Stores order and cart data.
6. **Dockerfile**: Containerizes the application.
7. **Flask Routing and Template Inheritance**: Includes a blog page and store page.
8. **README.md**: Provides information on the project, setup, and environment variables.
9. **Unique and Creative Products**: Tailored for engineers, including alcoholic beverages.

The application provides a user-friendly interface for engineers to browse and purchase products.


## Features

- Fetches product inventory from ShipStation API
- Product search with real-time filtering
- Stripe Checkout integration for secure payments
- Success modal with random funny thank you messages and emojis
- ShipStation API integration for order placement

## Getting Started

### Prerequisites

- Python 3.7+
- Flask

## Setting Up Environment Variables

To run this application, you will need to set up the following environment variables:

**Note**: The ShipStation API keys used are V1 API (legacy OpenAPI).

```makefile
export SHIPSTATION_API_KEY=your_shipstation_api_key
export SHIPSTATION_API_SECRET=your_shipstation_api_secret
```

## Running the Server

### Setup

**Important**: You must run the database setup script once before launching the application:

```bash
pip install -r requirements.txt
python setup_db.py
python app.py
```

The application should now be running on http://localhost:5000.

### Running with Docker

Alternatively, you can run the application using Docker:

```bash
docker build -t gear-up-store .
docker run -p 5000:5000 \
  -e SHIPSTATION_API_KEY=your_shipstation_api_key \
  -e SHIPSTATION_API_SECRET=your_shipstation_api_secret \
  -e OPENAI_API_KEY=your_openai_key \
  gear-up-store
```

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
