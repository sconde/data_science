import mechanize
from bs4 import BeautifulSoup


def getFreeLinks(nisdon_query_link =
                 'http://www.nisdon.com/search/label/free?max-results=',
                 max_query = 200):
    """
    Get a the list of classes and links
    """

    full_link = '%s%d' %(nisdon_query_link, max_query)
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    br.set_handle_robots(False)
    webpage = br.open(full_link).read()
    soupPage = BeautifulSoup(webpage, 'xml')
    # blog_post_div = soupPage.findAll("div",{"class":"blog-posts hfeed"})
    blog_post = soupPage.findAll("div",{"class":"post-outer"})

    all_link = map(lambda x:
                   x.findAll("div",{"class":"thumb"})[0].find('a')['href'].encode('ascii','ignore'),
                   blog_post)

    return all_link


free_link = getFreeLinks()
def getUdemyLinks(class01):
    # print class01
    br = mechanize.Browser(factory=mechanize.RobustFactory())
    br.set_handle_robots(False)
    webpage = br.open(class01).read()
    soupPage = BeautifulSoup(webpage, 'xml')
    udemy_links = soupPage.findAll("a", {"class":"button large visit"})[0]["href"].encode("ascii", "ignore")
    # print udemy_links
    return udemy_links

udemy_links = map(getUdemyLinks, free_link)
strip_links = map(lambda x: x[x.index('https', x.index('https')+1):], udemy_links)

# filter and only return class with coupon code
coupon_class = filter(lambda x: 'couponCode' in x, strip_links)
