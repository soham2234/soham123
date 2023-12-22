from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch JSON data from the URL
    url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
    response = requests.get(url)
    data = response.json()

    # Extract product information
    products = data['products']

    # Convert products to a list of dictionaries
    product_list = [{'id': key, **value} for key, value in products.items()]

    # Sort products by popularity in descending order
    sorted_product_list = sorted(product_list, key=lambda x: int(x['popularity']), reverse=True)

    # Render the template with the sorted product list
    return render_template('index.html', products=sorted_product_list)

if __name__ == '__main__':
    app.run(debug=True)
