# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Application Overview

This is a Flask-based e-commerce web application that integrates with ShipStation's V1 API (legacy OpenAPI) to manage product inventory and order fulfillment. The app serves as a custom storefront that can be integrated as a marketplace with ShipStation for automated order processing.

## Essential Commands

### Initial Setup (Required)
```bash
pip3 install -r requirements.txt
python3 setup_db.py  # Must run once before first launch
```

### Running the Application
```bash
# Set required environment variables
export SHIPSTATION_API_KEY=your_shipstation_api_key
export SHIPSTATION_API_SECRET=your_shipstation_api_secret

# Launch development server
python3 app.py
```

### Docker Alternative
```bash
docker build -t gear-up-store .
docker run -p 5000:5000 \
  -e SHIPSTATION_API_KEY=your_key \
  -e SHIPSTATION_API_SECRET=your_secret \
  gear-up-store
```

## Architecture Overview

### Core Components
- **`app.py`**: Main Flask application with all routes and business logic
- **`models.py`**: SQLAlchemy models (Cart, Order) 
- **`database.py`**: Database initialization
- **`shipstation.py`**: ShipStation API integration and XML/JSON transformations
- **`setup_db.py`**: Database setup script

### Key Integration Points

**ShipStation API Flow:**
- Products fetched from `/products` endpoint (cached 20 seconds)
- Orders exported as XML via `/shipstation_orders?action=export` 
- Webhook notifications received at `/shipstation_orders` (POST)

**Session-Based Architecture:**
- Anonymous shopping carts tied to Flask sessions
- No user authentication system
- Cart items stored in database with session_id reference

**Data Models:**
- `Cart`: session_id, product_id, quantity
- `Order`: UUID id, comma-separated product_ids, JSON shipping_info

### Critical Routes

- **`/store`**: Main product catalog (fetches from ShipStation)
- **`/add_item_to_cart`**: AJAX endpoint for cart management
- **`/place_order_db`**: Creates orders in local database
- **`/shipstation_orders`**: Bidirectional ShipStation integration endpoint

## Development Notes

### Environment Requirements
- **Python 3.7+** with Flask ecosystem
- **ShipStation V1 API credentials** (legacy OpenAPI)
- **SQLite** for local development

### API Integration Specifics
- ShipStation product fetching includes caching mechanism
- Orders are stored locally then exported to ShipStation as XML
- Webhook handling simulates processing delays (3-second sleep)

### Testing Features
- Built-in order simulation via "Simulate Business" functionality
- Test customer personas in `static/addresses.yml`
- Rate limiting prevents spam order generation

### Session Management
- Flask-Session with filesystem storage
- Session IDs auto-generated for anonymous users
- Cart persistence across browser sessions

## Important Constraints

- **No formal testing framework** - relies on manual testing and simulation features
- **V1 API dependency** - uses ShipStation's legacy OpenAPI
- **Session-based only** - no user accounts or authentication
- Use **python3** and **pip3** commands (not python/pip) on this system