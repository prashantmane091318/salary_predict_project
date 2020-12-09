from django.shortcuts import render
import pickle
# Create your views here.
def home_view(request):
    return render(request,"testapp/index.html")

def predict_view(request):
    #request.post.get()
    dict={}
    if request.method=="POST":
        name=request.POST.get("name")
        exp=request.POST.get("exp")
        model=pickle.load(open("model/mysalary.pkl","rb"))
        salary=round(model.predict([[10]])[0])
        print(salary)

    return render(request,"testapp/predict.html",{"salary":salary,"name":name})

