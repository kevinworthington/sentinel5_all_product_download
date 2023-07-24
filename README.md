# sentinel5_all_product_download

The following script uses the [sentinel5dl library](https://sentinel5dl.emissions-api.org/home.html) to access Sentinel data across multiple product lines.

Here's a [full list of available products](https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-5p/products-algorithms).

Surface Irradiance/erythemal dose, Suomi-NPP VIIRS Clouds, A-priori profile shapes for the NO2, HCHO and SO2 vertical column retrievals are not included among the products being downloaded.

## Running the script
To run the script, the following commands can be used, which first creates a visual environment with the required libraries.

```
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
# and to run the script use
python main.py
```

## future improvements include:
- Adding the ability to pass arguments from the command line so information isn't hard-coded.