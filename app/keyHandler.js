config = require('./config.js'),
lastTime = {},
throttledCommands = config.throttledCommands,
regexThrottle = new RegExp('^(' + throttledCommands.join('|') + ')$', 'i'),
regexFilter = new RegExp('^(' + config.filteredCommands.join('|') + ')$', 'i');
var PythonShell = require('python-shell');
 
for (var i = 0; i < throttledCommands.length; i++) {
    lastTime[throttledCommands[i]] = new Date().getTime();
}

var defaultKeyMap = config.keymap || {
    'up':'Up',
    'u':'Up',
    'left':'Left',
    'l':'Left',
    'h':'Left',
    'down':'Down',
    'd':'Down',
    'j':'Down',
    'right':'Right',
    'r':'Right',
    'k':'Right',
    'a':'a',
    'b':'b',
    'start':'s',
    's':'s'
};

function sendKey(command) {
    //if doesn't match the filtered words
    if (!command.match(regexFilter)) {
        var allowKey = true,
        key = defaultKeyMap[command] || command;
        //throttle certain commands (not individually though)
        if (key.match(regexThrottle)) {
            var newTime = new Date().getTime();
            if (newTime - lastTime[key] < config.timeToWait) {
                allowKey = false;
            } else {
                lastTime = newTime;
            }
        }
        if (allowKey) {
            var options = {args: [key]};
            PythonShell.run('./app/key.py', options, function (err) {
              if (err) console.log(err);
            });
        }
    }
}

exports.sendKey = sendKey;
