class Post:
    '''A simple encapsulation'''
    def __init__(self, info: dict):
        self.id = info['id']
        self.title = info['title']
        self.subtitle = info['subtitle']
        self.body = info['body']