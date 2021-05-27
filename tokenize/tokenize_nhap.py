import sentencepiece as spm 
from sklearn.model_selection import ShuffleSplit
from traceback import format_exc as _format_exc

s = spm.SentencePieceProcessor('data/jpa_wiki_100000.model')

#file1 = open('jyp_train.txt', 'r')
#Lines = file1.readlines()

# for i in Lines:
#     print(i)

path_input_eng = 'data/English_2.txt'
path_output_eng_train = 'toy-ende/data/tgt-train.txt'
path_output_eng_test = 'toy-ende/data/tgt-val.txt'

path_input_jyp = 'data/Japan_2.txt'
path_output_jyp_train = 'toy-ende/data/src-train.txt'
path_output_jyp_test = 'toy-ende/data/src-val.txt'



def count_unique(input_list):
  l1 = []
  
# taking an counter
  count = 0
  
# travesing the array
  for item in input_list:
      if item not in l1:
          count += 1
          l1.append(item)
  return count


def tokenize(sequence):
    test = s.Encode(sequence, out_type= str , enable_sampling= True , alpha = 0.01, nbest_size = 2)
    sequence_token = ''
    for j in range(0,len(test)):
        test_clean = test[j]
        test_clean = test_clean.replace('▁','')
        if test_clean != '':
            sequence_token = sequence_token + ' ' + test_clean
        else:
            continue
    return sequence_token


def save_file(path_input, path_output_train, path_output_test, check_token = False, number_line = 1000):
    open_file = open(path_input, 'r')
    save_file_train = open(path_output_train, 'w')
    save_file_test = open(path_output_test,'w')
    
    X = list(range(0,number_line))
    #print(X)
    train_index = []
    test_index = []

    rs = ShuffleSplit(n_splits=1, test_size=0.2, random_state=1)
    for x,y in rs.split(X):
      train_index = x
      test_index = y

  
    print(count_unique(train_index))

    for i in range(0,number_line):
        line = open_file.readline()
        if check_token == True:
            line = tokenize(line)
        if i in train_index:    
          save_file_train.write(line)
        else:
          save_file_test.write(line)
   



#print(tokenize('慈悲あまねく慈愛深きアッラーの御名において。'))
save_file(path_input_eng, path_output_eng_train, path_output_eng_test, number_line= 43164)
save_file(path_input_jyp, path_output_jyp_train, path_output_jyp_test, check_token = True, number_line= 43164)
#def