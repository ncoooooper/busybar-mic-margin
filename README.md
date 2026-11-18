# Mic Margin

Measure digital microphone headroom, held peak and clipping during a soundcheck.

Pipe mono, signed 16-bit little-endian PCM into python3 companion/meter.py ~/mic-levels.json, and set levels_file to that path. On macOS, for example, ffmpeg -f avfoundation -i :0 -ac 1 -ar 16000 -f s16le - feeds the meter over a pipe. The meter stores only aggregate level readings. Restart the meter to clear its held peak. This measures digital full scale, not acoustic sound pressure.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
