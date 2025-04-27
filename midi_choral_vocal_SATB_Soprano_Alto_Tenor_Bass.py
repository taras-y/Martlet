from music21 import stream, note, tempo, instrument, metadata, midi

# Створюємо темп Allegretto (приблизно 100–112 ударів на хвилину)
allegretto = tempo.MetronomeMark(number=108, text='Allegretto')

# Створюємо партитуру
choral_score = stream.Score()
choral_score.insert(0, metadata.Metadata())
choral_score.insert(0, allegretto)
choral_score.metadata.title = "Simple SATB Example"
choral_score.metadata.composer = "music21"

# Дані для кожного голосу
voices = [
    ("Soprano", instrument.Soprano(), ['B4:1.0', 'A4', 'B4', 'G4', 'B4:1.0', 'A4', 'B4', 'G4']),
    ("Alto", instrument.Alto(), ['r:1.0', 'r', 'r', 'r', 'r:1.0', 'r', 'r', 'r']),
    ("Tenor", instrument.Tenor(), ['r:1.0', 'r', 'r', 'r', 'r:1.0', 'r', 'r', 'r']),
    ("Bass", instrument.Bass(), ['r:1.0', 'r', 'r', 'r', 'r:1.0', 'r', 'r', 'r']),
]

# Додаємо кожен голос у Score
for name, instr, pitches in voices:
    part = stream.Part()
    part.id = name
    part.insert(0, instr)
    # part.insert(0, allegretto)

    default_duration=0.5
    for i, p in enumerate(pitches):
        if ':' in p:
            value, dur = p.split(':')
            duration = float(dur)
        else:
            value = p
            duration = default_duration

        if value.lower() == 'r':  # позначення паузи
            n = note.Rest(quarterLength=duration)
        else:
            n = note.Note(value, quarterLength=duration)
        # При бажанні додати слова:
        n.lyric = f"{name[0]}{i+1}"  # Наприклад: S1, A2, T3, B4
        part.append(n)

    choral_score.append(part)

# Зберігаємо у MIDI-файл
mf = midi.translate.music21ObjectToMidiFile(choral_score)
mf.open('choral_vocal_SATB.mid', 'wb')
mf.write()
mf.close()
