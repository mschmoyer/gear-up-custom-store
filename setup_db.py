from app import app, db, Cart, Order

with app.app_context():
    db.create_all()
