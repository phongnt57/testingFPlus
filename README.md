testingFPlus
============

Group 35 gồm các thành viên:
----------------------------

>   Phạm Hồng Phi

>   Ngô Thái Phong

>   Vũ Thanh Nam

Chương trình:
-------------

>   giải phương trình bậc 2 bằng JavaScript và tự động sinh đồ thị chương trình

1.Tìm một công cụ tạo đồ thị chương trình cho ngôn ngữ Javascript
-----------------------------------------------------------------

### Công cụ sử dụng:

EsGrapth

### Nguồn:

Esgraph Project: [link](<https://github.com/Swatinem/esgraph>)

### Cách sử dụng

>   Cài đặt Nodejs để sử dụng công cụ npm

>   Cài đặt sử dụng gói quản lý package npm của Nodejs: `npm install esgrath`

>   Chạy chương trình : `$ cat $file | esgraph | dot -Tpng > output.png`

2.Tạo ca kiểm thử theo tiêu chuẩn C1P
-------------------------------------

>Tương tự C1 nhưng các ca kiểm thử của C1P phải thực hiện mọi cặp điều kiện T, F
(True, False) cho các điểm điều kiện P1 và P2,...

####Ta có các test case:

VD: Với code ở trên ta gọi:

 
Điểm  | Câu lệnh
------------- | -------------
P1  | (!isNaN(a) \|\| !isNaN(b) \|\| !isNaN(c)) 
P2  | (a==0)
 P3 | (b==0)                                    
 P4 | (delta\<0)                                
 P5 | (c==0)   
 
Vậy ta có các ca kiểm thử:

Ca kiểm thử | Kết quả
------------|--------
(P1)| (F)
(P1, P2, P3, P5) | (T, T, T, T)
(P1, P2, P3, P5) | (T, T, T, F)
(P1, P2, P3) | (T, T, F)
(P1, P2, P4) | (T, F, T)
(P1, P2, P4) | (T, F, F)

Cụ thể đầu vào lần lượt như sau:

Đầu vào | Đầu ra
--------|-------
GiaiPTB2(a,1,1) | Expect value : không có kết quả.
GiaiPTB2(0,0,0) | Expect value : R
GiaiPTB2(0,0,1) | Expect value : không có kết quả
GiaiPTB2(1,0,4) | Expect value: 2 ,-2
GiaiPTB2(1,2,7) | Expect value : không có kết quả
GiaiPTB2(1,-3,2) | Expect value : 2,1
