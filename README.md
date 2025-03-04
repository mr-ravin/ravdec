# 📦 **Ravdec - Lossless Data Compression**

## 🔹 **Overview**
Ravdec is a Python module implementing a **lossless data compression** algorithm designed by [Ravin Kumar](https://mr-ravin.github.io) on **September 19, 2016**. This algorithm is designed exclusively for **textual data**, including **alphabets, numbers, and symbols**. The algorithm offers two modes: 

- When `enforced_8char_input=True`, the length of input data must be exactly divisible by **8**, ensuring a **fixed compression ratio of 1.1429**.
- When `enforced_8char_input=False`, the compression ratio starts at **1.0435** for a **24-character input** (minimum required length) and increases with input size, approaching **1.1429** for larger inputs.

---
## 🔧 **Development Details**
- **👨‍💻 Developer:** [Ravin Kumar](https://mr-ravin.github.io)  
- **📂 GitHub Repository:** [https://github.com/mr-ravin/ravdec/](https://github.com/mr-ravin/ravdec/)
- **🌐 JavaScript Implementation:** [https://github.com/mr-ravin/ravdecjs/](https://github.com/mr-ravin/ravdecjs/)

---
## 📊 **Compression Ratio**

### ✅ **When `enforced_8char_input=False`**
- Compression ratio starts at **1.0435** for a **24-character input** (minimum required length).
- Gradually increases, reaching **1.14** at **912-character length**, and further approaches **1.1429** as input size increases.
- Ideal for handling variable-length text data while still achieving efficient compression.

### 🚀 **When `enforced_8char_input=True`**
- Original data length must be exactly divisible by **8**, ensuring a **fixed compression ratio of 1.1429**.
- Much faster, making it suitable for **high-speed data compression**.
- Best for **real-time systems** where data is continuously growing and **frequency-based algorithms are time-consuming**.

---
## ⏳ **Complexity Analysis**

### **1️⃣ `enforced_8char_input = True`**
✅ **Time Complexity: O(n)**
✅ **Fixed Compression Ratio (1.1429)**
✅ **Ideal for continuously growing data**

- **Direct 7-bit conversion per character**
- **No padding calculations**
- **Optimized for speed**

### **2️⃣ `enforced_8char_input = False`**
📌 **Time Complexity: O(n) (with minor overhead)**
📌 **Compression ratio varies (~1.04 - 1.1429)**
📌 **Needs Padding Overhead**

- **Direct 7-bit conversion per character**
- **Padding calculation and storage overhead**
- **Slower compared to enforced mode**

### 📌 **Comparison Table**
| Mode | Time Complexity | Compression Ratio | Padding Overhead | Best Use Case |
|------|---------------|-----------------|----------------|---------------|
| `enforced_8char_input = True` | **O(n)** | **Fixed (1.1429)** | ❌ No Padding | **High-speed data streams** |
| `enforced_8char_input = False` | **O(n) (with minor overhead)** | **Variable (~1.04 - 1.1429)** | ✅ Needs Padding | **General text compression** |

---
## 🎯 **Use Cases**
- **📜 Log File Compression:** Reduces storage space while maintaining quick retrieval.
- **⚡ High-Speed Data Transmission:** Faster processing with `enforced_8char_input=True`.
- **📈 Fixed Compression Ratio Scenarios:** Ideal for predictable compression requirements.
- **📁 Data Archiving:** Efficient text storage without losing information.
- **⏳ Real-Time Compression:** `enforced_8char_input=True` ensures immediate compression without extra calculations.

---
## 🚀 **Features**
✅ **Fixed compression ratio** up to **1.1429** for `enforced_8char_input=True`.
✅ **Supports alphabets, numbers, and symbols**.
✅ **Optimized for real-time and high-speed data transmission**.

---
## 🛠️ **Functions**

### 📌 `file_compression(filename, enforced_8char_input=False)`
Compresses a text file and saves the compressed data with the `.rdc` extension.

### 📌 `file_decompression(filename, enforced_8char_input=False)`
Decompresses a previously compressed `.rdc` file back to its original form.

### 📌 `compression(read_data, enforced_8char_input=False)`
Compresses a string using **7-bit storage**, returning a compressed string.

### 📌 `decompression(compressed_text, enforced_8char_input=False)`
Decompresses a compressed string back to its original form.

---
## 📥 **Installation**

Install using pip:

```sh
pip install ravdec
```
or,

```sh
pip install git+https://github.com/mr-ravin/ravdec.git
```


---
## 🔄 **Example Usage**

### ✍ **Compressing and Decompressing Text**
```python
import ravdec

# When enforced_8char_input=True

data = 'Ravdec !'  # Length of data is divisible by 8

# Compress a string with enforced_8char_input=True
compressed_data = ravdec.compression(data, enforced_8char_input=True) # compressed_data is '¥\x87¶L¸Ð!'

# Decompress the string
decompressed_data = ravdec.decompression(compressed_data, enforced_8char_input=True)
print(compressed_data)    # Output: '¥\x87¶L¸Ð!'
print(decompressed_data)  # Output: 'Ravdec !'



# When enforced_8char_input=False (and input data has length >= 24)

data = 'R'*25
# Compress a string with enforced_8char_input=False
compressed_data = ravdec.compression(data) # by default enforced_8char_input=False

# Decompress the string
decompressed_data = ravdec.decompression(compressed_data) # by default enforced_8char_input=False
print(compressed_data)
print(decompressed_data)

```

### 🗂️ **Compressing and Decompressing Files**
```python
import ravdec

original_filename = "inputfile.txt"
compressed_filename = filename+".rdc"

# Compress a file
ravdec.file_compression(original_filename) # saves compressed data in compressed_filename

# Decompress the previously compressed file
ravdec.file_decompression(compressed_filename) # saves the decompressed data in original_filename (got after removing '.rdc' from compressed_filename)
```

---
## 📜 **Copyright License**
```python
Copyright (c) 2016 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
