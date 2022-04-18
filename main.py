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


knorrSeafoodBase = Product('10048001014326', 'Knorr', 'Ultimate Seafood Liquid Concentrate Base')
knorrCaldoBoullion = Product('10048001038537', 'Knorr', 'Shrimp Bouillon')
knorrCaldoTomate = Product('10048001761459', 'Knorr', 'Tomato Bouillon With Chicken Flavor')
leGoutCreamSoupBase = Product('10037500000329', 'Le Gout', 'Cream Soup Base')
knorrBrownGravyMix = Product('10048001005508', 'Knorr', 'Brown Gravy Mix')
knorrHollandaiseSauceMix = Product('10048001005829', 'Knorr', 'Hollandaise Sauce Mix')
hellmansVeganMayo = Product('10048001010724', 'Hellman\'s', 'Vegan Dressing & Sandwich Spread')
hellmansVeganMayo2 = Product('10048001010731', 'Best Foods', 'Vegan Dressing & Sandwich Spread')
knorrAlfredoPastaSauceMix = Product('10048001013305', 'Knorr', 'Alfredo Pasta Sauce Mix')
knorrBeefBoullon = Product('10048001039091', 'Knorr', 'Beef Flavor Bouillon')
knorrChickenBase = Product('10048001145433', 'Knorr', 'Chicken Base')
knorrBeefBase = Product('10048001509655', 'Knorr', 'Beef Base')
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
    '10048001014326': knorrSeafoodBase,
    '10048001038537': knorrCaldoBoullion,
    '10048001761459': knorrCaldoTomate,
    '10037500000329': leGoutCreamSoupBase,
    '10048001005508': knorrBrownGravyMix,
    '10048001005829': knorrHollandaiseSauceMix,
    '10048001010724': hellmansVeganMayo,
    '10048001010731': hellmansVeganMayo2,
    '10048001013305': knorrAlfredoPastaSauceMix,
    '10048001039091': knorrBeefBoullon,
    '10048001145433': knorrChickenBase,
    '10048001509655': knorrBeefBase,
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

youtube_links = {
    '10048001145433': 'https://www.youtube.com/watch?v=gtuwTL9LRRc',
    '10037500000329': 'https://www.youtube.com/watch?v=ohIT6Mbmu2Y',
    '10068400001994': 'https://youtu.be/CS2eL38BqX8',
    '10068400002236': 'https://youtu.be/CS2eL38BqX8',
    '10068400002342': 'https://youtu.be/CS2eL38BqX8',
    '10048001010724': 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
    '10048001010731': 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
    '10048001265308': 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
    '10048001356969': 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
    '10048001370491': 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
}

product_links = {
    'https://www.foodservicedirect.com/bases': ['10048001509655',
                                                '10048001503363',
                                                '10048001510170'],
    'https://www.foodservicedirect.com/cream-soup-bases': ['10037500000329'],
    'https://www.foodservicedirect.com/foh-mayo': ['10048001357539',
                                                   '10048001370507',
                                                   '10048001370491',
                                                   '10048001356969', ],
    'https://www.foodservicedirect.com/boh-mayo': ['10048001265742',
                                                   '10048001265308', ],
    'https://www.foodservicedirect.com/vegan-mayo': ['10048001010724',
                                                     '10048001010731'],
    'https://www.foodservicedirect.com/alfredo': ['10048001013305'],
    'https://www.foodservicedirect.com/caldo': ['10048001038537',
                                                '10048001759456',
                                                '10048001760452',
                                                '10048001039091',
                                                '10048001761459'],
    'https://www.foodservicedirect.com/demi': ['10048001386737'],
    'https://www.foodservicedirect.com/hollandaise': ['10048001005829'],
    'https://www.foodservicedirect.com/liquid-concentrated-bases': ['10048001145440',
                                                                    '10048001145433',
                                                                    '10048001014326',
                                                                    '10048001145457'],
    'https://www.foodservicedirect.com/single-knorr-professional-brown-gravy-mix-6-83-ounce-1-each-23044361.html':
        ['10048001005508'],
    'https://www.foodservicedirect.com/soup-du-jour': ['10068400002236',
                                                       '10068400001994',
                                                       '10068400002342,'],
}

create_table = '''
-- auto-generated definition
create table productoftheweek
(
    id                      int auto_increment
        primary key,
    productName             varchar(64)          not null,
    gtin                    varchar(32)          not null,
    productBrand            varchar(64)          not null,
    distributorName         varchar(64)          not null,
    lastDisplayed           date                 null,
    currentProductOfTheWeek tinyint(1) default 0 not null,
    productImage            longblob             null,
    youtubeLink             varchar(64)          null,
    specSheetImage          longblob             null,
    productLink             varchar(128)         null,  
    constraint productoftheweek_index_uindex
        unique (id)
);
'''

create_sample_table = '''
create table productoftheweek_samples
(
    id                   int auto_increment
        primary key,
    restaurantId         bigint      not null,
    productOfTheWeekGtin varchar(64) not null,
    constraint productoftheweek_samples_id_uindex
        unique (id)
);
'''


class InsertImagesToDataBase:
    def __init__(self):
        self.connection = self.get_connection()
        self.cursor = self.connection.cursor()
        self.database = 'productoftheweek'
        self.main_query = 'insert into productoftheweek (productName, gtin, productBrand, distributorName, ' \
                          'productImage, specSheetImage, youtubeLink) ' \
                          'values(%s, %s, %s, %s, %s, %s, %s) '

        self.photos_dir = Path('POTW Front of Pack Shots')
        self.spec_sheet_dir = Path('spec_sheets')

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
        self.cursor.execute('drop table if exists productoftheweek;')
        self.cursor.execute(create_table)
        self.cursor.execute('drop table if exists productoftheweek_samples;')
        self.cursor.execute(create_sample_table)

        for photo in Path.iterdir(self.photos_dir):
            gtin = self.get_gtin(photo.name)
            item = GTIN_TO_PRODUCT[gtin]

            spec_sheet_blob = None
            youtube_link = None

            if gtin == '10048001005508':
                with open(self.spec_sheet_dir / '10048001005508 - KNORR BROWN GRAY MIX.pdf', 'rb') as file:
                    spec_sheet_blob = file.read()

            if gtin in youtube_links.keys():
                youtube_link = youtube_links[gtin]

            with open(photo, 'rb') as photo_file:
                blob = photo_file.read()
                self.cursor.execute(self.main_query, (
                    item.product_name, item.gtin, item.product_brand, 'Unilever', blob, spec_sheet_blob, youtube_link))

        self.connection.commit()

    def insert_product_links(self):
        for k, v in product_links.items():
            query = 'update productoftheweek set productLink = %s where gtin = %s;'
            for gtin in v:
                self.cursor.execute(query, (k, gtin))
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
    db.insert_product_links()
    # db.insert_spec_sheets()

    # db.show_photo()
