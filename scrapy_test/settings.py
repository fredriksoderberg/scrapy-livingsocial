BOT_NAME = 'livingsocial'
SPIDER_MODULES = ['scrapy_test.spiders']
DATABASE = {
    'drivername' : 'postgresql',
    'host' : 'localhost',
    'port' : '5432',
    'username' : 'postgres',
    'password' : 'postgres',
    'database' : 'scrape'
}
ITEM_PIPELINES = {'scrapy_test.pipelines.LivingSocialPipeline': 300} 
DOWNLOAD_HANDLERS = {'s3': None}