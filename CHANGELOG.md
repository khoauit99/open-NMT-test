# lấy 50000 dòng 
+ head -n 50000 MultiCCAligned.en-ja.en >> eng.txt
+ head -n 50000 MultiCCAligned.en-ja.ja >> jyp.txt

# Các bước thực hiện 
+ b1 : tokenize với các tiếng như Nhật Bản ,...
+ b2 : build_vocab
+ b3 : train model 
+ b4 : test model


### tokenize
+ python3 tokenize/tokenize.py   
+ Tạo ra 2 file 1000 dòng mỗi thằng và nhật đã tokenize rồi.
+ Được lưu trong file toy-ende 



### sử dụng hàm build_vocab và train của OpenNMT để tạo model
+ python3 build_vocab.py -config config/config_build_vocab.yaml
+ python3 train.py -config config/config_train_model.yaml



### sử dụng hàm translate để dịch 
+ python3 translate.py -model toy-ende/run/model_step_80000.pt -src toy-ende/test.txt -output toy-ende/khoa_predict_2.txt


### Muốn train từ thằng model cũ 
+ python3 train.py -config config/config_transfer_learning.yaml -train_from (link model cần train tiếp).

# Chú ý để các số liệu nó phải tương đối giống nhau để mô hình có thể ra tốt . 
# Chú ý muốn hiểu các thông số thì phải vô file config để đọc