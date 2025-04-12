import logging
import os
from datetime import datetime

LOG_FILE=f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s %(message)s',
    level=logging.INFO
)
