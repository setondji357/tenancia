"""Contractors Models."""
from django.db import models


class ComposantAppartement(models.Model):
    """Composant Models."""

    libelle = models.CharField(max_length=50)
    utilite = models.CharField(max_length=256)


class Appartement(models.Model):
    """Appartment models."""

    LIBRE = 'LIBRE'
    RESERVE = 'RESERVE'
    OCCUPE = 'OCCUPE'
    BIENTOT_LIBRE = 'BIENTOT LIBRE'

    STATUT_APPARTEMENT = (
        (LIBRE, 'LIBRE'),
        (RESERVE, 'RESERVE'),
        (OCCUPE, 'OCCUPE'),
        (BIENTOT_LIBRE, 'BIENTOT_LIBRE')
        )
    intitule = models.CharField(max_length=50)
    """level indique le niveau de l'appartement sur
    l'immeuble: 0 pour le rez de chaussé
         et peut prendre des signes négatifs
         pour les sous sols."""
    level = models.IntegerField(null=False)
    autre_description = models.TextField(max_length=1024)
    immeuble = models. \
        ForeignKey('immeuble.Immeuble',
                   null=True, on_delete=models.SET_NULL)
    structure = models. \
        ManyToManyField(ComposantAppartement,
                        through='StructureAppartement',
                        related_name='structure',
                        blank=False)
    statut = models.CharField(max_length=50,
                              choices=STATUT_APPARTEMENT,
                              default='LIBRE')

    def __str__(self):
        """String.:return."""
        return 'Immeuble: intitule {0}'.format(self.intitule, )


class StructureAppartement(models.Model):
    """Structure Appartment."""

    appartement = models. \
        ForeignKey('Appartement',
                   related_name='appartement',
                   on_delete=models.SET_NULL,
                   null=True)
    composantAppartement = models. \
        ForeignKey('ComposantAppartement',
                   related_name='composant_appartement',
                   on_delete=models.SET_NULL, null=True)
    nbre = models.IntegerField(default=1)
    description = models.CharField(max_length=256)
