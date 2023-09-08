from bs4 import BeautifulSoup
# 前面几个方法使用的都是这个参数，所以统一使用这个（后面的那些方法没有引用这个html文本文件）
html_doc = """
            <html><head><title>The Dormouse's story</title></head>
            <body>
            <p class="title"><b>The Dormouse's story</b></p>

            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
            and they lived at the bottom of a well.</p>

            <p class="story">
                 Once upon a time there were three little sisters; and their names were
                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
                <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
                and they lived at the bottom of a well.
            </p>
            <div class="panel-body">
                <ul class="list" id="list-1">
                   <li class="element">Foo</li>
                   <li class="element">Bar</li>
                   <li class="element">Jay</li>
                </ul>
    
                <ul class="list list-samll" id="list-2">
                   <li class="element">Foo</li>
                   <li class="element">Bar</li>
                   <li class="element">Jay</li>
                </ul>
            </div>
            """

def demo1(html_doc):
    soup = BeautifulSoup(html_doc,"html.parser")
    print(soup.prettify())
    print(soup.title.string)
    print(soup.head.title)
    print(type(soup.title))
    print(soup.a.attrs["class"])
    print(soup.a.attrs["href"])
    print(soup.a.string)
    print(soup.p.children)
    for item in soup.findAll(class_="story"):
        print(item)
    print(soup.select("ul li"))

demo1(html_doc)