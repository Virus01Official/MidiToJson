import mido
import json

def midi_to_json(midi_file):
    mid = mido.MidiFile(midi_file)
    midi_data = []

    current_time = 0
    for i, track in enumerate(mid.tracks):
        for msg in track:
            current_time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                midi_data.append({
                    'time': current_time,
                    'note': msg.note,
                    'velocity': msg.velocity
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
