import time

while True:
  try:
    with open('logs.txt', 'a') as f:
      f.write(f"Logging at time {time.ctime()}\n")  # Add a newline for better readability
  except Exception as e:
    print(f"Error writing to log file: {e}")  # Handle potential errors gracefully
  
  time.sleep(5)
