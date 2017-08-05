import boto3
import random
import json

stream_name = 'JK-Stream'

client = boto3.client('firehose')

games = ('solitaire','war robots', 'tetris', 'cards', 'space junk', 'war of titans','ninja')

age_range = ['10-20','21-40','41-60','61+']

record = {}

for x in range(1,1000):
   record['game'] = random.choice(games)
   record['age_group'] = random.choice(age_range)
   response = client.put_record(
   DeliveryStreamName = stream_name,
   Record = {
     'Data' : json.dumps(record)
   }
   )
