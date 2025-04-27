from music21 import stream, note, midi, instrument

# Створюємо Score (загальна партитура)
score = stream.Score()

# Створюємо 3 незалежні Part (канали)
for i in range(3):
    part = stream.Part()
    
    # Вказуємо інструмент (впливає на канал)
    if i == 0:
        part.insert(0, instrument.Piano())
    elif i == 1:
        part.insert(0, instrument.Violin())
    else:
        part.insert(0, instrument.Flute())

    # Додаємо ноти до кожної частини
    for pitch in ['C4', 'D4', 'E4', 'F4']:
        part.append(note.Note(pitch, quarterLength=1.0))

    # Додаємо Part до Score
    score.append(part)

# Експортуємо в MIDI-файл
mf = midi.translate.music21ObjectToMidiFile(score)
mf.open('multichannel_output.mid', 'wb')
mf.write()
mf.close()
