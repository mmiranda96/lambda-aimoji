# -*- coding: utf-8 -*-
from functools import reduce

# Removes anything but emojis
def get_emojis(text):
    emojis = []
    for c in text:
        if c in emoji_dict.keys():
            emojis.append(c)
    return emojis

# Actual algorithm
def check_emojis(emojis, emoji_dict, emotion_dict):
    tones = {
        'Positivo': 0.0,
        'Negativo': 0.0,
        'Neutro': 0.0
    }
    emotions = {k: 0.0 for k in emotion_dict.keys()}

    for e in emojis:
        t = emoji_dict[e]
        emotion = t['emotion']
        value = t['value']
        tone = emotion_dict[emotion]['tone']
        q = emotion_dict[emotion]['value']
        tones[tone] += q * value
        emotions[emotion] += value

    tot_tones = reduce(lambda x, y: x + y, tones.values())
    tot_emotions = reduce(lambda x, y: x + y, emotions.values())

    tones = {k: 0 for k in tones.keys()} if tot_tones == 0 else {k: v / tot_tones for k, v in tones.items()}
    emotions = {k: 0 for k in emotions.keys()} if tot_emotions == 0 else {k: v / tot_emotions for k, v in emotions.items()}
    return (tones, emotions)

# File loading
with open('emoji_dict.csv', 'r') as f:
    lines = map(lambda x: x.replace('\n', '').replace('\r', ''), f.readlines()[1:])
    emoji_dict = {
        l[0]: {
            'code': l[1],
            'category': l[2],
            'description': l[3],
            'emotion': l[4],
            'value': int(l[5])
        } for l in map(lambda x: x.split(','), lines)
    }

with open('emotion_dict.csv', 'r') as f:
    lines = map(lambda x: x.replace('\n', '').replace('\r', ''), f.readlines()[1:])
    emotion_dict = {
        l[0]: {
            'tone': l[1],
            'value': float(l[2])
        } for l in map(lambda x: x.split(','), lines)
    }

# User input
print('Introduce una cadena con emojis (cualquier cosa que no sea emoji será ignorada): ', end='')
text = input()
print()
print('El texto es: ' + text)
emojis = get_emojis(text)
print('Los emojis en el texto son' + str(emojis))
values = check_emojis(emojis, emoji_dict, emotion_dict)
print('Los valores de tono son:')
print(values[0])
print()
print('Los valores de sentimientos son:')
print(values[1])
