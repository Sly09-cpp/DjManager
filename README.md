# Description
---

This is a simple Discord bot that plays music. It is still in development for tuning and features. Make sure to read the entire "Setup" section to understand what to consider when using this.

# Setup
---
#### Requirements
- Token from Discord Developer Portal bot
- (MacOS only) brew package manager

#### Installing Dependencies
This project will only work on Linux and MacOS for now. You can run this on Windows too by using the WSL, but the bot hasn't been tested in that environment yet, so it's uncertain how well it will perform.

With that said, the setup is pretty much automated with the `Setup.sh`/`Setup.zsh` scripts.

Open a terminal and run: `./Setup.sh` if you're on Linux or `./Setup.zsh` if you're on MacOS. 

#### Usage

Go to the root level of where you are keeping the directory open a terminal. Then, source your python environment: `source env/bin/activate`.

There are three flags you can use to make this work:
- `"-s"`, `"--Scan"`
  - This will scan your current directory and any subdirectories until it finds a `.token` file contain a **single line** value which is the token obtained from the Discord Developer Portal. If it cannot find it, the bot will not start at all.
  - Example: `python3 __main__.py -s` or `python3 __main__.py --Scan`
- `"-t"`, `"--Token"`
  - A token can be passed directly as an argument instead of being put in some file independently.
  - Example: `python3 __main__.py -t <value>` or `python3 __main__.py --Token <value>`
- `"-f"`, `"--File_Path"`
  - A path to a `.token` file containing the **single line** value of the token can be passed to extract the value from it.
  - Example: `python3 __main__.py -f <file_path>` or `python3 __main__.py --File_Path <path>`

Additionally, there is a `-c` and `--Cookies_Path` which is a path to `cookies.txt` file exported in the Mozilla/Netscape format of your cookies. If you don't pass this, then the bot will still work, but it might stop working if Youtube's API detects it as a bot.

# Upcoming features:
---
- Queues
- "GUI" buttons when a song is playing
- Search other websites aside from Youtube
- Play playlists with URL
- Sign in with a Google account to avoid Cookies obstacle

# License
---
MIT License

Copyright (c) 2026 Wilmer Cubillan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.