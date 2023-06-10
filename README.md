# Food Barcode Decoder
This project is a Python web application that allows users to search for product details using barcodes and retrieve health information and ingredients. It utilizes the Open Food Facts API and the Open Food Facts Python SDK.

## Key Features

- Barcode search functionality: Users can enter a barcode and retrieve detailed information about the corresponding product.
- Health information display: The application shows the health grade of the product using a neumorphic design and assigns a colored pill to indicate the grade.
- Ingredients and allergens: The application displays the list of ingredients and highlights any allergens found in the product.
- JSON display: The raw JSON response from the Open Food Facts API is shown in a preformatted section for reference.

## Changes Made

- Styling: The application has been styled using a neumorphic design approach.
- Search page: The search page features a centered barcode input field and search button, with a title displayed above them.
- Results page: The results page showcases the product details in a card-like layout, with clear headings and well-organized sections.
- Health grade colors: The background color of the health grade pill is dynamically assigned based on the nutriscore grade of the product. 

## How to Run the Application

1. **Clone the repository:**
```shell
   git clone https://github.com/ryanwittmers/food-api-decoder.git && cd food-api-decoder
```

2. **Install the required dependencies:**
```shell
    pip install -r requirements.txt
```

3. **Run the Django development server:**
```shell
    python manage.py runserver
```


5. **Access the application:**
- Open your web browser and visit `http://localhost:8080` to interact with the application.

These instructions assume that you have Python and Django installed on your system. 

## Credits

- Open Food Facts API: [https://world.openfoodfacts.org](https://world.openfoodfacts.org)
- Open Food Facts Python SDK: [https://github.com/openfoodfacts/openfoodfacts-python](https://github.com/openfoodfacts/openfoodfacts-python)

Feel free to contribute to the project by submitting bug reports or pull requests. Enjoy searching for product details with Open Food Facts Product Search!
