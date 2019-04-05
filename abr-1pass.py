# This is code for encoding video using 1-Pass ABR (average fixed bitrate) model, and calculated the PSNR, SSIM and VMAF of the encoded videos
# It encodes videos with birate from "2000k" to "64M",
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

# 1-pass ABR

videos=["crowd_run_1080p50","ducks","in_to_tree_1080p50","old_town_cross_1080p50","park_joy"]
bitrates=["2000k","4000k","8000k","16M","32M","64M"]

filepath="/home/zenyi/videos/"
filename="crowd_run_1080p50"
crf=29

rawformat=".y4m"
encformat=".mp4"
logformat=".log"


for video in videos:
	print 'video ', video, '\n'
	filename = video

	for bitrate in bitrates:
		print '1-pass ABR: bitrate ', bitrate, '\n'
		
		net="./ffmpeg -i \""+filepath+filename+rawformat+"\" -c:v libx264 -b:v "+bitrate+" \""+filepath+"output_videos/"+filename+"_"+bitrate+encformat+"\""
		print "ffmpeg command: ", net, "\n"
		log=os.system(net)
		print(log), "ffmpeg execution success!\n"


	# generate psnr.log & reportpsnr.log in /output_logs/
		netpsnr="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+bitrate+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi psnr=\""+filepath+"output_logs/psnr_"+filename+"_"+bitrate+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportpsnr_"+filename+"_"+bitrate+logformat+"\""
		print(netpsnr), '\n'
		os.system(netpsnr)
		print 'bitrate ', bitrate, ' psnr calculation success!'	

	# generate ssim.log & reportssim.log in /output_logs/
		netssim="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+bitrate+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi ssim=\""+filepath+"output_logs/ssim_"+filename+"_"+bitrate+logformat+"\" -f null - 2> \""+ filepath+"output_logs/reportssim_"+filename+"_"+bitrate+logformat+"\""
		print(netssim), '\n'
		os.system(netssim)
		print 'bitrate ', bitrate, ' ssim calculation success!'

	# generate vmaf.log & reportvmaf.log in /output_logs/
		netvmaf="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_"+bitrate+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json:log_path="+filepath+"output_logs/vmaf_"+filename+"_"+bitrate+".json\" -f null - 2> \""+ filepath+"output_logs/reportvmaf_"+filename+"_"+bitrate+logformat+"\""
		print(netvmaf), '\n'
		os.system(netvmaf)
		print 'bitrate ', bitrate, 'vmaf calculation success!'


	


print 'END'
