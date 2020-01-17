import logging
import io


def print_to_string(*args):
    output = io.StringIO()
    print(*args, file=output)
    contents = output.getvalue()
    output.close()
    return contents


def info(*args):
    infoLogger.info(print_to_string(*args))


def error(*args):
    errorLogger.error(print_to_string(*args))


formatter = logging.Formatter(
    '%(asctime)s %(name)s- %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setFormatter(formatter)

infoLogger = logging.getLogger('myInfoLogger')
infoLogger.setLevel(logging.INFO)
infoLogger.addHandler(console)

errorLogger = logging.getLogger('myErrorLogger')
errorLogger.setLevel(logging.ERROR)
errorLogger.addHandler(console)
errorLogger.addHandler(logging.FileHandler('error.log', mode='w'))
