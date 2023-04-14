# BRAINSTORM BOARD: FILE UPLOAD LEVEL 2
Hack = Solve Puzzle = Chơi ghép hình
--> Phải có đầy đủ các mảnh ghép, và biết phải ghép như thế nào

## Ta có:
1. Untrusted Data (file) bị user upload vào /upload/ trong DocumentRoot
2. Ta hoàn toàn có thể truy cập vào http://localhost:12002/upload/{session_id}/...
3. Biết đc rằng nguyên tắc của HTTPD chính là nhìn vào đuổi file cuối cùng của `{filename}.php` để xác định rằng đây có phải là tập tin PHP và đưa cho mod-php xử lý không?
4. Nếu tìm được cách upload file có đuôi `.php` thì HTTPD sẽ thực thi code ngay -> GAMEOVER

## Vấn đề [ý là tại sao lại không dùng cách giải giống level 1]:
1. Lập trình viên đã sàng lọc (filer) không cho phép upload đuôi file `.php` bằng cách nào? Bằng cách dùng `explode` để nổ dấu `.` trong filename rồi lấy phần tử có index [1]
```php
    $filename = $_FILES["file"]["name"];
    $extension = explode(".", $filename)[1];
    if ($extension === "php") {
        die("Hack detected");
    }
```
## Hướng giải quyết:
1. Ta biết rằng HTTPd chỉ lấy đuôi file (extension) cuối cùng để quyết định xem có xử lý như code PHP không. Liệu có cách nào tạo ra file name mà đuôi file cuối cùng vẫn là `*.php` nhưng khi vào `explode` thì đuôi file `php` không nằm ở vị trí 1 --> để né đoạn filter.


2. HTTPD có nhất thiết chỉ nhận diện extension file `php` để đưa cho mod-php xử lý hay không? Tức là liệu còn đuôi (extension) nào ngoài `php` mà HTTPD vẫn thực thi, mà ta chưa biết không?  
2b. Ta biết rằng mod-php xử lý file có extension cuối là php. Liệu có cách nào để mod-php vẫn excute extension khác không ?
2c. Liệu ngoài đuôi .php còn đuôi nào vẫn thực thi được file không
2d. Liệu có cách nào để mod-php chạy được code php mà không dùng đuôi php không

## ĐI KIỂM CHỨNG:
1. Ta upload file `abc.txt.php` và thấy rằng sau khi `explode` thì mảng `php` đã thành index [2] -> đã né được filter --> và đuôi file vẫn là 4 kí tự: `.php` --> HTTPD lúc này vẫn nhận thấy đây là tập tin code PHP --> thực thi nó --> Giả thiết thành công!!!

<!-- 2. Sẽ ra sao ...
3. Có nhất thiết ...
4.  -->

## NHÁP:
Sẽ ra sao nếu để đuổi .php  không phải vị trí số 1 --> tức là đuôi .php có thể ở vị trí khác --> `php` --> php đã ở vị trí ở số 0 --> nhưng đâu execute được.

Sẽ ra sao nếu đuổi không phải php --> ... --> đuôi .txt thì sao?

Sẽ ra sao nếu đuôi .php nằm ở phần tử có index khác [1] sau khi explode --> abc.abc.php.txt --> .php ở index [2] nè --> nhưng Vẫn ko execute được code PHP 

sẽ ra sao nếu biến php không ở vị trí 1 --> ... 

- Liệu có cách nào để "php" không ở index 1 k --> abc.abc.php.txt --> Vẫn ko execute được code PHP 
- Sẽ ra sao nếu để "php" ở index khác 1 
- Có nhất thiết "php" khác index 1 hoặc index [1] không phải php không

sẽ ra sao nếu file name sau khi nổ lớn hơn 2 phần như thông thường? --> 

sẽ  ra sao nếu extension "php" ở vị trí khác 1 nhưng vẫn execute được --> 7.5/10

có thể php ở cuối nhưng không phải vị trí 1 --> 7.6/10

sẽ ra sao nếu để php ở index cuối cùng nhưng phải > 1 --> SAI

Sẽ ra sao nếu explode file upload , extention php k nằm ở index[1] và mod-php xử lý dc file --> 8/10

Lẽ ra sao nếu PHP ngôn tình: 
ta ko là người đứng đầu (0) hoặc ở vị trí số 1 (1) đối nàng quen, ta chỉ có thể là người cuối cùng mà thôi --> Chơi cái gì dzậy --> đồ ngon dzậy

