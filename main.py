from tkinter import *
import numpy as np
import pandas as pd
import sklearn


l1=['احتقان بالأنف','ألم في الحلق والبلعوم','ارتفاع درجة الحرارة أكثر من 38','فقدان الشهية',
    'ألم في الأذن خاصة عند الاستلقاء','خروج إفرازات من الأذن','صعوبة في النوم','الشعور بضغط في منطقة الأذن',
    'ضعف في السمع','تورّم اللوزتَين واحمرارهما','التهاب الغدد وتورّمها في رقبتك أو الفك',
    'ألم يزداد سوءاً مع البلع أو الكلام','صعوبة في البلع','تضيق في الصدر ','تسرع دقات القلب',
    'العطاس','الحكة في العينين أو الأنف أو الفم','سيلان الأنف','انسداد الأنف نتيجة للاحتقان',
    'احمرار وتورّم ودموع بالعينين','صداع الرأس','بلغم مع وجود الدم','السعال المستمر لمدة 3 أسابيع أو أكثر',
    'ألم في الصدر','الشعور بالتوعك','التعرق الليلي','فقدان الوزن','إحساس بالحكة بالعين',
    'احمرار وتورم في الملتحمة','زيادة الإفرازات المخاطية','الإحساس بالجفاف في العين','زيادة في إفراز الدموع',
    'حمى في بعض الحالات','صوت صفير(أزيز) عند التنفس في بعض الحالات','قلة الحيوية والنشاط',
    'سعال متكرر يصاحبه خروج البلغم','غبش الرؤية','رؤية الوهج','دماع العين','فقدان الرؤية بالكامل أو فقدان مجال الرؤية',
    'آلام العين','رؤية الهالات حول الأضواء','ظهور بقع أو خطوط في الرؤية']

disease=['رشحة','التهاب الأذن الوسطى','التهاب الحلق','حساسية الأنف','السل الرئوي','حساسية العين',
         'التهاب القصبات','إعتام العين','الزَرَق','اعتلال شبكية العين']

l2=[0]*len(l1)

# TRAINING DATA -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'رشحة':0,'التهاب الأذن الوسطى':1,'التهاب الحلق':2,'حساسية الأنف':3,
                         'السل الرئوي':4,'حساسية العين':5,'التهاب القصبات':6,'إعتام العين':7,'الزَرَق':8,'اعتلال شبكية العين':9}},inplace=True)

# print(df.head())

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TESTING DATA --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'رشحة':0,'التهاب الأذن الوسطى':1,'التهاب الحلق':2,'حساسية الأنف':3,
                         'السل الرئوي':4,'حساسية العين':5,'التهاب القصبات':6,'إعتام العين':7,'الزَرَق':8,'اعتلال شبكية العين':9}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------
    l2=[0]*len(l1)
    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1
                break
    inputtest = [l2]
    print(l2)
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
# ------------------------------------------------------------------------------------
root = Tk()
root.configure(background='pink')

# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Symptom6 = StringVar()
Symptom6.set(None)
Symptom7 = StringVar()
Symptom7.set(None)
Symptom8 = StringVar()
Symptom8.set(None)

Name = StringVar()

# Heading
w2 = Label(root, justify=LEFT, text="Disease Predictor using Machine Learning", fg="black", bg="white")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

w2.config(font=("Aharoni", 30))
w2.grid(row=2, column=0, columnspan=2, padx=100)

# labels
NameLb = Label(root, text="Name of the Patient", fg="yellow", bg="black")
NameLb.grid(row=6, column=0, pady=15, sticky=W)


S1Lb = Label(root, text="Symptom 1", fg="yellow", bg="black")
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Symptom 2", fg="yellow", bg="black")
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Symptom 3", fg="yellow", bg="black")
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Symptom 4", fg="yellow", bg="black")
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Symptom 5", fg="yellow", bg="black")
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

S6Lb = Label(root, text="Symptom 6", fg="yellow", bg="black")
S6Lb.grid(row=12, column=0, pady=10, sticky=W)

S7Lb = Label(root, text="Symptom 7", fg="yellow", bg="black")
S7Lb.grid(row=13, column=0, pady=10, sticky=W)

S8Lb = Label(root, text="Symptom 8", fg="yellow", bg="black")
S8Lb.grid(row=14, column=0, pady=10, sticky=W)

lrLb = Label(root, text="DecisionTree", fg="white", bg="red")
lrLb.grid(row=15, column=0, pady=10,sticky=W)

# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=1)

S6En = OptionMenu(root, Symptom6,*OPTIONS)
S6En.grid(row=12, column=1)

S7En = OptionMenu(root, Symptom7,*OPTIONS)
S7En.grid(row=13, column=1)

S8En = OptionMenu(root, Symptom8,*OPTIONS)
S8En.grid(row=14, column=1)

dst = Button(root, text="DecisionTree", command=DecisionTree,bg="green",fg="yellow")
dst.grid(row=8, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="orange",fg="black")
t1.grid(row=15, column=1, padx=10)

root.mainloop()

