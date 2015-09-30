testingFPlus
============

1. Group 35 gồm các thành viên:
----------------------------

- Phạm Hồng Phi

- Ngô Thái Phong

- Vũ Thanh Nam


2. Kết quả bài làm:
-------------

>   giải phương trình bậc 2 bằng JavaScript và tự động sinh đồ thị chương trình

#### a. Mã chương trình
- Chương trình giải phương trình bậc 2

```js
function GiaiPTB2(a, b, c) {
    var nghiem = {};
    if (!isNaN(a) && !isNaN(b) && !isNaN(c)) {
        if (a == 0) {
            if (b == 0) {
                if (c == 0) {
                    nghiem.x = 'R';
                    return nghiem;
                }
                return nghiem;
            }
            nghiem.x = -c / b;
            return nghiem;
        } else {
            var delta = b * b - 4 * a * c;
            if (delta < 0) {
                return nghiem;
            }
            nghiem.x1 = (-b + Math.sqrt(delta)) / (2 * a);
            nghiem.x2 = (-b - Math.sqrt(delta)) / (2 * a);
            return nghiem;
        }
    }
    return nghiem;
}
```
- Chương trình tính tổng số chẵn của một mảng

```js
function evensum(array){
	var sum = 0;
	if(!Array.isArray(array)){
		return null;
	}
	for(var i =0 ; i< array.length; i++){
		if(array[i]%2 ==0){
			sum += array[i];
		}
	}
	return sum;
}
```

#### b. Đồ thị
- Chương trình giải phương trình bậc 2

![dothi](<output.png?raw=true>)

- Chương trình tính tổng số chẵn của một mảng

![dothi2](<output2.png?raw=true>)

3.Tìm một công cụ tạo đồ thị chương trình cho ngôn ngữ Javascript
-----------------------------------------------------------------

### a. Công cụ sử dụng:

Esgraph Project: [link](<https://github.com/Swatinem/esgraph>)

### b. Cách sử dụng:

-   Cài đặt Nodejs để sử dụng công cụ npm

-   Cài đặt esgraph bằng cách sử dụng gói quản lý package npm của Nodejs: `npm install esgrath`

-   Chạy chương trình : `$ cat $file | esgraph | dot -Tpng > output.png`

4.Tạo ca kiểm thử theo tiêu chuẩn C1P
-------------------------------------

>Tương tự C1 nhưng các ca kiểm thử của C1P phải thực hiện mọi cặp điều kiện T, F
(True, False) cho các điểm điều kiện P1 và P2,...

#### Ta có các test case:

VD: Với code ở trên ta gọi:


Điểm  | Câu lệnh
------------- | -------------
P1  | (!isNaN(a) \&\& !isNaN(b) \&\& !isNaN(c))
P2  | (a==0)
 P3 | (b==0)                                    
 P4 | (delta\<0)                                
 P5 | (c==0)   

#### Vậy ta có các ca kiểm thử:

Ca kiểm thử | Giá trị tương ứng
------------|--------
(P1)| (F)
(P1, P2, P3, P5) | (T, T, T, T)
(P1, P2, P3, P5) | (T, T, T, F)
(P1, P2, P3) | (T, T, F)
(P1, P2, P4) | (T, F, T)
(P1, P2, P4) | (T, F, F)

#### Cụ thể đầu vào lần lượt như sau:

Đầu vào | Đầu ra
--------|-------
GiaiPTB2('a',1,1) | Expect value : không có kết quả.
GiaiPTB2(0,0,0) | Expect value : R ( tập R - vô số nghiệm)
GiaiPTB2(0,0,1) | Expect value :  không có kết quả
GiaiPTB2(0,3,4) | Expect value: -4/3
GiaiPTB2(1,2,7) | Expect value : không có kết quả
GiaiPTB2(1,-3,2) | Expect value : 2,1



5.Tạo ca kiểm thử với vòng lặp chương trình tính tổng số chẵn của một mảng
-------------------------------------

>Ta phải thực hiện với các test case để kiểm thử lệnh lặp n lần:
-  Chạy 0 lần lặp
-  Chạy 1 lần lặp
-  Chạy 2 lần lặp
-  Chạy k lần với 2 < k < n - 1
-  Chạy n -1 lần
-  Chạy  n lần



#### Ta có các test case:



Ca kiểm thử | Giá trị tương ứng
------------|--------
(0  lần )  | 'a'
(1 lần )   | (0,1,3,5,7,9,11)
(2 lần )   | (0,2,3,5,7,9) 
(k   lần ) | (0,1,2,3,4,5,6,7,8,9,10)
(n-1 lần ) | (0,2,4,6,8,9)
(n lần)    | (0,2,4,6,8,10)

#### Cụ thể đầu vào lần lượt như sau:

Đầu vào | Đầu ra
--------|-------
evensum('a') | Expect value : expected null
evensum(0,1,3,5,7,9,11) | Expect value : 0
evensum(0,2,3,5,7,9) |   Expect value : 2
evensum(0,1,2,3,4,5,6,7,8,9,10) | Expect value: 30
evensum((0,2,4,6,8,9 | Expect value : 20
evensum((0,2,4,6,8,10) | Expect value : 30
