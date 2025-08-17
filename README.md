# Roblox Anti-AFK Script

A simple Python script that prevents you from being kicked for AFK (Away From Keyboard) in Roblox by performing actions at regular intervals.

## Features

- Presses spacebar and 'D' key every 40 seconds to simulate activity
- Automatically brings Roblox window to focus before performing actions
- Skips next action if any key is pressed (allowing for normal gameplay)
- Displays countdown timer until next action
- Color-coded console output for better visibility
- Automatically installs required Python packages

## Requirements

- Python 3.6 or later
- Roblox game running in windowed mode (not fullscreen)

## Installation

1. Ensure Python is installed on your system
2. Download the script file (e.g., `anti_afk.py`)
3. Run the script using Python:




The script will automatically install any missing dependencies.

## Usage

1. Launch Roblox and join your game
2. Run the script
3. The script will:
- Perform an action every 40 seconds
- Display a countdown until the next action
- Skip the next action if you press any key (to avoid interrupting gameplay)
4. Press Ctrl+C to stop the script

## Customization

You can adjust the interval by changing this line in the code:
```python
interval = 2 * 20  # 40 seconds (2 * 20)




