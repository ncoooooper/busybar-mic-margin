"""Write aggregate dBFS values from continuous signed 16-bit mono PCM on stdin."""
from array import array
from pathlib import Path
import argparse,json,math,sys

def db(level):
    return 20*math.log10(level/32768) if level>0 else None
def levels(stream,out):
    held=0;clipped=0
    while data:=stream.read(8000):
        data=data[:len(data)//2*2]
        if not data:break
        pcm=array("h",data)
        if sys.byteorder!="little":pcm.byteswap()
        peak=max(abs(v) for v in pcm);rms=math.sqrt(sum(v*v for v in pcm)/len(pcm))
        held=max(held,peak);clipped+=sum(v in (-32768,32767) for v in pcm)
        state=dict(peak_db=db(peak),rms_db=db(rms),held_db=db(held),clipped=clipped)
        tmp=out.with_suffix(out.suffix+".tmp");tmp.write_text(json.dumps(state));tmp.replace(out)
if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("output",type=Path);args=p.parse_args()
    levels(sys.stdin.buffer,args.output.expanduser())
