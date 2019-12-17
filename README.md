# ravdec
Ravdec is a module written in python, which is based on a Lossless Data Compression Algorithm designed by [Ravin Kumar](https://mr-ravin.github.io) on 19 September, 2016.This compression algorithm have a fixed compression ratio of 1.1429 in all possible cases, It accepts data of following format: alphabets,numbers, and symbols.It can be  used where the machine generates data at a very fast rate, that it became difficult for other algorithms to calculate the propability of a symbol, as data keeps on getting large, and is transmitted over the network with a much faster rate. In this case also,  the above module, and algorithm gives the same compression ratio.

### Ravdec- LossLess Data Compression

##### Algorithm Designer, and Module Developer: [Ravin Kumar](https://mr-ravin.github.io)

This compression algorithm have a fixed compression ratio of 1.1429 in all possible cases, It accepts data 
of following format: alphabets,numbers, and symbols.
Example: It can compress 1 GB to 896 MB.

### Application of Ravdec 

It can be  used where the machine generates data at a very fast rate, that it became difficult for other algorithms to calculate
the propability of a symbol, as data keeps on getting large, and is transmitted over the network with a much faster rate. In
this case also, the above module, and algorithm gives the same compression ratio.



NOTE- The data that is to be compressed should have length of multiple of 8.(i.e 8 elements, or 16
elemnts or 24...so on)

- file_compression(filename) : 
It is used to read data from a file, and create a compressed file wit extention of ".rav" 

- file_decompression(filename) :
It is used to read data from a previously compressed file, and create a decompressed file wit extention of ".dec" 


 #### Example:
 
 ```python
 
 import ravdec 

 # to compress the file have elements of multiple of 8.
 ravdec.file_compression("filename.txt")

 # to decompress the previously compressed file.
 ravdec.file_decompression("filename.rav")

 ```
 
- net_compression("data to be compressed of length of multiple of 8 ") - To compress the  original data to transmit, that is
   needed to be  transmitted.
- net_decompression(" previously compressed data")  - To decompress the previously compressed data, that is received.

It is used where the machine generates data at a very fast rate, that it became difficult for other algorithms to calculate the
propability of a symbol, as data keeps on getting large, and is transmitted over the network with a much faster rate.

#### Example:

```

import ravdec

# for compression
compressed_data=ravdec.net_compression("ASDFGHJK")

# note- data to be compressed should have length of multiple of 8.(i.e 8 elements, or 16 elemnts or 24...so on)
# for decompression

decompressed_data=ravdec.decompression("previously compressed data")

```

#### Application of this module:

It can be  used where the machine generates data at a very fast rate, that it became difficult for other algorithms to
calculate the probability of a symbol, as data keeps on getting large, and is transmitted over the network with a much faster
rate. In this case also, the above module, and algorithm gives the same compression ratio.

#### Installation using pip:
```
pip install ravdec
```

##### Note: This work can be used freely after providing citation and/or deserved credits to this work. Please use it at your own risk !!!
