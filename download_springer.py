import requests
import os
import pandas as pd
import logging
from lxml import html

logger = logging.getLogger('download_springer_textbooks')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


urls = {
    'english': 'https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v5',
    'german': 'https://resource-cms.springernature.com/springer-cms/rest/v1/content/17863240/data/v2'
}

DOWNLOAD_FOLDER = 'downloads/'
DOWNLOAD_BASE_URL = 'https://link.springer.com/content/pdf/'
logger.info('Processing downloads')
for language, url in urls.items():
    logger.info('Processing download for %s', language)
    df = pd.read_excel(url)
    download_path = DOWNLOAD_FOLDER + language
    if not os.path.exists(download_path):
        logger.info('Creating folder %s', download_path)
        os.makedirs(download_path)
    for index, row in df.iterrows():
        file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}"
        download_url = row.loc['DOI URL'].replace(
            'http://doi.org/',
            DOWNLOAD_BASE_URL
        )
        logger.info('Downloading %s', file_name)
        # replace / in filename as it treats it as directory
        with open('{}/{}.pdf'.format(download_path, file_name.replace('/', '-')), 'wb') as f:
            f.write(requests.get(download_url).content)


