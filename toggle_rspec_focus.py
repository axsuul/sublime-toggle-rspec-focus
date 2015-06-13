import sublime, sublime_plugin, re

class ToggleRspecFocusCommand(sublime_plugin.TextCommand):
    def run(self, edit, surplus=False):
        for region in self.view.sel():
            line = self.view.line(region)
            line_contents = self.view.substr(line)

            focus_regex = r'(?:it|describe|context)\s(?:.+?)(?:\"|\')(\,\s\:focus)(.+)do'
            focus_match = re.search(focus_regex, line_contents)

            # If :focus is found, remove it
            if focus_match:
                line_without_focus = re.sub(focus_match.group(1), "", line_contents)
                self.view.replace(edit, line, line_without_focus)

            # Otherwise, add it
            else:
                vanilla_regex = r'(\s*(?:it|describe|context)\s+(?:\"[^\"]+\"|\'[^\']+\'))(\,?.+)do'
                vanilla_match = re.search(vanilla_regex, line_contents)

                line_with_focus = vanilla_match.group(1) + ", :focus" + vanilla_match.group(2) + "do"

                self.view.replace(edit, line, line_with_focus)
