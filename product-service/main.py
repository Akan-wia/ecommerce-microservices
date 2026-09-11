from fastapi import FastAPI

# Initialize our FastAPI app (our mini-kitchen)
app = FastAPI()

# A mock database (just a simple list of products for now)
PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Headphones", "price": 149.99},
    {"id": 3, "name": "Coffee Maker", "price": 49.99}
]

# An endpoint (a specific window where people can ask for data)
@app.get("/products")
def get_products():
    return {"products": PRODUCTS}

    
    