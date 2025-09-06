# log monitoring script
LOG_FILE="/mnt/c/Users/manib/data_pipeline_project/logs/pipeline.log"
ALERT_FILE="/mnt/c/Users/manib/data_pipeline_project/logs/error_alert.log"
ALERT_EMAIL="admin@example.com"

grep "ERROR" $LOG_FILE | tail -n 10 > $ALERT_FILE

if [ -s $ALERT_FILE ]; then
   echo "Errors found in pipeline logs, sending alert..."
   mail -s "Data Pipeline Error Alert" "$ALERT_EMAIL" < "$ALERT_FILE"
fi