import os, sys, time

keyDelay = 0.1
keymap = {
    "Up": "shift",
    "Left": "option",
    "Down": "control",
    "Right": "command",
    "b": "b",
    "a": "5",
    "s": "s", #start
}

def sendKey(button):
    time.sleep(keyDelay)
    actual_key = keymap[button]
    arrow_cmd = """osascript \
                    -e 'tell application "KiGB" to activate' \
                    -e 'delay 0.1' \
                    -e 'tell application "System Events" to key down {0}' \
                    -e 'delay 0.1' \
                    -e 'tell application "System Events" to key up {0}'""" 
    buttn_cmd = """osascript \
                    -e 'tell application "KiGB" to activate' \
                    -e 'delay 0.1' \
                    -e 'tell application "System Events" to keystroke "{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}{0}"'"""
    if actual_key in ["b", "s"]:
        cmd = buttn_cmd
    else:
        cmd = arrow_cmd
    cmd = cmd.format(actual_key)
    os.system(cmd)
    return "done"

if __name__ == "__main__":
    sendKey(sys.argv[1])
