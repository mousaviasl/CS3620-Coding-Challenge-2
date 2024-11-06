def get_product_price(product_name):
    products = {
        "apple": 1.2,
        "banana": 0.5,
        "orange": 0.8,
        "milk": 1.5,
        "bread": 2.0
    }
    
    return products.get(product_name.lower(), "Product not found.")

# Example usage
product = input("Enter the product name: ")
print(f"The price of {product} is: ${get_product_price(product)}")