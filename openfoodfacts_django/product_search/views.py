import openfoodfacts.products
import json
import requests
import re

from django.shortcuts import render
from .forms import BarcodeForm
from bs4 import BeautifulSoup
from html import unescape

def search_product(request):
    product_name = "N/A"
    health_info = "N/A"
    ingredients = None
    pretty_product_details = "N/A"
    brand = "N/A"
    allergens = set()

    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data['barcode']
            product_details = openfoodfacts.products.get_product(barcode)

            if product_details['status'] == 1:
                form_submitted = True

                product = product_details['product']

                product_name = product.get('product_name', "N/A").title()
                health_info = product.get('nutriscore_grade', "N/A").capitalize()
                ingredients = product.get('ingredients_text', None).title()
                brand = product.get('brand_owner', None).title()
                pretty_product_details = json.dumps(product, indent=4, sort_keys=True)

                allergens_from_ingredients = product.get('allergens_from_ingredients', "")
                allergens_list = [allergen.strip().lstrip("en:").capitalize() for allergen in allergens_from_ingredients.split(',')]
                allergens = set(allergens_list)

                return render(request, 'results.html', {
                    'form': form,
                    'product_name': product_name,
                    'brand' : brand,
                    'health_info': health_info,
                    'ingredients': ingredients,
                    'pretty_product_details': pretty_product_details,
                    'allergens': allergens,
                    'form_submitted' : form_submitted
                })
    else:
        form = BarcodeForm()

    return render(request, 'search.html', {'form': form})