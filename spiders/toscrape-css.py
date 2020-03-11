# -*- coding: utf-8 -*-
import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'https://www.decathlon.es/es/p/bicicleta-carretera-freno-disco-triban-rc-500-negro/_/R-p-301728?mc=8502354&c=GRIS',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'id': quote.css("span.text::text").extract_first(),
                'nombre': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract()
            }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

