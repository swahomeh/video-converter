import os #deplicated and replaced by subprocess; os.system() == subprocess.run()
import subprocess
from subprocess import check_output


# subprocess.run(["ls", "-l", "solution"])

# command = "uname"
# commandArgument = "-a"
# print(f'Gathering system information with command: {command} {commandArgument}')
# subprocess.run([command, commandArgument])

# command = "ps"
# commandArgument = "-x"
# print(f'Gathering active process information with command: {command} {commandArgument}')
# subprocess.run([command, commandArgument])

#subprocess.Popen('dir E:\\CODES\\JS EXPERT\\x-vid') # r to import raw string....or double all backslashes

def convert(directory, savedir):
	# r=root, d=directories, f=files
	for file in os.listdir(directory):
    #for r, d, f in os.walk(directory): # takes care of sub-directories
        #for file in f:
        	if (file.endswith('.mkv')):
        	#if '.mkv' in file:
        		
        		print('[*] '+file+'\n\n')
        		print('[File Path] = '+directory+'\\'+file+'\n\n')
        		print('[Save Path] = '+os.path.join(savedir, file[:-4]+'.mp4\n\n'))

        		str1, str2 = file.split('(', 1)

        		print('[Split Text] = '+'"'+str1+'"\n\n')

        		ffmpegc = 'ffmpeg -i "'+directory+'\\'+file+'" -vf scale=320:240 "'+os.path.join(savedir, str1[:-1]+'.mp4"')

        		try:

        			#subprocess.run(ffmpegc, shell=True, stderr=subprocess.STDOUT)
        			subprocess.check_call(ffmpegc, stderr=subprocess.STDOUT)

        		except subprocess.CalledProcessError as e:
        			raise RuntimeError("The command '{}' returned with error (code {}): {}".format(e.cmd, e.returncode, e.output)) # placeholders implemented

if __name__ == "__main__":

    path = input('\n\nEnter source directory...\n\n')
    savedir = input('\n\nEnter the path to save files...\n\n')
    convert(path, savedir)