def metrics(Tp,Fp,Tn,Fn):
    Accuracy=(Tp+Tn)/(Tp+Tn+Fp+Fn)
    Precision=Tp/(Tp+Fp)
    Recall=Tp/(Tp+Fn)
    print('Accuracy :'+str(Accuracy))
    print('For class 0:  Precision :'+str(Precision)+' Recall :'+str(Recall))

    Precision=Tn/(Tn+Fn)
    Accuracy=Tn/(Tn+Fp)
    print('For class 1:  Precision :'+str(Precision)+' Recall :'+str(Recall))


    

def main():
    metrics(83891.000,3257.000,12031.000,819.000)

if __name__ == '__main__':
    main()