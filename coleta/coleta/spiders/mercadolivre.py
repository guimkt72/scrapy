import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/informatica/componentes-pc/placas/placas-video/4070ti_NoIndex_True#D[A:4070ti,on]"]
    page_count = 1
    max_pages = 3

    def parse(self, response):


        products = response.css('div.poly-card__content')

        for product in products: 
            
            yield {
                'brand' : product.css('h2.poly-box.poly-component__title a::text').get(),
                'price' : product.css('span.andes-money-amount__fraction::text').get(),
                'full' : product.css('span.poly-component__shipped-from::text').get(),
                'frete' : product.css('div.poly-component__shipping::text').get(),
                'internacional' : product.css('span.poly-component__cbt::text').get()
                }
            
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
            
        pass
