from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Utility function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Mock function for fetching available currencies (you can replace this with actual data later)
def get_available_currencies():
    return ["USD", "EUR", "GBP", "INR", "JPY"]

# Mock function to simulate adding a product to the catalog (replace with actual service interaction later)
def add_product_to_catalog(product):
    # Simulate product addition delay
    time.sleep(2)
    # Mock success response
    return {'status': 'success', 'message': 'Product added successfully'}

@app.route('/')
def home():
    return "Welcome to the Boutique Frontend!"

@app.route('/business', methods=['GET', 'POST'])
def business():
    if request.method == 'GET':
        # Fetch available currencies for the dropdown
        currencies = get_available_currencies()
        return render_template('business.html', currencies=currencies)
    
    if request.method == 'POST':
        # Process the submitted form data
        product_id = request.form['id']
        name = request.form['name']
        description = request.form['description']
        categories = request.form['categories'].split(',')
        currency_code = request.form['currencyCode']
        price_units = int(request.form['priceUnits'])
        price_nanos = int(request.form['priceNanos'])
        
        # Handle file upload
        file = request.files['picture']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            return "Invalid file type. Please upload an image.", 400
        
        # Prepare product data
        product = {
            "id": product_id,
            "name": name,
            "description": description,
            "picture": file_path,
            "priceUsd": {
                "currencyCode": currency_code,
                "units": price_units,
                "nanos": price_nanos
            },
            "categories": categories
        }
        
        # Simulate verification delay
        time.sleep(3)
        
        # Add product to catalog
        response = add_product_to_catalog(product)
        if response['status'] == 'success':
            return jsonify({"message": "Your product is verified and posted to the catalog!"}), 201
        else:
            return jsonify({"error": response['message']}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
