from sentinel5dl import search, download
import os
folder ="data"
# load data into the specified folder and remove if the folder exists
# if os.path.exists(folder):
#         os.rmdir(folder)
if not os.path.exists(folder):
        os.makedirs(folder)
# Search for Sentinel-5 products
# https://sentinel5dl.emissions-api.org/home.html
# product codes - https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-5p/products-algorithms
#
product_list=['L2__O3____','L2__O3_TCL','L2__O3__PR','L2__NO2___','L2__SO2___','L2__CO____','L2__CH4___','L2__HCHO__','L2__CLOUD_',
              'L2__AER_AI','L2__AER_LH']

for p in product_list:
        print(p)
        result = search(
                polygon='POLYGON((-109 41, -109 37, -102 37, -102 41, -109 41))',
                begin_ts='2021-07-26T00:00:00.000Z',
                end_ts='2021-08-25T23:59:59.999Z',
                product=p,
                processing_level='L2',
                processing_mode='Offline')


        # print(result.get('products'))

        # Download found products to the local folder
        #Not: response 429 means too many requests were sent
        download(result.get('products'),folder)