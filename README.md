# Springer Textbook downloader

This small script downloads the textbooks available in [SpringerNature](https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960) because of Coronavirus outbreak.

This script will create a `downloads/english` and a `downloads/german` forlder and download all the available pdfs.

To run in a virtualenv 

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python download_springer.py
```