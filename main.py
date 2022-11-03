import pandas as pd
import time
import json
from Historic_Crypto import LiveCryptoData
import logging
import logging.handlers
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024*1024,
    backupCount=1,
    encoding="utf8",
)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)


try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise
    

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    watch_list = ['BTC-USD', 'ETH-USD', 'ALGO-USD', 'MATIC-USD']
    
    try:
        for coin in watch_list:
            x = coin.strip("-USD")
            new = LiveCryptoData(coin).return_data()
            new_dict = new.to_dict(orient='records')
            for item in new_dict:
                price = float(item["price"])
                volume = item["volume"]
                coin_name = coin
            logger.info(f'crypto_name: {coin}, price:{price}')
    except KeyError:
        pass
