from argparse import ArgumentParser

import requests
import xmltodict
from django.conf import settings
from django.core.management import BaseCommand

import orders.models as models
from orders.models import Order


class Command(BaseCommand):
    """
    This command will create n Order objects depending of the number of Order returned
    by the API. The url API is in a .env just in case it was private.

    How does it work ? Parse the xml to a dict so it is easier to iterate inside.
    Then iterate through the orders which are located under statistics/orders/, for each
    order iterate through all the field. If the field has the same name of the django
    Order model field then adding the name of the field as key and the value as a value
    in an Order object. Append this object to a list (order_list) and finally bulk_create all
    Order object in the list.
    Little thing, because we are using an other model as a foreign key (OrderStatus) we need
    to identify this field in the dict by his type and then run the field name in a correspondance
    dict to then get the correct Model.
    """
    def agg_arguments(self, parser: ArgumentParser):
        pass

    def handle(self, *args, **options):
        try:
            response = requests.get(settings.LENGOW_API, verify=False, timeout=10)

            if response.status_code != 200:
                raise Exception("Alerte generale", response.status_code)

            json_resp = xmltodict.parse(response.text)
            order_list = []
            for order in json_resp["statistics"]["orders"]["order"]:
                data = {}
                for field in order:
                    if field in [o.name for o in Order._meta.get_fields()]:
                        if type(order[field]) == dict:
                            model_name = models.CORRESPONDANCE_DICT[field]
                            sub_data = {}
                            for item in order[field]:
                                sub_data[item] = order[field][item]
                            instance = getattr(
                                models, model_name
                            ).objects.update_or_create(**sub_data)[0]
                            data[field] = instance
                        else:
                            data[field] = order[field]
                if data:
                    order_list.append(Order(**data))

            # Since we do not check for the size of the batch lets do it in a
            # single operation
            Order.objects.bulk_create(order_list)

        except Exception as e:
            print(e)
