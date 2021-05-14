import sentencepiece as spm 

s = spm.SentencePieceProcessor('data/jpa_wiki_100000.model')

#file1 = open('jyp_train.txt', 'r')
#Lines = file1.readlines()

# for i in Lines:
#     print(i)

path_input_eng = 'data/eng.txt'
path_output_eng = 'data/eng_train_1000.txt'

path_input_jyp = 'data/jyp.txt'
path_output_jyp = 'data/jyp_train_1000.txt'

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


def save_file(path_input, path_output, check_token = False, number_line = 1000):
    open_file = open(path_input, 'r')
    save_file = open(path_output, 'w')
    for i in range(number_line):
        line = open_file.readline()
        if check_token == True:
            line = tokenize(line)
        save_file.write(line)



#print(tokenize('慈悲あまねく慈愛深きアッラーの御名において。'))
save_file(path_input_eng, path_output_eng)
save_file(path_input_jyp, path_output_jyp,check_token = True)
#def