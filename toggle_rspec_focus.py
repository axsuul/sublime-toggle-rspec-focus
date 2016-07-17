import sublime, sublime_plugin, re

class ToggleRspecFocusCommand(sublime_plugin.TextCommand):
    def type_regex_part():
        pass

    def run(self, edit, surplus=False):
        types = ["it", "describe", "context", "scenario", "feature"]
        type_regex_part = '.*(?:' + '|'.join(types) + ')\s+'

        for region in self.view.sel():
            line = self.view.line(region)
            line_contents = self.view.substr(line)

            focus_regex = r'.*' + type_regex_part + '(?:\"[^\"]+\"|\'[^\']+\'|.+)(\,\s\:focus)(.+)do'
            focus_match = re.search(focus_regex, line_contents)

            # If :focus is found, remove it
            if focus_match:
                line_without_focus = re.sub(focus_match.group(1), "", line_contents)
                self.view.replace(edit, line, line_without_focus)

            # Otherwise, add focus
            else:
                # the it "...." part
                prefix_regex = (
                    '(?:' + type_regex_part + '\"[^\"]+\"|' +
                    type_regex_part + '\'[^\']+\'|' +
                    type_regex_part + '[^\s]+)'
                )

                unfocused_regex = re.compile('(' + prefix_regex + ')(\,.+)?\s+do')
                unfocused_match = re.search(unfocused_regex, line_contents)

                options = ""

                if unfocused_match.group(2) is not None:
                    options = unfocused_match.group(2)

                if unfocused_match:
                    line_with_focus = unfocused_match.group(1) + ", :focus" + options + " do"

                    self.view.replace(edit, line, line_with_focus)
