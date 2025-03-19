from datetime import datetime

class App:
    def __init__(self, name, priority, start_time, end_time):
        self.name = name
        self.priority = priority
        self.start_time = start_time
        self.end_time = end_time

def time_to_minutes(time_str):
    return int(time_str[:2]) * 60 + int(time_str[3:5])

def main():
    N = int(input())
    registered_apps = []

    for _ in range(N):
        name, priority, start_time, end_time = input().split()
        priority = int(priority)
        start_time = time_to_minutes(start_time)
        end_time = time_to_minutes(end_time) - 1
        if start_time > end_time:
            continue
    
        can_registered = True
        for app in registered_apps:
            if start_time <= app.end_time and end_time >= app.start_time:
                if priority <= app.priority:
                    can_registered = False
                    break
        
        if can_registered:
            new_registered_app = [app for app in registered_apps if not (start_time <= app.end_time and end_time >= app.start_time)]
            new_registered_app.append(App(name, priority, start_time, end_time))
            registered_apps = new_registered_app
    
    querry_time = input()
    querry_minute = time_to_minutes(querry_time)

    for app in registered_apps:
        if app.start_time <= querry_minute <= app.end_time:
            print(app.name)
            return
    
    print("NA")

if __name__ == "__main__":
    main()