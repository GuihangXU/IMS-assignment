# This is code for encoding video using preset (with constant quality CRF=23) model, and calculated the PSNR, SSIM and VMAF of the encoded videos
# It encodes videos with preset from "ultrafast" to "placebo",
# the encoded videos are in the folder named "output_videos" which is in the same directory of the raw videos.

# At the same time, it calculates PSNR, SSIM & VMAF,
# the calculated statistics are shown in folder nameded "output_logs" which is in the same deirectory of the raw videos.
# There are 2 types of generated files, which are recorded the scores per frame & average score separately.
# For instant, the file which are started as "psnr_" is recorded the psnr scores per frame &
# that started as "reportpsnr_" is recorded the average psnr scores.

# the video names are shown in array named videos, please change video names here!
# please change filepath at where the raw .y4m videos stored
# please change the range of preset in array named presets
# The logformat (.log or .txt) define the format of output files which contains the calculatd PSNR, SSIM and VMAF(.json & .log).
import os

videos=["crowd_run_1080p50","ducks","in_to_tree_1080p50","old_town_cross_1080p50","park_joy"]
presets=["ultrafast", "superfast", "veryfast","faster","fast","medium","slow","slower","veryslow","placebo"]

filepath="/home/zenyi/videos/"
filename="crowd_run_1080p50"
crf=29

rawformat=".y4m"
encformat=".mp4"
logformat=".log"


for video in videos:
	print 'video ', video, '\n'
	filename = video

	for preset in presets:
		print 'preset ', preset, '\n'
		
		net="./ffmpeg -i \""+filepath+filename+rawformat+"\" -c:v libx264 -preset "+preset+" \""+filepath+"output_videos/"+filename+"_"+preset+encformat+"\""
		print "ffmpeg command: ", net, "\n"
		log=os.system(net)
		print(log), "ffmpeg execution success!\n"


		# generate psnr.log & reportpsnr.log in /output_logs/
		netpsnr="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+preset+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi psnr=\""+filepath+"output_logs/psnr_"+filename+"_"+preset+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportpsnr_"+filename+"_"+preset+logformat+"\""
		print(netpsnr), '\n'
		os.system(netpsnr)
		print 'preset ', preset, ' psnr calculation success!'	

	# generate ssim.log & reportssim.log in /output_logs/
		netssim="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+preset+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi ssim=\""+filepath+"output_logs/ssim_"+filename+"_"+preset+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportssim_"+filename+"_"+preset+logformat+"\""
		print(netssim), '\n'
		os.system(netssim)
		print 'preset ', preset, ' ssim calculation success!'

	# generate vmaf.log & reportvmaf.log in /output_logs/
		netvmaf="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+preset+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json:log_path="+filepath+"output_logs/vmaf_"+filename+"_"+preset+".json\" -f null - 2> \""+ filepath+"output_logs/reportvmaf_"+filename+"_"+preset+logformat+"\""
		print(netvmaf), '\n'
		os.system(netvmaf)
		print 'preset ', preset, 'vmaf calculation success!'


	


print 'END'





# test python generate psnr, ssim & vmaf

#os.system("./ffmpeg -i aki_1k.mp4 -i akiyo_cif.y4m -lavfi  psnr=psnr_2p.log -f null - 2> psnrreport_p2.txt")

#os.system("./ffmpeg -i aki_1k.mp4 -i akiyo_cif.y4m -lavfi ssim=ssim_p1.log -f null - 2> ssimreport_p1.log")

#os.system("./ffmpeg -i aki_1k.mp4 -i akiyo_cif.y4m -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json\" -f null - -report > vmaf_p1.log")





"""
# psnr
netpsnr="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi psnr=\""+filepath+"output_logs/psnr_"+filename+"_crf"+str(crf)+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportpsnr_"+filename+"_crf"+str(crf)+logformat+"\""

print(netpsnr), '\n'
os.system(netpsnr)
"""

'''
# ssim
netssim="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi ssim=\""+filepath+"output_logs/ssim_"+filename+"_crf"+str(crf)+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportssim_"+filename+"_crf"+str(crf)+logformat+"\""

print(netssim), '\n'
os.system(netssim)
'''

"""
for video in videos:
	print 'video ', video, '\n'
	filename = video

	for i in range(15,31):
		crf=i
	# generate vmaf.log & reportvmaf.log in /output_logs/
		netvmaf="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json:log_path="+filepath+"output_logs/vmaf_"+filename+"_crf"+str(crf)+".json\" -f null - 2> \""+ filepath+"output_logs/reportvmaf_"+filename+"_crf"+str(crf)+logformat+"\""
		print(netvmaf), '\n'
		os.system(netvmaf)

"""

'''
	# generate psnr.log & reportpsnr.log in /output_logs/
		netpsnr="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi psnr=\""+filepath+"output_logs/psnr_"+filename+"_crf"+str(crf)+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportpsnr_"+filename+"_crf"+str(crf)+logformat+"\""
		print(netpsnr), '\n'
		os.system(netpsnr)
		print 'number ', i, ' psnr calculation success!'	

	# generate ssim.log & reportssim.log in /output_logs/
		netssim="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi ssim=\""+filepath+"output_logs/ssim_"+filename+"_crf"+str(crf)+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportssim_"+filename+"_crf"+str(crf)+logformat+"\""
		print(netssim), '\n'
		os.system(netssim)
		print 'number ', i, ' ssim calculation success!'
'''


"""
	# generate -crf 15~30 .MP4 VIDEOs
		net="./ffmpeg -i \""+filepath+filename+ipformat+"\" -c:v libx264 -crf "+str(crf)+" \""+filepath+"output_videos/"+filename+"_crf"+str(crf)+opformat+"\""

		print 'number ', i, ', ffmpeg command ', net, '\n'
		log = os.system(net)
		print(log)
"""


"""

#log = os.system("./ffmpeg -i akiyo_1k.mkv -i akiyo_cif.y4m -lavfi psnr=psnr.log -f null -")
#print(log)

#log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 15 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf15.mp4"''')
#print(log)

#log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 16 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf16.mp4"''')
#print(log)

"""

"""
log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 17 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf17.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 18 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf18.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 19 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf19.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 20 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf20.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 21 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf21.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 22 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf22.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 23 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf23.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 24 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf24.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 25 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf25.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 26 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf26.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 27 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf27.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 28 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf28.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 29 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf29.mp4"''')
print(log)

log = os.system('''./ffmpeg -i "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_1080p50.y4m" -c:v libx264 -crf 30 "/media/zenyi/WD20SPZX/testvideoset1-5/park_joy_crf30.mp4"''')
print(log)

"""

