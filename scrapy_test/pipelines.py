from sqlalchemy.orm import sessionmaker
from models import Deals, create_deals_table
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

import settings

class LivingSocialPipeline(object):
    def __init__(self):
        engine = create_engine(URL(**settings.DATABASE))
        create_deals_table(engine)
        self.Session = sessionmaker(bind=engine)
        
    def process_item(self, item, spider):
        session = self.Session()
        deal =  Deals(**item)
        
        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
            
        return item