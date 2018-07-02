from requests_html import HTMLSession


def kindle_now():

    session = HTMLSession()

    url = 'https://www.amazon.ca/Kindle-Paperwhite-High-Resolution-Display-Built/dp/B00QJDU3KY'

    r = session.get(url)

    price = r.html.find('#priceblock_ourprice', first=True)

    # addesses = r.html.find('dl.address')[:3]

    # areas = r.html.find('a.p_area')[:3]
    # price = items.text
    msg = ''
    # print(price[0:1].text)

    msg += "The Kindle price is {}. \n".format(price.text)

    return msg


if __name__ == '__main__':
    print(kindle_now())
