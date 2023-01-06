# Steps to run a dataflow pipeline
In this demo, we will create a dataflow job to push data from pubsub to bigquery

### set the project and environment values
```
gcloud config set project <name-of-the-project>
project_name=<name-of-the-project>
```

### Create a cloud storage bucket as a staging location:
```
gsutil mb gs://demo-staging-bucket
```

Google has created a default bucket which has all the templates added. - `gs://dataflow-templates-us-central1/latest/`

```
gsutil ls gs://dataflow-templates-us-central1/latest/
```

You can also create your own template and run more complicated and customized jobs

### Create a pubsub topic
```
gcloud pubsub topics create dataflow-demo-topic
```

### Create BQ dataset
```
bq mk -d $project_name:temp_dataset
```

### Create BQ table
```
bq mk \
  -t \
  --description "pubsub to bq table" \
  --label test:dataflow \
  $project_name:temp_dataset.bq-dataflow-table \
  name:STRING,skills:STRING,age:INTEGER
```



### Create dataflow job from UI
- Job name - dataflow-demo
- Region - us-central1
- Dataflow template: Pub/Sub topics to BigQuery
- Topic: projects/$project_name/topics/dataflow-demo-topic
- Output table: $project_name:temp_dataset.bq-dataflow-table
- Temporary location: gs://demo-staging-bucket/temp



### publish messages to pubsub:
```
gcloud pubsub topics publish  projects/$project_name/topics/dataflow-demo-topic --message="{\"name\": \"Alex\",\"skills\": \"GCP\",\"age\": 30}"

gcloud pubsub topics publish  projects/$project_name/topics/dataflow-demo-topic --message="{\"name\": \"Sam\",\"skills\": \"AWS\",\"age\": 40}"

gcloud pubsub topics publish  projects/$project_name/topics/dataflow-demo-topic --message="{\"name\": \"Angela\",\"skills\": \"Azure\",\"age\": 35}"
```

### Query the Bigquery table
```
bq query --use_legacy_sql=false 'SELECT * FROM `'"$project_name.temp_dataset.bq-dataflow-table"'`'
```

