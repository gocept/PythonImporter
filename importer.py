import sublime
import sublime_plugin


class AddPythonImportStatementCommand(sublime_plugin.TextCommand):
    """Add the current selection as import statement at top of the file."""

    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                self.insert(edit, "import %s\n" % self.view.substr(region))

    def insert(self, edit, text):
        beginning_of_file = self.view.substr(sublime.Region(0, 100))
        if beginning_of_file.startswith('#'):
            # Omit encoding header
            index = beginning_of_file.find('\n') + 1
        else:
            index = 0
        self.view.insert(edit, index, text)
