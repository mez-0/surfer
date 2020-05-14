import os
from lib import logger, jobs, arguments
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import NestedCompleter

args = arguments.get_args()

def start_cli():
	session = PromptSession()
	try:
		while True:
			cmd = session.prompt(prompt, style=style, completer=completer)
			if 'help' in cmd:
				show_help()
			else:
				jobs.do(cmd)
	except KeyboardInterrupt as e:
		quit()

def show_help():
	for c,h in helper.items():
		print('%-9s %s' % (c, logger.blue(h)))

def get_files():
	hosted_path = args.directory
	d = set()
	files = os.listdir(hosted_path)
	for f in files:
		d.add(f)
	return d

style = Style.from_dict({
    # User input (default text).
    '':          '#ffffff',
    # Prompt.
    'pointer': '#ffffff'
})

prompt = [
    ('class:pointer', 'surfer> '),
]

completer = NestedCompleter.from_nested_dict({
    'list': None,
    'exit': None,
    'add': None,
    'delete': None,
    'read':get_files(),
    'generate': {
    	'curl':get_files(),
    	'wget':get_files(),
    	'Invoke-WebRequest':get_files(),
    	'DownloadString':get_files()
    	}
})

helper = {
	'list':'List the contents of the server directory',
	'generate':'Generate download utility commands',
	'read':'Read the contents of a file',
	'add':'Add a file to the server directory',
	'delete':'Delete a file from the server directory',
	'exit':'Close Surfer.py'
}