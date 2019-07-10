from dataprocessing import DataReader, DataGenerator
from modeling import LanguageClassifier
from Enviroment import Enviroment as env
from metrics import print_confusion_matrix
from keras.models import load_model
from keras.utils.np_utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle
import os 
import numpy as np

def load_data(): 
    with open(env().path_to_arrays, "rb") as f_pickle:
        X_tr = pickle.load(f_pickle)
        X_te = pickle.load(f_pickle)
        y_tr = pickle.load(f_pickle)
        y_te = pickle.load(f_pickle)
        word_to_idx = pickle.load(f_pickle)
        idx_to_word = pickle.load(f_pickle)
        max_words = pickle.load(f_pickle)
    return X_tr, X_te, y_tr, y_te, word_to_idx, idx_to_word, max_words

def main():
    dr = DataReader(env().data_dir)
    data, labels = dr.create_dataset()
    dr.save_data_csv()
    data, labels = dr.load_dataset()
    dg = DataGenerator(data, labels)
    data, labels = dg.generate_data()

    X_train, X_test, y_train, y_test = dg.split_train_test(env().DIM_TEST)

    dg.save_data(X_train, X_test, y_train, y_test)

    X_train, X_test, y_train, y_test, word_to_idx, idx_to_word, max_words_length = load_data()

    print(len(X_train))

    langclassifier = LanguageClassifier(X_train,y_train,X_test,y_test)
    langclassifier.train_model()

    # langclassifier = load_model("lang_classifiercheckpoint.h5")
    # predictions  = langclassifier.predict(X_test)

    print(np.argmax(predictions[0]))
    print(np.argmax(predictions[1]))
    print(np.argmax(predictions[2]))
    print(np.argmax(predictions[3]))
    print(np.argmax(predictions[4]))
    print(np.argmax(predictions[5]))
    print(np.argmax(predictions[6]))
    print(np.argmax(predictions[7]))
    print(np.argmax(predictions[8]))
    print(np.argmax(predictions[9]))
    print(np.argmax(predictions[10]))
    print(np.argmax(predictions[11]))
    print(np.argmax(predictions[12]))
    print(np.argmax(predictions[13]))
    print(np.argmax(predictions[14]))
    print(np.argmax(predictions[15]))
    print(np.argmax(predictions[16]))
    print(np.argmax(predictions[17]))
    print(np.argmax(predictions[18]))
    print(np.argmax(predictions[19]))
    print(np.argmax(predictions[20]))
    print(np.argmax(predictions[21]))
    print(np.argmax(predictions[22]))
    print(np.argmax(predictions[23]))
    print(np.argmax(predictions[24]))
    print(np.argmax(predictions[25]))
    print(np.argmax(predictions[26]))
    print(np.argmax(predictions[27]))
    print(np.argmax(predictions[28]))
    print(np.argmax(predictions[29]))
    print(np.argmax(predictions[30]))
    print(np.argmax(predictions[31]))
    # y_pred = langclassifier.predict_classes(X_test)
    # y_pred = to_categorical(y_pred, num_classes=y_test.shape[1])

    # Evaluation on Test set
    # scores = langclassifier.evaluate(X_test, y_test, verbose=1)
    # print("%s: %.2f%%" % (langclassifier.metrics_names[1], scores[1]*100))
    
    # cnf_matrix = confusion_matrix(np.argmax(y_pred,axis=1), np.argmax(y_test,axis=1))
    # print(cnf_matrix)

if __name__ == '__main__':
    main()