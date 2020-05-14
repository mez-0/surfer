from lib import logger, arguments
import os

args = arguments.get_args()

def do(cmd):
	if 'list' in cmd:
		get_hosted_files()

def get_hosted_files():
	hosted_path = args.directory
	url = f'http://{args.server_address}:{args.server_port}/'
	if not os.path.exists(hosted_path):
		logger.msg('Creating directory: ',hosted_path,'blue')
		os.mkdir(hosted_path)
	else:
		files = os.listdir(hosted_path)
		logger.list(url,files)
		print()        		