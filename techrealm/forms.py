from django import forms

class CursoFormulario(forms.Form):
    nombreCurso = forms.CharField()
    nivelCurso = forms.CharField()
    fechaCurso = forms.DateField()
