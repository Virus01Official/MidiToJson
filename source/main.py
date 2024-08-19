import mido
import json

def midi_to_json(midi_file):
    mid = mido.MidiFile(midi_file)
    midi_data = []

    current_time = 0
    tempo = 500000  # Default tempo (120 BPM in microseconds per beat)
    ticks_per_beat = mid.ticks_per_beat

    for track in mid.tracks:
        for msg in track:
            current_time += msg.time
            if msg.type == 'set_tempo':
                tempo = msg.tempo
            elif msg.type == 'note_on' and msg.velocity > 0:
                bpm = mido.tempo2bpm(tempo)
                time_in_seconds = mido.tick2second(current_time, ticks_per_beat, tempo)
                midi_data.append({
                    'time': time_in_seconds,
                    'note': msg.note,
                    'velocity': msg.velocity,
                    'bpm': bpm
                })

    return midi_data

def save_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    input_file = 'song.mid'  # Your MIDI file
    output_file = 'song.json'  # Output JSON file

    midi_data = midi_to_json(input_file)
    save_json(midi_data, output_file)
    print(f"Converted {input_file} to {output_file}")
