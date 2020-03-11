# -*- coding: utf-8 -*-
import scrapy


class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    allowed_domains = ['https://www.decathlon.es/es/']
    # start_urls = [
    #     'https://www.decathlon.es/es/p/bicicleta-carretera-freno-disco-triban-rc-500-negro/_/R-p-301728?mc=8502354&c=GRIS',
    #     'https://www.decathlon.es/es/p/sudadera-chandal-cremallera-gimnasia-pilates-domyos-900-mujer-azul/_/R-p-308545?mc=8554753&c=GRIS',
    #     'https://www.decathlon.es/es/p/zapatillas-impermeables-de-senderismo-en-montana-merrell-kangri-peak-ltr-hombre/_/R-p-X8582701?mc=8582701']
    start_urls = [
        "https://www.decathlon.es/es/p/zapatillas-impermeables-de-senderismo-en-montana-merrell-kangri-peak-ltr-hombre/_/R-p-X8582701?mc=8582701","https://www.decathlon.es/es/p/zapatillas-impermeables-de-senderismo-en-montana-merrell-kangri-peak-ltr-mujer/_/R-p-X8582700?mc=8582700","https://www.decathlon.es/es/p/botas-de-senderismo-en-la-nieve-hombre-columbia-hailstone-negras/_/R-p-X8401362?mc=8401362&c=NEGRO","https://www.decathlon.es/es/p/botas-de-senderismo-en-la-nieve-mujer-columbia-hailstone-grises/_/R-p-X8530980?mc=8530980&c=GRIS","https://www.decathlon.es/es/p/zapatilla-de-montana-y-trekking-mujer-chiruca-marbella/_/R-p-X8590476?mc=8590476","https://www.decathlon.es/es/p/zapatillas-de-senderismo-naturaleza-nh500-marron-negro-hombre/_/R-p-301763?mc=8502455&c=MARR%C3%93N_BEIGE","https://www.decathlon.es/es/p/colchon-inflable-camping-quechua-confort-140-cm-2-personas/_/R-p-157798?mc=8382708&c=AZUL","https://www.decathlon.es/es/p/colchon-inflable-camping-quechua-confort-120-cm-2-personas/_/R-p-157797?mc=8382707&c=AZUL","https://www.decathlon.es/es/p/colchon-inflable-camping-quechua-confort-70-cm-1-persona/_/R-p-157796?mc=8382706&c=AZUL","https://www.decathlon.es/es/p/pantalon-de-montana-y-trekking-quechua-mh-500-hombre-negro/_/R-p-302494?mc=8505087&c=AZUL_AZUL+TURQUESA","https://www.decathlon.es/es/p/forro-polar-de-senderismo-montana-mujer-mh500-beige/_/R-p-302607?mc=8550842&c=ROJO","https://www.decathlon.es/es/p/forro-polar-de-senderismo-montana-mujer-mh500-beige/_/R-p-302607?mc=8550842&c=ROJO","https://www.decathlon.es/es/p/chaqueta-3en1-trekking-viaje-travel-100-hombre-gris/_/R-p-177091?mc=8492928&c=AZUL","https://www.decathlon.es/es/p/frontal-energizer-vision-hd-focus/_/R-p-X8570640?mc=8570640","https://www.decathlon.es/es/p/zapatillas-de-tenis-ninos-adidas-altasport-azul/_/R-p-X8541634?mc=8541634","https://www.decathlon.es/es/p/zapatillas-de-tenis-hombre-court-lite-2-blanco-multi-terreno/_/R-p-X8556070?mc=8556070","https://www.decathlon.es/es/p/camiseta-de-tenis-mujer-manga-corta-ts-soft-500-rosa-jaspeado/_/R-p-300390?mc=8487385&c=AZUL","https://www.decathlon.es/es/p/zapatillas-de-tenis-ninos-adidas-altasport-negro-rosa/_/R-p-X8521122?mc=8521122","https://www.decathlon.es/es/p/zapatillas-de-tenis-ninos-mujer-talla35-38-altasport-blanco/_/R-p-X8582991?mc=8582991","https://www.decathlon.es/es/p/zapatillas-de-tenis-hombre-puma-smash-blanco-negro/_/R-p-X8591367?mc=8591367","https://www.decathlon.es/es/p/zapatilla-de-tenis-mujer-puma-smash-blanco-rojo/_/R-p-X8591380?mc=8591380","https://www.decathlon.es/es/p/pantalon-golf-mujer-azul-marino/_/R-p-304029?mc=8525049&c=ROSA","https://www.decathlon.es/es/p/polo-golf-mujer-blanco/_/R-p-143646?mc=8563228&c=BLANCO","https://www.decathlon.es/es/p/camiseta-manga-corta-gimnasia-pilates-adidas-regular-mujer-rosa/_/R-p-X8557235?mc=8557235&c=ROSA","https://www.decathlon.es/es/p/pantalon-corto-chandal-gimnasia-puma-500-nino-azul/_/R-p-X8519599?mc=8519599&c=AZUL","https://www.decathlon.es/es/p/camiseta-manga-corta-gimnasia-pilates-domyos-510-mujer-blanco/_/R-p-307532?mc=8557044&c=ROSA","https://www.decathlon.es/es/p/leggings-short-mallas-deportivas-gimnasia-artistica-femenina-domyos-500-negro/_/R-p-180613?mc=8552868&c=NEGRO","https://www.decathlon.es/es/p/camiseta-manga-corta-gimnasia-pilates-domyos-540-hombre-azul-grisaceo-negro/_/R-p-303209?mc=8512698&c=GRIS_AZUL","https://www.decathlon.es/es/p/camiseta-manga-corta-cardio-fitness-puma-training-hombre-naranja/_/R-p-X8542152?mc=8542152","https://www.decathlon.es/es/p/mallas-leggings-deportivos-gimnasia-pilates-adidas-linear-500-mujer-negro/_/R-p-X8534431?mc=8534431&c=NEGRO","https://www.decathlon.es/es/p/pantalon-corto-chandal-gimnasia-puma-g1-nino-algodon-negro/_/R-p-X8534356?mc=8534356","https://www.decathlon.es/es/p/camiseta-sin-mangas-tirantes-gimnasia-pilates-domyos-560-hombre-gris-oscuro/_/R-p-304491?mc=8525257&c=GRIS","https://www.decathlon.es/es/p/balon-baloncesto-spalding-team-nba-talla-7/_/R-p-X8583318?mc=8583318","https://www.decathlon.es/es/p/balon-de-futbol-adidas-conext-replica-clasificacion-de-la-euro-2020/_/R-p-X8541467?mc=8541467","https://www.decathlon.es/es/p/pantalon-corto-voley-playa-copaya-bv500-turquesa-hombre/_/R-p-176674?mc=8407978&c=AZUL_AZUL+TURQUESA","https://www.decathlon.es/es/p/camiseta-tirantes-voley-playa-copaya-bv500-verde-mujer/_/R-p-176691?mc=8408067&c=VERDE","https://www.decathlon.es/es/p/pantalon-corto-voley-playa-copaya-bv500-turquesa-hombre/_/R-p-176674?mc=8407978&c=AZUL_AZUL+TURQUESA","https://www.decathlon.es/es/p/botas-futbol-kipsta-agility-900-fg-terrenos-secos-nino-azul-rojo/_/R-p-192471?mc=8497506&c=AZUL","https://www.decathlon.es/es/p/botas-de-futbol-adulto-kipsta-agility-700-piel-hg-turf-negro/_/R-p-117632?mc=8496958&c=NEGRO","https://www.decathlon.es/es/p/sudadera-chandal-cremallera-gimnasia-pilates-domyos-900-mujer-azul/_/R-p-308545?mc=8554753&c=GRIS","https://www.decathlon.es/es/p/guardabarros-16/_/R-p-13691?mc=4467819&c=NEGRO","https://www.decathlon.es/es/p/pantalon-ciclismo-mtb-rockrider-rockrider-am-500-hombre-azul/_/R-p-307471?mc=8544455","https://www.decathlon.es/es/p/maillot-ciclismo-mtb-manga-corta-hombre-rockrider-st-100-rojo/_/R-p-301154?mc=8517604&c=AZUL","https://www.decathlon.es/es/p/maillot-ciclismo-mtb-manga-corta-hombre-rockrider-st-100-rojo/_/R-p-301154?mc=8517604&c=AZUL","https://www.decathlon.es/es/p/calcetines-antideslizantes-piscina-natacion-proteccion-hongos-akkua-azul-blanco/_/R-p-X8586232?mc=8586232","https://www.decathlon.es/es/p/banador-natacion-boxer-speedo-hombre-negro-verde/_/R-p-X8481095?mc=8481095&c=NEGRO","https://www.decathlon.es/es/p/mochila-arena-fastpack-2-1-negro-verde/_/R-p-X8571941?mc=8571941","https://www.decathlon.es/es/p/banador-moldeador-aquagym-piscina-nabaiji-mary-sujeccion-pecho-espalda-u-negro/_/R-p-149056?mc=8547302&c=NEGRO","https://www.decathlon.es/es/p/banador-moldeador-aquagym-piscina-nabaiji-karli-mujer-efecto-vientre-plano-negro/_/R-p-3670?mc=8405226&c=AZUL","https://www.decathlon.es/es/p/top-de-bikini-de-aquafitness-para-mujer-lou-juni-negro-naranja/_/R-p-305681?mc=8547356&c=NEGRO","https://www.decathlon.es/es/p/banador-aquafitness-piscina-nabaiji-lena-mujer-escote-con-transparencias-negro/_/R-p-304578?mc=8547338&c=AZUL","https://www.decathlon.es/es/p/mascara-snorkel-subea-easybreath-adulto-azul/_/R-p-1616?mc=8514880&c=NARANJA_ROSA","https://www.decathlon.es/es/p/escarpines-cangrejeras-zapatillas-acuaticas-de-snorkel-subea-snk120-adulto-rosa/_/R-p-169796?mc=8484949&c=AZUL","https://www.decathlon.es/es/p/kit-snorkel-subea-snk-mascara-easybreath-aletas-adulto-azul-verde-negro/_/R-p-164613?mc=8503206&c=ROSA","https://www.decathlon.es/es/p/banador-largo-surf-olaian-900-tween-neon-palme-nino-verde/_/R-p-304087?mc=8518447&c=AZUL","https://www.decathlon.es/es/p/guantes-evolutiv-by-night-negro-manoplas-integradas/_/R-p-172603?mc=8519271&c=NEGRO","https://www.decathlon.es/es/p/zapatillas-atletismo-running-kalenji-run-support-ninos-negro-gris-rojo/_/R-p-166011?mc=8488191&c=AZUL","https://www.decathlon.es/es/p/zapatillas-atletismo-running-kalenji-kiprun-fast-ninos-rojas-azules/_/R-p-188192?mc=8505280&c=BLANCO","https://www.decathlon.es/es/p/pantalon-corto-deportivo-atletismo-kalenji-split-hombre-azul-naranja/_/R-p-165475?mc=8522899&c=AZUL","https://www.decathlon.es/es/p/zapatillas-caminar-adidas-lite-racer-mujer-negro/_/R-p-X8541571?mc=8541571","https://www.decathlon.es/es/p/zapatillas-caminar-skechers-dual-lite-hombre-azul/_/R-p-X8406045?mc=8406045&c=AZUL","https://www.decathlon.es/es/p/zapatillas-caminar-nike-viale-full-mujer-negro/_/R-p-X8541482?mc=8541482","https://www.decathlon.es/es/p/zapatillas-caminar-newfell-pw-580-impermeables-mujer-negro/_/R-p-145959?mc=8392711&c=AZUL","https://www.decathlon.es/es/p/zapatillas-caminar-newfeel-pw-140-mujer-blanco/_/R-p-168495?mc=8403143&c=NARANJA_ROSA","https://www.decathlon.es/es/p/bailarinas-caminar-newfeel-pw-160-br-easy-mujer-azul/_/R-p-302450?mc=8504701&c=AZUL","https://www.decathlon.es/es/p/zapatillas-caminar-newfeel-pw-500-fresh-mujer-azul-lavanda/_/R-p-168493?mc=8526349&c=AZUL"
    ]

    def parse(self, response):
        vacio = ""
        #Extracting the content using css selectors
        # titles = response.css('.title.may-blank::text').extract()
        # votes = response.css('.score.unvoted::text').extract()
        # times = response.css('time::attr(title)').extract()
        # comments = response.css('.comments::text').extract()
        idd = response.xpath('//div[@class="product-refs"]/small/text()').extract()
        nombre = response.xpath('//div[@id="conversion-zone"]/h1/text()').extract()
        opiniones = response.xpath('//span[@class="number-star"]/text()').extract()
        if opiniones is None :
            opiniones = '--'
        if opiniones and nombre:
            opiniones = response.xpath('//span[@class="number-star"]/text()').extract()
        else:
            opiniones = vacio
        
        # rating = response.xpath('//div[@class="es-avispp"]/text()').extract()
        brand = response.xpath('//div[@class="col brand"]/a/img').extract()
        precio = response.xpath('//div[@class="dkt-price__cartridge"]/@data-price').extract()
        precio_rebaja = response.xpath('//span[@class="dkt-price__info-addon"]/text()').extract_first()
        if precio_rebaja and precio:
            precio_rebaja = response.xpath('//span[@class="dkt-price__info-addon"]/text()').extract_first()
        else:
            precio_rebaja = precio
        #img = response.xpath('//input[@id="pdm_productdetailsmaincartridge"]').extract()
        #img = response.xpath('//div[@id="pp-0-0"]/a/picture/@data-iesrc').extract()
        # img = response.xpath('//noscript').extract()
        img = response.xpath('/html/head/meta[@property="og:image"]/@content').extract()
        url = response.xpath('/html/head/meta[@property="og:url"]/@content').extract()
        rating = response.xpath('//span[@class="product-note rating-value"]/text()').extract()
        if rating is None :
            rating = '0'
        if rating and nombre:
            rating = response.xpath('//span[@class="product-note rating-value"]/text()').extract()
        else:
            rating = '0.0'
        
        # if len(precio_rebaja) >1:
        #     precio_rebaja = precio_rebaja[1].extract()
        # elif len(precio_rebaja) == 1:
        #     precio_rebaja = precio_rebaja[0].extract()
        # else:
        #     precio_rebaja = ""
        # precio_previo = response.xpath('//div[@id="conversion-zone"]/div[@class="product-price-and-button"]/div/div/span[@class="dkt-price__info-addon"]/span[@class="dkt-price__previous-price"]/').extract()
        
        # img = response.xpath('//*div[@id="pp-0-0"]/a/picture').extract()
       
        #Give the extracted content row wise
        for item in zip(idd, nombre, opiniones, brand, precio, precio_rebaja, img, url, rating):
            #create a dictionary to store the scraped info
            scraped_info = {
                'idd' : item[0],
                'nombre' : item[1],
                'opiniones' : item[2],
                'brand' : item[3],
                'precio' : item[4],
                'precio_rebaja' : item[5],
                'img' : item[6],
                'url' : item[7],
                'rating' : item[8]
                # 'rating' : item[3]
                
                # 'precio_previo' : item[5],
                # 'precio' : item[5],
                
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

