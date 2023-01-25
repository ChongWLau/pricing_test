import csv
from datetime import datetime

from dashboard.models import Quotes


def snake_case(s: str):
    return '_'.join(s.lower().split(' '))


def run():

    with open('Data.csv', newline='') as csvfile:
        quotes = []
    
        for n, quote in enumerate(csv.DictReader(csvfile)):
            
            fq = {snake_case(k): v for k,v in quote.items()}
            fq['id'] = fq.pop('quote_number')
            fq['transaction_date'] = datetime.strptime(
                fq['transaction_date'], '%d/%m/%Y'
            ).date()
            for k, v in fq.items():
                if v == '':
                    fq[k] = None

            q = Quotes(**fq)
            quotes.append(q)
            
            if len(quotes) > 1000:
                Quotes.objects.bulk_create(quotes)
                quotes = []    
                        
            if (n+1) % 1000 == 0:
                print('completed: ', n+1)
        
        if quotes:
            Quotes.objects.bulk_create(quotes)
