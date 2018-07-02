from requests_html import HTMLSession


def gas_now():

    session = HTMLSession()

    url = 'http://www.quebeccitygasprices.com/'

    r = session.get(url)

    prices = r.html.find('div.price_num')[:3]  # , first=True)

    addesses = r.html.find('dl.address')[:3]

    areas = r.html.find('a.p_area')[:3]
    # prices = items.text
    msg = ''
    # print(prices[0:1].text)
    for i, j, k in zip(prices, addesses, areas):
        msg += "The gas price is {} at {} in {}. \n".format(
            i.text, j.text, k.text)
        # print(msg)

    return msg


if __name__ == '__main__':
    print(gas_now())
