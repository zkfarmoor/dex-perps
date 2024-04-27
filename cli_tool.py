# file: cli_tool.py

import argparse
import json

def update_setting(setting_path, value):
    with open('settings.json', 'r+') as f:
        settings = json.load(f)
        keys = setting_path.split('.')
        for key in keys[:-1]:
            settings = settings.get(key, {})
        settings[keys[-1]] = value
        f.seek(0)
        json.dump(settings, f, indent=4)
        f.truncate()

def main():
    parser = argparse.ArgumentParser(description="Manage Trading Bot")
    parser.add_argument('--set', type=str, help="Set a configuration path (e.g., 'arbitrage.price_difference_percent')")
    parser.add_argument('--value', type=float, help="Value to set the configuration to")
    
    args = parser.parse_args()
    if args.set and args.value is not None:
        update_setting(args.set, args.value)
        print(f"Updated {args.set} to {args.value}")
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
