from django.shortcuts import render, redirect
from .models import addNewTrainer

def TrainerList(request):
    trainer = addNewTrainer.objects.all()
    return render(request, "index.html", {"alltrainer": trainer})

def addTrainers(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        image = request.FILES.get('image')

        trainer = addNewTrainer(
            name=name,
            subject=subject,
            contact=contact,
            email=email,
            image=image if image else None
        )
        trainer.save()
        return redirect("alltrainers")
    return render(request, "index.html")

def update_trainer(request, id):
    trainer = addNewTrainer.objects.get(id=id)  # always fetch existing trainer

    if request.method == "POST":
        trainer.name = request.POST.get('name')
        trainer.subject = request.POST.get('subject')
        trainer.contact = request.POST.get('contact')
        trainer.email = request.POST.get('email')

        image = request.FILES.get('image')
        if image:
            trainer.image = image

        trainer.save()
        return redirect("alltrainers")

    return render(request, "index.html", {'trainer': trainer})


def delete_trainer(request,id):
    trainer = addNewTrainer.objects.filter(id=id)
    trainer.delete()
    
    return redirect("alltrainers")