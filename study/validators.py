from rest_framework import serializers


class LinkValidator:
    def __init__(self, link):
        self.link = link

    def __call__(self, value):
        if (dict(value).get(self.link) and 'youtube.com' not in dict(value).get(self.link).split('/')) and (
        'wwyoutube.com') not in dict(value).get(self.link).split('/'):
            raise serializers.ValidationError('Видео должно быть c youtube.com')
