# Food Barcode Decoder
This project is a Python web application that allows users to search for product details using barcodes and retrieve health information and ingredients. It utilizes the Open Food Facts API and the Open Food Facts Python SDK.

## Key Features

- Barcode search functionality: Users can enter a barcode and retrieve detailed information about the corresponding product.
- Health information display: The application shows the health grade of the product using a neumorphic design and assigns a colored pill to indicate the grade.
- Ingredients and allergens: The application displays the list of ingredients and highlights any allergens found in the product.
- JSON display: The raw JSON response from the Open Food Facts API is shown in a preformatted section for reference.

## Changes Made
- Search page: The search page features a centered barcode input field and search button, with a title displayed above them.
- Results page: The results page showcases the product details in a card-like layout, with clear headings and well-organized sections.
- Health grade colors: The background color of the health grade pill is dynamically assigned based on the nutriscore grade of the product. 

## How to Run the Application

### Prerequisites
Ensure you have Python 3, pip, and Git installed.
- Know which operating system you're on. If you don't, please refer to this helpful video: [How to Check Your OS Version](https://www.youtube.com/watch?v=r94vuvwUSkY)
#### Git
> This will allow you to clone the repository and get started building the project.
   - [Windows](https://git-scm.com/download/win)
   - macOS:
      - There are several ways to install Git on macOS. The easiest is probably to install the Xcode Command Line Tools. On Mavericks (10.9) or above you can do this simply by trying to run git from the Terminal app the very first time: `git --version`
   - Linux (if you're running Linux and don't know how to install Git, you probably shouldn't be on Linux)

#### Python
> This will allow you to install and build all of the dependencies for the project.
If you do not, head over to the [Python Website](https://www.python.org/downloads/) to download the distribution that matches your operating system.
   - [Windows](https://www.python.org/downloads/windows/)
   - [macOS](https://www.python.org/downloads/macos/)
   - [Linux](https://www.python.org/downloads/source/) (see note above about Git installation)

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
- Once you've ran the commands above successfully, open your web browser and visit `http://localhost:8080` to interact with the application.

These instructions assume that you have Python and Django installed on your system. 

## Credits

- Open Food Facts API: [https://world.openfoodfacts.org](https://world.openfoodfacts.org)
- Open Food Facts Python SDK: [https://github.com/openfoodfacts/openfoodfacts-python](https://github.com/openfoodfacts/openfoodfacts-python)

Feel free to contribute to the project by submitting bug reports or pull requests.
