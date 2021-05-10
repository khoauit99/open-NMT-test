# Bước để train và implement model.

### Step 1 : we need install package OpenNMT-py
### Step 2 : clone and setting project
- git clone https://github.com/OpenNMT/OpenNMT-py.git
- cd OpenNMT-py
- pip install -e .

### Step 3 : Prepare data 
- But this project already has data
- wget https://s3.amazonaws.com/opennmt-trainingdata/toy-ende.tar.gz
- tar xf toy-ende.tar.gz
- cd toy-ende


### Step 4 : Prepare data 2
- make file yaml like @config_build_vocab
- After that: run 'onmt_build_vocab -config toy_en_de.yaml -n_sample 10000' 
- In toy-ende file it will make a new file run


### Step 5 : Train and Create model
- make file yaml like @config_train_model
- but you must have GPU to train data because this code using GPU to train data
- run 'onmt_train -config toy_en_de.yaml'

### Step 6 : Translate - using model 
- run 'onmt_translate -model toy-ende/run/model_step_1000.pt -src toy-ende/src-test.txt -output toy-ende/pred_1000.txt -gpu 0 -verbose'





# Ngoài lề về mấy cái config.


### 1. Ở trong file opts là nơi chứa các quy định để chạy / build model / hay làm bất cứ sử lý nào với các tham số defaul đã được set trong đó.

### 2. Nhưng chúng ta có thể can thiệp các tham số đó bằng cách tạo file yaml để can thiệp các tham số chúng ta muốn can thiệp vào.