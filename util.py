from config import config

def debug(message, feature_toggle = config['is_debug']):
    if feature_toggle:
        import datetime
        import inspect
        now = datetime.datetime.now()
        invoker = inspect.stack()[1][3]
        print("DEBUG: " + str(now.strftime("%H:%M:%S:%f"))[0:-3] + ": " + invoker + ": " + message)

