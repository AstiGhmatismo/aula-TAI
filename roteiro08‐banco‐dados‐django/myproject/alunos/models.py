from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["nome"]

    def calcular_media(self):
        valores = list(self.notas.values_list("valor", flat=True))
        if not valores:
            return 0
        return sum(valores) / len(valores)
    
    def aprovado(self):
        return self.calcular_media() >= 7
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "media": round(self.calcular_media(), 2),
            "aprovado": self.aprovado(),
            "notas": [nota.to_dict() for nota in self.notas.all()],
        }

class Nota(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.Cascade,
        related_name="notas",
    )
    valor = models.FloatField()
    descricao = models.Charfield(max_length=60, blank=True, default="")

    def to_dict(self):
        return {
            "id": self.id,
            "valor": self.valor,
            "descricao": self.descricao,
        }