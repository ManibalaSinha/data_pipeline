#check and restart process
PIPELINE_SCRIPT="/mnt/c/Users/manib/data_pipeline_project/pipeline.py"
LOG_FILE="/mnt/c/Users/manib/data_pipeline_project/logs/pipeline.log"

if ! pgrep -f "$PIPELINE_SCRIPT" > /dev/null
then
   echo "$(date): pipeline.py not running. Starting..." >> /mnt/c/Users/manib/data_pipeline_project/logs/cron_debug.log
   nohup python3 "$PIPELINE_SCRIPT" >> "$LOG_FILE" 2>&1 &
fi