import base64
import io
import mysql.connector
from dataclasses import dataclass
from pathlib import Path
from PIL import Image


@dataclass
class Product:
    gtin: str
    product_brand: str
    product_name: str


knorrSeafoodBase = Product('048001014329', 'Knorr', 'Ultimate Seafood Liquid Concentrate Base')
knorrCaldoBoullion = Product('048001038530', 'Knorr', 'Shrimp Bouillon')
knorrCaldoTomate = Product('048001765450', 'Knorr', 'Tomato Bouillon With Chicken Flavor')
leGoutCreamSoupBase = Product('10037500000329', 'Le Gout', 'Cream Soup Base')
leGoutCreamSoupBaseBucket = Product('10037500000541', 'Le Gout', 'Cream Soup Base')
knorrBrownGravyMix = Product('10048001005508', 'Knorr', 'Brown Gravy Mix')
knorrHollandaiseSauceMix = Product('10048001005805', 'Knorr', 'Hollandaise Sauce Mix')
hellmansVeganMayo = Product('10048001010724', 'Hellman\'s', 'Vegan Dressing & Sandwich Spread')
hellmansVeganMayo2 = Product('10048001010731', 'Best Foods', 'Vegan Dressing & Sandwich Spread')
knorrAlfredoPastaSauceMix = Product('10048001013305', 'Knorr', 'Alfredo Pasta Sauce Mix')
knorrBeefBoullon = Product('10048001039091', 'Knorr', 'Beef Flavor Bouillon')
knorrChickenBase = Product('10048001145433', 'Knorr', 'Chicken Base')
knorrBeefBase = Product('10048001145440', 'Knorr', 'Beef Base')
knorrVegBase = Product('10048001145457', 'Knorr', 'Vegetable Base')
hellmansMayoGallon = Product('10048001265308', 'Hellman\'s', 'Mayonnaise')
bestFoodsMayoGallon = Product('10048001265742', 'Best Foods', 'Mayonnaise')
hellmansMayoBottle = Product('10048001356969', 'Hellman\'s', 'Mayonnaise')
bestFoodsMayoBottle = Product('10048001357539', 'Best Foods', 'Mayonnaise')
hellmansMayoBottle2 = Product('10048001370491', 'Hellman\'s', 'Mayonnaise')
bestFoodsMayoBottle2 = Product('10048001370507', 'Best Foods', 'Mayonnaise')
knorrDemiGlaceMix = Product('10048001386737', 'Knorr', 'Demi-Glace Sauce Mix')
knorrRoastedChickenBase = Product('10048001503363', 'Knorr', 'Roasted Chicken Base')
knorrChickenBouillon = Product('10048001760452', 'Knorr', 'Chicken Bouillon')
knorrButtNutSoup = Product('10068400001994', 'Knorr', 'Butternut Squash Soup Mix')
knorrVegChiliMix = Product('10068400002236', 'Knorr', 'Three Bean Vegetable Chili Mix')
knorrTomatoSoupMix = Product('10068400002342', 'Knorr', 'Tomato Bisque with Basil Soup Mix')

GTIN_TO_PRODUCT = {
    '048001014329': knorrSeafoodBase,
    '048001038530': knorrCaldoBoullion,
    '048001765450': knorrCaldoTomate,
    '10037500000329': leGoutCreamSoupBase,
    '10037500000541': leGoutCreamSoupBaseBucket,
    '10048001005508': knorrBrownGravyMix,
    '10048001005805': knorrHollandaiseSauceMix,
    '10048001010724': hellmansVeganMayo,
    '10048001010731': hellmansVeganMayo2,
    '10048001013305': knorrAlfredoPastaSauceMix,
    '10048001039091': knorrBeefBoullon,
    '10048001145433': knorrChickenBase,
    '10048001145440': knorrBeefBase,
    '10048001145457': knorrVegBase,
    '10048001265308': hellmansMayoGallon,
    '10048001265742': bestFoodsMayoGallon,
    '10048001356969': hellmansMayoBottle,
    '10048001357539': bestFoodsMayoBottle,
    '10048001370491': hellmansMayoBottle2,
    '10048001370507': bestFoodsMayoBottle2,
    '10048001386737': knorrDemiGlaceMix,
    '10048001503363': knorrRoastedChickenBase,
    '10048001760452': knorrChickenBouillon,
    '10068400001994': knorrButtNutSoup,
    '10068400002236': knorrVegChiliMix,
    '10068400002342': knorrTomatoSoupMix,
}


class InsertImagesToDataBase:
    def __init__(self):
        self.connection = self.get_connection()
        self.cursor = self.connection.cursor()
        self.database = 'productoftheweek'
        self.query = 'insert into productoftheweek (productName, gtin, productBrand, distributorName, productImage) ' \
                     'values(%s, %s, %s, %s, %s) '

        self.photos_dir = Path('POTW Front of Pack Shots')

    @staticmethod
    def get_connection():
        return mysql.connector.connect(host='localhost', database='siftit', user='root', password='1234')

    def test_connection(self):
        self.cursor.execute('select * from restaurant')
        for res in self.cursor:
            print(res)

    @staticmethod
    def get_gtin(filename: str):
        num = filename.split('_')[0]
        return num if '.' not in num else num.split('.')[0]

    def insert_photos(self):
        self.cursor.execute('truncate table productoftheweek;')
        for photo in Path.iterdir(self.photos_dir):
            gtin = self.get_gtin(photo.name)
            item = GTIN_TO_PRODUCT[gtin]

            with open(photo, 'rb') as photo_file:
                blob = photo_file.read()
                self.cursor.execute(self.query, (item.product_name, item.gtin, item.product_brand, 'Unilever', blob))

        self.connection.commit()

    def show_photo(self):
        self.cursor.execute('select productImage from productoftheweek where id = 27;')
        data = self.cursor.fetchall()
        image = data[0][0]
        binary_data = base64.b64decode(image)
        image = Image.open(io.BytesIO(binary_data))
        image.show()


if __name__ == '__main__':
    db = InsertImagesToDataBase()
    db.insert_photos()
    # db.show_photo()
