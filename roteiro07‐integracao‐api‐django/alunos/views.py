import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .aluno import Aluno

alunos = []
aluno1 = Aluno("João Silva", 17)
aluno1.adicionar_nota(8.5)
aluno2 = Aluno("Maria Souza", 16)
aluno2.adicionar_nota(9.0)
alunos.extend([aluno1, aluno2])

def pagina_inicial(request):
    return render(request, "index.html")

@csrf_exempt
@require_http_methods(["GET", "POST"])

def api_alunos(request):
    if request.method == "GET":
        dados = [aluno.to_dict() for aluno in alunos]
        return JsonResponse({"error": "Json inválido"}, status=400)
    
    nome = payload.get("nome")
    idade = payload.get("idade")

    if not nome or not isinstance(idade, int):
        return JsonResponse({"error": "Dados inválidos."}, status=400)
        novo_aluno = Aluno(nome, idade)
        alunos.append(novo_aluno)
        return JsonResponse(novo_aluno.to_dict(), status=201)
    
@csrf_exempt
@require_http_methods(["DELETE"])

def remover_aluno(request, aluno_id):
    global alunos
    existe = any(a.id == aluno_id for a in alunos)
    if not existe:
        return JsonResponse({"erro": "Aluno não encontrado"}, status=404)
    alunos = [a for a in alunos if a.id != aluno_id]
    return JsonResponse({"mensagem": "Aluno removido com sucesso"})