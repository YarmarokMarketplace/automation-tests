import requests


def test_mar84_sort_products_by_price_and_newness_api():
    """API requests for testing sorting by price and newness"""
    url_server = 'https://yarmarok.onrender.com/api/notices?page=1&limit=9&sort={sort}'

    sort_types = ['newest', 'oldest', 'expensive', 'cheapest']

    print("=======GET /sort=======")
    for sort in sort_types:
        url_server = url_server.format(sort=sort)

        payload = {}
        headers = {}

        response = requests.request(
            "GET", url_server, headers=headers, data=payload)
        assert response.status_code == 200


def test_mar176_filter_products_by_state_of_item_api():
    """API requests for testing filtering by state of item - new, used"""
    url_server = 'https://yarmarok.onrender.com/api/notices?page=1&limit=9goodtype={goodtype}'
    goodtype = ['used', 'new']

    print("=======GET /filter state=======")
    for sort in goodtype:
        url_server = url_server.format(goodtype=goodtype)

        payload = {}
        headers = {}

        response = requests.request(
            "GET", url_server, headers=headers, data=payload)
        assert response.status_code == 200


def test_mar176_filter_products_by_price_api():
    """API requests for testing filtering by state of item - new, used"""
    url_server = 'https://yarmarok.onrender.com/api/notices?page=1&limit=9priceRange={price_range}'
    price_range = ['0-500', '300-1000', '100-200']

    print("=======GET /filter price=======")
    for sort in price_range:
        url_server = url_server.format(price_range=price_range)

        payload = {}
        headers = {}

        response = requests.request(
            "GET", url_server, headers=headers, data=payload)
        assert response.status_code == 200
