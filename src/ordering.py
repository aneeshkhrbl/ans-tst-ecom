from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class OrderRequest(BaseModel):
    item_id: int
    quantity: int
    customer_email: str

# Change this from "/ordering/checkout" to "/checkout"
@app.post("/checkout")
def place_order(order: OrderRequest):
    # In a real app, this would deduct stock from the catalog and bill the customer
    order_id = str(uuid.uuid4())
    
    return {
        "status": "Order Placed Successfully",
        "order_id": order_id,
        "details": {
            "item_id": order.item_id,
            "quantity": order.quantity,
            "email": order.customer_email
        }
    }