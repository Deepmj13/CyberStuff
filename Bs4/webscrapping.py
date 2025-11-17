import requests
from bs4 import BeautifulSoup

def get_product(product_name):
    product_name = product_name.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={product_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first product card
    product = soup.find("div", class_="_2kHMtA")

    if product:
        # Extract name
        name_tag = product.find("div", class_="_4rR01T")
        name = name_tag.text if name_tag else "No name found"

        # Extract price
        price_tag = product.find("div", class_="_30jeq3")
        price = price_tag.text if price_tag else "No price found"

        # Extract rating
        rating_tag = product.find("div", class_="_3LWZlK")
        rating = rating_tag.text if rating_tag else "No rating found"

        return name, price, rating
        
    return "product not found"

product_name = input("Enter the product name: ")
result = get_product(product_name)

if result == "product not found":
    print("Product not found")
else:
    name, price, rating = result
    print("Name   :", name)
    print("Price  :", price)
    print("Rating :", rating)

