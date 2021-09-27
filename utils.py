import requests

def send_phone_notification(values):
    '''input parameters:
        values (dict)
        '''
    
    ifttt_values = {
        'value1': values['title'],
        'value2': values['text'],
        'value3': values['link']
    }


    api_key_file = open('api_key.data', 'r')
    api_key = api_key_file.read().strip()
    url = "https://maker.ifttt.com/trigger/send_notification/with/key/" + api_key

    return requests.post(url, data=ifttt_values)

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
