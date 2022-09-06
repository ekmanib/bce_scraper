from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BceSpider(CrawlSpider):
    
    name = 'bce'

    start_urls = [
        'https://contenido.bce.fin.ec/documentos/Administracion/sectorMonetario.html',
        'https://contenido.bce.fin.ec/documentos/Administracion/sectorExterno.html',
        'https://contenido.bce.fin.ec/documentos/Administracion/sectorFiscal.html',
        'https://contenido.bce.fin.ec/documentos/Administracion/sectorReal.html',
        'https://contenido.bce.fin.ec/documentos/Administracion/pagos.html'
        ]

    rules = (
        Rule(LinkExtractor(allow=r'documentos/Administracion/bi'), callback='parse_url', follow=False),
    )

    def parse_url(self, response):
        yield (
            {'url' : response.url}
        )
        
    
