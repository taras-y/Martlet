### requirements - https://pypi.org/project/music21/
### pip install music21

from music21 import stream, note, meter, key, tempo, metadata, midi

# Створюємо нотний потік
score = stream.Score()
score.insert(0, metadata.Metadata())
score.metadata.title = "Martlet - Vocal Melody (With Lyrics)"
score.metadata.composer = "Mykola Leontovych"

# Додаємо тактовий розмір, тональність і темп
part = stream.Part()
part.append(meter.TimeSignature('4/4'))
part.append(key.Key('C'))
part.append(tempo.MetronomeMark(number=90))

# Текст вокалу (розбитий на склади для lyric-треку)
lyrics_syllables = [
    'Martlets', 'a-', 'bove', 'Spring', 'fields', 'and', 'hills',
    'Wish-', 'ing', 'us', 'cheers', 'Win-', 'ter', 'cold', 'ends',

    'Fly-', 'ing', 'a-', 'round', 'Coun-', 'tries', 'and', 'towns',
    'Ne-', 'ver', 'brought', 'harms', 'Be-', 'ing', 'nice', 'guests',

    'Se-', 'ri-', 'nus', 'birds', 'Mart-', 'lets', 'best', 'friends',
    'Show', 'their', 'homes', 'Wel-', 'com-', 'ing', 'guests',

    'Sheeps', 'roll-', 'ing', 'down', 'Val-', 'leys', 'and', 'hills',
    'Got', 'ma-', 'ny', 'lambs', 'Mart-', 'let', 'be-', 'lieves',

    'You', 'have', 'best', 'goods', 'Rea-', 'dy', 'for', 'sales',
    'You’ll', 'get', 'for', 'sure', 'Great', 'mo-', 'ney', 'wealth',

    'Mo-', 'ney', 'some-', 'times', 'Does-', 'n’t', 'make', 'sense',
    'Look', 'at', 'your', 'wife', 'She’s', 've-', 'ry', 'nice',

    'Martlets', 'a-', 'bove', 'Spring', 'fields', 'and', 'hills',
    'Wish-', 'ing', 'us', 'cheers', 'Win-', 'ter', 'cold', 'ends',
]

# Нотна послідовність
melody_notes = [
    # Перша сторінка
    ('B4', 1),  # Mart
    ('A4', 1),  # lets
    ('B4', 1),  # a
    ('G4', 1),  # bove

    ('B4', 1),  # spring
    ('A4', 1),  # fields
    ('B4', 1),  # and
    ('G4', 1),  # hills

    ('B4', 1),  # Wi
    ('A4', 1),  # shing
    ('B4', 1),  # us
    ('G4', 1),  # cheers

    ('B4', 1),  # Win
    ('A4', 1),  # ter
    ('B4', 1),  # cold
    ('G4', 1),  # ends    

    ('B4', 1),  # Fly
    ('A4', 1),  # ing
    ('B4', 1),  # a
    ('G4', 1),  # round

    ('B4', 1),  # Coun
    ('A4', 1),  # tries
    ('B4', 1),  # and
    ('G4', 1),  # towns

    ('B4', 1),  # Ne
    ('A4', 1),  # ver
    ('B4', 1),  # brought
    ('G4', 1),  # harms

    ('B4', 1),  # Be
    ('A4', 1),  # ing
    ('B4', 1),  # nice
    ('G4', 1),  # guests

    ('B4', 1),  # Se
    ('A4', 1),  # ri
    ('B4', 1),  # nus
    ('G4', 1),  # birds
 
    ('B4', 1),  # Mart
    ('A4', 1),  # lets
    ('B4', 1),  # best
    ('G4', 1),  # friends
 
    ('B4', 1),  # Show
    ('A4', 1),  # the
    ('B4', 1),  # ir
    ('G4', 1),  # homes
 
    ('B4', 1),  # Wel
    ('A4', 1),  # co
    ('B4', 1),  # ming
    ('G4', 1),  # guests

    ('B4', 1),  # Sheeps
    ('A4', 1),  # rol
    ('B4', 1),  # ling
    ('G4', 1),  # down
 
    ('B4', 1),  # Val
    ('A4', 1),  # leys
    ('B4', 1),  # and
    ('G4', 1),  # hills
 
    ('B4', 1),  # Got
    ('A4', 1),  # ma
    ('B4', 1),  # ny
    ('G4', 1),  # lambs
 
    ('B4', 1),  # Mart
    ('A4', 1),  # let
    ('B4', 1),  # be
    ('G4', 1),  # lieves

    ('B4', 1),  # You
    ('A4', 1),  # have
    ('B4', 1),  # best
    ('G4', 1),  # goods
 
    ('B4', 1),  # Rea
    ('A4', 1),  # dy
    ('B4', 1),  # for
    ('G4', 1),  # sales
 
    ('B4', 1),  # You'll
    ('A4', 1),  # get
    ('B4', 1),  # for
    ('G4', 1),  # sure
 
    ('B4', 1),  # Great
    ('A4', 1),  # mo
    ('B4', 1),  # ney
    ('G4', 1),  # wealth
 
    # Друга сторінка
    ('C5', 1),  # You
    ('B4', 1),  # have
    ('B4', 1),  # best
    ('A4', 1),  # goods
 
    ('B4', 1),  # Rea
    ('A4', 1),  # dy
    ('A4', 1),  # for
    ('G4', 1),  # sales
 
    ('A4', 1),  # You'll
    ('G4', 1),  # get
    ('G4', 1),  # for
    ('F4', 1),  # sure
 
    ('G4', 1),  # Great
    ('F4', 1),  # mo
    ('F4', 1),  # ney
    ('G4', 1),  # wealth

    ('G4', 1),  # Mo
    ('F4', 1),  # ney
    ('G4', 1),  # some
    ('E4', 1),  # times
 
    ('G4', 1),  # Doe
    ('F4', 1),  # sn't
    ('G4', 1),  # make
    ('E4', 1),  # sense
 
    ('G4', 1),  # Look
    ('F4', 1),  # at
    ('G4', 1),  # your
    ('E4', 1),  # wife
 
    ('G4', 1),  # She's
    ('F4', 1),  # ve
    ('G4', 1),  # ry
    ('E4', 1),  # nice

    ('B4', 1),  # Mo
    ('A4', 1),  # ney
    ('B4', 1),  # some
    ('G4', 1),  # times
 
    ('B4', 1),  # Doe
    ('A4', 1),  # sn't
    ('B4', 1),  # make
    ('G4', 1),  # sense
 
    ('B4', 1),  # Look
    ('A4', 1),  # at
    ('B4', 1),  # your
    ('G4', 1),  # wife
 
    ('B4', 1),  # She's
    ('A4', 1),  # ve
    ('B4', 1),  # ry
    ('G4', 1),  # nice
 
    ('B4', 1),  # Mart
    ('A4', 1),  # lets
    ('B4', 1),  # a
    ('G4', 1),  # bove

    ('B4', 1),  # Mart
    ('A4', 1),  # lets
    ('B4', 1),  # a
    ('G4', 1),  # bove

    ('B4', 1),  # Spring
    ('A4', 1),  # fields
    ('B4', 1),  # and
    ('G4', 1),  # hills

    ('B4', 1),  # Wi
    ('A4', 1),  # shing
    ('B4', 1),  # us
    ('G4', 1),  # cheers

    # Останні 4 ноти
    ('B4', 1),  # Win
    ('A4', 1),  # ter
    ('B4', 1),  # cold
    ('G4', 1),  # ends
]

# Додаємо ноти та лірику
for (pitch, duration), lyric in zip(melody_notes, lyrics_syllables):
    n = note.Note(pitch)
    n.quarterLength = duration
    n.addLyric(lyric)
    part.append(n)

score.append(part)

# Зберігаємо у MIDI-файл
mf = midi.translate.music21ObjectToMidiFile(score)
mf.open('martlet_vocal_with_lyrics.mid', 'wb')
mf.write()
mf.close()

print("Готово! Файл 'martlet_vocal_with_lyrics.mid' створено.")
