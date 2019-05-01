
# dict_student ={"Maths":65,"English":80,"Physics":89,"Chemistry":70,"Hindi":92}
class Student:
    def __init__(self):
        self._subject =''
        self._marks=0
        self._std={}

    @property
    def __setitem__(self,a,b):
        self._subject[a]=b

    def __getitem__(self, item):
        return self._std .get(item)


def  cal_marks():
    cnt =0
    std =Student()
    summ=0
    while cnt<=5:
        s =input(f"enter input {cnt} : subject ")
        m= input(f"enter marsk for {s}  :  ")
        std.__setitem__(s,m)
        summ =summ+m

    print(summ  )

cal_marks()


