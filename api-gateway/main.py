import httpx
from fastapi import FastAPI, HTTPException

# Initialize our API Gateway (The Reception Desk)
app = FastAPI()

# Addresses of our internal microservices
PRODUCT_SERVICE_URL = "http://product-service:8000"
ORDER_SERVICE_URL = "http://order-service:8001"


# Route for getting products (Gateway asks Product Service)
@app.get("/products")
async def get_products():
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{PRODUCT_SERVICE_URL}/products")
      return response.json()
    except httpx.ConnectError:
      raise HTTPException(
          status_code=503, detail="Product Service is offline!"
      )


# Route for getting orders (Gateway asks Order Service)
@app.get("/orders")
async def get_orders():
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{ORDER_SERVICE_URL}/orders")
      return response.json()
    except httpx.ConnectError:
      raise HTTPException(status_code=503, detail="Order Service is offline!")


# Route for placing an order (Gateway forwards to Order Service)
@app.post("/orders")
async def create_order(product_id: int, quantity: int):
  async with httpx.AsyncClient() as client:
    try:
      response = await client.post(
          f"{ORDER_SERVICE_URL}/orders?product_id={product_id}&quantity={quantity}"
      )
      return response.json()
    except httpx.ConnectError:
      raise HTTPException(status_code=503, detail="Order Service is offline!")