import time
from speech import listen, say
import webbrowser
# Functions


def what_time_is_it(root):
    t = time.localtime(time.time())
    return f'It is {t.tm_hour}:{t.tm_min}'


def search(root):
    say('What do you want me to look up?')
    search = listen()
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    return f'This is what I found on {search}.'


def what_is_your_name(root):
    return 'My name is Helpie!'


def bye(root):
    say('Goodbye')
    root.quit()
    root.update()
    exit()


def location():
    say('What place do you want to find?')
    search = listen()
    url = 'https://google.nl/maps/place/' + search + '/&amp;'
    webbrowser.get().open(url)
    return 'I think this is the place.'


command_list = {
    'what time is it': what_time_is_it,
    'search': search,
    'what is': search,
    'what is your name': what_is_your_name,
    'exit': bye,
    'bye': bye,
    'goodbye': bye,
    'location': location,
    'place': location,
    'where is': location,
}
