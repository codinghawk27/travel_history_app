import pandas as pd
import pydeck as pdk
import random
import streamlit as st
from datetime import datetime
from geopy.distance import geodesic


# --------------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------------
travels = [
    {"city": "Paris", "country": "Frankreich", "year": 1976, "lat": 48.8566, "lon": 2.3522},
    {"city": "Prag", "country": "Tschechien", "year": 1980, "lat": 50.08736, "lon": 14.42132},
    {"city": "München", "country": "Deutschland", "year": 1981, "lat": 48.1372, "lon": 11.5755},
    {"city": "S'Arenal", "country": "Spanien", "year": 1983, "lat": 39.500808, "lon": 2.756264},
    {"city": "London", "country": "UK", "year": 1984, "lat": 51.5072, "lon": -0.1275},
    {"city": "Brighton", "country": "UK", "year": 1984, "lat": 50.8429, "lon": -0.1313},
    {"city": "München", "country": "Deutschland", "year": 1985, "lat": 48.1372, "lon": 11.5755},
    {"city": "Vaduz", "country": "Liechtenstein", "year": 1985, "lat": 47.1415, "lon": 9.5215},
    {"city": "Malbun", "country": "Liechtenstein", "year": 1985, "lat": 47.09751, "lon": 9.615041},
    {"city": "Göteborg", "country": "Schweden", "year": 1986, "lat": 57.707233, "lon": 11.967017},
    {"city": "Oslo", "country": "Norwegen", "year": 1986, "lat": 59.91333, "lon": 10.73897},
    {"city": "Stockholm", "country": "Schweden", "year": 1986, "lat": 59.325117, "lon": 18.071093},
    {"city": "Turku", "country": "Finnland", "year": 1986, "lat": 60.451753, "lon": 22.267052},
    {"city": "Bonita Springs", "country": "USA", "year": 1987, "lat": 26.339806, "lon": -81.778697},
    {"city": "Naples", "country": "USA", "year": 1987, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 1987, "lat": 28.542111, "lon": -81.37903},
    {"city": "Luxemburg", "country": "Luxemburg", "year": 1987, "lat": 49.611172, "lon": 6.129762},
    {"city": "Washington D.C.", "country": "USA", "year": 1988, "lat": 38.895037, "lon": -77.036543},
    {"city": "Naples", "country": "USA", "year": 1988, "lat": 26.142198, "lon": -81.794294},
    {"city": "Paris", "country": "Frankreich", "year": 1988, "lat": 48.8566, "lon": 2.3522},
    {"city": "Bonita Springs", "country": "USA", "year": 1989, "lat": 26.339806, "lon": -81.778697},
    {"city": "Naples", "country": "USA", "year": 1989, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 1989, "lat": 28.542111, "lon": -81.37903},
    {"city": "Berlin", "country": "Deutschland", "year": 1989, "lat": 52.510885, "lon": 13.398937},
    {"city": "Valletta", "country": "Malta", "year": 1989, "lat": 35.898998, "lon": 14.513661},
    {"city": "Gozo", "country": "Malta", "year": 1989, "lat": 36.046778, "lon": 14.258256},
    {"city": "Rom", "country": "Italien", "year": 1990, "lat": 41.89332, "lon": 12.482932},
    {"city": "Naples", "country": "USA", "year": 1991, "lat": 26.142198, "lon": -81.794294},
    {"city": "Bern", "country": "Schweiz", "year": 1991, "lat": 46.948271, "lon": 7.451451},
    {"city": "Brüssel", "country": "Belgien", "year": 1992, "lat": 50.846557, "lon": 4.351697},
    {"city": "Sydney", "country": "Australien", "year": 1992, "lat": -33.854816, "lon": 151.216454},
    {"city": "Alice Springs", "country": "Australien", "year": 1992, "lat": -23.698388, "lon": 133.881289},
    {"city": "Cairns", "country": "Australien", "year": 1992, "lat": -16.920666, "lon": 145.772185},
    {"city": "Rockhampton", "country": "Australien", "year": 1992, "lat": -23.37825, "lon": 150.513444},
    {"city": "Yeppoon", "country": "Australien", "year": 1992, "lat": -23.134804, "lon": 150.743662},
    {"city": "K'gari", "country": "Australien", "year": 1992, "lat": -25.24672, "lon": 153.146804},
    {"city": "Brisbane", "country": "Australien", "year": 1992, "lat": -27.468968, "lon": 153.023499},
    {"city": "Melbourne", "country": "Australien", "year": 1992, "lat": -37.814218, "lon": 144.963161},
    {"city": "Athen", "country": "Griechenland", "year": 1993, "lat": 37.984149, "lon": 23.727984},
    {"city": "Sydney", "country": "Australien", "year": 1994, "lat": -33.854816, "lon": 151.216454},
    {"city": "Alice Springs", "country": "Australien", "year": 1994, "lat": -23.698388, "lon": 133.881289},
    {"city": "Darwin", "country": "Australien", "year": 1994, "lat": -12.46344, "lon": 130.845642},
    {"city": "Palm Cove", "country": "Australien", "year": 1994, "lat": -16.747201, "lon": 145.668545},
    {"city": "Brisbane", "country": "Australien", "year": 1994, "lat": -27.468968, "lon": 153.023499},
    {"city": "Vaduz", "country": "Liechtenstein", "year": 1994, "lat": 47.1415, "lon": 9.5215},
    {"city": "Malbun", "country": "Liechtenstein", "year": 1994, "lat": 47.09751, "lon": 9.615041},
    {"city": "Alcúdia", "country": "Spanien", "year": 1997, "lat": 39.852832, "lon": 3.121385},
    {"city": "München", "country": "Deutschland", "year": 2000, "lat": 48.1372, "lon": 11.5755},
    {"city": "Costa Calma", "country": "Spanien", "year": 2001, "lat": 28.160768, "lon": -14.230078},
    {"city": "Dresden", "country": "Deutschland", "year": 2006, "lat": 51.049329, "lon": 13.738144},
    {"city": "Paris", "country": "Frankreich", "year": 2007, "lat": 48.8566, "lon": 2.3522},
    {"city": "Disneyland Paris", "country": "Frankreich", "year": 2007, "lat": 48.87232, "lon": 2.775542},
    {"city": "Paris", "country": "Frankreich", "year": 2008, "lat": 48.8566, "lon": 2.3522},
    {"city": "Muro", "country": "Spanien", "year": 2009, "lat": 39.737064, "lon": 3.056707},
    {"city": "Rom", "country": "Italien", "year": 2010, "lat": 41.89332, "lon": 12.482932},
    {"city": "Naples", "country": "USA", "year": 2011, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 2011, "lat": 28.542111, "lon": -81.37903},
    {"city": "Naples", "country": "USA", "year": 2012, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 2012, "lat": 28.542111, "lon": -81.37903},
    {"city": "Washington D.C.", "country": "USA", "year": 2012, "lat": 38.895037, "lon": -77.036543},
    {"city": "Shanghai", "country": "China", "year": 2013, "lat": 31.225299, "lon": 121.48905},
    {"city": "San Francisco", "country": "USA", "year": 2013, "lat": 37.779259, "lon": -122.419329},
    {"city": "Los Angeles", "country": "USA", "year": 2013, "lat": 34.053691, "lon": -118.242767},
    {"city": "San Diego", "country": "USA", "year": 2013, "lat": 32.717421, "lon": -117.162771},
    {"city": "Las Vegas", "country": "USA", "year": 2013, "lat": 36.167256, "lon": -115.148516},
    {"city": "Naples", "country": "USA", "year": 2014, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 2014, "lat": 28.542111, "lon": -81.37903},
    {"city": "Disneyland Paris", "country": "Frankreich", "year": 2014, "lat": 48.87232, "lon": 2.775542},
    {"city": "Passau", "country": "Deutschland", "year": 2014, "lat": 48.574823, "lon": 13.460974},
    {"city": "Dubai", "country": "VAE", "year": 2015, "lat": 25.0657, "lon": 55.1713},
    {"city": "Luxemburg", "country": "Luxemburg", "year": 2015, "lat": 49.611172, "lon": 6.129762},
    {"city": "Naples", "country": "USA", "year": 2015, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 2015, "lat": 28.542111, "lon": -81.37903},
    {"city": "Shanghai", "country": "China", "year": 2016, "lat": 31.225299, "lon": 121.48905},
    {"city": "Toronto", "country": "Kanada", "year": 2016, "lat": 43.653963, "lon": -79.387207},
    {"city": "Naples", "country": "USA", "year": 2016, "lat": 26.142198, "lon": -81.794294},
    {"city": "Orlando", "country": "USA", "year": 2016, "lat": 28.542111, "lon": -81.37903},
    {"city": "Shanghai", "country": "China", "year": 2017, "lat": 31.225299, "lon": 121.48905},
    {"city": "Sydney", "country": "Australien", "year": 2017, "lat": -33.854816, "lon": 151.216454},
    {"city": "Brisbane", "country": "Australien", "year": 2017, "lat": -27.468968, "lon": 153.023499},
    {"city": "Hyderabad", "country": "Indien", "year": 2018, "lat": 17.388786, "lon": 78.461065},
    {"city": "Alice Springs", "country": "Australien", "year": 2018, "lat": -23.698388, "lon": 133.881289},
    {"city": "Cairns", "country": "Australien", "year": 2018, "lat": -16.920666, "lon": 145.772185},
    {"city": "Shanghai", "country": "China", "year": 2018, "lat": 31.225299, "lon": 121.48905},
    {"city": "Sydney", "country": "Australien", "year": 2018, "lat": -33.854816, "lon": 151.216454},
    {"city": "Brisbane", "country": "Australien", "year": 2018, "lat": -27.468968, "lon": 153.023499},
    {"city": "Naha", "country": "Japan", "year": 2019, "lat": 26.213854, "lon": 127.692221},
    {"city": "Kyoto", "country": "Japan", "year": 2019, "lat": 35.023132, "lon": 135.763407},
    {"city": "Nara", "country": "Japan", "year": 2019, "lat": 34.5666644, "lon": 135.7666636},
    {"city": "Osaka", "country": "Japan", "year": 2019, "lat": 34.693757, "lon": 135.501454},
    {"city": "Hiroshima", "country": "Japan", "year": 2019, "lat": 34.391606, "lon": 132.451816},
    {"city": "Tokio", "country": "Japan", "year": 2020, "lat": 35.682839, "lon": 139.759455},
    {"city": "Naha", "country": "Japan", "year": 2020, "lat": 26.213854, "lon": 127.692221},
    {"city": "Motobu", "country": "Japan", "year": 2020, "lat": 26.657781, "lon": 127.897847},
    {"city": "Naha", "country": "Japan", "year": 2021, "lat": 26.213854, "lon": 127.692221},
    {"city": "Motobu", "country": "Japan", "year": 2021, "lat": 26.657781, "lon": 127.897847},
    {"city": "Tokio", "country": "Japan", "year": 2021, "lat": 35.682839, "lon": 139.759455},
    {"city": "Erfurt", "country": "Deutschland", "year": 2022, "lat": 50.977797, "lon": 11.028736},
    {"city": "Wien", "country": "Österreich", "year": 2023, "lat": 48.208354, "lon": 16.372504},
    {"city": "Playa de Muro", "country": "Spanien", "year": 2023, "lat": 39.808503, "lon": 3.118361},
    {"city": "Potsdam", "country": "Deutschland", "year": 2024, "lat": 52.400931, "lon": 13.05914},
    {"city": "Berlin", "country": "Deutschland", "year": 2024, "lat": 52.510885, "lon": 13.398937},
    {"city": "Jena", "country": "Deutschland", "year": 2024, "lat": 50.928172, "lon": 11.587936},
    {"city": "Olympia", "country": "USA", "year": 2024, "lat": 47.045102, "lon": -122.895008},
    {"city": "Seattle", "country": "USA", "year": 2024, "lat": 47.603832, "lon": -122.330062},
    {"city": "Honolulu", "country": "USA", "year": 2024, "lat": 21.304547, "lon": -157.855676},
    {"city": "Kobe", "country": "Japan", "year": 2024, "lat": 34.693238, "lon": 135.194376},
    {"city": "Nagoya", "country": "Japan", "year": 2024, "lat": 35.185105, "lon": 136.899844},
    {"city": "Yokohama", "country": "Japan", "year": 2024, "lat": 35.444991, "lon": 139.636768},
    {"city": "Tokio", "country": "Japan", "year": 2024, "lat": 35.682839, "lon": 139.759455},
    {"city": "Budapest", "country": "Ungarn", "year": 2025, "lat": 47.498382, "lon": 19.040471},
]
travels = pd.DataFrame(travels)

images = {
    "Paris": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg/1920px-La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg",
    "Prag": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Hradschin_Prag.jpg",
    "München": "https://upload.wikimedia.org/wikipedia/commons/5/58/Muenchen-Altstadt.jpg",
    "S'Arenal": "https://upload.wikimedia.org/wikipedia/commons/a/a3/Platja_de_Palma_1.jpg",
    "London": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/London_Montage_L.jpg/960px-London_Montage_L.jpg",
    "Brighton": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Brighton_Seafront.jpg/1920px-Brighton_Seafront.jpg",
    "Vaduz": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Liechtenstein_asv2022-10_img02_Vaduz_Aussicht_beim_Schloss.jpg/1920px-Liechtenstein_asv2022-10_img02_Vaduz_Aussicht_beim_Schloss.jpg",
    "Malbun": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Malbun_seen_from_Augstenberg_%28valo139%29.jpg/1920px-Malbun_seen_from_Augstenberg_%28valo139%29.jpg",
    "Göteborg": "https://upload.wikimedia.org/wikipedia/commons/a/a8/Gothenburg_new_montage_2012.png",
    "Oslo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Holmenkollen-Oslo-Panorama_M%C3%A4rz_2025.jpg/1920px-Holmenkollen-Oslo-Panorama_M%C3%A4rz_2025.jpg",
    "Stockholm": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Stockholm.jpg/800px-Stockholm.jpg",
    "Turku": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Aurajoki%2C_Turku_2.jpg/1920px-Aurajoki%2C_Turku_2.jpg",
    "Bonita Springs": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Bonita_Beach.JPG/1920px-Bonita_Beach.JPG",
    "Naples": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Naples_Beach3.jpg/1920px-Naples_Beach3.jpg",
    "Orlando": "https://upload.wikimedia.org/wikipedia/commons/2/26/Orlando_Montage.png",
    "Luxemburg": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Luxemburg.jpg/1920px-Luxemburg.jpg",
    "Washington D.C.": "https://upload.wikimedia.org/wikipedia/commons/8/81/Washington_Montage_2016.png",
    "Berlin": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Nr_2_Berlin_Panorama_von_der_Siegess%C3%A4ule_2021.jpg/1920px-Nr_2_Berlin_Panorama_von_der_Siegess%C3%A4ule_2021.jpg",
    "Valletta": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Panorama_of_Valletta.jpg/1920px-Panorama_of_Valletta.jpg",
    "Gozo": "https://upload.wikimedia.org/wikipedia/commons/b/b9/Gozo_from_space_via_laser_ESA378503_%28cropped%29.jpg",
    "Rom": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Rome_Montage_2017.png",
    "Bern": "https://upload.wikimedia.org/wikipedia/commons/7/75/Bern_luftaufnahme.png",
    "Brüssel": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/TE-Collage_Brussels.png/800px-TE-Collage_Brussels.png",
    "Sydney": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Sydney_Opera_House_and_Harbour_Bridge_Dusk_%282%29_2019-06-21.jpg/1920px-Sydney_Opera_House_and_Harbour_Bridge_Dusk_%282%29_2019-06-21.jpg",
    "Alice Springs": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Alice_Springs%2C_2015_%2801%29.JPG/1280px-Alice_Springs%2C_2015_%2801%29.JPG",
    "Cairns": "https://upload.wikimedia.org/wikipedia/commons/a/a1/CairnsQueensland.jpg",
    "Rockhampton": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Rockhampton_1.jpg/1920px-Rockhampton_1.jpg",
    "Yeppoon": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/02/32/04/ee/rosslyn-bay-resort.jpg?w=600&h=-1&s=1",
    "K'gari": "https://upload.wikimedia.org/wikipedia/commons/e/e4/Fraser_Island.png",
    "Brisbane": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Brisbane_May_2013.jpg/1920px-Brisbane_May_2013.jpg",
    "Melbourne": "https://upload.wikimedia.org/wikipedia/commons/f/f4/Melbourne_montage_6.jpg",
    "Athen": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg/1920px-Monastiraki_Square_and_Acropolis_in_Athens_%2844149181684%29.jpg",
    "Darwin": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Darwin_homebanner.jpg/1920px-Darwin_homebanner.jpg",
    "Palm Cove": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Palm_trees_at_Palm_Cove_Beach%2C_Queensland%2C_2020%2C_03.jpg/500px-Palm_trees_at_Palm_Cove_Beach%2C_Queensland%2C_2020%2C_03.jpg",
    "Alcúdia": "https://upload.wikimedia.org/wikipedia/commons/7/73/Alcudia_Stadtmauer.jpg",
    "Costa Calma": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Costa_Calma_D81_6933_%2839814790835%29.jpg/1920px-Costa_Calma_D81_6933_%2839814790835%29.jpg",
    "Dresden": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/HFBK_Dresden_2024_Luftbild_Toni_Klemm_2500px.jpg/1920px-HFBK_Dresden_2024_Luftbild_Toni_Klemm_2500px.jpg",
    "Disneyland Paris": "https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Sleeping_Beauty_Castle%2C_Disneyland%2C_Paris.jpg/1920px-Sleeping_Beauty_Castle%2C_Disneyland%2C_Paris.jpg",
    "Muro": "https://abcmallorcastorage.blob.core.windows.net/images/2016/07/muro-5.jpg",
    "Shanghai": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Huangpu_Park_20124-Shanghai_%2832208802494%29.jpg/1920px-Huangpu_Park_20124-Shanghai_%2832208802494%29.jpg",
    "San Francisco": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/The_Golden_Gate_Bridge_2019.jpg/1920px-The_Golden_Gate_Bridge_2019.jpg",
    "Los Angeles": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Los_Angeles_with_Mount_Baldy.jpg/1920px-Los_Angeles_with_Mount_Baldy.jpg",
    "San Diego": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/SD_Montage.jpg/800px-SD_Montage.jpg",
    "Las Vegas": "https://upload.wikimedia.org/wikipedia/commons/e/ee/Las_Vegas_Strip_09_2017_4897.jpg",
    "Passau": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Der_Passauer_Dom_vom_%22F%C3%BCnferlsteg%22_aus_gesehen.JPG/1920px-Der_Passauer_Dom_vom_%22F%C3%BCnferlsteg%22_aus_gesehen.JPG",
    "Dubai": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Dubai_Skyline_mit_Burj_Khalifa_%2818241030269%29.jpg/1920px-Dubai_Skyline_mit_Burj_Khalifa_%2818241030269%29.jpg",
    "Toronto": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Toronto_Skyline_viewed_from_Algonquin_Island_%2816-9_crop%29.jpg/1920px-Toronto_Skyline_viewed_from_Algonquin_Island_%2816-9_crop%29.jpg",
    "Hyderabad": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Hyderabad_montage-2.png",
    "Naha": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Naha_Shuri_Castle16s5s3200.jpg/1920px-Naha_Shuri_Castle16s5s3200.jpg",
    "Kyoto": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/%E4%BA%AC%E9%83%BD%E5%A4%9C%E6%99%AF_2015_%2831985638715%29.jpg/1920px-%E4%BA%AC%E9%83%BD%E5%A4%9C%E6%99%AF_2015_%2831985638715%29.jpg",
    "Nara": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Naracityview2005.jpg",
    "Osaka": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Osaka_Castle_03bs3200.jpg/1920px-Osaka_Castle_03bs3200.jpg",
    "Tokio": "https://upload.wikimedia.org/wikipedia/commons/b/bf/Tokyo_Montage_2015.jpg",
    "Motobu": "https://visitokinawajapan.com/wp-content/themes/visit-okinawa_multi-language/lang/en/assets/img/destinations/okinawa-main-island/northern-okinawa-main-island/motobu-peninsula/de988_02_motobu-peninsula-kouri-island.webp",
    "Erfurt": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Erfurt_cathedral_and_severi_church.jpg/1920px-Erfurt_cathedral_and_severi_church.jpg",
    "Wien": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Collage_von_Wien.jpg/960px-Collage_von_Wien.jpg",
    "Playa de Muro": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0f/f8/b2/93/zona-central-da-praia.jpg?w=900&h=500&s=1",
    "Potsdam": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Havel-Park-Lake-Babelsberg-Downtown-Potsdam-Green.jpg",
    "Jena": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Zentrum_Jenas_2008-05-24.JPG/1920px-Zentrum_Jenas_2008-05-24.JPG",
    "Olympia": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/2009-0606-WashingtonStateCapitol.jpg/500px-2009-0606-WashingtonStateCapitol.jpg",
    "Seattle": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Seattle_4.jpg/1920px-Seattle_4.jpg",
    "Honolulu": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/S%C3%BCdk%C3%BCste_Oahus.jpg/1920px-S%C3%BCdk%C3%BCste_Oahus.jpg",
    "Kobe": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Port_of_Kobe02s4100.jpg/1920px-Port_of_Kobe02s4100.jpg",
    "Nagoya": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Nagoya_Night_View.jpg/1920px-Nagoya_Night_View.jpg",
    "Yokohama": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Minato_Mirai_21_Mid_View.JPG/1920px-Minato_Mirai_21_Mid_View.JPG",
    "Budapest": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/20190503_Hungarian_Parliament_Building_1814_2263_DxO.jpg/1920px-20190503_Hungarian_Parliament_Building_1814_2263_DxO.jpg",
    "Hiroshima": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Atomic_Bomb_Dome_and_Motoyaso_River%2C_Hiroshima%2C_Northwest_view_20190417_1.jpg/1920px-Atomic_Bomb_Dome_and_Motoyaso_River%2C_Hiroshima%2C_Northwest_view_20190417_1.jpg",
    
}
travels["image"] = travels["city"].map(images)

# Continents mapping
continents_mapping = {
    "Europa": ["Italien", "Deutschland", "Frankreich", "Spanien"],
    "Nordamerika": ["USA", "Kanada", "Mexiko"],
    "Südamerika": ["Brasilien", "Argentinien", "Chile"],
    "Asien": ["Japan", "China", "Thailand", "Indien"],
    "Afrika": ["Südafrika", "Ägypten", "Marokko"],
    "Ozeanien": ["Australien", "Neuseeland"],
}
capital_cities = [
    "Paris",
    "Prag",
    "London",
    "Vaduz",
    "Oslo",
    "Stockholm",
    "Luxemburg",
    "Washington D.C.",
    "Berlin",
    "Valletta",
    "Rom",
    "Bern",
    "Brüssel",
    "Athen",
    "Tokio",
    "Wien",
    "Budapest",
]

# Starting point is Stuttgart
stuttgart_coords = (48.783333, 9.183333)

def distance_from_stuttgart(lat, lon):
    return geodesic(stuttgart_coords, (lat, lon)).kilometers

travels["distance_km"] = travels.apply(lambda r: distance_from_stuttgart(r["lat"], r["lon"]), axis=1)


# --------------------------------------------------------------------------------
# App-Layout
# --------------------------------------------------------------------------------
st.set_page_config(page_title="Travel History", layout="wide")
st.title("🌍 Roger's persönliches Reise-Archiv")

st.markdown("Willkommen! Diese App zeigt eine interaktive Übersicht deiner Reisen und Abenteuer.")

# Tabs
interactive_map, travel_diary, stats, future, quiz = st.tabs([
    "1. Interaktive Karte",
    "2. Reisetagebuch",
    "3. Statistiken",
    "4. Zukunft",
    "5. Quiz",
])

if "future_travels" not in st.session_state:
    st.session_state["future_travels"] = pd.DataFrame(columns=["city", "country", "year"])
if "current_question" not in st.session_state:
    st.session_state["current_question"] = random.choice(travels.to_dict(orient="records"))
if "score" not in st.session_state:
    st.session_state["score"] = 0

# --------------------------------------------------------------------------------
# 1. Interaktive Karte
# --------------------------------------------------------------------------------
with interactive_map:    
    st.subheader("Bereiste Orte")

    # Variante 1:
    selected_city = st.selectbox("Wähle eine Stadt", travels["city"])
    row = travels[travels["city"] == selected_city].iloc[0]

    # Center map view to the selected city
    view_state = pdk.ViewState(
        latitude=row["lat"],
        longitude=row["lon"],
        zoom=2,
    )

    # Layer with all travelled places
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=travels,
        get_position="[lon, lat]",
        get_color="[200, 30, 0, 160]",
        get_radius=50_000,
        pickable=True,
    )

    tooltip = {
        "html": "<b>{city}</b>, {country}<br/>Jahr: {year}<br/><img src='{image}' width='150'/>",
        "style": {"backgroundColor": "white", "color": "black"},
    }

    st.pydeck_chart(
        pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            map_style="light",
            tooltip=tooltip,
        )
    )

    st.write(f"**{row['city']} ({row['country']}, {row['year']})**")
    st.image(images.get(row["city"], ""), width=400)

# --------------------------------------------------------------------------------
# 2. Reisetagebuch
# --------------------------------------------------------------------------------
with travel_diary:
    st.subheader("Dein Reisetagebuch")
    year = st.slider("Wähle ein Jahr", int(travels["year"].min()), int(travels["year"].max()))
    selection = travels[travels["year"] == year]
    if not selection.empty:
        st.dataframe(
            selection[["city", "country", "year", "distance_km", "lat", "lon"]],
            hide_index=True
        )
        for _, r in selection.iterrows():
            st.markdown(f"### {r['city']} - {r['country']}")
            st.image(images.get(r["city"], ""), width=300)
            st.write("Hier könnte eine Anekdote oder ein Reisebericht stehen ✍️")
    else:
        st.info("Keine Reisen in diesem Jahr eingetragen.")

# --------------------------------------------------------------------------------
# 3. Statistiken & Fun Facts
# --------------------------------------------------------------------------------
with stats:
    st.subheader("Statistiken über deine Reisen")

    # Calculations
    num_cities = int(travels["city"].nunique())
    num_countries = int(travels["country"].nunique())
    num_travels = int(travels.shape[0])
    current_year = datetime.now().year
    travels_this_year = int(travels[travels["year"] == current_year].shape[0])
    total_km = int(travels["distance_km"].sum())
    average_km = round(travels["distance_km"].mean(), 0)
    # Capital cities
    traveled_capitals = travels[travels["city"].isin(capital_cities)]
    num_capitals = int(traveled_capitals["city"].nunique())
    worldwide_capitals = 195
    percentage_capitals = round(num_capitals / worldwide_capitals * 100, 2)
    # Average travels per year
    travels_per_year = travels.groupby("year").size()
    mean_travels_per_year = travels_per_year.mean().round(2)
    delta_travels = travels_this_year - mean_travels_per_year
    # Continents mapping
    traveled_continents = {k for k, l in continents_mapping.items() if travels["country"].isin(l).any()}
    num_continents = len(traveled_continents)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏙️ Bereiste Städte", num_cities)
    with col2:
        st.metric("🌍 Bereiste Länder", num_countries)
    with col3:
        st.metric("🧳 Reisen insgesamt", num_travels)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.metric("📅 Reisen dieses Jahr", travels_this_year, delta=f"{delta_travels:+.1f} ggü. Ø")
    with col5:
        st.metric("✈️ Zurückgelegte km", f"{total_km:,}".replace(",", "."))  # mit Tausenderpunkten
    with col6:
        st.metric("🏛️ Bereiste Hauptstädte", num_capitals)

    col7, col8, col9 = st.columns(3)
    with col7:
        st.metric("📊 Anteil Hauptstädte (%)", percentage_capitals)
    with col8:
        st.metric("🌎 Kontinente bereist", num_continents)
    with col9:
        st.metric("📐 ∅ Distanz pro Reise (km)", f"{int(average_km):,}".replace(",", "."))


    st.markdown("---")

    # Diagramme
    st.write("### 📈 Reisen pro Jahr")
    st.bar_chart(travels.groupby("year").size())

    # Top-Reiseziele
    st.write("### 🏆 Top-Reiseziele (nach Ländern)")
    st.write(travels["country"].value_counts())

    # Entfernteste Reise
    furthest_travel = travels.loc[travels["distance_km"].idxmax()]
    st.write("### 📏 Entfernteste Reise")
    st.write(
        f"{furthest_travel['city']} ({furthest_travel['country']}) - "
        f"{int(furthest_travel['distance_km']):,} km von Stuttgart entfernt".replace(",", ".")
    )

# --------------------------------------------------------------------------------
# 4. Zukunftsperspektive
# --------------------------------------------------------------------------------
with future:
    st.subheader("🌟 Deine Wunschliste")

    # Input fields
    city = st.text_input("Stadt")
    country = st.text_input("Land")
    year = st.number_input("Jahr", min_value=datetime.now().year, max_value=2100, step=1)

    # Button to add a new place
    if st.button("Reiseziel hinzufügen"):
        if city and country:
            st.session_state["future_travels"] = pd.concat(
                [st.session_state["future_travels"],
                pd.DataFrame([{"city": city, "country": country, "year": year}])]
            ).reset_index(drop=True)
            st.success(f"{city}, {country} ({year}) hinzugefügt!")
    st.write("### Deine zukünftigen Reisen")
    st.dataframe(st.session_state["future_travels"])

# --------------------------------------------------------------------------------
# 5. Quiz
# --------------------------------------------------------------------------------
with quiz:
    st.subheader("Quiz-Modus")
    
    question = st.session_state["current_question"]
    st.write(f"In welchem Jahr warst du in {question['city']}?")

    with st.form(key="quiz_form"):
        answer = st.number_input("Antwort (Jahr)", min_value=1962, max_value=2100, step=1)
        submit = st.form_submit_button("✅ Prüfen")
        next_question = st.form_submit_button("Nächste Frage")

        if submit:
            correct_answers = travels[travels["city"] == question["city"]]["year"].values
            if answer in correct_answers:
                st.success("Richtig! 🎉")
                st.balloons()
                st.session_state["score"] += 1
            else:
                st.error(f"❌ Leider falsch - korrekt wäre {correct_answers} gewesen.")

        if next_question:
            question = random.choice(travels.to_dict(orient="records"))
            while question == st.session_state["current_question"]:
                question = random.choice(travels.to_dict(orient="records"))
            st.write(question)
            st.session_state["current_question"] = question
            st.rerun()

    st.write(f"🏆 Punkte: {st.session_state.score}")
