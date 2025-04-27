from flask import Flask
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='database-1.ch8swm0cidn9.ap-southeast-2.rds.amazonaws.com',
    user='admin',
    password='derrahisyam144',
    database='utsdb'
)

@app.route('/')
def show_products():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM produk")
        products = cursor.fetchall()

    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>List Produk</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container mt-5">
        <h1 class="mb-4">List Produk</h1>
        <div class="row">
    '''

    for p in products:
        product_name = p[1]
        product_price = p[3]
        product_image = p[2]

        html += f'''
        <div class="col-md-4 mb-4">
            <div class="card">
                <img src="{product_image}" class="card-img-top" alt="{product_name}">
                <div class="card-body">
                    <h5 class="card-title">{product_name}</h5>
                    <p class="card-text">${product_price}</p>
                </div>
            </div>
        </div>
        '''

    html += '''
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
