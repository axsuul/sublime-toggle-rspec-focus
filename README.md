# sublime-toggle-rspec-focus

A Sublime Text plugin that comes in handy when working with RSpec. 

![Toggle RSpec Focus in Action!](http://i.imgur.com/TYhUzZK.gif)

Often you will find yourself adding `:focus` to test specific examples. This plugin makes it easy by allowing you to toggle `:focus` on a specific line with a keyboard shortcut.

## Installation

Use [Package Control](https://packagecontrol.io/packages/Toggle%20RSpec%20Focus) to install. You may need to restart Sublime Text!

## Usage

The default keyboard shortcut is `ctrl+shift+o` to focus/unfocus. To change this, you can edit your key bindings in **Preferences > Key Bindings - User** with

```json
{ 
    "keys": ["ctrl+shift+o"], 
    "command": "toggle_rspec_focus" 
}
```
