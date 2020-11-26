import os
import PyQt5
--hidden-import=PyQt5.sip
dirname = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
print(plugin_path)
