def file_compression(filename):
  read_file=open(filename,'r')
  read_data=read_file.read()
  fname=filename.split('.')
  e=fname[0]
  fname=str(e)+'.rav'
  wrt_file=open(fname,'w')
  cnt=0
  act_len=len(read_data)
  multiple=act_len/8
  binval=""
  for i in range(0,multiple):
    tmp=read_data[8*i:(8*i)+8]
    for j in range(0,8):
      tmp2=ord(tmp[j])
      tmp3=bin(tmp2)
      tmp3=tmp3[2:]
      while len(tmp3)<7:
        tmp3='0'+tmp3
      binval=binval+tmp3
    #print binval
  while cnt< len(binval):
    repl=binval[cnt:8+cnt]
    wrt_data=chr(int(repl,2))
    cnt=cnt+8
    wrt_file.write(wrt_data)
  
  read_file.close()
  wrt_file.close()

def file_decompression(filename):
  read_file=open(filename,'r')
  read_data=read_file.read()
  fname=filename.split('.')
  e=fname[0]
  fname=str(e)+'.dec'
  wrt_file=open(fname,'w')
  cnt=0
  act_len=len(read_data)
  multiple=act_len/7
  binval=""
  for i in range(0,multiple):
    tmp=read_data[7*i:(7*i)+7]
    for j in range(0,7):
      tmp2=ord(tmp[j])
      tmp3=bin(tmp2)
      tmp3=tmp3[2:]
      while len(tmp3)<8:
        tmp3='0'+tmp3
      binval=binval+tmp3
    #print binval
    print len(binval)
  while cnt< len(binval):
    repl=binval[cnt:7+cnt]
    repl='0'+repl
    wrt_data=chr(int(repl,2))
    cnt=cnt+7
    wrt_file.write(wrt_data)
  read_file.close()
  wrt_file.close()

def net_compression(read_data):
  return_data=""
  cnt=0
  act_len=len(read_data)
  multiple=act_len/8
  binval=""
  for i in range(0,multiple):
    tmp=read_data[8*i:(8*i)+8]
    for j in range(0,8):
      tmp2=ord(tmp[j])
      tmp3=bin(tmp2)
      tmp3=tmp3[2:]
      while len(tmp3)<7:
        tmp3='0'+tmp3
      binval=binval+tmp3
  while cnt< len(binval):
    repl=binval[cnt:8+cnt]
    wrt_data=chr(int(repl,2))
    cnt=cnt+8
    return_data=return_data+wrt_data
  return return_data

def net_decompression(read_data):
  return_data=""
  cnt=0
  act_len=len(read_data)
  multiple=act_len/7
  binval=""
  for i in range(0,multiple):
    tmp=read_data[7*i:(7*i)+7]
    for j in range(0,7):
      tmp2=ord(tmp[j])
      tmp3=bin(tmp2)
      tmp3=tmp3[2:]
      while len(tmp3)<8:
        tmp3='0'+tmp3
      binval=binval+tmp3
  while cnt< len(binval):
    repl=binval[cnt:7+cnt]
    repl='0'+repl
    wrt_data=chr(int(repl,2))
    cnt=cnt+7
    return_data=return_data+wrt_data
  return return_data
