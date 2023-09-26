import csv
import json

def parse_specification(specification):
    props = {}
    entries = specification.split("|")
    for entry in entries:
        if ":" in entry:
            key, value = entry.split(":", 1)
            props[key]=value
    return props

class Product:
    
    def __init__(self, id, name, category, selling_price, about_product, product_specification):
        self.id = id
        self.name = name
        self.category = category
        self.price = selling_price
        self.description = about_product
        self.details = Details(product_specification)

class Details:

    def __init__(self, specification):
        props = parse_specification(specification)
        if 'Itemmodelnumber' in props:
            self.model_number =  props['Itemmodelnumber']
        if 'ProductDimensions' in props:
            self.product_dimensions =  props['ProductDimensions']
        if 'ShippingWeight' in props:
            self.shipping_weight =  props['ShippingWeight']
        if 'ItemWeight' in props:
            self.item_weight =  props['ItemWeight']
        if 'Manufacturerrecommendedage' in props:
            self.manufacture_recommended_age =  props['Manufacturerrecommendedage']
        if 'ASIN' in props:
            self.asin =  props['ASIN']
        if 'DateFirstAvailable' in props:
            self.date_first_available =  props['DateFirstAvailable']
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


# Read csv products_amazon
with open('products_amazon.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skip the header
    next(csv_reader)

    # Create a list to store the data
    data = []
    for line in csv_reader:
        data.append(Product(line[0], line[1], line[4], line[7], line[10], line[11]))

    # Write the data to a new sql file
    with open('products_amazon.sql', 'w') as sql_file:
        sql_file.write("INSERT INTO products_amazon (id, name, category, price, description, details) VALUES\n")
        for product in data:
            sql_file.write(f"({product.id}, '{product.name}', '{product.category}', {product.price}, '{product.description}', '{product.details.toJSON()}'),\n")
        sql_file.write(";")

    