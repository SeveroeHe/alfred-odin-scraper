import os, sys

TEST_PATH_PREFIX = "./"
PATH_PREFIX = "~/.aws/"

def get_file(file):
	return PATH_PREFIX + file

def parse_args(args, idx):
	try:
		ret = args[idx]
	except:
		ret = ""
	return ret

def update_aws_config(file, content):
	with open(file, "r+") as f:
		f.seek(0)
		f.write(content)
		f.truncate()
		f.close()

def form_credential_content(principle, credentials):
	ret = "[default]\n"
	if principle:
		ret += "aws_access_key_id = " + principle + "\n"
	if credentials:
		ret += "aws_secret_access_key = " + credentials + "\n"
	return ret

def form_config_content(region):
	ret = "[default]\n"
	if region:
		ret += "region = " + region + "\n"
	return ret

if __name__ == '__main__':
	# parse principle and credentials
	principle = parse_args(sys.argv, 1)
	credentials = parse_args(sys.argv, 2)
	region = parse_args(sys.argv, 3)
	print(principle, credentials, region)

	# change credential file
	update_aws_config(get_file('credentials'), form_credential_content(principle, credentials))

	# change config file
	update_aws_config(get_file('config'), form_config_content(region))	

	# call iam
	os.system("aws iam get-user")



