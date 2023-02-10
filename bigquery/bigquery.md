# BigQuery Slots:
Combination of compute power, memory, disk and other resources required to run a job.

### How to know the number of slots consumed by a query ?
Run a query and capture the job ID

Run the following query to get the slots used by all the jobs
```bash
select job_id
      ,total_slot_ms / TIMESTAMP_DIFF(end_time,start_time,MILLISECOND) as num_slot
from `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
```

Run this query to get the slot used by the job by passing the job id 
```bash
select job_id
      ,total_slot_ms / TIMESTAMP_DIFF(end_time,start_time,MILLISECOND) as num_slot
from `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT where job_id = <ID received from the job>
```


From CLI, run the query with dry-run option to get the amount of data which will be processed
```bash
$ bq query --use_legacy_sql=false --dry_run 'SELECT * FROM `bigquery-public-data.london_bicycles.cycle_hire` WHERE duration>=1200';
Query successfully validated. Assuming the tables are not modified, running this query will process 2784394803 bytes of data.
```


# Partition Tables:

Creating partition tables in BQ
https://cloud.google.com/bigquery/docs/creating-partitioned-tables
 
```bash
bq query --use_legacy_sql=false ' CREATE TABLE dataset.example_table ( company STRING, value FLOAT64, ds DATE) PARTITION BY ds OPTIONS( expiration_timestamp=TIMESTAMP "2028-01-01 00:00:00 UTC", description="Example table create in BQ CLI", labels=[("example","summary")] );'
```


Understanding BQ utilization plans and ways to improve a query performance:
https://medium.com/slalom-build/using-bigquery-execution-plans-to-improve-query-performance-af141b0cc33d

SQL performance tips:
https://towardsdatascience.com/5-bigquery-sql-performance-tips-for-modern-data-scientists-f880b79cfa71


Understanding BQ slots:
https://cloud.google.com/bigquery/docs/slots





