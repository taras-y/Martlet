from music21 import converter, instrument, stream

# 1. Зчитування MIDI-файлу
midi_path = 'Щедрик.mid'  # ← вкажи шлях до свого MIDI-файлу
midi_score = converter.parse(midi_path)

# 2. Вивід кількості партій
print(f"Знайдено {len(midi_score.parts)} партій у MIDI")

# 3. Призначаємо голоси SATB (напр., перші 4 треки)
soprano = midi_score.parts[0].flatten()
alto    = midi_score.parts[1].flatten()
tenor   = midi_score.parts[2].flatten()
bass    = midi_score.parts[3].flatten()

# 4. Додаємо позначки інструментів/голосів
soprano.insert(0, instrument.Soprano())
alto.insert(0, instrument.Alto())
tenor.insert(0, instrument.Tenor())
bass.insert(0, instrument.Bass())

# 5. Збираємо нову партитуру
score = stream.Score()
score.insert(0, soprano)
score.insert(0, alto)
score.insert(0, tenor)
score.insert(0, bass)

# 6. Переглянути/експортувати
score.show('text')     # Текстовий вигляд
# score.show()         # Нотний вигляд (музе-скрипт / Lilypond / MuseScore)
