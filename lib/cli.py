from lib import logger, jobs

from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import NestedCompleter

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
    'generate': {'curl','wget','Invoke-WebRequest','DownloadString'}
})

def start_cli():
	session = PromptSession()
	try:
		while True:
			cmd = session.prompt(prompt, style=style, completer=completer)
			jobs.do(cmd)
	except KeyboardInterrupt as e:
		quit()

