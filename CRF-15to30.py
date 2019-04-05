# This is code for encoding video using CRF model, and calculated the PSNR, SSIM and VMAF of the encoded videos
# It generates videos with crf from 15 to 30,
# the encoded videos are shown in the folder named "output_videos" which is in the same directory of the raw videos.

# At the same time, it calculates PSNR, SSIM & VMAF,
# the calculated statistics are shown in folder nameded "output_logs" which is in the same deirectory of the raw videos.
# There are 2 types of generated files, which are recorded the scores per frame & average score separately.
# For instant, the file which are started as "psnr_" is recorded the psnr scores per frame &
# that started as "reportpsnr_" is recorded the average psnr scores.

# please change filepath at where the raw .y4m videos stored
# please change the range of crf within the range of 0-51 (8-bit YUV video)
# The logformat (.log or .txt) define the format of output files which contains the calculatd PSNR, SSIM and VMAF.

import os

videos=["crowd_run_1080p50","ducks","in_to_tree_1080p50","old_town_cross_1080p50","park_joy"]

filepath="/media/zenyi/WD20SPZX/videos/"
filename="crowd_run_1080p50"
crf=30
rawformat=".y4m"
encformat=".mp4"
logformat=".log"

for video in videos:
	print 'video ', video, '\n'
	filename = video

	for i in range(15,31):
		crf=i
	
	# generate -crf 15~30 .MP4 VIDEOs
		net="./ffmpeg -i \""+filepath+filename+rawformat+"\" -c:v libx264 -crf "+str(crf)+" \""+filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\""

		print 'number ', i, ', ffmpeg command ', net, '\n'
		log = os.system(net)
		print(log)

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

	# generate vmaf.log & reportvmaf.log in /output_logs/
		netvmaf="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json:log_path="+filepath+"output_logs/vmaf_"+filename+"_crf"+str(crf)+".json\" -f null - 2> \""+ filepath+"output_logs/reportvmaf_"+filename+"_crf"+str(crf)+logformat+"\""
		print(netvmaf), '\n'
		os.system(netvmaf)


print 'END'




"""
# vmaf
netvmaf="./ffmpeg -i \"" +filepath+"output_videos/"+filename+"_crf"+str(crf)+encformat+"\" -i \""+filepath+filename+rawformat+"\" -lavfi libvmaf=\"model_path=./model/vmaf_v0.6.1.pkl:psnr=1:log_fmt=json:log_path="+filepath+"output_logs/vmaf_"+filename+"_crf"+str(crf)+".json\" -f null - 2> \""+ filepath+"output_logs/reportvmaf_"+filename+"_crf"+str(crf)+logformat+"\""

print(netvmaf), '\n'
os.system(netvmaf)
"""
