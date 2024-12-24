# API Documentation
 Tài liệu API

## Endpoints

### POST /predict
Upload image for classification

Request:
- Method: POST
- Endpoint: /predict
- Content-Type: multipart/form-data
- Body: image file

Response:
```json
{
    "class": "T-shirt",
    "confidence": 0.95,
    "similar_items": [
        {
            "image_url": "...",
            "product_url": "...",
            "price": "29.99"
        }
    ]
}