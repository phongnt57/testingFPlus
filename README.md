# testingFPlus
Group 35

Chương trình giải phương trình bậc 2 bằng JavaScript và tự động sinh đồ thị chương trình
1.	Tìm một công cụ tạo đồ thị chương trình cho ngôn ngữ Javascript

Công cụ sử dụng:
EsGrapth

Nguồn:
https://github.com/Swatinem/esgraph

Cách sử dụng
	
- Cài đặt sử dụng gói quản lý package npm: npm install esgrath.
- Chạy chương trình : $ cat $file | esgraph | dot -Tpng > output.png 


	Tạo ca kiểm thử theo tiêu chuẩn C1P
kiểm thử sao cho mỗi lệnh được thực thi ít nhất 1 lần.
Ta có các test case:

 GiaiPTB2(1,1,a) . Expect value : không có kết quả.

 GiaiPTB2(0,0,0). Expect value : R
 
 GiaiPTB2(1,0,4). Expect value: 2 ,-2
 
 GiaiPTB2(1,2,7) : Expect value : không có kết quả
 
 GiaiPTB2(1,-3,2) . Expect value : 2,1
 

 

