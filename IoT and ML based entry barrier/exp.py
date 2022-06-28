from datetime import datetime
from influxdb import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

average_temp=97
has_mask=True

token = "K9oFiWcCztZvs4cdZUvFYB9Hc7LXJgbsU0Oi2wT7KTUpp3cX6oVcJdB0t28Y_jbtY4QAJB7NqiJl87npe_k-8w=="
org = "priteshdeshmukh9844@gmail.com"
bucket = "IoT_Bucket"

client = InfluxDBClient(url="https://ap-southeast-2-1.aws.cloud2.influxdata.com/", token=token)

write_api = client.write_api(write_options=SYNCHRONOUS)

point = Point("mem").tag("host", "host1").field("temperature",average_temp,"mask",has_mask).time(datetime.utcnow(), WritePrecision.NS)
write_api.write(bucket, org, point)