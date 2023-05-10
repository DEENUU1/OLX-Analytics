import fetchData
import json
from abc import abstractmethod, ABC


class Parser(ABC):
    @abstractmethod
    def data_parse(self, data):
        pass




url = fetchData.UrlBuilderHouse().build_url(
    limit="40",
    area_min="25",
    price_min="600",
)

print(json.dumps(fetchData.FetchData(url).fetch_data(), indent=4))