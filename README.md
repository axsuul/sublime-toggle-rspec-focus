# sublime-toggle-rspec-focus

A Sublime Text plugin that comes in handy when working with RSpec. 

![Toggle RSpec Focus in Action!](http://i.imgur.com/TYhUzZK.gif)

Often you will find yourself adding `:focus` to test specific examples. This plugin makes it easy by allowing you to toggle `:focus` on a specific line with a keyboard shortcut.

## Installation

Using [Package Control](https://packagecontrol.io/), look for **Toggle RSpec Focus** to install it.

## Usage

This plugin gives you the `toggle_rspec_focus` command that you can utilize in your key bindings. In your **Key Bindings - User** file, you would do something like

```json
{ "keys": ["super+shift+o"], "command": "toggle_rspec_focus" }
```
