from fastapi import FastAPI

# Initialize our Order Service mini-app
app = FastAPI()

# A mock database to store placed orders
ORDERS = []

# An endpoint to place a new order
@app.post("/orders")
def create_order(product_id: int, quantity: int):
    new_order = {
        "order_id": len(ORDERS) + 1,
        "product_id": product_id,
        "quantity": quantity,
        "status": "Confirmed"
    }
    ORDERS.append(new_order)
    return {"message": "Order placed successfully!", "order": new_order}

# An endpoint to view all orders
@app.get("/orders")
def get_orders():
    return {"orders": ORDERS}