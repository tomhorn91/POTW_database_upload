import base64
import io
import mysql.connector
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Product:
    id: int
    product_name: str
    product_image_path: Path
    free_sample_code: str
    product_blurb: str
    url: str


bases = Product(1,
                'Knorr® Professional Ultimate Bases',
                Path('POTW Front of Pack Shots/10048001509655_C1C1_conversion1.jpg'),
                '0000-0000',
                r"The workhorse of your kitchen, relying on real ingredients and flavor rather than salt.",
                r'https://www.foodservicedirect.com/bases')

cream_soup = Product(2,
                     'LeGout® Cream Soup Base',
                     Path('POTW Front of Pack Shots/10037500000329_C1N1_conversion1.jpg'),
                     '0000-0000',
                     r"Delivers consistently creamy flavor; the perfect foundation for a broad range of recipes.",
                     r'https://www.foodservicedirect.com/cream-soup-bases')

small_mayo = Product(3,
                     "Hellmann's® / Best Foods® Real Mayo",
                     Path('POTW Front of Pack Shots/10048001370491_C1N1_conversion1.jpg'),
                     '0000-0000',
                     r"Show your guests that you care about quality, whether they dine onsite or at home.",
                     r'https://www.foodservicedirect.com/foh-mayo')

big_mayo = Product(4,
                   "Hellmann's® / Best Foods® Real Mayo",
                   Path('POTW Front of Pack Shots/10048001265308_C1C1_conversion1.jpg'),
                   '0000-0000',
                   r"Provide the taste your guests love with the performance you can rely on.",
                   r'https://www.foodservicedirect.com/boh-mayo')

vegan_mayo = Product(5,
                     "Hellmann's® / Best Foods® Vegan Mayo",
                     Path('POTW Front of Pack Shots/10048001010724_C1C1_conversion1.jpg'),
                     '0000-0000',
                     r"A multi-purpose, delicious, egg-free dressing for sandwiches, salads, and dipping sauces.",
                     r'https://www.foodservicedirect.com/vegan-mayo')

alfredo = Product(6,
                  'Knorr Alfredo Sauce JAW 4 1.33lb',
                  Path('POTW Front of Pack Shots/10048001013305_C1C1_conversion1.jpg'),
                  '0000-0000',
                  r"A versatile sauce that will deliver on taste and performance.",
                  r'https://www.foodservicedirect.com/alfredo')

caldo = Product(7,
                'Knorr® Professional Caldo',
                Path('POTW Front of Pack Shots/10048001039091_C1N1_conversion1.jpg'),
                '0000-0000',
                r"Add that authentic Latin flavor to your menu.",
                r'https://www.foodservicedirect.com/caldo')

demi_glace = Product(8,
                     'Knorr Demi Glace Sauce 4 1.75 lbs',
                     Path('POTW Front of Pack Shots/10048001386737_C1C1_conversion1.jpg'),
                     '0000-0000',
                     r"Delivers a perfect balance of beef, mirepoix, and tomato flavors.",
                     r'https://www.foodservicedirect.com/demi')

hollandaise = Product(9,
                      'Knorr Ultimate Hollandaise Sauce 4 30.2z',
                      Path('POTW Front of Pack Shots/10048001005829_C1C1_conversion1.jpg'),
                      '0000-0000',
                      r"Serve scratch-like flavor without breaking or separating.",
                      r'https://www.foodservicedirect.com/hollandaise')

conc_bases = Product(10,
                     'Knorr® Professional Liquid Concentrates',
                     Path('POTW Front of Pack Shots/10048001145433_C1N1_conversion1.jpg'),
                     '0000-0000',
                     r"Concentrated liquid base instantly creates broths and stocks with exceptional flavor, color, and aroma",
                     r'https://www.foodservicedirect.com/liquid-concentrated-bases')

gravy = Product(11,
                'Knorr® Professional Brown Gravy',
                Path('POTW Front of Pack Shots/10048001005508_C1N1_conversion1.jpg'),
                '0000-0000',
                r"Combines vegetables and select seasonings to make a rich homemade tasting gravy.",
                r'https://www.foodservicedirect.com/single-knorr-professional-brown-gravy-mix-6-83-ounce-1-each-23044361.html')

soup = Product(12,
               'Knorr® Professional Soup du Jour',
               Path('POTW Front of Pack Shots/10068400002236_C1C1_conversion1.jpg'),
               '0000-0000',
               r"Consistently deliver scratch-like taste, on-trend flavors, and with the added convenience of a shelf stable format.",
               r'https://www.foodservicedirect.com/soup-du-jour')

products = [
    bases, cream_soup, small_mayo, big_mayo, vegan_mayo, alfredo, caldo, demi_glace, hollandaise, conc_bases, gravy,
    soup
]

spec_sheets = {
    3: Path('selling_stories/Best Foods_FOH Mayo_selling story_editable_210310_english.pdf'),
    4: Path('selling_stories/Best Foods_FOH Mayo_selling story_editable_210310_english.pdf'),
    5: Path('selling_stories/HLMN_Vegan Mayo_Selling Story 1_editable_211101_english.pptx.pdf'),
    6: Path('selling_stories/Knorr Professional_Alfredo Sauce Just Add Water_210910_English.pdf'),
    7: Path('selling_stories/Knorr Professional_Caldo_Selling Story_2079_English.pdf'),
    8: Path('selling_stories/Knorr Professional_Demi Glace_Selling Story_20714_English.pdf'),
    9: Path('selling_stories/Knorr Professional_Hollandaise_ Selling Story _21915_English.pdf'),
    10: Path('selling_stories/Knorr Professional_Liquid Concentrated Bases_Selling Story_20122_English.pdf'),
    11: Path('selling_stories/Knorr Professional_Selling Story_Gravies_Customizable_191218_English.pdf'),
    12: Path('selling_stories/Knorr Professional_Soup du Jour_Selling Story_Customizable_210727_English.pdf.pdf'),
    1: Path('selling_stories/Knorr Professional_Ultimate Bases_Selling Story_2079_English.pdf'),
    2: Path('selling_stories/LeGout_Cream Soup Base _Selling Story_2078_English.pdf'),
}

youtube = {
    2: 'https://www.youtube.com/watch?v=ohIT6Mbmu2Y',
    5: 'https://www.youtube.com/watch?v=rkOfYSrVpR0',
    10: 'https://www.youtube.com/watch?v=gtuwTL9LRRc',

}

create_table = '''
-- auto-generated definition
create table productoftheweek
(
    id                      int auto_increment
        primary key,
    productName             varchar(64)          not null,
    distributorName         varchar(64)          not null,
    lastDisplayed           date                 null,
    currentProductOfTheWeek tinyint(1) default 0 not null,
    productImage            longblob             null,
    youtubeLink             varchar(64)          null,
    specSheetImage          longblob             null,
    productLink             varchar(128)         null,
    freeSampleCode          varchar(32)          null,  
    productBlurb            varchar(256)         null,
    constraint productoftheweek_index_uindex
        unique (id)
);
'''

create_sample_table = '''
create table productoftheweek_samples
(
    id                          int auto_increment
        primary key,
    restaurantId                bigint                    not null,
    productOfTheWeekId          int                       not null,
    dateOrdered                 date default '1999-01-01' not null,
    constraint productoftheweek_samples_id_uindex
        unique (id)
);
'''

MAIN_QUERY = 'insert into productoftheweek (productName, distributorName, productImage, productLink, freeSampleCode, productBlurb) ' \
             'values(%s, %s, %s, %s, %s, %s) '

SPEC_SHEET_QUERY = 'update productoftheweek set specSheetImage = %s where id = %s;'

YOUTUBE_QUERY = 'update productoftheweek set youtubeLink = %s where id = %s;'


def main():
    connection = mysql.connector.connect(host='localhost', database='siftit', user='root', password='1234')
    cursor = connection.cursor()

    cursor.execute('drop table if exists productoftheweek;')
    cursor.execute(create_table)
    cursor.execute('drop table if exists productoftheweek_samples;')
    cursor.execute(create_sample_table)

    for product in products:
        blob = None
        with open(product.product_image_path, 'rb') as photo:
            blob = photo.read()

        blob = base64.b64encode(blob)

        cursor.execute(MAIN_QUERY,
                       (product.product_name, 'Unilever Food Solutions', blob, product.url, product.free_sample_code, product.product_blurb))
        connection.commit()

        if product.id in spec_sheets:
            spec_blob = None
            with open(spec_sheets[product.id], 'rb') as spec_photo:
                spec_blob = spec_photo.read()
            spec_blob = base64.b64encode(spec_blob)

            cursor.execute(SPEC_SHEET_QUERY, (spec_blob, product.id))
            connection.commit()

        if product.id in youtube:
            cursor.execute(YOUTUBE_QUERY, (youtube[product.id], product.id))
            connection.commit()


if __name__ == '__main__':
    main()
