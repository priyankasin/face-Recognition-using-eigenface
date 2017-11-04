import os
import shutil


def data_spilts(train=None):

	path="/home/priyanka/Desktop/scripts/att_faces"
	dst_train = "/home/priyanka/Desktop/scripts/Train"
	dst_test= "/home/priyanka/Desktop/scripts/Test"

	for dirname , dirnames , filenames in os. walk (path):
		for subdirname in dirnames :
			subject_path = os. path . join ( dirname , subdirname )
			subject_path1 = os. path . join ( dst_train, subdirname)
			for f in os. listdir (subject_path1):
				os.remove(os.path.join(subject_path1, f))
			i=0
			subject_path2 = os. path . join ( dst_test, subdirname)
			for f in os. listdir (subject_path2):
				os.remove(os.path.join(subject_path2, f))
			
			for filename in os. listdir ( subject_path ):
				if i<train:
					try :
						path_file = os.path.join(subject_path,filename)
						shutil.copy2(path_file,subject_path1)
				
					except:
						print(" Unexpected error")
				else:
					try :
						path_file = os.path.join(subject_path,filename)
						shutil.copy2(path_file,subject_path2) 
					except:
						print(" Unexpected error")
				i=i+1