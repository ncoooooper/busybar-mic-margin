# Mic Margin

Measure digital microphone headroom, held peak and clipping during a soundcheck.

Watch the bar while adjusting input gain. The current headroom tells you about the latest sample and the held peak remembers a loud syllable you may have missed.

## Read the margin on a soundcheck

1. Start the PCM meter with the intended input and point the companion at its JSON output.
2. Speak or play the loudest expected passage. Read the remaining digital headroom on the front.
3. Turn once to **PEAK HOLD** for the maximum level captured since the meter started. The sample shows 6.0 dB of headroom and a held peak of −6.0 dBFS.

![The 6.0 dB headroom page changes to a held peak of minus 6.0 dB.](media/guide/inspect-held-peak.gif)

## Check a new gain setting

1. Adjust the input on the recording device, then repeat the same passage. Turn back to **PEAK HEADROOM** to see the current margin.
2. Read the rear of the peak-hold page for the clipped-sample count. Restart the meter if you want to clear its held maximum for another take.
3. Browse to the RMS page if you also need a reading of average signal level.

![The held peak returns to 6.0 dB of headroom and the meter animation settles.](media/guide/return-to-mic-headroom.gif)

## Example from the emulator

The test signal reached half of digital full scale. That is approximately −6.0 dBFS, leaving 6.0 dB before clipping. These figures describe the digital samples. They are not a measurement of room sound pressure. Generated half-scale PCM supplied to the production meter.

## Set up the source

Pipe mono, signed 16-bit little-endian PCM into python3 companion/meter.py ~/mic-levels.json, and set levels_file to that path. On macOS, for example, ffmpeg -f avfoundation -i :0 -ac 1 -ar 16000 -f s16le - feeds the meter over a pipe. The meter stores only aggregate level readings. Restart the meter to clear its held peak. This measures digital full scale, not acoustic sound pressure.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
