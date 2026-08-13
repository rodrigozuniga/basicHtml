from datetime import datetime

# Open the file in append mode
with open("log.txt", "a") as file:
    # Add a timestamp so you know when it ran
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"--- Run at {current_time} UTC ---\n")
    
    # Write the numbers 1 to 10
    for i in range(1, 11):
        file.write(f"{i}\n")
    
    file.write("\n") # Add a blank line between runs

print("Numbers successfully saved to log.txt")
