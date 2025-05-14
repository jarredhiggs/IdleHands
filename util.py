from config import config

def debug(message, feature_toggle = config['is_debug']):
    if feature_toggle:
        import datetime
        now = datetime.datetime.now()
        print("DEBUG: " + str(now.strftime("%H:%M:%S:%f"))[0:-3] + ": " + message)