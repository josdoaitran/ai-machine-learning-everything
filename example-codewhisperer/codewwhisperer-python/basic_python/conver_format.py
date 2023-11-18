products = [
    {
        'url': 'https://test.com/products/001',
        'name': 'Product 001',
        'description': 'Product 001 description',
        'price': '100',
        'currency': 'USD',
    },
    {
        'url': 'https://test.com/products/002',
        'name': 'Product 002',
        'description': 'Product 002 description',
        'price': '200',
        'currency': 'USD'
    },
    {
        'url': 'https://test.com/products/003',
        'name': 'Product 003',
        'description': 'Product 003 description',
        'price': '300',
        'currency': 'USD'
    }
]

# write the method to convert the products list to XML
def convert_to_xml(products):
    xml = '<products>'
    for product in products:
        xml += f'<product url="{product["url"]}" name="{product["name"]}" description="{product["description"]}" price="{product["price"]}" currency="{product["currency"]}"/>'
    xml += '</products>'
    return xml

# write the method to convert the products list to CSV
def convert_to_csv(products):
    csv = 'url,name,description,price,currency\n'
    for product in products:
        csv += f'{product["url"]},{product["name"]},{product["description"]},{product["price"]},{product["currency"]}\n'
    return csv

# write the method to convert the products list to JSON
def convert_to_json(products):
    json = '['
    for product in products:
        json += f'{{"url":"{product["url"]}", "name":"{product["name"]}", "description":"{product["description"]}", "price":"{product["price"]}", "currency":"{product["currency"]}"}},'
    json = json[:-1] + ']'
    return json

# write the method to convert the products list to YAML
def convert_to_yaml(products):
    yaml = '---\n'
    for product in products:
        yaml += f'url: {product["url"]}\nname: {product["name"]}\ndescription: {product["description"]}\nprice: {product["price"]}\ncurrency: {product["currency"]}\n---\n'
    return yaml

# write the method to convert the products list to TSV
def convert_to_tsv(products):
    tsv = 'url\tname\tdescription\tprice\tcurrency\n'
    for product in products:
        tsv += f'{product["url"]}\t{product["name"]}\t{product["description"]}\t{product["price"]}\t{product["currency"]}\n'
    return tsv

# write the method to convert the products list to HTML
def convert_to_html(products):
    html = '<table><tr><th>url</th><th>name</th><th>description</th><th>price</th><th>currency</th></tr>'
    for product in products:
        html += f'<tr><td>{product["url"]}</td><td>{product["name"]}</td><td>{product["description"]}</td><td>{product["price"]}</td><td>{product["currency"]}</td></tr>'
    html += '</table>'
    return html

# write the executable main method
if __name__ == '__main__':
    # write the code to convert the products list to the desired format
    # and print the converted list
    print(convert_to_xml(products))
    print(convert_to_csv(products))
    print(convert_to_json(products))
    print(convert_to_yaml(products))
    print(convert_to_tsv(products))
    print(convert_to_html(products))










