import requests
from bs4 import BeautifulSoup

def product_info(product_name):
    try:
        product = product_name.replace(" ", "+")
        url = f"https://www.flipkart.com/search?q={product}"

        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                            "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9"
            }

        response = requests.post(url,headers=headers, timeout=60)
        
        if response.status_code != 200:
            return None
        
        bs4 = BeautifulSoup(response.text, "html.parser")

        target = bs4.find_all("div", class_="tUxRFH")

        if not target:
            return None
        
        items = []

        for i in target:

            name = i.find("div", class_="KzDlHZ").text 
            name = name if name else "Name Missing"

            price = i.find("div", class_="_4b5DiR").text
            price = price if price else "Price Missing"

            rating = i.find("div", class_="XQDdHH").text
            rating = rating if rating else "Rating Missing"

            items.append(
                {
                    "Name": name,
                    "Price":price,
                    "Rating":rating
                }
            )

        return items

    except Exception as e:
        print("Error :", e)
        return None
    

product_name = input("Enter Name of the Product")

result = product_info(product_name)

if not result:
    print("Product not found")
else:
    print(f"\nFound Products : {len(result)}\n")
    for product in result:
        print("\nName :", product["Name"])
        print("Price :", product["Price"])
        print("Rating :", product["Rating"])