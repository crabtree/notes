import datetime
import shutil

time_to_clean = datetime.datetime.now() - datetime.timedelta(hours=12)
dirname = 'recordings/{:s}'.format(time_to_clean.strftime("%Y%m%d%H"))
shutil.rmtree(dirname)
