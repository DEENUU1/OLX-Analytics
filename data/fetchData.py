import json
from requests import get
from abc import ABC, abstractmethod


class UrlBuilder(ABC):

    BASE_URL = "https://www.olx.pl/api/v1/offers/?offset=0"

    @abstractmethod
    def build_url(self, **kwargs: str) -> str:
        pass

    def fetch_data(self, url: str) -> dict | None:
        response = get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return None


class UrlBuilderApartment(UrlBuilder):

    def build_url(self, **kwargs) -> str:
        url = f"{self.BASE_URL}"

        parameters = {
            'limit': '&limit={}',
            'category_id': '&category_id={}',
            'build_type': '&filter_enum_builttype%5B0%5D={}',
            'floor_select': '&filter_enum_floor_select%5B0%5D=floor_{}',
            'furniture': '&filter_enum_furniture%5B0%5D={}',
            'rooms': '&filter_enum_rooms%5B0%5D={}',
            'area_min': '&filter_float_m%3Afrom={}',
            'area_max': '&filter_float_m%3Ato={}',
            'price_min': '&filter_float_price%3Afrom={}',
            'price_max': '&filter_float_price%3Ato={}',
            'region_id': '&region_id={}',
            'city_id': '&city_id={}',
        }

        for key, value in parameters.items():
            argument = kwargs.get(key)
            if argument:
                if key == 'floor_select':
                    url += value.format(argument)
                else:
                    url += value.format(argument)

        return url


class UrlBuilderHouse(UrlBuilder):

    def build_url(self, **kwargs) -> str:
        url = f"{self.BASE_URL}"

        parameters = {
            'limit': '&limit={}',
            'build_type': '&filter_enum_builttype%5B0%5D={}',
            'market_type': '&filter_enum_market[0]=primary={}',
            'furniture': '&filter_enum_furniture%5B0%5D={}',
            'floor_count': '&filter_enum_floor%5B0%5D={}',
            'area_min': '&filter_float_area%3Afrom={}',
            'area_max': '&filter_float_area%3Ato={}',
            'plot_area_min': '&filter_float_m%3Ato={}',
            'plot_area_max': '&filter_float_price%3Afrom={}',
            'price_per_m_min': '&filter_float_price_per_m%3Afrom={}',
            'price_per_m_max': '&filter_float_price_per_m%3Ato={}',
            'price_min': '&filter_float_price%3Afrom={}',
            'price_max': '&filter_float_price%3Ato={}',
            'region_id': '&region_id={}',
            'city_id': '&city_id={}',
        }

        for key, value in parameters.items():
            argument = kwargs.get(key)
            if argument:
                url += value.format(argument)

        url += f"&category_id=3"

        return url


# class UrlBuilderCar(UrlBuilder):
#
#     def build_url(self, **kwargs: str) -> str:
#         url = f"{self.BASE_URL}"
#         url += f"&limit={kwargs.get('limit')}"
#         url += f"&category_id={kwargs.get('category_id')}"
#         url += f"&filter_enum_car_body[0]={kwargs.get('car_body_type')}"
#         url += f"&filter_enum_color[0]={kwargs.get('color')}"
#         url += f"&filter_enum_condition[0]={kwargs.get('condition')}"
#         url += f"&filter_enum_country_origin[0]={kwargs.get('country_origin')}"
#         url += f"&filter_enum_drive[0]={kwargs.get('drive')}"
#         url += f"&filter_enum_petrol[0]={kwargs.get('petrol')}"
#         url += f"&filter_enum_righthanddrive[0]={kwargs.get('steering_wheel_type')}"
#         url += f"&filter_enum_transmission[0]={kwargs.get('transmission')}"
#         url += f"&filter_float_enginepower%3Afrom={kwargs.get('engine_power_min')}"
#         url += f"&filter_float_enginepower%3Ato={kwargs.get('engine_power_max')}"
#         url += f"&filter_float_enginesize%3Afrom={kwargs.get('engine_size_min')}"
#         url += f"&filter_float_enginesize%3Ato={kwargs.get('engine_size_max')}"
#         url += f"&filter_float_milage%3Afrom={kwargs.get('milage_min')}"
#         url += f"&filter_float_milage%3Ato={kwargs.get('milage_max')}"
#         url += f"&filter_float_price%3Afrom={kwargs.get('price_from')}"
#         url += f"&filter_float_price%3Ato={kwargs.get('price_to')}"
#         url += f"&filter_float_year%3Afrom={kwargs.get('year_from')}"
#         url += f"&filter_float_year%3Ato={kwargs.get('year_to')}"
#
#         return url


