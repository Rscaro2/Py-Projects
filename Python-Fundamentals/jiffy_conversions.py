# Name: Rishi Scaro, Date: 10/22/2026, Description: This program converts jiffies to seconds, minutes, hours, and calculates frames per second (FPS) based on user input.

def convert_time_and_fps(jiffies, jiffies_per_frame): 
    seconds = jiffies * 0.01 
    fps = 1 / (jiffies_per_frame * 0.01)
    return seconds, fps

def  convert_seconds_to_minutes_hours(seconds):
    minutes = seconds / 60
    hours = seconds / 3600
    return minutes, hours


def display_results(seconds, minutes, hours, fps):
    print(f"Time in seconds: {seconds:.3f} s")
    print(f"Time in minutes: {minutes:.3f} min")
    print(f"Hours: {hours:.3f}")
    print(f"Frames per second (FPS): {fps:.3f} fps")

def main(): 
    jiffies = float(input("Enter the number of jiffies: "))
    jiffies_per_frame = float(input("Enter the number of jiffies per frame: "))

    seconds, fps = convert_time_and_fps(jiffies, jiffies_per_frame)
    minutes, hours = convert_seconds_to_minutes_hours(seconds)

    display_results(seconds, minutes, hours, fps)

main()

        