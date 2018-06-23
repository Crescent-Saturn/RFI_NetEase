from requests_html import HTMLSession

session = HTMLSession()

url = 'http://www.quebeccitygasprices.com/'

r = session.get(url)

prices = r.html.find('div.price_num')[:5]  # , first=True)

addesses = r.html.find('dl.address')[:5]

areas = r.html.find('a.p_area')[:5]
# prices = items.text

# print(prices[0:1].text)
for i, j, k in zip(prices, addesses, areas):
    print("The gas price is {} at {} in {}. ".format(i.text, j.text, k.text))
