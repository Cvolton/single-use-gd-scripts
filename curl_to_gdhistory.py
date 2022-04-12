from datetime import datetime
import pytz
import os
import json

basedir = "/run/media/cvolton/DATA/linuxbackup/downloadGJLevel22/-1/"
convertdir = "/run/media/cvolton/DATA/linuxbackup/downloadGJLevel22/-1_converted/"

for file in os.listdir(basedir):
	filedate = datetime.strptime("-".join(file.split("-")[:-1]), "%Y-%m-%d_%H-%M")
	aware_date = pytz.timezone('Europe/Prague').localize(filedate)
	print(f"{aware_date} - {file}")

	f = open(f"{basedir}/{file}", "r")
	response_json = {
		"created": str(aware_date),
		"unprocessed_post_parameters": {"secret": "Wmfd2893gb7", "levelID": -1, "extras": 1},
		"endpoint": "downloadGJLevel22",
		"raw_output": f.read()
	}
	f.close()

	f = open(f"{convertdir}/{file}.json", "w")
	json.dump(response_json, f)
	f.close()
#
