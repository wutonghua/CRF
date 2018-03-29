import CRFPP
from  crf_segment import crf_segmenter
tagger = CRFPP.Tagger("-m " + "crf_model")
while True:
	line=input("请输入:")
	seg_result=crf_segmenter(line, tagger)
	print(seg_result)